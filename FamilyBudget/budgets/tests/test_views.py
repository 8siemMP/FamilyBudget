import pytest
from rest_framework import status


class TestBudgetsView(object):
    @pytest.mark.django_db
    def test_list_view(self, client, empty_budget):
        response = client.get(path='/budgets/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

        client._login(empty_budget.owner)
        response = client.get(path='/budgets/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    @pytest.mark.django_db
    def test_detail_view(self, client, empty_budget):
        response = client.get(path='/budgets/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

        client._login(empty_budget.owner)
        response = client.get(path=f'/budgets/{empty_budget.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'first test budget'

    @pytest.mark.django_db
    def test_detail_permissions(self, client, budget_extra_priv, some_user, normal_user2, staff_user):
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

        client._login(budget_extra_priv.owner)
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_200_OK

        client._login(normal_user2)
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_200_OK

        client._login(staff_user)
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_200_OK

        client._login(some_user)
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_add_permission(self, client, empty_budget, some_user):
        assert f'{some_user.id}' not in empty_budget.privileges
        client._login(empty_budget.owner)
        response = client.post(
            path=f'/budgets/{empty_budget.id}/privileges/{some_user.id}/',
            data={'permission': 'Read-only'}
        )
        assert response.status_code == status.HTTP_201_CREATED
        empty_budget.refresh_from_db()
        assert empty_budget.privileges[f'{some_user.id}'] == 'R'

        client._login(some_user)
        response = client.get(path=f'/budgets/{empty_budget.id}/')
        assert response.status_code == status.HTTP_200_OK

        client._login(empty_budget.owner)
        response = client.post(
            path=f'/budgets/{empty_budget.id}/privileges/{some_user.id}/',
            data={'permission': 'Editor'}
        )
        assert response.status_code == status.HTTP_201_CREATED
        empty_budget.refresh_from_db()
        assert empty_budget.privileges[f'{some_user.id}'] == 'E'

        client._login(some_user)
        response = client.get(path=f'/budgets/{empty_budget.id}/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_del_permission(self, client, budget_extra_priv, normal_user2):
        assert f'{normal_user2.id}' in budget_extra_priv.privileges
        client._login(normal_user2)
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_200_OK

        client._login(budget_extra_priv.owner)
        response = client.delete(path=f'/budgets/{budget_extra_priv.id}/privileges/{normal_user2.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

        budget_extra_priv.refresh_from_db()
        assert f'{normal_user2.id}' not in budget_extra_priv.privileges

        client._login(normal_user2)
        response = client.get(path=f'/budgets/{budget_extra_priv.id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND
