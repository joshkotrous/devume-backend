# Generated by Django 5.0.3 on 2024-04-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0023_merge_20240417_0150"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="3ae2a113c7b24e2c8727803519be6ed7", max_length=255, unique=True
            ),
        ),
    ]