from rest_framework import viewsets
from .permissions import AnswerPermission
from .models import Answer
from .serializers import AnswerSerSerializer
from django_filters import rest_framework as filters
from UserApp.models import User


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [AnswerPermission,]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = (
        'student',
        'exercise',
    )

    def get_queryset(self):
        if self.request.user.groups.filter(name=User.Group_type.TEACHER).exists():
            return Answer.objects.filter(exercise__classroom__teacher=self.request.user)
        elif self.request.user.groups.filter(name=User.Group_type.STUDENT).exists():
            return Answer.objects.filter(student=self.request.user)
        else:
            return Answer.objects.all()


