# Generated by Django 5.0.7 on 2024-08-30 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0005_remove_city_new_text_remove_city_plot_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="city",
            name="desc",
        ),
        migrations.RemoveField(
            model_name="city",
            name="title",
        ),
    ]
