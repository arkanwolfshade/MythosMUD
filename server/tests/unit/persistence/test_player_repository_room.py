"""Unit tests for player_repository_room helpers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.persistence.repositories.player_repository_room import (
    should_skip_room_validation,
    validate_and_fix_player_room,
    validate_and_fix_player_room_with_persistence,
)


def _player(current_room_id: str, tutorial_instance_id: str | None = None) -> MagicMock:
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.current_room_id = current_room_id
    player.tutorial_instance_id = tutorial_instance_id
    return player


def test_should_skip_room_validation_empty_cache() -> None:
    player = _player("any_room")
    assert should_skip_room_validation({}, player) is True


def test_should_skip_room_validation_instanced_room() -> None:
    player = _player("instance_dungeon_001")
    assert should_skip_room_validation({"other": MagicMock()}, player) is True


def test_should_skip_room_validation_tutorial_bedroom() -> None:
    player = _player("earth_arkhamcity_sanitarium_room_tutorial_bedroom_001", tutorial_instance_id="tut-1")
    assert should_skip_room_validation({"other": MagicMock()}, player) is True


def test_validate_and_fix_player_room_valid() -> None:
    player = _player("arkham_square")
    room_cache = {"arkham_square": MagicMock()}
    logger = MagicMock()
    assert validate_and_fix_player_room(room_cache, player, logger) is False


def test_validate_and_fix_player_room_moves_to_foyer() -> None:
    player = _player("invalid_room")
    room_cache = {
        "earth_arkhamcity_sanitarium_room_foyer_001": MagicMock(),
    }
    logger = MagicMock()
    assert validate_and_fix_player_room(room_cache, player, logger) is True
    assert player.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"
    logger.info.assert_called_once()


def test_validate_and_fix_player_room_fallback_missing_in_cache() -> None:
    player = _player("invalid_room")
    room_cache = {"other_room": MagicMock()}
    logger = MagicMock()
    assert validate_and_fix_player_room(room_cache, player, logger) is False
    logger.debug.assert_called_once()


def test_validate_and_fix_player_room_already_at_fallback() -> None:
    player = _player("earth_arkhamcity_sanitarium_room_foyer_001")
    room_cache = {"other_room": MagicMock()}
    logger = MagicMock()
    assert validate_and_fix_player_room(room_cache, player, logger) is False


@pytest.mark.asyncio
async def test_validate_and_fix_player_room_with_persistence_commits() -> None:
    player = _player("invalid_room")
    room_cache = {"earth_arkhamcity_sanitarium_room_foyer_001": MagicMock()}
    logger = MagicMock()
    session = AsyncMock()
    result = await validate_and_fix_player_room_with_persistence(room_cache, player, session, logger)
    assert result is True
    session.execute.assert_awaited_once()
    session.commit.assert_awaited_once()
    logger.debug.assert_called_once()
