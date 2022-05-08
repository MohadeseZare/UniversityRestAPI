import datetime


from django.db import models
from classroom.models import Classroom

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    upload_pdf = models.FileField(upload_to='uploads/', null=True)
    expire_date = models.DateTimeField()
