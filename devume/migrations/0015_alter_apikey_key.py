# Generated by Django 5.0.3 on 2024-04-16 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0014_alter_apikey_key_alter_state_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="604665e549954fc78cf1f4081a0b6d98",
                max_length=255,
                unique=True,
            ),
        ),
    ]
