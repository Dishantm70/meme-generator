from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        else:
            return request.user.is_authenticated