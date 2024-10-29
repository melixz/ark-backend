from django.db import models
from .base import ImageBase
from .plot import Plot


class PlotLand(models.Model):
    """Модель земельного участка в застройке."""

    LAND_TYPE_CHOICES = [("SNT", "СНТ"), ("IJS", "ИЖС")]

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
        land_count = 1
        new_path = f"{self.land_type}-{land_count}"

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
