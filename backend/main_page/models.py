from django.db import models
from django.utils.translation import gettext as _


class Header(models.Model):
    logo_icon = models.ImageField(
        upload_to="logos/", blank=True, null=True, verbose_name=_("Логотип")
    )
    phone_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name=_("Иконка телефона")
    )
    phone_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Номер телефона")
    )
    header_bgr = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True, verbose_name=_("Фон заголовка")
    )
    header_title = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Заголовок")
    )
    header_title_bottom = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Подзаголовок")
    )
    nav_bgr = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True, verbose_name=_("Фон навигации")
    )
    bgr_bottom = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True, verbose_name=_("Нижний фон")
    )

    def __str__(self):
        return self.header_title or _("Header")

    class Meta:
        verbose_name = _("Заголовок")
        verbose_name_plural = _("Заголовки")
        ordering = ["header_title"]


class MainContent(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    bgr_image = models.ImageField(
        upload_to="content/",
        blank=True,
        null=True,
        verbose_name=_("Фоновое изображение"),
    )
    path = models.TextField(verbose_name=_("Путь"))
    class_name = models.CharField(
        max_length=100, verbose_name=_("Класс контента"), default=""
    )

    def __str__(self):
        return self.name

    @property
    def routes(self):
        return [
            {
                "path": f"{self.path}/details",
                "element": f"<{self.name.replace(' ', '')}DetailsPage />",
            }
        ]

    class Meta:
        verbose_name = _("Основное содержание")
        verbose_name_plural = _("Основное содержание")
        ordering = ["name"]


class Advantages(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    desc = models.TextField(blank=True, null=True, verbose_name=_("Описание"))
    climate = models.CharField(max_length=255, verbose_name=_("Климат"))
    nature = models.CharField(max_length=255, verbose_name=_("Природа"))
    accessibility = models.CharField(max_length=255, verbose_name=_("Доступность"))
    infrastructure = models.CharField(max_length=255, verbose_name=_("Инфраструктура"))
    possibilities = models.CharField(max_length=255, verbose_name=_("Возможности"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Преимущества")
        verbose_name_plural = _("Преимущества")
        ordering = ["title"]


class Card(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    description = models.TextField(verbose_name=_("Описание"))
    path = models.TextField(verbose_name=_("Путь"))
    image = models.ImageField(upload_to="cards/", verbose_name=_("Изображение"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Карточка")
        verbose_name_plural = _("Карточки")
        ordering = ["title"]


class Footer(models.Model):
    telegram_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name=_("Иконка Telegram")
    )
    whatsapp_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name=_("Иконка WhatsApp")
    )
    viber_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name=_("Иконка Viber")
    )
    youtube_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name=_("Иконка YouTube")
    )
    vk_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name=_("Иконка VK")
    )
    phone_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Номер телефона")
    )
    color_text = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Цвет текста")
    )

    def __str__(self):
        return self.phone_number or _("Footer")

    class Meta:
        verbose_name = _("Футер")
        verbose_name_plural = _("Футеры")
        ordering = ["phone_number"]
