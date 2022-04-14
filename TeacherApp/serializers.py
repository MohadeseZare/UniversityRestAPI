from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
   # username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Teacher
        fields = '__all__'