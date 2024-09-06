# Generated by Django 4.1 on 2024-09-06 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0015_dynamicformsubmission_delete_contactrequest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartment",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("studio", "Студия"),
                    ("one_room", "Однокомнатная"),
                    ("two_room", "Двухкомнатная"),
                    ("three_room", "Трехкомнатная"),
                ],
                max_length=50,
                null=True,
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="apartments",
                to="arc.city",
                verbose_name="Город",
            ),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="complex",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="apartments",
                to="arc.complex",
                verbose_name="Комплекс",
            ),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="path",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Путь"
            ),
        ),
        migrations.AlterField(
            model_name="apartmentimage",
            name="apartment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="arc.apartment",
                verbose_name="Квартира",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentimage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="apartmentimage",
            name="image_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("slider_image", "Картинка для слайдера"),
                    ("additional_image", "Дополнительное изображение"),
                ],
                max_length=20,
                null=True,
                verbose_name="Тип изображения",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="apartment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sections",
                to="arc.apartment",
                verbose_name="Квартира",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="apartment_number",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Номер квартиры"
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="area",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Площадь",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="delivery_date",
            field=models.DateField(blank=True, null=True, verbose_name="Срок сдачи"),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="floor",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Этаж"
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Цена",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="room_count",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Количество комнат"
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Название секции"
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Название города"
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="path",
            field=models.CharField(
                blank=True, default="", max_length=100, null=True, verbose_name="Путь"
            ),
        ),
        migrations.AlterField(
            model_name="complex",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="complexes",
                to="arc.city",
                verbose_name="Город",
            ),
        ),
        migrations.AlterField(
            model_name="complex",
            name="name",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Название комплекса"
            ),
        ),
        migrations.AlterField(
            model_name="complex",
            name="path",
            field=models.CharField(
                blank=True, default="", max_length=100, null=True, verbose_name="Путь"
            ),
        ),
        migrations.AlterField(
            model_name="compleximage",
            name="complex",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="arc.complex",
                verbose_name="Комплекс",
            ),
        ),
        migrations.AlterField(
            model_name="compleximage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="compleximage",
            name="image_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("slider_image", "Картинка для слайдера"),
                    ("additional_image", "Дополнительное изображение"),
                ],
                max_length=20,
                null=True,
                verbose_name="Тип изображения",
            ),
        ),
        migrations.AlterField(
            model_name="dynamicformsubmission",
            name="data",
            field=models.JSONField(blank=True, null=True, verbose_name="Данные формы"),
        ),
        migrations.AlterField(
            model_name="dynamicformsubmission",
            name="name",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Название формы"
            ),
        ),
        migrations.AlterField(
            model_name="newsection",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="new_sections",
                to="arc.city",
                verbose_name="Город",
            ),
        ),
        migrations.AlterField(
            model_name="plot",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plots",
                to="arc.city",
                verbose_name="Город",
            ),
        ),
        migrations.AlterField(
            model_name="plot",
            name="district",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Район"
            ),
        ),
        migrations.AlterField(
            model_name="plot",
            name="path",
            field=models.CharField(
                blank=True, default="", max_length=100, null=True, verbose_name="Путь"
            ),
        ),
        migrations.AlterField(
            model_name="plotimage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="plotimage",
            name="image_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("slider_image", "Картинка для слайдера"),
                    ("additional_image", "Дополнительное изображение"),
                ],
                max_length=20,
                null=True,
                verbose_name="Тип изображения",
            ),
        ),
        migrations.AlterField(
            model_name="plotimage",
            name="plot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="arc.plot",
                verbose_name="Застройка",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="area",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=5,
                null=True,
                verbose_name="Площадь участка (в сотках)",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="developed",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="Разработан"
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="electricity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Свет",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="gas",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Газ",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="land_type",
            field=models.CharField(
                blank=True,
                choices=[("SNT", "СНТ"), ("IJS", "ИЖС")],
                max_length=3,
                null=True,
                verbose_name="Тип участка",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="path",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Путь"
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="plot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lands",
                to="arc.plot",
                verbose_name="Застройка",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Цена за участок",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="sewage",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Стоки",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="water",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Вода",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandimage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Изображение"
            ),
        ),
        migrations.AlterField(
            model_name="plotlandimage",
            name="image_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("slider_image", "Картинка для слайдера"),
                    ("additional_image", "Дополнительное изображение"),
                ],
                max_length=20,
                null=True,
                verbose_name="Тип изображения",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandimage",
            name="plot_land",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="arc.plotland",
                verbose_name="Участок",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="area",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Площадь",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="electricity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Свет",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="gas",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Газ",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="land_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("privatized", "Приватизированный"),
                    ("settlement", "Земли населенных пунктов"),
                ],
                default="privatized",
                max_length=20,
                null=True,
                verbose_name="Статус земли",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="plot_land",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sections",
                to="arc.plotland",
                verbose_name="Участок",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Цена",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="sewage",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Стоки",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Название секции"
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="water",
            field=models.CharField(
                blank=True,
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                null=True,
                verbose_name="Вода",
            ),
        ),
        migrations.AlterField(
            model_name="plotsection",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plot_sections",
                to="arc.city",
                verbose_name="Город",
            ),
        ),
    ]