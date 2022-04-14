from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


#def perform_create(self, serializer):
   # serializer.save(user=self.request.user)
# Create your views here.
