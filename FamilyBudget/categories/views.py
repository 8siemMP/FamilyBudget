from categories.models import Category
from categories.serializers import CategorySerializer
from common.viewset import BudgetRelatedViewSet


class CategoryViewSet(BudgetRelatedViewSet):
    model = Category
    serializer_class = CategorySerializer
    filterset_fields = ['name']
