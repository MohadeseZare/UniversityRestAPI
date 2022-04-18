from django.db import models
'''
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    semat_type = models.TextChoices('Teacher', 'Studernt')
    nationalCode = models.IntegerField()
    school_name = models.CharField(max_length=250)
    semat = models.CharField(blank=False, choices=semat_type.choices, max_length=8)

    def __str__(self):
        return self.username
'''


