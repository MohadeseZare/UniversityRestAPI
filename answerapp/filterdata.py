
from rest_framework import serializers

class FilteredClassroomRelatedCurentsSudent(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(FilteredClassroomRelatedCurentsSudent, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(classroom__students=request.user)