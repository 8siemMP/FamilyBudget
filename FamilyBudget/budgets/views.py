from rest_framework import viewsets, permissions

from budgets.models import Budget
from budgets.permissions import HasBudgetPermission
from budgets.serializers import BudgetSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated, HasBudgetPermission]
    filterset_fields = ['name']

    def get_queryset(self):
        return Budget.objects.filter(privileges=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
