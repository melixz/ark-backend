# Generated by Django 4.1 on 2024-09-03 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="path",
            field=models.CharField(default="", max_length=100, verbose_name="Путь"),
        ),
        migrations.AddField(
            model_name="plotland",
            name="path",
            field=models.CharField(default="", max_length=100, verbose_name="Путь"),
        ),
    ]
