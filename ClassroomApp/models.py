from django.db import models
from TeacherApp.models import Teacher
from CourseApp.models import Course
from StudentApp.models import Student
from UserApp.models import User

class Classroom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField(User, related_name='students')

