# Generated by Django 3.2.13 on 2022-04-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExerciseApp', '0006_alter_exercise_expiredate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='expiredate',
            field=models.DateTimeField(),
        ),
    ]
