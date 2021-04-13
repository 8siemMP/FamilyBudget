from rest_framework import permissions
from budgets.models import Privilege, OWNER, READ_ONLY


class HasBudgetPermission(permissions.BasePermission):
    """
    Checking user privileges for requested budget from m2m model
    """

    def has_object_permission(self, request, view, obj):
        try:
            privilege = obj.privilege_set.get(user=request.user)
        except Privilege.DoesNotExist:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'PUT':
            return privilege != READ_ONLY

        return privilege == OWNER
