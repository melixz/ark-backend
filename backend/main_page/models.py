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
    class_name = models.CharField(
        max_length=100, verbose_name="Класс контента", default=""
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


class Card(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    link = models.URLField(max_length=200, verbose_name="Ссылка")
    image = models.ImageField(upload_to="cards/", verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"


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
