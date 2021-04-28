from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows full access only to admin users. For Authenticated users read-only.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and request.user.is_authenticated
        ) or request.user.is_staff
