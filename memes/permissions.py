from rest_framework.permissions import BasePermission


class CookieConsentAcceptedPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.cookie_consent_accepted