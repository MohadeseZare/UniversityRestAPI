from django.db import models
from ClassroomApp.models import Classroom

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    Classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    filePDF = models.CharField(max_length=4000)
