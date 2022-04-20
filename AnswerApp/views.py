from rest_framework import viewsets
from .permissions import AnswerPermission
from .models import Answer
from .serializers import AnswerSerSerializer
from django_filters import rest_framework as filters



class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [AnswerPermission,]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'student',
        'exercise',
    )


