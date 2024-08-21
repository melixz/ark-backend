from django.db import models


class Developer(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    path = models.CharField(max_length=255, verbose_name="Путь")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Застройщик"
        verbose_name_plural = "Застройщики"
