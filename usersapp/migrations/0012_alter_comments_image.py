# Generated by Django 4.1.7 on 2023-03-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0011_alter_comments_reception'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comments_images', verbose_name='الصورة'),
        ),
    ]