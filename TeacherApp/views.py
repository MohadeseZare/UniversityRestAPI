from rest_framework import viewsets, permissions
from .models import Teacher
from .serializers import TeacherSerializer
from UserApp.views import UserViewSet
from rest_framework.decorators import action
from django.http import HttpResponseRedirect
from django.urls import reverse

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




    @action(detail=False, methods=['post'])
    def create(self, request):
        firstname = request.POST['FirstName']
        lastname = request.POST['LastName']
        nationalCode = request.POST['NationalCode']
        schoolName = request.POST['SchoolName']
        teacher = Teacher(FirstName=firstname, LastName=lastname, NationalCode=nationalCode, SchoolName=schoolName)
        teacher.save()

        UserViewSet.create(self, request)
        return HttpResponseRedirect(reverse('Teachers'))

#def perform_create(self, serializer):
   # serializer.save(user=self.request.user)
# Create your views here.
