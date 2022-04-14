from django.db import models
from TeacherApp.models import Teacher
from CourseApp.models import Course
from StudentApp.models import Student

class Classroom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

