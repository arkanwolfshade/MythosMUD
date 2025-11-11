"""Tests for MovementService posture-based movement guards."""

from unittest.mock import Mock, patch
from uuid import uuid4

import pytest

from server.events.event_bus import EventBus
from server.game.movement_service import MovementService
from server.models.room import Room


@pytest.fixture
def event_bus():
    """Provide an event bus instance for room construction."""
    return EventBus()


@pytest.fixture
def player_combat_service():
    """Provide a combat service stub that reports players out of combat."""
    service = Mock()
    service.is_player_in_combat_sync.return_value = False
    return service


def _build_room(room_id: str, exits: dict[str, str], event_bus: EventBus) -> Room:
    """Helper to build a Room with minimal required metadata."""
    room_data = {
        "id": room_id,
        "name": f"Test Room {room_id}",
        "description": "A test chamber used by the Miskatonic faculty.",
        "plane": "earth",
        "zone": "arkham",
        "sub_zone": "lab",
        "exits": exits,
    }
    return Room(room_data, event_bus)


@pytest.fixture
def movement_harness(event_bus, player_combat_service):
    """Create a MovementService with patched persistence for controlled tests."""
    mock_persistence = Mock()

    with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
        movement_service = MovementService(event_bus, player_combat_service=player_combat_service)

    # Ensure the patched persistence is retained post-construction
    movement_service._persistence = mock_persistence
    return movement_service, mock_persistence


def _configure_player(mock_persistence, player_id: str, current_room_id: str, position: str) -> Mock:
    """Configure persistence mocks for a single player with the provided posture."""
    player = Mock()
    player.player_id = player_id
    player.name = "Prof. Test"
    player.current_room_id = current_room_id
    player.get_stats.return_value = {"position": position}

    def get_player(identifier):
        if str(identifier) in {player_id, player.name}:
            return player
        return None

    mock_persistence.get_player.side_effect = get_player
    mock_persistence.get_player_by_name.side_effect = lambda name: player if name == player.name else None
    mock_persistence.save_player = Mock()

    return player


def _configure_rooms(mock_persistence, event_bus, player_id: str):
    """Prepare from/to rooms for movement testing."""
    from_room = _build_room("room_1", {"north": "room_2"}, event_bus)
    to_room = _build_room("room_2", {}, event_bus)

    # Ensure the player is registered in the origin room
    from_room._players.add(player_id)

    mock_persistence.get_room.side_effect = lambda room_id: from_room if room_id == "room_1" else to_room

    return from_room, to_room


class TestMovementPositionGuards:
    """Verify that non-standing postures block movement just like combat guards."""

    def test_move_player_blocked_while_sitting(self, movement_harness, event_bus):
        movement_service, mock_persistence = movement_harness
        player_id = str(uuid4())

        player = _configure_player(mock_persistence, player_id, "room_1", position="sitting")
        from_room, to_room = _configure_rooms(mock_persistence, event_bus, player_id)

        result = movement_service.move_player(player_id, "room_1", "room_2")

        assert result is False
        player.get_stats.assert_called_once()
        mock_persistence.save_player.assert_not_called()
        # Player should remain in the original room roster
        assert player_id in from_room._players
        assert player_id not in to_room._players

    def test_move_player_blocked_while_lying(self, movement_harness, event_bus):
        movement_service, mock_persistence = movement_harness
        player_id = str(uuid4())

        player = _configure_player(mock_persistence, player_id, "room_1", position="lying")
        from_room, to_room = _configure_rooms(mock_persistence, event_bus, player_id)

        result = movement_service.move_player(player_id, "room_1", "room_2")

        assert result is False
        player.get_stats.assert_called_once()
        mock_persistence.save_player.assert_not_called()
        assert player_id in from_room._players
        assert player_id not in to_room._players
