
from rest_framework import serializers

class FilteredClassroomRelatedCurentTeacher(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(FilteredClassroomRelatedCurentTeacher, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(teacher=request.user)