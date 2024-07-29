from django.db import models


class Header(models.Model):
    logo_icon = models.ImageField(upload_to="logos/", blank=True, null=True)
    phone_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    header_bgr = models.ImageField(upload_to="backgrounds/", blank=True, null=True)
    header_title = models.CharField(max_length=255, blank=True, null=True)
    header_title_bottom = models.CharField(max_length=255, blank=True, null=True)
    nav_bgr = models.ImageField(upload_to="backgrounds/", blank=True, null=True)
    bgr_bottom = models.ImageField(upload_to="backgrounds/", blank=True, null=True)

    def __str__(self):
        return self.header_title or "Header"


class MainContent(models.Model):
    name = models.CharField(max_length=255)
    bgr_image = models.ImageField(upload_to="content/", blank=True, null=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Section1(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    climate = models.CharField(max_length=255)
    nature = models.CharField(max_length=255)
    assessability = models.CharField(max_length=255)
    infrastructure = models.CharField(max_length=255)
    possibilities = models.CharField(max_length=255)


class Section2Card(models.Model):
    icon = models.ImageField(upload_to="icons/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    background = models.ImageField(upload_to="backgrounds/")
    button_text = models.CharField(max_length=255)


class Section2(models.Model):
    title = models.CharField(max_length=255)
    cards = models.ManyToManyField(Section2Card)


class Section3(models.Model):
    image = models.ImageField(upload_to="backgrounds/")
    tg_link = models.URLField(max_length=200)
    viber_link = models.URLField(max_length=200)
    whatsup_link = models.URLField(max_length=200)
    bgr_button = models.ImageField(upload_to="backgrounds/")


class Footer(models.Model):
    telegram_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    whatsapp_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    viber_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    youtube_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    vk_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    color_text = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.phone_number or "Footer"
