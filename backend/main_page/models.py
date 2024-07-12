from django.db import models


class Header(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    navigation_background_color = models.CharField(max_length=7, blank=True, null=True)
    telegram_icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    whatsapp_icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    viber_icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    phone_icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    header_background = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or 'Header'


class MainSection(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
