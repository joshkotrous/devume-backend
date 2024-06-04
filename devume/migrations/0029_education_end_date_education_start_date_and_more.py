# Generated by Django 5.0.3 on 2024-05-31 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0028_workexperience_job_title_alter_apikey_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="end_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="education",
            name="start_date",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="aa69ec4715c14b09a4f187d21c948952", max_length=255, unique=True
            ),
        ),
    ]