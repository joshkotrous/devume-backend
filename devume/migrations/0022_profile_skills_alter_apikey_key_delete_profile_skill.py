# Generated by Django 5.0.3 on 2024-04-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devume", "0021_alter_apikey_key_alter_education_field_of_study"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="skills",
            field=models.JSONField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="apikey",
            name="key",
            field=models.CharField(
                default="3fea700959024e66bc994b5a9b8d53ab",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.DeleteModel(
            name="Profile_Skill",
        ),
    ]
