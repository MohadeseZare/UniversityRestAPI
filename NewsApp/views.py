from rest_framework import viewsets
from rest_framework_guardian import filters
from ExerciseApp.permissions import TeacherPermission
from .models import News
from .serializers import NewsSerializer
from django_filters import rest_framework as filters

class NewsViewSet(viewsets.ModelViewSet):

    permission_classes = [TeacherPermission,]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'Classroom',
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name='teachergroup').exists():
            return News.objects.filter(Classroom__teacher=self.request.user)
        elif self.request.user.groups.filter(name='studentgroup').exists():
            return News.objects.filter(Classroom__students=self.request.user)
        else:
            return News.objects.all()


