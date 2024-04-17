# Generated by Django 5.0.3 on 2024-04-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0012_alter_apikey_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="a5149615d80544f78ff163869b7798c9",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="country",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
