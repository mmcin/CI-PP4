# Generated by Django 4.1.1 on 2022-10-27 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hillbox', '0002_remove_flyingsite_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='slug',
        ),
    ]
