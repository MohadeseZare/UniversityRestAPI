from django.db import models

class Course(models.Model):
    Title = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']