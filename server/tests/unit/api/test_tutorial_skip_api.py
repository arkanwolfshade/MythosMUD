"""Skipping First Exposure at creation is server-verified (#1081): the eligibility endpoint and create-character."""

# pyright: reportAny=false
# Reason: unittest.mock.MagicMock/AsyncMock inherit Any in typeshed (NonCallableMock(Base, Any)); these tests drive
# the route through mocked player, quest and persistence services, so mock attribute access is Any.

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request

from server.api.character_creation import create_character_with_stats
from server.api.tutorial_skip import tutorial_skip_eligibility
from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.exceptions import LoggedHTTPException
from server.models import Stats
from server.models.user import User
from server.schemas.players import CreateCharacterRequest, PlayerRead, PositionState

STATS = {"str": 10, "int": 10, "wis": 10, "dex": 10, "con": 10, "cha": 10}


def _user() -> User:
    return User(
        id=uuid.uuid4(),
        username="veteran",
        email="veteran@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )


def _request() -> Request:
    request = Mock(spec=Request)
    request.app = MagicMock()
    return request


def _created(user: User) -> PlayerRead:
    return PlayerRead(
        id=uuid.uuid4(),
        name="Newcomer",
        user_id=user.id,
        profession_id=0,
        profession_name=None,
        profession_description=None,
        profession_flavor_text=None,
        stats=Stats.model_validate(STATS),
        inventory=[],
        created_at=datetime.now(UTC),
        last_active=datetime.now(UTC),
        is_admin=False,
        in_combat=False,
        position=PositionState.STANDING,
        current_room_id=RECOVERY_WARD_ROOM_ID,
    )


async def _create(user: User, player_service: MagicMock, *, start_in_tutorial: bool) -> object:
    with (
        patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False),
        patch("server.api.character_creation.character_creation_limiter"),
    ):
        return await create_character_with_stats(
            request=_request(),
            request_data=CreateCharacterRequest(name="Newcomer", stats=STATS, start_in_tutorial=start_in_tutorial),
            current_user=user,
            player_service=player_service,
            profession_service=AsyncMock(),
            skill_service=AsyncMock(),
            persistence=AsyncMock(),
            quest_service=AsyncMock(),
        )


@pytest.mark.asyncio
async def test_the_eligibility_endpoint_reports_whether_the_account_may_skip() -> None:
    persistence = AsyncMock()
    persistence.get_players_by_user_id = AsyncMock(return_value=["a character"])
    with patch(
        "server.api.tutorial_skip.account_completed_first_exposure", new=AsyncMock(return_value=True)
    ) as completed:
        result = await tutorial_skip_eligibility(
            current_user=_user(), persistence=persistence, quest_service=AsyncMock()
        )

    assert result.eligible is True
    call = completed.await_args
    assert call is not None
    assert call.args[0] == ["a character"]  # every character on the account, deleted ones included


@pytest.mark.asyncio
async def test_an_account_that_never_finished_the_tutorial_cannot_skip_it() -> None:
    """start_in_tutorial=false used to be trusted; now the server refuses it and creates nothing."""
    player_service = MagicMock()
    player_service.create_player_with_stats = AsyncMock()
    with (
        patch("server.api.tutorial_skip.account_completed_first_exposure", new=AsyncMock(return_value=False)),
        pytest.raises(LoggedHTTPException) as refused,
    ):
        _ = await _create(_user(), player_service, start_in_tutorial=False)

    assert refused.value.status_code == 403
    player_service.create_player_with_stats.assert_not_awaited()


@pytest.mark.asyncio
async def test_an_eligible_skip_starts_in_the_ward_with_the_finished_end_state() -> None:
    user = _user()
    created = _created(user)
    player_service = MagicMock()
    player_service.create_player_with_stats = AsyncMock(return_value=created)
    with (
        patch("server.api.tutorial_skip.account_completed_first_exposure", new=AsyncMock(return_value=True)),
        patch("server.api.tutorial_skip.skip_first_exposure", new=AsyncMock()) as skip,
    ):
        _ = await _create(user, player_service, start_in_tutorial=False)

    kwargs = player_service.create_player_with_stats.await_args.kwargs
    assert kwargs["start_in_tutorial"] is False
    assert kwargs["starting_room_id"] == RECOVERY_WARD_ROOM_ID
    skip.assert_awaited_once()
    call = skip.await_args
    assert call is not None
    assert call.args[0] == created.id


@pytest.mark.asyncio
async def test_a_character_that_takes_the_tutorial_is_not_checked_or_skipped() -> None:
    user = _user()
    player_service = MagicMock()
    player_service.create_player_with_stats = AsyncMock(return_value=_created(user))
    player_service.get_default_starting_room.return_value = "foyer"
    with (
        patch("server.api.tutorial_skip.account_completed_first_exposure", new=AsyncMock()) as completed,
        patch("server.api.tutorial_skip.skip_first_exposure", new=AsyncMock()) as skip,
    ):
        _ = await _create(user, player_service, start_in_tutorial=True)

    completed.assert_not_awaited()
    skip.assert_not_awaited()
    assert player_service.create_player_with_stats.await_args.kwargs["start_in_tutorial"] is True
