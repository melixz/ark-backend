import os
from io import BytesIO
from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from PIL import Image


class ImageBase(models.Model):
    IMAGE_TYPE_CHOICES = [
        ("slider_image", "Картинка для слайдера"),
        ("additional_image", "Дополнительное изображение"),
    ]
    image = models.ImageField(
        upload_to="images/", verbose_name="Изображение", blank=True, null=True
    )
    image_type = models.CharField(
        max_length=40,
        choices=IMAGE_TYPE_CHOICES,
        verbose_name="Тип изображения",
        blank=True,
        null=True,
    )
    parent_field_name = None

    class Meta:
        abstract = True

    def get_parent_instance(self):
        return getattr(self, self.parent_field_name, None)

    def save(self, *args, **kwargs):
        if not self.pk:
            parent_instance = self.get_parent_instance()
            if parent_instance and self.image_type:
                image_count = self.__class__.objects.filter(
                    **{self.parent_field_name: parent_instance},
                    image_type=self.image_type,
                ).count()
                if image_count >= 10:
                    raise ValidationError(
                        f"Для категории '{self.get_image_type_display()}' можно загрузить до 10 изображений."
                    )
        super().save(*args, **kwargs)
        self.process_image()

    def process_image(self):
        if not self.image:
            return
        try:
            with Image.open(self.image.path) as img:
                img_format = img.format
                if img_format not in ["JPEG", "PNG", "WEBP"]:
                    img_format = "JPEG"

                if img.mode in ("RGBA", "LA") or (
                    img.mode == "P" and "transparency" in img.info
                ):
                    if img_format != "WEBP":
                        img = img.convert("RGBA")
                        img_format = "PNG"

                max_size = (1920, 1080)
                img.thumbnail(max_size, Image.LANCZOS)

                buffer = BytesIO()
                img.save(buffer, format=img_format, quality=85)
                buffer.seek(0)

                extension = "jpg" if img_format == "JPEG" else img_format.lower()
                new_name = f"{os.path.splitext(self.image.name)[0]}.{extension}"

                self.image.save(new_name, ContentFile(buffer.getvalue()), save=False)
                super().save(update_fields=["image"])
        except Exception as e:
            print(f"Ошибка обработки изображения: {e}")

    def __str__(self):
        return f"{self.get_parent_instance()} - {self.get_image_type_display()}"
