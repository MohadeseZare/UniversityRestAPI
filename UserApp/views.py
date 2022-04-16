from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    '''
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'update':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
'''



    def create(self, request):
        nationalCode = request.POST['NationalCode']
        lastname = request.POST['LastName']
        firstname = request.POST['FirstName']
        user = User.objects.create_user(nationalCode, '', nationalCode)
        user.last_name = lastname
        user.first_name = firstname
        user.save()





