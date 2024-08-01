# Generated by Django 5.0.7 on 2024-07-29 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Footer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "telegram_icon",
                    models.ImageField(blank=True, null=True, upload_to="icons/"),
                ),
                (
                    "whatsapp_icon",
                    models.ImageField(blank=True, null=True, upload_to="icons/"),
                ),
                (
                    "viber_icon",
                    models.ImageField(blank=True, null=True, upload_to="icons/"),
                ),
                (
                    "vk_icon",
                    models.ImageField(blank=True, null=True, upload_to="icons/"),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="mainsection",
            options={"ordering": ["title"]},
        ),
        migrations.RemoveField(
            model_name="header",
            name="telegram_icon",
        ),
        migrations.RemoveField(
            model_name="header",
            name="viber_icon",
        ),
        migrations.RemoveField(
            model_name="header",
            name="whatsapp_icon",
        ),
        migrations.RemoveField(
            model_name="mainsection",
            name="content",
        ),
        migrations.AddField(
            model_name="header",
            name="phone_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="mainsection",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="main_sections/"),
        ),
        migrations.AddField(
            model_name="mainsection",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="main_sections/"
                    ),
                ),
                (
                    "main_section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contents",
                        to="main_page.mainsection",
                    ),
                ),
            ],
        ),
    ]