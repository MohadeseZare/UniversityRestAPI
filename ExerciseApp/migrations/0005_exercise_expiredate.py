# Generated by Django 3.2.13 on 2022-04-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExerciseApp', '0004_alter_exercise_uploadpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='expiredate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
