from rest_framework import viewsets, permissions
from .models import Exercise
from .serializers import ExerciseSerializer
from django_filters import rest_framework as filters

class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'Classroom',
    )




