# Generated by Django 5.0.7 on 2024-09-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0015_remove_city_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="section",
            name="desc",
        ),
        migrations.AddField(
            model_name="section",
            name="desc_1",
            field=models.TextField(blank=True, null=True, verbose_name="Описание 1"),
        ),
        migrations.AddField(
            model_name="section",
            name="desc_2",
            field=models.TextField(blank=True, null=True, verbose_name="Описание 2"),
        ),
    ]
