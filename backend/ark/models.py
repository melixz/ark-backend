import os
from io import BytesIO
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from PIL import Image
from slugify import slugify


class ImageBase(models.Model):
    IMAGE_TYPE_CHOICES = [
        ("slider_image", "Картинка для слайдера"),
        ("additional_image", "Дополнительное изображение"),
    ]
    image = models.ImageField(
        upload_to="images/", verbose_name="Изображение", blank=True, null=True
    )
    image_type = models.CharField(
        max_length=40,
        choices=IMAGE_TYPE_CHOICES,
        verbose_name="Тип изображения",
        blank=True,
        null=True,
    )
    parent_field_name = None

    class Meta:
        abstract = True

    def get_parent_instance(self):
        return getattr(self, self.parent_field_name, None)

    def save(self, *args, **kwargs):
        if not self.pk:
            parent_instance = self.get_parent_instance()
            if parent_instance and self.image_type:
                image_count = self.__class__.objects.filter(
                    **{self.parent_field_name: parent_instance},
                    image_type=self.image_type,
                ).count()
                if image_count >= 10:
                    raise ValidationError(
                        f"Для категории '{self.get_image_type_display()}' можно загрузить до 10 изображений."
                    )
        super().save(*args, **kwargs)
        self.process_image()

    def process_image(self):
        if not self.image:
            return
        try:
            with Image.open(self.image.path) as img:
                img_format = img.format
                if img_format not in ["JPEG", "PNG", "WEBP"]:
                    img_format = "JPEG"

                if img.mode in ("RGBA", "LA") or (
                    img.mode == "P" and "transparency" in img.info
                ):
                    if img_format != "WEBP":
                        img = img.convert("RGBA")
                        img_format = "PNG"

                max_size = (1920, 1080)
                img.thumbnail(max_size, Image.LANCZOS)

                buffer = BytesIO()
                img.save(buffer, format=img_format, quality=85)
                buffer.seek(0)

                extension = "jpg" if img_format == "JPEG" else img_format.lower()
                new_name = f"{os.path.splitext(self.image.name)[0]}.{extension}"

                self.image.save(new_name, ContentFile(buffer.getvalue()), save=False)
                super().save(update_fields=["image"])
        except Exception as e:
            print(f"Ошибка обработки изображения: {e}")

    def __str__(self):
        return f"{self.get_parent_instance()} - {self.get_image_type_display()}"


class City(models.Model):
    """Модель города, содержащая информацию о новостройках и застройках."""

    name = models.CharField(
        max_length=100, verbose_name="Название города", blank=False, null=False
    )
    path = models.CharField(
        max_length=100, verbose_name="Путь", default="", blank=False, null=False
    )
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
        """Переопределение метода save для автоматического формирования пути."""
        if not self.path:
            self.path = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Complex(models.Model):
    """Модель жилого комплекса."""

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="complexes", verbose_name="Город"
    )
    name = models.CharField(
        max_length=400, verbose_name="Название комплекса", blank=False, null=False
    )
    title = models.CharField(
        max_length=255, verbose_name="Заголовок", blank=True, null=True
    )
    desk = models.TextField(verbose_name="Описание", blank=True, null=True)
    path = models.CharField(
        max_length=100, verbose_name="Путь", blank=False, null=False
    )
    card_bg = models.ImageField(
        upload_to="complexes/cards/",
        verbose_name="Фон карточки в слайдере",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Комплекс"
        verbose_name_plural = "Комплексы"
        unique_together = ("city", "path")

    def save(self, *args, **kwargs):
        """Переопределение метода save для автоматического формирования пути."""
        if not self.path:
            self.path = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ComplexImage(ImageBase):
    """Модель изображений для комплекса."""

    complex = models.ForeignKey(
        Complex,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Комплекс",
    )
    parent_field_name = "complex"  # Указание на поле родителя

    class Meta:
        verbose_name = "Изображение комплекса"
        verbose_name_plural = "Изображения комплексов"

    def get_parent_instance(self):
        return self.complex


class Plot(models.Model):
    """Модель застройки."""

    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="plots", verbose_name="Город"
    )
    district = models.CharField(
        max_length=400, verbose_name="Район", blank=False, null=False
    )
    title = models.CharField(
        max_length=255, verbose_name="Заголовок", blank=True, null=True
    )
    desk = models.TextField(verbose_name="Описание", blank=True, null=True)
    path = models.CharField(
        max_length=100, verbose_name="Путь", blank=False, null=False
    )
    card_bg = models.ImageField(
        upload_to="plots/cards/",
        verbose_name="Фон карточки в слайдере",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Застройка"
        verbose_name_plural = "Застройки"
        unique_together = ("city", "path")

    def save(self, *args, **kwargs):
        """Переопределение метода save для автоматического формирования пути."""
        if not self.path:
            self.path = slugify(self.district)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.district


class PlotImage(ImageBase):
    """Модель изображений для застройки."""

    plot = models.ForeignKey(
        Plot, on_delete=models.CASCADE, related_name="images", verbose_name="Застройка"
    )
    parent_field_name = "plot"

    class Meta:
        verbose_name = "Изображение застройки"
        verbose_name_plural = "Изображения застроек"

    def get_parent_instance(self):
        return self.plot


class NewSection(models.Model):
    """Модель секции новостроек для города."""

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
    """Модель секции застроек для города."""

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
    """Модель квартиры в жилом комплексе."""

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
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория",
        blank=False,
        null=False,
    )
    path = models.CharField(
        max_length=100, verbose_name="Путь", blank=False, null=False
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок квартиры")
    desk = models.TextField(verbose_name="Описание", blank=True, null=True)
    floor_count = models.PositiveIntegerField(
        verbose_name="Количество этажей", blank=True, null=True
    )

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        unique_together = (
            "complex",
            "path",
        )  # Уникальность в пределах комплекса и пути

    def generate_sequential_path(self):
        """Генерация уникального пути на основе категории и последовательного номера внутри комплекса."""
        # Начинаем с номера 1
        apartment_count = 1
        new_path = f"{self.category}-{apartment_count}"

        # Проверяем, что сгенерированный путь уникален внутри данного комплекса и категории
        while Apartment.objects.filter(
            complex=self.complex, category=self.category, path=new_path
        ).exists():
            apartment_count += 1
            new_path = f"{self.category}-{apartment_count}"

        return new_path

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = self.generate_sequential_path()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_category_display()} - {self.complex.name}"


