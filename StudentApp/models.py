from django.db import models
from CourseApp.models import Course

class Student(models.Model):
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    NationalCode = models.IntegerField()
    UserName = models.CharField(max_length=250)
    Password = models.CharField(max_length=50)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

