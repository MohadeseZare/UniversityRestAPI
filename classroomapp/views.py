from rest_framework import viewsets, permissions
from .models import Classroom
from .serializers import ClassroomSerializer
from django_filters import rest_framework as filters

class ClassroomViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'teacher',
        'students',
    )



