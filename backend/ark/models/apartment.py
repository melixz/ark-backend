from django.db import models
from .base import ImageBase
from .complex import Complex
from .city import City


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
        unique_together = ("complex", "path")

    def generate_sequential_path(self):
        """Генерация уникального пути на основе категории и последовательного номера внутри комплекса."""
        apartment_count = 1
        new_path = f"{self.category}-{apartment_count}"

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
