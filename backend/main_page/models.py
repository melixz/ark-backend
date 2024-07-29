from django.db import models


class Header(models.Model):
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    navigation_background_color = models.CharField(max_length=7, blank=True, null=True)
    phone_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    header_background = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Header"


class MainSection(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="main_sections/", null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Content(models.Model):
    main_section = models.ForeignKey(
        MainSection, related_name="contents", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="main_sections/", null=True, blank=True)

    def __str__(self):
        return self.title


class Footer(models.Model):
    telegram_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    whatsapp_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    viber_icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    vk_icon = models.ImageField(upload_to="icons/", blank=True, null=True)

    def __str__(self):
        return self.title or "Footer"
