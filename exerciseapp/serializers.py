from rest_framework import serializers
from .models import Exercise
from classroomapp.models import Classroom
from .filterdata import FilteredClassroomRelatedCurentTeacher



class ExerciseSerializer(serializers.ModelSerializer):
    classroom = FilteredClassroomRelatedCurentTeacher(queryset=Classroom.objects)

    class Meta:
        model = Exercise
        fields = '__all__'

