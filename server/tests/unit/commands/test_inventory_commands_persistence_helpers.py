"""
Unit tests for inventory command persistence helper functions.

Tests the persistence helper functions in inventory_commands.py.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.inventory_commands import _clone_inventory, _persist_player
from server.models.player import Player


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock(spec=Player)
    player.name = "TestPlayer"
    player.get_inventory = MagicMock(return_value=[{"item_name": "sword"}])
    return player


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    persistence.save_player = MagicMock()
    return persistence


def test_clone_inventory(mock_player):
    """Test _clone_inventory() clones player inventory."""
    result = _clone_inventory(mock_player)
    assert result == [{"item_name": "sword"}]
    # Verify it's a deep copy (modifying result shouldn't affect original)
    result.append({"item_name": "shield"})
    assert len(mock_player.get_inventory()) == 1


def test_persist_player_success(mock_persistence, mock_player):
    """Test _persist_player() successfully saves player."""
    result = _persist_player(mock_persistence, mock_player)
    assert result is None
    mock_persistence.save_player.assert_called_once_with(mock_player)


def test_persist_player_error(mock_persistence, mock_player):
    """Test _persist_player() handles save errors."""
    from server.schemas.inventory_schema import InventorySchemaValidationError

    mock_persistence.save_player = MagicMock(side_effect=InventorySchemaValidationError("Invalid inventory"))
    result = _persist_player(mock_persistence, mock_player)
    assert result is not None
    assert "result" in result
