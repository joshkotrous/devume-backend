# Generated by Django 5.0.3 on 2024-04-02 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devume', '0004_profile_country_profile_state_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=200)),
                ('degree', models.CharField(choices=[('A', 'Associates'), ('B', 'Bachelors'), ('M', 'Masters'), ('D', 'Doctorate')], max_length=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('skills', models.JSONField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devume.profile')),
            ],
        ),
    ]
