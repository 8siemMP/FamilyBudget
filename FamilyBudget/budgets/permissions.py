from rest_framework import permissions

from common.permissions import AbstactBudgetPermission


class HasBudgetPermission(AbstactBudgetPermission):
    """ Checking user privileges for requested budget """

    def get_budget_object(self, obj):
        return obj


class HasRelatedBudgetPermission(AbstactBudgetPermission):
    """ Checking user privileges for requested object with related budget """

    def get_budget_object(self, obj):
        return obj.budget


class IsBudgetOwner(permissions.BasePermission):
    """ Checking is loged user a budget owner """
    def has_object_permission(self, request, view, obj):
        return request.user == view.budget.owner
