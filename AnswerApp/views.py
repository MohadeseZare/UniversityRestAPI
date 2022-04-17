from rest_framework import viewsets, permissions
from .models import Answer, Exercise, Student
from .serializers import AnswerSerSerializer
from django import utils
from rest_framework import status
from rest_framework.response import Response


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerSerializer
    filter_fields = (
        'student',
        'exercise',
    )


