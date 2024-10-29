from django.db import models
from slugify import slugify
from .base import ImageBase
from .city import City


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
