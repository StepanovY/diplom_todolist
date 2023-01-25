import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_goal_delete(
    user,
    get_auth_client,
    board_participant_factory,
    goal_factory,
):

    board_participant = board_participant_factory(user=user)
    goal = goal_factory(
        category__board=board_participant.board, category__user=user, user=user
    )

    auth_client = get_auth_client(user)
    url = reverse('retrieve_goal', kwargs={'pk': goal.pk})
    response = auth_client.delete(path=url)

    assert response.status_code == 204
    assert response.data is None


@pytest.mark.django_db
def test_goal_delete_with_another_auth_user(
    user_factory,
    get_auth_client,
    board_participant_factory,
    goal_factory,
):
    user1 = user_factory()
    user2 = user_factory()
    board_participant = board_participant_factory(user=user1)
    goal = goal_factory(
        category__board=board_participant.board,
        category__user=user1,
        user=user1,
    )

    auth_client = get_auth_client(user2)
    url = reverse('retrieve_goal', kwargs={'pk': goal.pk})
    response = auth_client.delete(path=url)

    assert response.status_code == 404
    assert response.data == {'detail': 'Not found.'}