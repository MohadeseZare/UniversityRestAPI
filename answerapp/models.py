from django.db import models
from exerciseapp.models import Exercise
from userapp.models import User

class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    uploadpdf = models.FileField(upload_to='uploads/', null=True)


