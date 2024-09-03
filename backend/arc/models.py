from django.utils.text import slugify
from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image


class ImageBase(models.Model):
    IMAGE_TYPE_CHOICES = [
        ("slider_image", "Картинка для слайдера"),
        ("additional_image", "Дополнительное изображение"),
    ]
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    image_type = models.CharField(
        max_length=20, choices=IMAGE_TYPE_CHOICES, verbose_name="Тип изображения"
    )

    class Meta:
        abstract = True

    def get_parent_instance(self):
        raise NotImplementedError("Метод должен быть реализован в наследуемой модели")

    def save(self, *args, **kwargs):
        if self.pk is None:
            parent_instance = self.get_parent_instance()
            if (
                self.image_type == "slider_image"
                and self.__class__.objects.filter(
                    **{
                        self._meta.get_field(
                            "complex"
                            if isinstance(parent_instance, Complex)
                            else (
                                "plot"
                                if isinstance(parent_instance, Plot)
                                else "apartment"
                            )
                        ).name: parent_instance
                    },
                    image_type="slider_image",
                ).count()
                >= 10
            ):
                raise ValidationError(
                    "Для категории 'Картинка для слайдера' можно загрузить до 10 изображений."
                )
            elif (
                self.image_type == "additional_image"
                and self.__class__.objects.filter(
                    **{
                        self._meta.get_field(
                            "complex"
                            if isinstance(parent_instance, Complex)
                            else (
                                "plot"
                                if isinstance(parent_instance, Plot)
                                else "apartment"
                            )
                        ).name: parent_instance
                    },
                    image_type="additional_image",
                ).count()
                >= 10
            ):
                raise ValidationError(
                    "Для категории 'Дополнительное изображение' можно загрузить до 10 изображений."
                )

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.image.path, quality=70, optimize=True)

    def __str__(self):
        return f"{self.get_parent_instance()} - {self.get_image_type_display()}"


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название города")
    path = models.CharField(max_length=100, verbose_name="Путь", default="")
    new_title = models.CharField(
        max_length=255, verbose_name="Заголовок для новостройки", blank=True, null=True
    )
    new_desc = models.TextField(
        verbose_name="Описание для новостройки", blank=True, null=True
    )
    plot_title = models.CharField(
        max_length=255, verbose_name="Заголовок для застройки", blank=True, null=True
    )
    plot_desc = models.TextField(
        verbose_name="Описание для застройки", blank=True, null=True
    )
    complex_card_bg = models.ImageField(
        upload_to="cities/complexes/cards/",
        verbose_name="Фон карточки города для комплексов",
        blank=True,
        null=True,
    )
    complex_bg = models.ImageField(
        upload_to="cities/complexes/bg/",
        verbose_name="Фон для комплексов",
        blank=True,
        null=True,
    )
    plot_card_bg = models.ImageField(
        upload_to="cities/plots/cards/",
        verbose_name="Фон карточки города для застроек",
        blank=True,
        null=True,
    )
    plot_bg = models.ImageField(
        upload_to="cities/plots/bg/",
        verbose_name="Фон для застроек",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def save(self, *args, **kwargs):
        if not self.path:
            if self.new_title or self.new_desc:
                self.path = f"/new/{slugify(self.name)}"
            elif self.plot_title or self.plot_desc:
                self.path = f"/plots/{slugify(self.name)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Complex(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="complexes", verbose_name="Город"
    )
    name = models.CharField(max_length=200, verbose_name="Название комплекса")
    path = models.CharField(max_length=100, verbose_name="Путь", default="")
    card_bg = models.ImageField(
        upload_to="complexes/cards/",
        verbose_name="Фон карточки в слайдере",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Комплекс"
        verbose_name_plural = "Комплексы"

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = f"{self.city.path}/{slugify(self.name)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ComplexImage(ImageBase):
    complex = models.ForeignKey(
        Complex,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Комплекс",
    )

    class Meta:
        verbose_name = "Изображение комплекса"
        verbose_name_plural = "Изображения комплексов"

    def get_parent_instance(self):
        return self.complex


class Plot(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="plots", verbose_name="Город"
    )
    district = models.CharField(max_length=200, verbose_name="Район", blank=True)
    path = models.CharField(max_length=100, verbose_name="Путь", default="")
    card_bg = models.ImageField(
        upload_to="plots/cards/",
        verbose_name="Фон карточки в слайдере",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Застройка"
        verbose_name_plural = "Застройки"

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = f"{self.city.path}/{slugify(self.district)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.district


class PlotImage(ImageBase):
    plot = models.ForeignKey(
        Plot, on_delete=models.CASCADE, related_name="images", verbose_name="Застройка"
    )

    class Meta:
        verbose_name = "Изображение застройки"
        verbose_name_plural = "Изображения застроек"

    def get_parent_instance(self):
        return self.plot


class NewSection(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="new_sections",
        verbose_name="Город",
    )
    title = models.CharField(
        max_length=255, verbose_name="Заголовок", blank=True, null=True
    )
    desc_1 = models.TextField(verbose_name="Описание 1", blank=True, null=True)
    desc_2 = models.TextField(verbose_name="Описание 2", blank=True, null=True)
    image_1 = models.ImageField(
        upload_to="new_sections/", verbose_name="Изображение 1", blank=True, null=True
    )
    image_2 = models.ImageField(
        upload_to="new_sections/", verbose_name="Изображение 2", blank=True, null=True
    )
    image_3 = models.ImageField(
        upload_to="new_sections/", verbose_name="Изображение 3", blank=True, null=True
    )
    image_4 = models.ImageField(
        upload_to="new_sections/", verbose_name="Изображение 4", blank=True, null=True
    )
    loc = models.CharField(
        max_length=255, verbose_name="Локация", blank=True, null=True
    )

    class Meta:
        verbose_name = "Секция новостроек"
        verbose_name_plural = "Секции новостроек"

    def __str__(self):
        return self.title or f"{self.city.name} - {self.loc}"


class PlotSection(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="plot_sections",
        verbose_name="Город",
    )
    title = models.CharField(
        max_length=255, verbose_name="Заголовок", blank=True, null=True
    )
    desc_1 = models.TextField(verbose_name="Описание 1", blank=True, null=True)
    desc_2 = models.TextField(verbose_name="Описание 2", blank=True, null=True)
    image_1 = models.ImageField(
        upload_to="plot_sections/", verbose_name="Изображение 1", blank=True, null=True
    )
    image_2 = models.ImageField(
        upload_to="plot_sections/", verbose_name="Изображение 2", blank=True, null=True
    )
    image_3 = models.ImageField(
        upload_to="plot_sections/", verbose_name="Изображение 3", blank=True, null=True
    )
    image_4 = models.ImageField(
        upload_to="plot_sections/", verbose_name="Изображение 4", blank=True, null=True
    )
    loc = models.CharField(
        max_length=255, verbose_name="Локация", blank=True, null=True
    )

    class Meta:
        verbose_name = "Секция застроек"
        verbose_name_plural = "Секции застроек"

    def __str__(self):
        return self.title or f"{self.city.name} - {self.loc}"


class Apartment(models.Model):
    CATEGORY_CHOICES = [
        ("studio", "Студия"),
        ("one_room", "Однокомнатная"),
        ("two_room", "Двухкомнатная"),
        ("three_room", "Трехкомнатная"),
    ]
    complex = models.ForeignKey(
        Complex,
        on_delete=models.CASCADE,
        related_name="apartments",
        verbose_name="Комплекс",
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="apartments", verbose_name="Город"
    )
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория"
    )
    path = models.CharField(max_length=100, verbose_name="Путь", blank=True)

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = f"{slugify(self.complex.path)}/{slugify(self.category.replace('_', '-'))}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_category_display()} - {self.complex.name}"


class ApartmentImage(ImageBase):
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Квартира",
    )

    class Meta:
        verbose_name = "Изображение квартиры"
        verbose_name_plural = "Изображения квартир"

    def get_parent_instance(self):
        return self.apartment


