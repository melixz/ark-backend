# Generated by Django 4.1 on 2024-09-05 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0009_contactrequest"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contactrequest",
            options={
                "verbose_name": "Форма обратной связи",
                "verbose_name_plural": "Форма обратной связи",
            },
        ),
    ]
