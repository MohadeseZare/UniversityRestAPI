from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-id']