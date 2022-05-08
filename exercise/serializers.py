from rest_framework import serializers

from .models import Exercise
from classroom.models import Classroom


class ExerciseSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ExerciseSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['classroom'].queryset = Classroom.objects.filter(teacher=request_user)

    class Meta:
        model = Exercise
        fields = '__all__'
