from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Answer, Exercise
from django import utils
from rest_framework.serializers import  ValidationError
from .filterdata import FilteredClassroomRelatedcurentsSudent


class AnswerSerSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())
    exercise = FilteredClassroomRelatedcurentsSudent(queryset=Exercise.objects)

    class Meta:
        model = Answer
        fields = '__all__'

    def validate(self, attrs):

        answers = Answer.objects.filter(student=attrs['student'])
        exercise = Exercise.objects.get(id=attrs['exercise'].id)
        if exercise.expiredate < utils.timezone.now():
            raise ValidationError("This exercise timeout.")
        if answers.filter(exercise=exercise):
            raise ValidationError("you cant add Two Answer for One exercise.")
        return attrs

