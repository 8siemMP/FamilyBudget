from rest_framework import permissions


class AbstactBudgetPermission(permissions.BasePermission):
    """ Abstract class for serializers of budgets and related objects """

    def get_budget_object(self, obj):
        raise NotImplemented

    def has_object_permission(self, request, view, obj):
        budget = self.get_budget_object(obj)

        if request.user == budget.owner:
            return True

        if request.method in permissions.SAFE_METHODS:
            return f'{request.user.id}' in budget.privileges

        if request.method in ('PUT', 'PATCH'):
            return budget.privileges.get(f'{request.user.id}', None) == 'E'
