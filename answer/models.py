from django.db import models
from exercise.models import Exercise
from user.models import User


class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    upload_pdf = models.FileField(upload_to='uploads/', null=True)
