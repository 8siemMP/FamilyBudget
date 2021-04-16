from common.viewset import BudgetRelatedViewSet
from entries.models import Entry
from entries.serializers import EntrySerializer


class EntryViewSet(BudgetRelatedViewSet):
    model = Entry
    serializer_class = EntrySerializer
    filterset_fields = ['name', 'amount']
