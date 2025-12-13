"""
Shared fixtures for NPC admin command integration tests.

This module provides common fixtures used across all NPC admin command test modules.
"""

from unittest.mock import MagicMock
from uuid import uuid4

import pytest


@pytest.fixture
def mock_admin_player():
    """Create a mock admin player."""
    player = MagicMock()
    player.id = str(uuid4())
    player.name = "admin_player"
    player.is_admin = True
    player.current_room_id = "earth_arkhamcity_downtown_001"
    return player


@pytest.fixture
def mock_regular_player():
    """Create a mock regular player."""
    player = MagicMock()
    player.id = str(uuid4())
    player.name = "regular_player"
    player.is_admin = False
    player.current_room_id = "earth_arkhamcity_downtown_001"
    return player


@pytest.fixture
def mock_request():
    """Create a mock FastAPI request."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_alias_storage():
    """Create a mock alias storage."""
    return MagicMock()


@pytest.fixture
def sample_npc_definition():
    """Create a sample NPC definition."""
    return {
        "id": 1,
        "name": "Test Shopkeeper",
        "npc_type": "shopkeeper",
        "sub_zone_id": "arkhamcity_downtown",
        "room_id": "earth_arkhamcity_downtown_001",
        "base_stats": {"dp": 100, "mp": 50},
        "behavior_config": {"aggressive": False},
        "ai_integration_stub": {"enabled": True},
    }
