# Generated by Django 5.0.3 on 2024-04-07 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0007_alter_profile_bio_alter_profile_birth_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="last_name",
        ),
    ]
