import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_board_create(
        user,
        get_auth_client,
):
    data = {
        'title': 'test board',
    }

    auth_client = get_auth_client(user)

    url = reverse('board_create')

    response = auth_client.post(
        path=url,
        data=data,
    )

    assert response.status_code == 201

    expected_response = {
        'id': response.data['id'],
        'title': 'test board',
        'is_deleted': False,
        'created': response.data['created'],
        'updated': response.data['updated'],
    }

    assert response.data == expected_response


@pytest.mark.django_db
def test_board_create_with_not_auth_user(
        client,
):
    data = {
        'title': 'test board',
    }

    url = reverse('board_create')

    response = client.post(
        path=url,
        data=data,
    )

    assert response.status_code == 403
    assert response.data == {
        'detail': 'Authentication credentials were not provided.'
    }
