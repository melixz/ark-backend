# Generated by Django 5.0.4 on 2024-09-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ark", "0002_alter_apartment_path_alter_complex_path_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartmentsection",
            name="apartment_number",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Номер квартиры"
            ),
        ),
    ]
