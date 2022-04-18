from rest_framework import viewsets
from rest_framework_guardian import filters
from .permissions import CustomObjectPermissions
from .models import News
from .serializers import NewsSerializer
from django_filters import rest_framework as filters

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = [CustomObjectPermissions]
    serializer_class = NewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'Classroom',
    )


