# Generated by Django 3.1.6 on 2021-02-23 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
    ]
