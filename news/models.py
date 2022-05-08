from django.db import models
from classroom.models import Classroom

class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
