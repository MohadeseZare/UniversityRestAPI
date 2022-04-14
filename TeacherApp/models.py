from django.db import models


# This class created for Save , update,deleted ,list Teacher
class Teacher(models.Model):
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    NationalCode = models.IntegerField()
    SchoolName = models.CharField(max_length=250)
    UserName = models.CharField(max_length=250)
    Password = models.CharField(max_length=50)



