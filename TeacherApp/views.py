from rest_framework import viewsets, permissions
from .models import Teacher
from .serializers import TeacherSerializer
from UserApp.models import User
from UserApp.serializers import UserSerializer
from UserApp.views import UserViewSet
from rest_framework.response import Response

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer




'''
    def create(self, request):
        firstname = request.POST['FirstName']
        lastname = request.POST['LastName']
        nationalCode = request.POST['NationalCode']
        schoolName = request.POST['SchoolName']
        teacher = Teacher(FirstName=firstname, LastName=lastname, NationalCode=nationalCode, SchoolName=schoolName)
        teacher.save()

        UserViewSet.create(self, request)
        respons = {
        "id": teacher.id,
        "FirstName": firstname,
        "LastName": lastname,
        "NationalCode": nationalCode,
        "SchoolName": schoolName
    }
        return Response(respons)
'''

