"""Unit tests for player_presence_utils."""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from unittest.mock import MagicMock

from server.exceptions import DatabaseError
from server.realtime.player_presence_utils import (
    _is_uuid_string,
    _is_valid_name,
    extract_player_name,
    get_player_position,
)


def test_is_valid_name() -> None:
    assert _is_valid_name("Armitage") is True
    assert _is_valid_name("  ") is False
    assert _is_valid_name(None) is False


def test_is_uuid_string() -> None:
    pid = str(uuid.uuid4())
    assert _is_uuid_string(pid) is True
    assert _is_uuid_string("not-a-uuid") is False


def test_extract_player_name_from_player_name() -> None:
    player_id = uuid.uuid4()
    player = SimpleNamespace(name="Henry Arkwright")
    assert extract_player_name(player, player_id) == "Henry Arkwright"  # type: ignore[arg-type]


def test_extract_player_name_from_user() -> None:
    player_id = uuid.uuid4()
    user = SimpleNamespace(username="warden", display_name=None)
    player = SimpleNamespace(name="", user=user)
    assert extract_player_name(player, player_id) == "warden"  # type: ignore[arg-type]


def test_extract_player_name_placeholder() -> None:
    player_id = uuid.uuid4()
    player = SimpleNamespace(name="")
    assert extract_player_name(player, player_id) == "Unknown Player"  # type: ignore[arg-type]


def test_extract_player_name_rejects_uuid_string() -> None:
    player_id = uuid.uuid4()
    uuid_name = str(uuid.uuid4())
    player = SimpleNamespace(name=uuid_name)
    assert extract_player_name(player, player_id) == "Unknown Player"  # type: ignore[arg-type]


def test_extract_player_name_user_access_error() -> None:
    player_id = uuid.uuid4()

    class BadUser:
        @property
        def username(self) -> str:
            raise DatabaseError("db")

    player = SimpleNamespace(name="", user=BadUser())
    assert extract_player_name(player, player_id) == "Unknown Player"  # type: ignore[arg-type]


def test_get_player_position_default() -> None:
    player_id = uuid.uuid4()
    player = SimpleNamespace()
    assert get_player_position(player, player_id) == "standing"  # type: ignore[arg-type]


def test_get_player_position_from_stats() -> None:
    player_id = uuid.uuid4()
    player = SimpleNamespace(get_stats=lambda: {"position": "resting"})
    assert get_player_position(player, player_id) == "resting"  # type: ignore[arg-type]


def test_get_player_position_stats_error() -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    player.get_stats.side_effect = AttributeError("missing")
    assert get_player_position(player, player_id) == "standing"
