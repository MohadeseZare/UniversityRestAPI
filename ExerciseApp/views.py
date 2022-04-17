from rest_framework import viewsets, permissions
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    filter_fields = (
        'Classroom',
    )




