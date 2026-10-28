"""Unit tests for how PlayerCreationService places new characters who start in the tutorial."""

from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.constants.instance_rooms import PENDING_INSTANCE_ID
from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM
from server.game.player_creation_service import PlayerCreationService
from server.models import Stats
from server.models.player import Player

DOWNTOWN_ID = "earth_arkhamcity_downtown_intersection_church_garrison"


def _service() -> tuple[PlayerCreationService, AsyncMock]:
    """A creation service over fakes; returns (service, the save_player mock)."""
    save_player: AsyncMock = AsyncMock()
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    persistence.get_active_players_by_user_id = AsyncMock(return_value=[])
    persistence.save_player = save_player
    converter: MagicMock = MagicMock()
    converter.convert_player_to_schema = AsyncMock(return_value=MagicMock())
    return PlayerCreationService(persistence, converter), save_player


def _saved(save_player: AsyncMock) -> Player:
    saved = save_player.await_args
    assert saved is not None
    player = cast(object, saved.args[0])
    assert isinstance(player, Player)
    return player


@pytest.mark.asyncio
async def test_create_player_marks_a_tutorial_character_pending_in_a_world_room() -> None:
    """The instance is built on first connect, so creation stores the pending marker and a real, enterable room."""
    service, save_player = _service()

    _ = await service.create_player("Newcomer", starting_room_id=DOWNTOWN_ID)

    player = _saved(save_player)
    assert player.tutorial_instance_id == PENDING_INSTANCE_ID
    assert player.current_room_id == DOWNTOWN_ID
    assert player.respawn_room_id in (None, DEFAULT_RESPAWN_ROOM)  # never a template room


@pytest.mark.asyncio
async def test_create_player_without_the_tutorial_has_no_marker() -> None:
    service, save_player = _service()

    _ = await service.create_player("Veteran", starting_room_id=DOWNTOWN_ID, start_in_tutorial=False)

    player = _saved(save_player)
    assert player.tutorial_instance_id is None
    assert player.current_room_id == DOWNTOWN_ID


@pytest.mark.asyncio
async def test_create_player_with_stats_marks_a_tutorial_character_pending_in_a_world_room() -> None:
    service, save_player = _service()

    _ = await service.create_player_with_stats("Rolled", Stats(), starting_room_id=DOWNTOWN_ID)

    player = _saved(save_player)
    assert player.tutorial_instance_id == PENDING_INSTANCE_ID
    assert player.current_room_id == DOWNTOWN_ID
    assert player.respawn_room_id in (None, DEFAULT_RESPAWN_ROOM)


@pytest.mark.asyncio
async def test_create_player_with_stats_without_the_tutorial_has_no_marker() -> None:
    service, save_player = _service()

    _ = await service.create_player_with_stats(
        "Skipper", Stats(), starting_room_id=DOWNTOWN_ID, start_in_tutorial=False
    )

    assert _saved(save_player).tutorial_instance_id is None
