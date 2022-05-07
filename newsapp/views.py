from rest_framework import viewsets
from exerciseapp.permissions import TeacherPermission
from .models import News
from .serializers import NewsSerializer
from django_filters import rest_framework as filters
from userapp.models import User


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [TeacherPermission, ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'classroom',
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name=User.GroupType.TEACHER).exists():
            return News.objects.filter(classroom__teacher=self.request.user)
        elif self.request.user.groups.filter(name=User.GroupType.STUDENT).exists():
            return News.objects.filter(classroom__students=self.request.user)
        else:
            return News.objects.all()
