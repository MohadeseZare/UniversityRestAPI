from rest_framework import permissions
from UserApp.models import User

class TeacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        if request.user.groups.filter(name=User.GroupType.TEACHER).exists():
            return True
