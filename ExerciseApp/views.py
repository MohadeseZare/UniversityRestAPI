from rest_framework import viewsets, permissions
from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

'''
    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(Classroom=3)
        return query_set

    def get_querysetForClassroom(self):
        queryset = self.queryset
        query_set = queryset.filter(Classroom=3)
        return query_set
'''



