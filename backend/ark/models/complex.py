from django.db import models
from slugify import slugify
from .base import ImageBase
from .city import City


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
    parent_field_name = "complex"

    class Meta:
        verbose_name = "Изображение комплекса"
        verbose_name_plural = "Изображения комплексов"

    def get_parent_instance(self):
        return self.complex
