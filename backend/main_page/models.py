from django.db import models


class Header(models.Model):
    left_image = models.ImageField(upload_to='images/')
    left_alt = models.CharField(max_length=255)
    center_text = models.CharField(max_length=255)
    right_buttons = models.JSONField()  # Assuming right_buttons is a JSON field containing buttons info


class MainSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()


class FooterSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
