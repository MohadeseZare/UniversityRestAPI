from rest_framework import permissions


class AnswerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS :
            return True
        if request.user.groups.filter(name='studentgroup').exists():
            return True

