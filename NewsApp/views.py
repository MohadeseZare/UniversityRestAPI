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


