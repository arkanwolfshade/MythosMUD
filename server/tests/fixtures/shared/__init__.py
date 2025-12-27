"""
Shared fixtures and builders for all test tiers.
"""

from collections.abc import Callable
from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

import pytest


def make_user_dict(
    username: str = "testuser",
    email: str | None = None,
    user_id: str | None = None,
) -> dict[str, Any]:
    """Create a user dictionary for testing."""
    import uuid

    return {
        "id": user_id or str(uuid.uuid4()),
        "username": username,
        "email": email or f"{username}@example.com",
        "display_name": username,
        "hashed_password": "hashed_password",
        "is_active": True,
        "is_superuser": False,
        "is_verified": True,
    }


def make_player_dict(
    name: str = "testplayer",
    player_id: str | None = None,
    user_id: str | None = None,
    room_id: str = "earth_arkhamcity_intersection_derby_high",
) -> dict[str, Any]:
    """Create a player dictionary for testing."""
    import uuid

    return {
        "player_id": player_id or str(uuid.uuid4()),
        "user_id": user_id or str(uuid.uuid4()),
        "name": name,
        "current_room_id": room_id,
    }


@pytest.fixture
def fake_clock() -> Callable[[], float]:
    """Provide a monotonic counter for time-based tests."""
    counter = [0.0]

    def get_time() -> float:
        counter[0] += 1.0
        return counter[0]

    return get_time


class StubPersistence:
    """Stub persistence layer for unit tests."""

    def __init__(self) -> None:
        self._players: dict[str, Any] = {}

    def get_player_by_name(self, name: str) -> Any | None:
        """Get a player by name."""
        return self._players.get(name)

    def add_player(self, name: str, player: Any) -> None:
        """Add a player to the stub."""
        self._players[name] = player


@pytest.fixture
def stub_persistence() -> StubPersistence:
    """Provide a stub persistence layer."""
    return StubPersistence()

