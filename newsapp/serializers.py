
from rest_framework import serializers
from classroomapp.models import Classroom
from exerciseapp.filterdata import FilteredClassroomRelatedCurentTeacher
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    classroom = FilteredClassroomRelatedCurentTeacher(queryset=Classroom.objects)
    class Meta:
        model = News
        fields = '__all__'

