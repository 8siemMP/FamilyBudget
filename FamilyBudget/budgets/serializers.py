from rest_framework import serializers
from budgets.models import Budget, OWNER


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    def save(self, **kwargs):
        assert 'creator' in kwargs
        creator = kwargs.pop('creator')
        instance = super().save(**kwargs)
        instance.privilege_set.create(user=creator, role=OWNER)
        return instance

    class Meta:
        model = Budget
        fields = ['name', 'url']
