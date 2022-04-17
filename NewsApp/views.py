from rest_framework import viewsets
from rest_framework_guardian import filters
from .permissions import CustomObjectPermissions
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = [CustomObjectPermissions]
    serializer_class = NewsSerializer
    filter_fields = (
        'Classroom',
    )
    #filter_backends = [filters.ObjectPermissionsFilter]

