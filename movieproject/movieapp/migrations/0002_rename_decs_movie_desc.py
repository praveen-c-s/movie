# Generated by Django 4.2.4 on 2023-09-19 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='decs',
            new_name='desc',
        ),
    ]
