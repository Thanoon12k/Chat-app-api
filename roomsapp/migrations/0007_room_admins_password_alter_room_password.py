# Generated by Django 4.1.5 on 2023-01-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomsapp', '0006_room_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='admins_password',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='password',
            field=models.CharField(max_length=25),
        ),
    ]