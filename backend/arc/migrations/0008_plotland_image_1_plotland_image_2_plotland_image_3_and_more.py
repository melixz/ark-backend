# Generated by Django 4.1 on 2024-09-04 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0007_plotland_area"),
    ]

    operations = [
        migrations.AddField(
            model_name="plotland",
            name="image_1",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="plots/lands/",
                verbose_name="Изображение 1",
            ),
        ),
        migrations.AddField(
            model_name="plotland",
            name="image_2",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="plots/lands/",
                verbose_name="Изображение 2",
            ),
        ),
        migrations.AddField(
            model_name="plotland",
            name="image_3",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="plots/lands/",
                verbose_name="Изображение 3",
            ),
        ),
        migrations.AddField(
            model_name="plotland",
            name="image_4",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="plots/lands/",
                verbose_name="Изображение 4",
            ),
        ),
        migrations.AddField(
            model_name="plotland",
            name="image_5",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="plots/lands/",
                verbose_name="Изображение 5",
            ),
        ),
        migrations.CreateModel(
            name="PlotLandImage",
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
                    "image",
                    models.ImageField(upload_to="images/", verbose_name="Изображение"),
                ),
                (
                    "image_type",
                    models.CharField(
                        choices=[
                            ("slider_image", "Картинка для слайдера"),
                            ("additional_image", "Дополнительное изображение"),
                        ],
                        max_length=20,
                        verbose_name="Тип изображения",
                    ),
                ),
                (
                    "plot_land",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="arc.plotland",
                        verbose_name="Участок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение участка",
                "verbose_name_plural": "Изображения участков",
            },
        ),
    ]