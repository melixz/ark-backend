from django.db import models


class Header(models.Model):
    objects = models.Manager(
        left_image=models.ImageField(upload_to='images/'))
    left_alt = models.CharField(max_length=255)
    center_text = models.CharField(max_length=255)
    right_buttons = models.JSONField()


class MainSection(models.Model):
    objects = models.Manager(
        title=models.CharField(max_length=255))
    content = models.TextField()


class FooterSection(models.Model):
    objects = models.Manager(
        title=models.CharField(max_length=255))
    content = models.TextField()
