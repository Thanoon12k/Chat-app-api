# Generated by Django 4.1.7 on 2023-03-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomsapp', '0016_alter_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='token',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='توكن'),
        ),
    ]