from rest_framework import viewsets
from .models import Exercise
from .serializers import ExerciseSerializer
from django_filters import rest_framework as filters
from .permissions import TeacherPermission

class ExerciseViewSet(viewsets.ModelViewSet):
    permission_classes = [TeacherPermission,]
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    filterset_fields = (
        'Classroom',
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name='teachergroup').exists():
            return Exercise.objects.filter(Classroom__teacher=self.request.user)
        elif self.request.user.groups.filter(name='studentgroup').exists():
            return Exercise.objects.filter(Classroom__students=self.request.user)
        else:
            return Exercise.objects.all()





