# Generated by Django 5.0.3 on 2024-04-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0025_alter_apikey_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="a9f804a1b60b42b8a2549ab863fe02e1", max_length=255, unique=True
            ),
        ),
    ]
