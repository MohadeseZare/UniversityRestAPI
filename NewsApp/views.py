from rest_framework import viewsets, permissions
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

