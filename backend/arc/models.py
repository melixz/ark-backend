import os
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
            parent_field_name = None

            if isinstance(parent_instance, Complex):
                parent_field_name = "complex"
            elif isinstance(parent_instance, Plot):
                parent_field_name = "plot"
            elif isinstance(parent_instance, PlotLand):
                parent_field_name = "plot_land"
            elif isinstance(parent_instance, Apartment):
                parent_field_name = "apartment"

            if parent_field_name:
                if (
                    self.image_type == "slider_image"
                    and self.__class__.objects.filter(
                        **{
                            self._meta.get_field(
                                parent_field_name
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
                                parent_field_name
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
        self.process_image()

    def process_image(self):
        img = Image.open(self.image.path)

        if img.mode in ("RGBA", "LA") or (
            img.mode == "P" and "transparency" in img.info
        ):
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background

        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))

        file_root, file_ext = os.path.splitext(self.image.path)
        if file_ext.lower() != ".jpg" and file_ext.lower() != ".jpeg":
            new_image_path = f"{file_root}.jpg"
            img.save(new_image_path, format="JPEG", quality=70, optimize=True)
            self.image.name = os.path.basename(new_image_path)
            if os.path.exists(self.image.path):
                os.remove(self.image.path)
        else:
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
    floor_count = models.PositiveIntegerField(
        verbose_name="Количество этажей", blank=True, null=True
    )

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
        ("SNT", "СНТ"),
        ("IJS", "ИЖС"),
    ]
    plot = models.ForeignKey(
        "Plot", on_delete=models.CASCADE, related_name="lands", verbose_name="Застройка"
    )
    land_type = models.CharField(
        max_length=3, choices=LAND_TYPE_CHOICES, verbose_name="Тип участка"
    )
    area = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Площадь участка (в сотках)"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за участок"
    )
    path = models.CharField(max_length=100, verbose_name="Путь", blank=True)

    # Дополнительные поля для участка
    gas = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Газ",
        default="нет",
    )
    electricity = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Свет",
        default="нет",
    )
    water = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Вода",
        default="нет",
    )
    sewage = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Стоки",
        default="нет",
    )
    developed = models.BooleanField(default=False, verbose_name="Разработан")

    # Обязательные изображения
    image_1 = models.ImageField(
        upload_to="plots/lands/", verbose_name="Изображение 1", blank=True, null=True
    )
    image_2 = models.ImageField(
        upload_to="plots/lands/", verbose_name="Изображение 2", blank=True, null=True
    )
    image_3 = models.ImageField(
        upload_to="plots/lands/", verbose_name="Изображение 3", blank=True, null=True
    )
    image_4 = models.ImageField(
        upload_to="plots/lands/", verbose_name="Изображение 4", blank=True, null=True
    )
    image_5 = models.ImageField(
        upload_to="plots/lands/", verbose_name="Изображение 5", blank=True, null=True
    )

    class Meta:
        verbose_name = "Участок"
        verbose_name_plural = "Участки"

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = self.land_type
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_land_type_display()} - {self.plot.district}"


class PlotLandImage(ImageBase):
    plot_land = models.ForeignKey(
        "PlotLand",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Участок",
    )

    class Meta:
        verbose_name = "Изображение участка"
        verbose_name_plural = "Изображения участков"

    def get_parent_instance(self):
        return self.plot_land


class PlotLandSection(models.Model):
    STATUS_CHOICES = [
        ("privatized", "Приватизированный"),
        ("settlement", "Земли населенных пунктов"),
    ]

    plot_land = models.ForeignKey(
        "PlotLand",
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name="Участок",
    )
    title = models.CharField(max_length=255, verbose_name="Название секции")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Площадь")
    land_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        verbose_name="Статус земли",
        default="privatized",
    )
    gas = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Газ",
        default="нет",
    )
    electricity = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Свет",
        default="нет",
    )
    water = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Вода",
        default="нет",
    )
    sewage = models.CharField(
        max_length=20,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("возможность", "Есть возможность подключения"),
        ],
        verbose_name="Стоки",
        default="нет",
    )
    image_1 = models.ImageField(
        upload_to="plot_land_sections/",
        verbose_name="Изображение 1",
        blank=True,
        null=True,
    )
    image_2 = models.ImageField(
        upload_to="plot_land_sections/",
        verbose_name="Изображение 2",
        blank=True,
        null=True,
    )
    image_3 = models.ImageField(
        upload_to="plot_land_sections/",
        verbose_name="Изображение 3",
        blank=True,
        null=True,
    )
    image_4 = models.ImageField(
        upload_to="plot_land_sections/",
        verbose_name="Изображение 4",
        blank=True,
        null=True,
    )
    image_5 = models.ImageField(
        upload_to="plot_land_sections/",
        verbose_name="Изображение 5",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Секция участка"
        verbose_name_plural = "Секции участков"

    def __str__(self):
        return self.title


class DynamicFormSubmission(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название формы")
    data = models.JSONField(verbose_name="Данные формы")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Отправка формы"
        verbose_name_plural = "Отправки форм"

    def __str__(self):
        return f"{self.name} - {self.submitted_at}"
