# Generated by Django 5.0.7 on 2024-07-29 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_page", "0003_maincontent_section1_section2card_section3_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Section1",
            new_name="SectionOne",
        ),
        migrations.RenameModel(
            old_name="Section3",
            new_name="SectionThree",
        ),
        migrations.RenameModel(
            old_name="Section2",
            new_name="SectionTwo",
        ),
        migrations.RenameModel(
            old_name="Section2Card",
            new_name="SectionTwoCard",
        ),
        migrations.RenameField(
            model_name="sectionone",
            old_name="assessability",
            new_name="accessibility",
        ),
    ]