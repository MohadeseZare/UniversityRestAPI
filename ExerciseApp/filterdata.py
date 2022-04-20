
from rest_framework import serializers

class FilteredClassroomRelatedcurentteacher(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(FilteredClassroomRelatedcurentteacher, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(teacher=request.user)