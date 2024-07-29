from django.db import models


class Header(models.Model):
    logo_icon = models.ImageField(
        upload_to="logos/", blank=True, null=True, verbose_name="Логотип"
    )
    phone_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name="Иконка телефона"
    )
    phone_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Номер телефона"
    )
    header_bgr = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True, verbose_name="Фон заголовка"
    )
    header_title = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Заголовок"
    )
    header_title_bottom = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Подзаголовок"
    )
    nav_bgr = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True, verbose_name="Фон навигации"
    )
    bgr_bottom = models.ImageField(
        upload_to="backgrounds/", blank=True, null=True, verbose_name="Нижний фон"
    )

    def __str__(self):
        return self.header_title or "Header"

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"


class MainContent(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    bgr_image = models.ImageField(
        upload_to="content/", blank=True, null=True, verbose_name="Фоновое изображение"
    )
    path = models.TextField(verbose_name="Путь")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Основное содержание"
        verbose_name_plural = "Основные содержания"


class SectionOne(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    desc = models.TextField(blank=True, null=True, verbose_name="Описание")
    climate = models.CharField(max_length=255, verbose_name="Климат")
    nature = models.CharField(max_length=255, verbose_name="Природа")
    accessibility = models.CharField(max_length=255, verbose_name="Доступность")
    infrastructure = models.CharField(max_length=255, verbose_name="Инфраструктура")
    possibilities = models.CharField(max_length=255, verbose_name="Возможности")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Раздел 1"
        verbose_name_plural = "Разделы 1"


class SectionTwoCard(models.Model):
    icon = models.ImageField(upload_to="icons/", verbose_name="Иконка")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    background = models.ImageField(upload_to="backgrounds/", verbose_name="Фон")
    button_text = models.CharField(max_length=255, verbose_name="Текст кнопки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка раздела 2"
        verbose_name_plural = "Карточки раздела 2"


class SectionTwo(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    cards = models.ManyToManyField(SectionTwoCard, verbose_name="Карточки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Раздел 2"
        verbose_name_plural = "Разделы 2"


class SectionThree(models.Model):
    image = models.ImageField(upload_to="backgrounds/", verbose_name="Изображение")
    tg_link = models.URLField(max_length=200, verbose_name="Ссылка Telegram")
    viber_link = models.URLField(max_length=200, verbose_name="Ссылка Viber")
    whatsup_link = models.URLField(max_length=200, verbose_name="Ссылка WhatsApp")
    bgr_button = models.ImageField(upload_to="backgrounds/", verbose_name="Фон кнопки")

    def __str__(self):
        return "Раздел 3"

    class Meta:
        verbose_name = "Раздел 3"
        verbose_name_plural = "Разделы 3"


class Footer(models.Model):
    telegram_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name="Иконка Telegram"
    )
    whatsapp_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name="Иконка WhatsApp"
    )
    viber_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name="Иконка Viber"
    )
    youtube_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name="Иконка YouTube"
    )
    vk_icon = models.ImageField(
        upload_to="icons/", blank=True, null=True, verbose_name="Иконка VK"
    )
    phone_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Номер телефона"
    )
    color_text = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Цвет текста"
    )

    def __str__(self):
        return self.phone_number or "Footer"

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футеры"