class ApartmentSection(models.Model):
    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name="Квартира",
    )
    title = models.CharField(max_length=255, verbose_name="Название секции")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    floor = models.PositiveIntegerField(verbose_name="Этаж")
    room_count = models.PositiveIntegerField(verbose_name="Количество комнат")
    apartment_number = models.CharField(max_length=10, verbose_name="Номер квартиры")
    area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Площадь")
    delivery_date = models.DateField(verbose_name="Срок сдачи")
    image_1 = models.ImageField(
        upload_to="apartments/sections/",
        verbose_name="Изображение 1",
        blank=True,
        null=True,
    )
    image_2 = models.ImageField(
        upload_to="apartments/sections/",
        verbose_name="Изображение 2",
        blank=True,
        null=True,
    )
    image_3 = models.ImageField(
        upload_to="apartments/sections/",
        verbose_name="Изображение 3",
        blank=True,
        null=True,
    )
    image_4 = models.ImageField(
        upload_to="apartments/sections/",
        verbose_name="Изображение 4",
        blank=True,
        null=True,
    )
    image_5 = models.ImageField(
        upload_to="apartments/sections/",
        verbose_name="Изображение 5",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Секция квартиры"
        verbose_name_plural = "Секции квартир"

    def __str__(self):
        return f"{self.title} - {self.apartment}"


class PlotLand(models.Model):
    LAND_TYPE_CHOICES = [
        ("6", "6 соток"),
        ("8", "8 соток"),
        ("10", "10 соток"),
        ("12", "12 соток"),
    ]
    plot = models.ForeignKey(
        Plot, on_delete=models.CASCADE, related_name="lands", verbose_name="Застройка"
    )
    land_type = models.CharField(
        max_length=2, choices=LAND_TYPE_CHOICES, verbose_name="Тип участка"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за участок"
    )
    path = models.CharField(max_length=100, verbose_name="Путь", blank=True)

    class Meta:
        verbose_name = "Участок"
        verbose_name_plural = "Участки"

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = (
                f"{slugify(self.plot.path)}/{slugify(self.get_land_type_display())}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_land_type_display()} - {self.plot.district}"
