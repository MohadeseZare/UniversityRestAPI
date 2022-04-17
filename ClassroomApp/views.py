from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Classroom
from .serializers import ClassroomSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_fields = (
        'teacher',
        'students',
    )



