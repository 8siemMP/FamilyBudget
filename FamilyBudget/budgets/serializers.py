from collections import OrderedDict

from rest_framework import serializers
from rest_framework.reverse import reverse

from budgets.models import Budget


def get_user_api_url(pk, request):
    return reverse('user-detail', kwargs={'pk': pk}, request=request)


class PrivilegeSerializer(serializers.Serializer):
    user = serializers.URLField(read_only=True)
    permission = serializers.CharField()

    def to_representation(self, instance):
        if isinstance(instance, OrderedDict):
            user_pk = self.context['request'].parser_context['kwargs']['user_pk']
            permission = instance['permission']
        else:
            user_pk, permission = instance
        return {
            'user': get_user_api_url(user_pk, self.context['request']),
            'permission': permission
        }


class PrivilegesField(serializers.Field):
    def to_representation(self, instance):
        return [
            {
                'user': get_user_api_url(key, self.context['request']),
                'permission': Budget.PERMISSION[val]
            } for key, val in instance.items()
        ]


class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    privileges = PrivilegesField(read_only=True)

    class Meta:
        model = Budget
        fields = ['name', 'url', 'owner', 'entries', 'summary', 'privileges']
