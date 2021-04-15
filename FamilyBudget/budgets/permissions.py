from rest_framework import permissions


class HasBudgetPermission(permissions.BasePermission):
    """
    Checking user privileges for requested budget from m2m model
    """

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        if request.method in permissions.SAFE_METHODS:
            return f'{request.user.id}' in obj.privileges

        if request.method == 'PUT':
            return obj.privileges.get(f'{request.user.id}', None) == 'E'


class IsBudgetOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == view.budget.owner
