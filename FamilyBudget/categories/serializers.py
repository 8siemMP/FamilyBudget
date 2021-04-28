from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    entries = serializers.HyperlinkedRelatedField(view_name='entry-detail', read_only=True, required=False, many=True)

    class Meta:
        model = Category
        fields = ['name', 'budget', 'entries', 'url']
