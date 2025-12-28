"""
Unit tests for idle movement.

Tests the IdleMovementHandler class.
"""

from unittest.mock import MagicMock

import pytest

from server.npc.idle_movement import IdleMovementHandler


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def idle_movement_handler(mock_persistence, mock_event_bus):
    """Create an IdleMovementHandler instance."""
    return IdleMovementHandler(event_bus=mock_event_bus, persistence=mock_persistence)


def test_idle_movement_handler_init(mock_persistence, mock_event_bus):
    """Test IdleMovementHandler initialization."""
    handler = IdleMovementHandler(event_bus=mock_event_bus, persistence=mock_persistence)
    assert handler.persistence == mock_persistence
    assert handler.movement_integration is not None


def test_idle_movement_handler_init_no_persistence():
    """Test IdleMovementHandler initialization fails without persistence."""
    with pytest.raises(ValueError, match="persistence.*required"):
        IdleMovementHandler(persistence=None)


def test_should_idle_move_disabled(idle_movement_handler):
    """Test should_idle_move() returns False when idle movement is disabled."""
    npc_instance = MagicMock()
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": False}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_should_idle_move_in_combat(idle_movement_handler):
    """Test should_idle_move() returns False when NPC is in combat."""
    npc_instance = MagicMock()
    npc_instance.combat_state = MagicMock()
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_should_idle_move_not_alive(idle_movement_handler):
    """Test should_idle_move() returns False when NPC is not alive."""
    npc_instance = MagicMock()
    npc_instance.is_alive = False
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False
