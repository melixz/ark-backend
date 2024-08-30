from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название города")
    path = models.CharField(max_length=100, verbose_name="Путь", default="")
    image = models.ImageField(upload_to="cities/", verbose_name="Изображение", blank=True, null=True)
    new_title = models.CharField(max_length=255, verbose_name="Заголовок для новостройки", blank=True, null=True)
    new_desc = models.TextField(verbose_name="Описание для новостройки", blank=True, null=True)
    plot_title = models.CharField(max_length=255, verbose_name="Заголовок для застройки", blank=True, null=True)
    plot_desc = models.TextField(verbose_name="Описание для застройки", blank=True, null=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def clean(self):
        if not (self.new_title and self.new_desc) and not (self.plot_title and self.plot_desc):
            raise ValidationError(
                "Вы должны заполнить либо 'Заголовок для новостройки' и 'Описание для новостройки', либо 'Заголовок для застройки' и 'Описание для застройки'.")

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


class Plot(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="plots", verbose_name="Город")
    district = models.CharField(max_length=200, verbose_name="Район", blank=True)
    path = models.CharField(max_length=100, verbose_name="Путь", default="")

    class Meta:
        verbose_name = "Застройка"
        verbose_name_plural = "Застройки"

    def save(self, *args, **kwargs):
        if self.district and not self.district.startswith("Район -"):
            self.district = f"Район - {self.district}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.district


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


class Apartment(models.Model):
    CATEGORY_CHOICES = [
        ("studio", "Студия"),
        ("one_bedroom", "Однокомнатная"),
        ("two_bedroom", "Двухкомнатная"),
        ("three_bedroom", "Трехкомнатная"),
    ]
    complex = models.ForeignKey("Complex", on_delete=models.CASCADE, related_name="apartments", verbose_name="Комплекс")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория")

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"

    def __str__(self):
        return f"{self.get_category_display()} - {self.complex.name}"


class ApartmentImage(models.Model):
    APARTMENT_IMAGE_TYPE_CHOICES = [
        ("floor_plan", "Схема квартиры"),
        ("slider_image", "Картинка для слайдера"),
    ]
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="images", verbose_name="Квартира")
    image = models.ImageField(upload_to="apartments/images/", verbose_name="Изображение")
    image_type = models.CharField(max_length=20, choices=APARTMENT_IMAGE_TYPE_CHOICES, verbose_name="Тип изображения")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def clean(self):
        if self.image_type == "floor_plan" and ApartmentImage.objects.filter(apartment=self.apartment,
                                                                             image_type="floor_plan").count() >= 10:
            raise ValidationError("Для категории 'Схема квартиры' можно загрузить только 10 изображений.")
        elif self.image_type == "slider_image" and ApartmentImage.objects.filter(apartment=self.apartment,
                                                                                 image_type="slider_image").count() >= 10:
            raise ValidationError("Для категории 'Картинка для слайдера' можно загрузить до 10 изображений.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.image.path, quality=70, optimize=True)

    def __str__(self):
        return f"{self.apartment} - {self.get_image_type_display()}"
