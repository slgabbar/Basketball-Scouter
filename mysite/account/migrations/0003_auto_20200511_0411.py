# Generated by Django 3.0.2 on 2020-05-11 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200423_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='team_location',
            field=models.CharField(default='team_location', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='team_name',
            field=models.CharField(default='team_name', max_length=100),
        ),
    ]
