from django.db import models
from CourseApp.models import Course

class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=4000)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
