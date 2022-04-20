from rest_framework import serializers
from .models import Classroom
from UserApp.models import User



class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(semat='T'))
    students = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(semat='S'), many=True)
    class Meta:
        model = Classroom
        fields = '__all__'
