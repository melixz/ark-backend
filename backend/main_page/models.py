from django.db import models


class CustomManager(models.Manager):
    def custom_method(self):
        pass


class Header(models.Model):
    left_image = models.ImageField(upload_to='images/')
    left_alt = models.CharField(max_length=255)
    center_text = models.CharField(max_length=255)
    right_buttons = models.JSONField()
    objects = CustomManager()


class MainSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    objects = CustomManager()


class FooterSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    objects = CustomManager()
