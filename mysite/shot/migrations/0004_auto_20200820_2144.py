# Generated by Django 3.0.7 on 2020-08-20 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20200813_2218'),
        ('shot', '0003_shot_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shot',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game'),
        ),
    ]
