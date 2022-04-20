from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset =User.objects.all()
    serializer_class = UserSerializer





