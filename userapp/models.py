from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GroupType(models.TextChoices):
        TEACHER = 'teacher_group'
        STUDENT = 'student_group'

    class PostType(models.TextChoices):
        ADMIN = 'A', 'Admin'
        TEACHER = 'T', 'Teacher'
        STUDENT = 'S', 'Student'

    nationalCode = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=50, blank=True, null=True)
    post = models.CharField(blank=True, choices=PostType.choices, max_length=8, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.email
