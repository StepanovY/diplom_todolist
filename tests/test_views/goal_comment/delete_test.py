import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_goal_comment_delete(
        user,
        get_auth_client,
        board_participant_factory,
        goal_comment_factory,
):
    board_participant = board_participant_factory(user=user)
    goal_comment = goal_comment_factory(
        goal__category__board=board_participant.board,
        goal__category__user=user,
        goal__user=user,
        user=user,
    )

    auth_client = get_auth_client(user)
    url = reverse('retrieve_goal_comment', kwargs={'pk': goal_comment.pk})
    response = auth_client.delete(path=url)

    assert response.status_code == 204
    assert response.data is None


@pytest.mark.django_db
def test_goal_comment_delete_with_another_auth_user(
        user_factory,
        get_auth_client,
        board_participant_factory,
        goal_comment_factory,
):
    user1 = user_factory()
    user2 = user_factory()
    board_participant = board_participant_factory(user=user1)
    goal_comment = goal_comment_factory(
        goal__category__board=board_participant.board,
        goal__category__user=user1,
        goal__user=user1,
        user=user1,
    )

    auth_client = get_auth_client(user2)
    url = reverse('retrieve_goal_comment', kwargs={'pk': goal_comment.pk})
    response = auth_client.delete(path=url)

    assert response.status_code == 404
    assert response.data == {'detail': 'Not found.'}
