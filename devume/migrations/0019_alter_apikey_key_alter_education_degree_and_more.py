# Generated by Django 5.0.3 on 2024-04-16 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0018_education_field_of_study_alter_apikey_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="e6bd6097afb84d199f16649ce84e2f8c",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="degree",
            field=models.CharField(
                choices=[
                    ("Associates", "Associates"),
                    ("Bachelors", "Bachelors"),
                    ("Masters", "Masters"),
                    ("Doctorate", "Doctorate"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="school_name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
