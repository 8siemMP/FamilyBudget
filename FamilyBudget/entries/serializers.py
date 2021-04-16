from rest_framework import serializers

from entries.models import Entry


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ['name', 'budget', 'amount', 'category', 'url']
