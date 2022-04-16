from rest_framework import viewsets,permissions
from .models import Answer
from .serializers import AnswerSerSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerSerializer

