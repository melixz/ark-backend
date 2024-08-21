# Generated by Django 5.0.7 on 2024-08-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Developer",
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
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                ("description", models.TextField(verbose_name="Описание")),
                ("path", models.CharField(max_length=255, verbose_name="Путь")),
            ],
            options={
                "verbose_name": "Застройщик",
                "verbose_name_plural": "Застройщики",
            },
        ),
    ]