import pytest
from rest_framework import status


class TestCategoriesView(object):
    @pytest.mark.django_db
    def test_list_view(self, client, empty_category):
        response = client.get(path='/categories/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

        client._login(empty_category.budget.owner)
        response = client.get(path='/categories/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
