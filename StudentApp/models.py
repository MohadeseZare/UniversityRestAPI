from django.db import models


class Student(models.Model):
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    NationalCode = models.IntegerField()



