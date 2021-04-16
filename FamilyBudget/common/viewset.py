from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from budgets.permissions import HasRelatedBudgetPermission


class BudgetRelatedViewSet(viewsets.ModelViewSet):
    model = None
    permission_classes = [permissions.IsAuthenticated, HasRelatedBudgetPermission]

    def get_queryset(self):
        return self.model.objects.filter(
            Q(budget__privileges__has_key=f"{self.request.user.id}") | Q(budget__owner=self.request.user)
        )

    def perform_create(self, serializer):
        if serializer.validated_data['budget'].permission(self.request.user.id) not in ['Editor', 'Owner']:
            raise PermissionDenied()
        super().perform_create(serializer)

    def perform_update(self, serializer):
        if serializer.validated_data['budget'].permission(self.request.user.id) not in ['Editor', 'Owner']:
            raise PermissionDenied()
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.budget.permission(self.request.user.id) not in ['Editor', 'Owner']:
            raise PermissionDenied()
        super().perform_destroy(instance)
