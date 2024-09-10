from django.db import migrations, models
import django.db.models.deletion
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ("arc", "0016_alter_apartment_category_alter_apartment_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartment",
            name="category",
            field=models.CharField(
                choices=[
                    ("studio", "Студия"),
                    ("one_room", "Однокомнатная"),
                    ("two_room", "Двухкомнатная"),
                    ("three_room", "Трехкомнатная"),
                ],
                default="studio",  # Строка по умолчанию
                max_length=50,
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="apartment",
            name="city",
            field=models.ForeignKey(
                default=1,  # Целочисленное значение по умолчанию, если ID 1 существует
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
                default=1,  # Целочисленное значение по умолчанию
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
                blank=True,
                default="",  # Строка по умолчанию вместо числа
                max_length=100,
                verbose_name="Путь",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentimage",
            name="apartment",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="arc.apartment",
                verbose_name="Квартира",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="apartment",
            field=models.ForeignKey(
                default=1,
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
                default="",  # Строка по умолчанию
                max_length=10,
                verbose_name="Номер квартиры",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="area",
            field=models.DecimalField(
                decimal_places=2,
                default=1.00,  # Числовое значение с плавающей точкой
                max_digits=6,
                verbose_name="Площадь",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="delivery_date",
            field=models.DateField(
                default=date.today,  # Текущая дата по умолчанию
                verbose_name="Срок сдачи",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="floor",
            field=models.PositiveIntegerField(
                default=1,  # Целочисленное значение
                verbose_name="Этаж",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=1.00,  # Значение с плавающей точкой
                max_digits=10,
                verbose_name="Цена",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="room_count",
            field=models.PositiveIntegerField(
                default=1,  # Целочисленное значение
                verbose_name="Количество комнат",
            ),
        ),
        migrations.AlterField(
            model_name="apartmentsection",
            name="title",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=255,
                verbose_name="Название секции",
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=100,
                verbose_name="Название города",
            ),
        ),
        migrations.AlterField(
            model_name="city",
            name="path",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=100,
                verbose_name="Путь",
            ),
        ),
        migrations.AlterField(
            model_name="complex",
            name="city",
            field=models.ForeignKey(
                default=1,
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
                default="",  # Строка по умолчанию
                max_length=200,
                verbose_name="Название комплекса",
            ),
        ),
        migrations.AlterField(
            model_name="complex",
            name="path",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=100,
                verbose_name="Путь",
            ),
        ),
        migrations.AlterField(
            model_name="compleximage",
            name="complex",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="arc.complex",
                verbose_name="Комплекс",
            ),
        ),
        migrations.AlterField(
            model_name="dynamicformsubmission",
            name="data",
            field=models.JSONField(
                default=dict,  # Пустой словарь по умолчанию
                verbose_name="Данные формы",
            ),
        ),
        migrations.AlterField(
            model_name="dynamicformsubmission",
            name="name",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=255,
                verbose_name="Название формы",
            ),
        ),
        migrations.AlterField(
            model_name="newsection",
            name="city",
            field=models.ForeignKey(
                default=1,
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
                default=1,
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
                blank=True,
                default="",  # Строка по умолчанию
                max_length=200,
                verbose_name="Район",
            ),
        ),
        migrations.AlterField(
            model_name="plot",
            name="path",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=100,
                verbose_name="Путь",
            ),
        ),
        migrations.AlterField(
            model_name="plotimage",
            name="plot",
            field=models.ForeignKey(
                default=1,
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
                decimal_places=2,
                default=1.00,  # Число с плавающей точкой
                max_digits=5,
                verbose_name="Площадь участка (в сотках)",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="developed",
            field=models.BooleanField(
                default=False,  # Логическое значение
                verbose_name="Разработан",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="electricity",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Свет",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="gas",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Газ",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="land_type",
            field=models.CharField(
                choices=[("SNT", "СНТ"), ("IJS", "ИЖС")],
                default="SNT",  # Строка по умолчанию для выбора типа
                max_length=3,
                verbose_name="Тип участка",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="path",
            field=models.CharField(
                blank=True,
                default="",  # Строка по умолчанию
                max_length=100,
                verbose_name="Путь",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="plot",
            field=models.ForeignKey(
                default=1,
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
                decimal_places=2,
                default=1.00,  # Значение с плавающей точкой
                max_digits=10,
                verbose_name="Цена за участок",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="sewage",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Стоки",
            ),
        ),
        migrations.AlterField(
            model_name="plotland",
            name="water",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Вода",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandimage",
            name="plot_land",
            field=models.ForeignKey(
                default=1,
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
                decimal_places=2,
                default=1.00,  # Значение с плавающей точкой
                max_digits=6,
                verbose_name="Площадь",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="electricity",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Свет",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="gas",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Газ",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="land_status",
            field=models.CharField(
                choices=[
                    ("privatized", "Приватизированный"),
                    ("settlement", "Земли населенных пунктов"),
                ],
                default="privatized",  # Строка по умолчанию
                max_length=20,
                verbose_name="Статус земли",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="plot_land",
            field=models.ForeignKey(
                default=1,
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
                decimal_places=2,
                default=1.00,  # Значение с плавающей точкой
                max_digits=10,
                verbose_name="Цена",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="sewage",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Стоки",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="title",
            field=models.CharField(
                default="",  # Строка по умолчанию
                max_length=255,
                verbose_name="Название секции",
            ),
        ),
        migrations.AlterField(
            model_name="plotlandsection",
            name="water",
            field=models.CharField(
                choices=[
                    ("да", "Да"),
                    ("нет", "Нет"),
                    ("возможность", "Есть возможность подключения"),
                ],
                default="нет",
                max_length=20,
                verbose_name="Вода",
            ),
        ),
        migrations.AlterField(
            model_name="plotsection",
            name="city",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plot_sections",
                to="arc.city",
                verbose_name="Город",
            ),
        ),
    ]
