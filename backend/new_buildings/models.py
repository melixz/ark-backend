from django.db import models


class NewBuilding(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    bgr_image = models.ImageField(
        upload_to="new_buildings/",
        blank=True,
        null=True,
        verbose_name="Фоновое изображение",
    )
    path = models.TextField(verbose_name="Путь")
    class_name = models.CharField(
        max_length=100, verbose_name="Класс контента", default=""
    )

    def __str__(self):
        return self.name

    @property
    def routes(self):
        return [
            {
                "path": f"{self.path}/details",
                "element": f"<{self.name.replace(' ', '')}DetailsPage />",
            }
        ]

    class Meta:
        verbose_name = "Новостройки"
        verbose_name_plural = "Новостройки"
