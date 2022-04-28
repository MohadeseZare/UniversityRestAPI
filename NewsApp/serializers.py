
from rest_framework import serializers
from ClassroomApp.models import Classroom
from ExerciseApp.filterdata import FilteredClassroomRelatedcurentteacher
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    classroom = FilteredClassroomRelatedcurentteacher(queryset=Classroom.objects)
    class Meta:
        model = News
        fields = '__all__'

