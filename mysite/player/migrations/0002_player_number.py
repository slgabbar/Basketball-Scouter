# Generated by Django 3.0.2 on 2020-03-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='number',
            field=models.IntegerField(default=69),
            preserve_default=False,
        ),
    ]
