from rest_framework import serializers
from .models import Answer
from django.contrib.auth.models import Group


class AnswerSerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


