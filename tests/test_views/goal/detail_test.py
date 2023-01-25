import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_goal_detail(
    user,
    get_auth_client,
    board_participant_factory,
    goal_factory,
):
    board_participant = board_participant_factory(user=user)
    goal = goal_factory(
        category__board=board_participant.board, category__user=user, user=user
    )

    expected_response = {
        'id': goal.id,
        'title': goal.title,
        'category': goal.category.id,
        'description': '',
        'due_date': None,
        'status': 1,
        'priority': 2,
        'created': goal.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        'updated': goal.created.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        'user': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        },
    }

    auth_client = get_auth_client(user)
    url = reverse('retrieve_goal', kwargs={'pk': goal.pk})
    response = auth_client.get(path=url)

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_goal_detail_with_not_auth_user(
    user,
    client,
    board_participant_factory,
    goal_factory,
):

    board_participant = board_participant_factory(user=user)
    goal = goal_factory(
        category__board=board_participant.board, category__user=user, user=user
    )

    url = reverse('retrieve_goal', kwargs={'pk': goal.pk})
    response = client.get(path=url)

    assert response.status_code == 403
    assert response.data == {
        'detail': 'Authentication credentials were not provided.'
    }