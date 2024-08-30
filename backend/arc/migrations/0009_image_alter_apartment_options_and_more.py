# Generated by Django 5.0.7 on 2024-08-30 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0008_apartment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="images/")),
                ("description", models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name="apartment",
            options={},
        ),
        migrations.AlterField(
            model_name="apartment",
            name="category",
            field=models.CharField(
                choices=[
                    ("studio", "Studio"),
                    ("one_bedroom", "One Bedroom"),
                    ("two_bedroom", "Two Bedroom"),
                    ("three_bedroom", "Three Bedroom"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="complex",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="apartments",
                to="arc.complex",
            ),
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="floor_plan",
        ),
        migrations.RemoveField(
            model_name="apartment",
            name="slider_images",
        ),
        migrations.AddField(
            model_name="apartment",
            name="floor_plan",
            field=models.ManyToManyField(
                related_name="apartments_floor_plans", to="arc.image"
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="slider_images",
            field=models.ManyToManyField(
                related_name="apartments_slider_images", to="arc.image"
            ),
        ),
    ]
