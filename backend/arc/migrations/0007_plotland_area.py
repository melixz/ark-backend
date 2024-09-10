# Generated by Django 4.1 on 2024-09-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0006_plotland_developed_plotland_electricity_plotland_gas_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="plotland",
            name="area",
            field=models.DecimalField(
                decimal_places=2,
                default=1,
                max_digits=5,
                verbose_name="Площадь участка (в сотках)",
            ),
            preserve_default=False,
        ),
    ]
