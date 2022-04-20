from rest_framework import serializers
from .models import Exercise
from ClassroomApp.models import Classroom
from .filterdata import FilteredClassroomRelatedcurentteacher



class ExerciseSerializer(serializers.ModelSerializer):
    Classroom = FilteredClassroomRelatedcurentteacher(queryset=Classroom.objects)

    class Meta:
        model = Exercise
        fields = '__all__'

