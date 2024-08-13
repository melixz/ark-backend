from django.db import models


class Plot(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to="plots/", verbose_name="Изображение")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    area = models.CharField(max_length=100, verbose_name="Площадь")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание")
    path = models.TextField(verbose_name="Путь")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Участок под застройку"
        verbose_name_plural = "Участки под застройку"
