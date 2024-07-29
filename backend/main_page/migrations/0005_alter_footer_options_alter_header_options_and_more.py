# Generated by Django 5.0.7 on 2024-07-29 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0004_rename_section1_sectionone_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="footer",
            options={"verbose_name": "Футер", "verbose_name_plural": "Футеры"},
        ),
        migrations.AlterModelOptions(
            name="header",
            options={"verbose_name": "Заголовок", "verbose_name_plural": "Заголовки"},
        ),
        migrations.AlterModelOptions(
            name="maincontent",
            options={
                "verbose_name": "Основное содержание",
                "verbose_name_plural": "Основные содержания",
            },
        ),
        migrations.AlterModelOptions(
            name="sectionone",
            options={"verbose_name": "Раздел 1", "verbose_name_plural": "Разделы 1"},
        ),
        migrations.AlterModelOptions(
            name="sectionthree",
            options={"verbose_name": "Раздел 3", "verbose_name_plural": "Разделы 3"},
        ),
        migrations.AlterModelOptions(
            name="sectiontwo",
            options={"verbose_name": "Раздел 2", "verbose_name_plural": "Разделы 2"},
        ),
        migrations.AlterModelOptions(
            name="sectiontwocard",
            options={
                "verbose_name": "Карточка раздела 2",
                "verbose_name_plural": "Карточки раздела 2",
            },
        ),
        migrations.RemoveField(
            model_name="maincontent",
            name="url",
        ),
        migrations.AddField(
            model_name="maincontent",
            name="path",
            field=models.TextField(default=1, verbose_name="Путь"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="footer",
            name="color_text",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Цвет текста"
            ),
        ),
        migrations.AlterField(
            model_name="footer",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Номер телефона"
            ),
        ),
        migrations.AlterField(
            model_name="footer",
            name="telegram_icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="icons/",
                verbose_name="Иконка Telegram",
            ),
        ),
        migrations.AlterField(
            model_name="footer",
            name="viber_icon",
            field=models.ImageField(
                blank=True, null=True, upload_to="icons/", verbose_name="Иконка Viber"
            ),
        ),
        migrations.AlterField(
            model_name="footer",
            name="vk_icon",
            field=models.ImageField(
                blank=True, null=True, upload_to="icons/", verbose_name="Иконка VK"
            ),
        ),
        migrations.AlterField(
            model_name="footer",
            name="whatsapp_icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="icons/",
                verbose_name="Иконка WhatsApp",
            ),
        ),
        migrations.AlterField(
            model_name="footer",
            name="youtube_icon",
            field=models.ImageField(
                blank=True, null=True, upload_to="icons/", verbose_name="Иконка YouTube"
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="bgr_bottom",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="backgrounds/",
                verbose_name="Нижний фон",
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="header_bgr",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="backgrounds/",
                verbose_name="Фон заголовка",
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="header_title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Заголовок"
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="header_title_bottom",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Подзаголовок"
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="logo_icon",
            field=models.ImageField(
                blank=True, null=True, upload_to="logos/", verbose_name="Логотип"
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="nav_bgr",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="backgrounds/",
                verbose_name="Фон навигации",
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="phone_icon",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="icons/",
                verbose_name="Иконка телефона",
            ),
        ),
        migrations.AlterField(
            model_name="header",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Номер телефона"
            ),
        ),
        migrations.AlterField(
            model_name="maincontent",
            name="bgr_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="content/",
                verbose_name="Фоновое изображение",
            ),
        ),
        migrations.AlterField(
            model_name="maincontent",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="accessibility",
            field=models.CharField(max_length=255, verbose_name="Доступность"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="climate",
            field=models.CharField(max_length=255, verbose_name="Климат"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="desc",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="infrastructure",
            field=models.CharField(max_length=255, verbose_name="Инфраструктура"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="nature",
            field=models.CharField(max_length=255, verbose_name="Природа"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="possibilities",
            field=models.CharField(max_length=255, verbose_name="Возможности"),
        ),
        migrations.AlterField(
            model_name="sectionone",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="sectionthree",
            name="bgr_button",
            field=models.ImageField(
                upload_to="backgrounds/", verbose_name="Фон кнопки"
            ),
        ),
        migrations.AlterField(
            model_name="sectionthree",
            name="image",
            field=models.ImageField(
                upload_to="backgrounds/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="sectionthree",
            name="tg_link",
            field=models.URLField(verbose_name="Ссылка Telegram"),
        ),
        migrations.AlterField(
            model_name="sectionthree",
            name="viber_link",
            field=models.URLField(verbose_name="Ссылка Viber"),
        ),
        migrations.AlterField(
            model_name="sectionthree",
            name="whatsup_link",
            field=models.URLField(verbose_name="Ссылка WhatsApp"),
        ),
        migrations.AlterField(
            model_name="sectiontwo",
            name="cards",
            field=models.ManyToManyField(
                to="main_page.sectiontwocard", verbose_name="Карточки"
            ),
        ),
        migrations.AlterField(
            model_name="sectiontwo",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="sectiontwocard",
            name="background",
            field=models.ImageField(upload_to="backgrounds/", verbose_name="Фон"),
        ),
        migrations.AlterField(
            model_name="sectiontwocard",
            name="button_text",
            field=models.CharField(max_length=255, verbose_name="Текст кнопки"),
        ),
        migrations.AlterField(
            model_name="sectiontwocard",
            name="description",
            field=models.TextField(verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="sectiontwocard",
            name="icon",
            field=models.ImageField(upload_to="icons/", verbose_name="Иконка"),
        ),
        migrations.AlterField(
            model_name="sectiontwocard",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Заголовок"),
        ),
    ]
