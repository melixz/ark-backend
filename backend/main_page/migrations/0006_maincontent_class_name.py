# Generated by Django 5.0.7 on 2024-08-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0005_alter_footer_options_alter_header_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="maincontent",
            name="class_name",
            field=models.CharField(
                default="", max_length=100, verbose_name="Класс контента"
            ),
        ),
    ]
