from rest_framework import serializers
from .models import Classroom
from UserApp.models import User



class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(post='T'))
    students = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(post='S'), many=True)
    class Meta:
        model = Classroom
        fields = '__all__'
