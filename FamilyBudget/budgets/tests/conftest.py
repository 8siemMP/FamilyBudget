import pytest
from budgets.models import Budget
from users.tests.conftest import *


__all__ = ['empty_budget', 'budget_extra_priv']


@pytest.fixture
def empty_budget(normal_user1):
    budget = Budget.objects.create(name='first test budget', owner=normal_user1)
    budget.save()
    return budget


@pytest.fixture
def budget_extra_priv(normal_user1, normal_user2, staff_user):
    budget = Budget.objects.create(
        name='test budget with extra privileges',
        owner=normal_user1,
        privileges={
            f'{normal_user2.id}': 'R',
            f'{staff_user.id}': 'E'
        }
    )
    budget.save()
    return budget
