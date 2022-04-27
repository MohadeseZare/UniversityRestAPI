from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'nationalCode', 'school_name', 'semat', 'groups']

  def validate(self, attrs):
      attrs["password"] = make_password(attrs["password"])
      return attrs
