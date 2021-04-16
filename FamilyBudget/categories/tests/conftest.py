import pytest

from budgets.tests.conftest import *
from users.tests.conftest import *
from categories.models import Category


__all__ = ['empty_category', ]


@pytest.fixture
def empty_category(empty_budget):
    category = Category.objects.create(name='first test category', budget=empty_budget)
    category.save()
    return category
