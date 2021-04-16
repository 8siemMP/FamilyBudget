import pytest


class TestBudgetsView(object):
    @pytest.mark.django_db
    def test_user_del_cascade(self, budget_extra_priv, normal_user2):
        assert f'{normal_user2.id}' in budget_extra_priv.privileges
        normal_user2.delete()
        budget_extra_priv.refresh_from_db()
        assert f'{normal_user2.id}' not in budget_extra_priv.privileges
