# Generated by Django 4.1.5 on 2023-01-19 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomsapp', '0008_room_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='admins',
            new_name='admin_users',
        ),
    ]
