# Generated by Django 5.1.7 on 2025-04-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='title',
        ),
    ]
