from rest_framework import viewsets, permissions, status
from .models import Student
from .serializers import StudentSerializer
from UserApp.views import UserViewSet
from rest_framework.decorators import action
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



    def create(self, request):
        firstname = request.POST['FirstName']
        lastname = request.POST['LastName']
        nationalCode = request.POST['NationalCode']
        student = Student(FirstName=firstname, LastName=lastname, NationalCode=nationalCode)
        student.save()
        UserViewSet.create(self, request)
        respons={
        "id": student.id,
        "FirstName": firstname,
        "LastName": lastname,
        "NationalCode": nationalCode
        }
        return Response(respons)



