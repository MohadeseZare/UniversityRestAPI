# Generated by Django 3.2.13 on 2022-04-14 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClassroomApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='title',
        ),
    ]
