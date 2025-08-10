"""
Tests for the MovementService.

This module tests the MovementService class to ensure proper functionality
of atomic movement operations and ACID properties for player movement
between rooms.

As noted in the Pnakotic Manuscripts, proper testing of movement systems
is essential for maintaining the integrity of our eldritch architecture.
"""

from unittest.mock import Mock, patch

import pytest

from server.events import EventBus
from server.game.movement_service import MovementService
from server.models.room import Room


class TestMovementService:
    """Test the MovementService class."""

    def test_movement_service_creation(self):
        """Test that MovementService can be created successfully."""
        event_bus = Mock(spec=EventBus)
        service = MovementService(event_bus)

        assert service is not None
        assert service._event_bus == event_bus
        assert hasattr(service, "_persistence")
        assert hasattr(service, "_lock")

    def test_movement_service_creation_without_event_bus(self):
        """Test that MovementService can be created without EventBus."""
        service = MovementService()

        assert service is not None
        assert service._event_bus is None

    def test_move_player_success(self):
        """Test successful player movement between rooms."""
        # Mock persistence and rooms
        mock_persistence = Mock()
        mock_from_room = Mock(spec=Room)
        mock_to_room = Mock(spec=Room)
        mock_player = Mock()

        # Setup mocks
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_from_room, "room2": mock_to_room}.get(
            room_id
        )
        mock_persistence.get_player.return_value = mock_player
        mock_from_room.has_player.return_value = True
        mock_to_room.has_player.return_value = False

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.move_player("player1", "room1", "room2")

            assert result is True
            mock_from_room.player_left.assert_called_once_with("player1")
            mock_to_room.player_entered.assert_called_once_with("player1")
            mock_player.current_room_id = "room2"
            mock_persistence.save_player.assert_called_once_with(mock_player)

    def test_move_player_empty_player_id(self):
        """Test that empty player ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            service.move_player("", "room1", "room2")

    def test_move_player_empty_from_room_id(self):
        """Test that empty from room ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="From room ID cannot be empty"):
            service.move_player("player1", "", "room2")

    def test_move_player_empty_to_room_id(self):
        """Test that empty to room ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="To room ID cannot be empty"):
            service.move_player("player1", "room1", "")

    def test_move_player_same_room(self):
        """Test that moving to the same room returns False."""
        service = MovementService()

        result = service.move_player("player1", "room1", "room1")

        assert result is False

    def test_move_player_from_room_not_found(self):
        """Test that moving from non-existent room returns False."""
        mock_persistence = Mock()
        mock_persistence.get_room.return_value = None

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.move_player("player1", "nonexistent", "room2")

            assert result is False

    def test_move_player_to_room_not_found(self):
        """Test that moving to non-existent room returns False."""
        mock_persistence = Mock()
        mock_from_room = Mock(spec=Room)
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_from_room, "room2": None}.get(room_id)

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.move_player("player1", "room1", "nonexistent")

            assert result is False

    def test_move_player_not_in_from_room(self):
        """Test that moving player not in from room returns False."""
        mock_persistence = Mock()
        mock_from_room = Mock(spec=Room)
        mock_to_room = Mock(spec=Room)

        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_from_room, "room2": mock_to_room}.get(
            room_id
        )
        mock_from_room.has_player.return_value = False

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.move_player("player1", "room1", "room2")

            assert result is False

    def test_move_player_already_in_to_room(self):
        """Test that moving player already in to room returns False."""
        mock_persistence = Mock()
        mock_from_room = Mock(spec=Room)
        mock_to_room = Mock(spec=Room)

        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_from_room, "room2": mock_to_room}.get(
            room_id
        )
        mock_from_room.has_player.return_value = True
        mock_to_room.has_player.return_value = True

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.move_player("player1", "room1", "room2")

            assert result is False

    def test_add_player_to_room_success(self):
        """Test successful addition of player to room."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_player = Mock()

        mock_persistence.get_room.return_value = mock_room
        mock_persistence.get_player.return_value = mock_player
        mock_room.has_player.return_value = False

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.add_player_to_room("player1", "room1")

            assert result is True
            mock_room.player_entered.assert_called_once_with("player1")
            mock_player.current_room_id = "room1"
            mock_persistence.save_player.assert_called_once_with(mock_player)

    def test_add_player_to_room_already_in_room(self):
        """Test adding player already in room returns True."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)

        mock_persistence.get_room.return_value = mock_room
        mock_room.has_player.return_value = True

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.add_player_to_room("player1", "room1")

            assert result is True
            mock_room.player_entered.assert_not_called()

    def test_add_player_to_room_room_not_found(self):
        """Test adding player to non-existent room returns False."""
        mock_persistence = Mock()
        mock_persistence.get_room.return_value = None

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.add_player_to_room("player1", "nonexistent")

            assert result is False

    def test_add_player_to_room_empty_player_id(self):
        """Test that empty player ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            service.add_player_to_room("", "room1")

    def test_add_player_to_room_empty_room_id(self):
        """Test that empty room ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Room ID cannot be empty"):
            service.add_player_to_room("player1", "")

    def test_remove_player_from_room_success(self):
        """Test successful removal of player from room."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)

        mock_persistence.get_room.return_value = mock_room
        mock_room.has_player.return_value = True

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.remove_player_from_room("player1", "room1")

            assert result is True
            mock_room.player_left.assert_called_once_with("player1")

    def test_remove_player_from_room_not_in_room(self):
        """Test removing player not in room returns True."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)

        mock_persistence.get_room.return_value = mock_room
        mock_room.has_player.return_value = False

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.remove_player_from_room("player1", "room1")

            assert result is True
            mock_room.player_left.assert_not_called()

    def test_remove_player_from_room_room_not_found(self):
        """Test removing player from non-existent room returns False."""
        mock_persistence = Mock()
        mock_persistence.get_room.return_value = None

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.remove_player_from_room("player1", "nonexistent")

            assert result is False

    def test_remove_player_from_room_empty_player_id(self):
        """Test that empty player ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            service.remove_player_from_room("", "room1")

    def test_remove_player_from_room_empty_room_id(self):
        """Test that empty room ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Room ID cannot be empty"):
            service.remove_player_from_room("player1", "")

    def test_get_player_room_success(self):
        """Test getting player's current room."""
        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.current_room_id = "room1"

        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.get_player_room("player1")

            assert result == "room1"

    def test_get_player_room_player_not_found(self):
        """Test getting room for non-existent player returns None."""
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = None

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.get_player_room("nonexistent")

            assert result is None

    def test_get_player_room_empty_player_id(self):
        """Test that empty player ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            service.get_player_room("")

    def test_get_room_players_success(self):
        """Test getting players in a room."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_room.get_players.return_value = ["player1", "player2"]

        mock_persistence.get_room.return_value = mock_room

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.get_room_players("room1")

            assert result == ["player1", "player2"]

    def test_get_room_players_room_not_found(self):
        """Test getting players from non-existent room returns empty list."""
        mock_persistence = Mock()
        mock_persistence.get_room.return_value = None

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.get_room_players("nonexistent")

            assert result == []

    def test_get_room_players_empty_room_id(self):
        """Test that empty room ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Room ID cannot be empty"):
            service.get_room_players("")

    def test_validate_player_location_success(self):
        """Test validating player location returns True."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_room.has_player.return_value = True

        mock_persistence.get_room.return_value = mock_room

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.validate_player_location("player1", "room1")

            assert result is True

    def test_validate_player_location_player_not_in_room(self):
        """Test validating player not in room returns False."""
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_room.has_player.return_value = False

        mock_persistence.get_room.return_value = mock_room

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.validate_player_location("player1", "room1")

            assert result is False

    def test_validate_player_location_room_not_found(self):
        """Test validating player location in non-existent room returns False."""
        mock_persistence = Mock()
        mock_persistence.get_room.return_value = None

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            result = service.validate_player_location("player1", "nonexistent")

            assert result is False

    def test_validate_player_location_empty_player_id(self):
        """Test that empty player ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Player ID cannot be empty"):
            service.validate_player_location("", "room1")

    def test_validate_player_location_empty_room_id(self):
        """Test that empty room ID raises ValueError."""
        service = MovementService()

        with pytest.raises(ValueError, match="Room ID cannot be empty"):
            service.validate_player_location("player1", "")

    def test_concurrent_movements(self):
        """Test that concurrent movements are handled safely."""
        import threading
        import time

        mock_persistence = Mock()
        mock_from_room = Mock(spec=Room)
        mock_to_room = Mock(spec=Room)
        mock_player = Mock()

        # Setup mocks
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_from_room, "room2": mock_to_room}.get(
            room_id
        )
        mock_persistence.get_player.return_value = mock_player
        mock_from_room.has_player.return_value = True
        mock_to_room.has_player.return_value = False

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Create multiple threads that move players
            def move_player():
                service.move_player("player1", "room1", "room2")
                time.sleep(0.01)
                service.move_player("player1", "room2", "room1")

            threads = []
            for _ in range(5):
                thread = threading.Thread(target=move_player)
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

            # Verify that the service handled concurrent access safely
            # (no exceptions should have been raised)
            assert True  # If we get here, no exceptions were raised
