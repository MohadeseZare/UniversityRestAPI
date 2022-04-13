from django.db import models
from CourseApp.models import Course

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    filePDF = models.CharField(max_length=4000)
