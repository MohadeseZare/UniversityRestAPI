import datetime


from django.db import models
from ClassroomApp.models import Classroom

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    Classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    uploadPDF = models.FileField(upload_to='uploads/', null=True)
    expiredate = models.DateTimeField()