class ApartmentImage(ImageBase):
    """Модель изображений для квартиры."""

    apartment = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Квартира",
    )
    parent_field_name = "apartment"

    class Meta:
        verbose_name = "Изображение квартиры"
        verbose_name_plural = "Изображения квартир"

    def get_parent_instance(self):
        return self.apartment


class ApartmentSection(models.Model):
    """Модель секции внутри квартиры."""

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
    apartment_number = models.CharField(
        max_length=10, verbose_name="Номер квартиры", blank=True, null=True
    )
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
    """Модель земельного участка в застройке."""

    LAND_TYPE_CHOICES = [
        ("SNT", "СНТ"),
        ("IJS", "ИЖС"),
    ]

    plot = models.ForeignKey(
        Plot, on_delete=models.CASCADE, related_name="lands", verbose_name="Застройка"
    )
    land_type = models.CharField(
        max_length=3,
        choices=LAND_TYPE_CHOICES,
        verbose_name="Тип участка",
        blank=False,
        null=False,
    )
    area = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Площадь участка (в сотках)",
        blank=False,
        null=False,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за участок",
        blank=False,
        null=False,
    )
    path = models.CharField(
        max_length=100, verbose_name="Путь", blank=False, null=False
    )
    gas = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Газ",
        default="нет",
    )
    electricity = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Свет",
        default="нет",
    )
    water = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Вода",
        default="нет",
    )
    sewage = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Стоки",
        default="нет",
    )
    developed = models.BooleanField(default=False, verbose_name="Разработан")
    title = models.CharField(max_length=255, verbose_name="Заголовок участка")
    desk = models.TextField(verbose_name="Описание", blank=True, null=True)
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
        unique_together = ("plot", "path")

    def generate_sequential_path(self):
        """Генерация уникального пути на основе последовательного номера для каждого типа участка в пределах одной застройки."""
        # Начинаем с номера 1
        land_count = 1
        new_path = f"{self.land_type}-{land_count}"

        # Проверяем, что сгенерированный путь уникален внутри данной застройки и типа участка
        while PlotLand.objects.filter(
            plot=self.plot, land_type=self.land_type, path=new_path
        ).exists():
            land_count += 1
            new_path = f"{self.land_type}-{land_count}"

        return new_path

    def save(self, *args, **kwargs):
        if not self.path:
            self.path = self.generate_sequential_path()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_land_type_display()} - {self.plot.district}"


class PlotLandImage(ImageBase):
    """Модель изображений для земельного участка."""

    plot_land = models.ForeignKey(
        PlotLand,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Участок",
    )
    parent_field_name = "plot_land"

    class Meta:
        verbose_name = "Изображение участка"
        verbose_name_plural = "Изображения участков"

    def get_parent_instance(self):
        return self.plot_land


class PlotLandSection(models.Model):
    """Модель секции внутри земельного участка."""

    STATUS_CHOICES = [
        ("privatized", "Приватизированный"),
        ("settlement", "Земли населенных пунктов"),
    ]

    plot_land = models.ForeignKey(
        PlotLand,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name="Участок",
    )
    title = models.CharField(max_length=255, verbose_name="Название секции")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Площадь")
    land_status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        verbose_name="Статус земли",
        default="privatized",
    )
    gas = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Газ",
        default="нет",
    )
    electricity = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Свет",
        default="нет",
    )
    water = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
        ],
        verbose_name="Вода",
        default="нет",
    )
    sewage = models.CharField(
        max_length=40,
        choices=[
            ("да", "Да"),
            ("нет", "Нет"),
            ("Есть возможность подключения", "Есть возможность подключения"),
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
    """Модель для хранения отправок динамических форм."""

    name = models.CharField(max_length=255, verbose_name="Название формы")
    data = models.JSONField(
        verbose_name="Данные формы"
    )  # Поле для хранения данных формы в виде JSON
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    class Meta:
        verbose_name = "Отправка формы"
        verbose_name_plural = "Отправки форм"

    def __str__(self):
        return f"{self.name} - {self.submitted_at}"
