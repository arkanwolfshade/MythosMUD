"""
Unit tests for combat persistence handler - core functionality.

Tests initialization, persistence layer access, and DP/posture updates.
"""

# pyright: reportPrivateUsage=false
# Reason: these tests drive the handler's private DP persistence helpers directly.

import uuid
from unittest.mock import MagicMock

import pytest

from server.services.combat_persistence_handler import CombatPersistenceHandler

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    return MagicMock()


@pytest.fixture
def persistence_handler(mock_combat_service):
    """Create CombatPersistenceHandler instance."""
    return CombatPersistenceHandler(mock_combat_service)


@pytest.fixture
def mock_player():
    """Create mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.stats = {"current_dp": 50, "max_dp": 100, "position": "standing"}
    player.get_stats = MagicMock(return_value={"current_dp": 50, "max_dp": 100, "position": "standing"})
    player.set_stats = MagicMock()
    player.apply_dp_change = MagicMock(return_value=(50, False, False))
    return player


def test_persistence_handler_init(persistence_handler, mock_combat_service):
    """Test CombatPersistenceHandler initialization."""
    assert persistence_handler._combat_service == mock_combat_service
