from django.db import models
from ExerciseApp.models import Exercise
from StudentApp.models import Student

class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    uploadPDF = models.FileField(upload_to='uploads/', null=True)


