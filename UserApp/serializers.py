from rest_framework import serializers
from .models import  User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = "__all__"



'''
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
'''