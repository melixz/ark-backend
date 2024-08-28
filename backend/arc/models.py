from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название города")
    path = models.CharField(max_length=100, verbose_name="Путь", default="")
    image = models.ImageField(upload_to="cities/", verbose_name="Изображение", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок", default="", blank=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Complex(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="complexes", verbose_name="Город")
    name = models.CharField(max_length=200, verbose_name="Название комплекса")
    path = models.CharField(max_length=100, verbose_name="Путь", default="")
    studia = models.PositiveIntegerField(verbose_name="Количество студий", default=0)
    one = models.PositiveIntegerField(verbose_name="Количество 1-комнатных квартир", default=0)
    two = models.PositiveIntegerField(verbose_name="Количество 2-комнатных квартир", default=0)
    three = models.PositiveIntegerField(verbose_name="Количество 3-комнатных квартир", default=0)

    class Meta:
        verbose_name = "Комплекс"
        verbose_name_plural = "Комплексы"

    def __str__(self):
        return self.name


class Section(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="sections", verbose_name="Город")
    title = models.CharField(max_length=255, verbose_name="Заголовок", blank=True, null=True)
    desc = models.TextField(verbose_name="Описание", blank=True, null=True)
    image_1 = models.ImageField(upload_to="sections/", verbose_name="Изображение 1", blank=True, null=True)
    image_2 = models.ImageField(upload_to="sections/", verbose_name="Изображение 2", blank=True, null=True)
    image_3 = models.ImageField(upload_to="sections/", verbose_name="Изображение 3", blank=True, null=True)
    loc = models.CharField(max_length=255, verbose_name="Локация", blank=True, null=True)

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

    def __str__(self):
        return self.title or f"{self.city.name} - {self.loc}"
