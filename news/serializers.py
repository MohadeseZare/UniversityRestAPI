from rest_framework import serializers
from classroom.models import Classroom

from .models import News


class NewsSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(NewsSerializer, self).__init__(*args, **kwargs)
        request_user = self.context['request'].user
        self.fields['classroom'].queryset = Classroom.objects.filter(teacher=request_user)

    class Meta:
        model = News
        fields = '__all__'
