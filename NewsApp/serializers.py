from django.contrib.auth.models import Group
from rest_framework_guardian.serializers import ObjectPermissionsAssignmentMixin
from rest_framework import serializers
from .models import News

class NewsSerializer(ObjectPermissionsAssignmentMixin,serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

        def get_permissions_map(self, created):
            current_user = self.context['request'].user
            readers = Group.objects.get(name='readers')
            supervisors = Group.objects.get(name='supervisors')

            return {
                'view_post': [current_user, readers],
                'change_post': [current_user],
                'delete_post': [current_user, supervisors]
            }