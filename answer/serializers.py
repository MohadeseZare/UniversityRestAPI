from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Answer, Exercise
from django import utils
from rest_framework.serializers import ValidationError


class AnswerSerializer(serializers.ModelSerializer):
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __init__(self, *args, **kwargs):
        super(AnswerSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['exercise'].queryset = Exercise.objects.filter(classroom__students=request_user)

    class Meta:
        model = Answer
        fields = '__all__'

    def validate(self, attrs):

        answers = Answer.objects.filter(student=attrs['student'])

        exercise = Exercise.objects.get(id=attrs['exercise'].id)
        if exercise.expire_date < utils.timezone.now():
            raise ValidationError("This exercise timeout.")
        if answers.filter(exercise=exercise) and self.context['request'].method == 'POST':
            raise ValidationError("you cant add Two Answer for One exercise.")
        return attrs
