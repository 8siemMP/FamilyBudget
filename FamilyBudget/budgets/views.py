from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet

from budgets.models import Budget
from budgets.permissions import HasBudgetPermission
from budgets.serializers import BudgetSerializer, PrivilegeSerializer

User = get_user_model()


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated, HasBudgetPermission]
    filterset_fields = ['name']

    def get_queryset(self):
        return Budget.objects.filter(Q(privileges__has_key=f"{self.request.user.id}") | Q(owner=self.request.user))

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PrivilegeManagementViewSet(mixins.CreateModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin,
                                 GenericViewSet):
    serializer_class = PrivilegeSerializer
    permission_classes = [permissions.IsAuthenticated]

    _budget = None

    @property
    def budget(self):
        if self._budget is None:
            self._budget = Budget.objects.get(pk=self.kwargs['budget_pk'])
        return self._budget

    def get_object(self):
        user_id = self.kwargs['user_pk']
        return f'{user_id}', self.budget.permission(user_id)

    def perform_create(self, serializer):
        user_id = "%d" % self.kwargs['user_pk']
        permission = self.request.data['permission'][0]
        assert permission in Budget.PERMISSION.keys()
        self.budget.privileges[user_id] = permission
        self.budget.save()

    def perform_destroy(self, instance):
        if self.kwargs['user_pk'] == self.budget.owner.id:
            raise Exception   # TODO better exception
        user_id = "%d" % self.kwargs['user_pk']
        assert user_id == instance[0]
        del self.budget.privileges[user_id]     # TODO better exception
        self.budget.save()
