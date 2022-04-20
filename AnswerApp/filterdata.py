
from rest_framework import serializers

class FilteredClassroomRelatedcurentsSudent(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(FilteredClassroomRelatedcurentsSudent, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(Classroom__students=request.user)