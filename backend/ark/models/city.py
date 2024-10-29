from django.db import models
from slugify import slugify


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
