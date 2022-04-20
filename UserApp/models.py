from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    semat_type = (
        ('A', 'Admin'),
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    nationalCode = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=250, blank=True, null=True)
    semat = models.CharField(blank=True, choices=semat_type, max_length=8, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)



