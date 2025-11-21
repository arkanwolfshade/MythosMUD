"""
Test movement persistence to database.

This test verifies that when a player moves between rooms,
their location is properly saved to the database.
"""

from unittest.mock import Mock, patch
from uuid import uuid4

import pytest

from server.exceptions import DatabaseError
from server.game.movement_service import MovementService
from server.models.player import Player
from server.models.room import Room


class TestMovementPersistence:
    """Test that player movement is properly persisted to database."""

    def test_move_player_persists_to_database(self):
        """Test that move_player saves the player's new location to database."""
        # Create mock persistence layer
        mock_persistence = Mock()

        # Create test player (use proper UUID format)
        test_player_id = str(uuid4())
        test_user_id = str(uuid4())
        player = Player(player_id=test_player_id, user_id=test_user_id, name="TestPlayer", current_room_id="room_1")

        # Create test rooms
        room_1 = Room({"id": "room_1", "name": "Room 1", "description": "First room", "exits": {"north": "room_2"}})
        room_2 = Room({"id": "room_2", "name": "Room 2", "description": "Second room", "exits": {"south": "room_1"}})

        # Configure mocks
        mock_persistence.get_player.return_value = player
        mock_persistence.get_room.side_effect = lambda room_id: room_1 if room_id == "room_1" else room_2

        # Create movement service with mocked persistence
        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            movement_service = MovementService()

            # Add player to room_1
            room_1.player_entered(test_player_id)

            # Move player from room_1 to room_2
            success = movement_service.move_player(test_player_id, "room_1", "room_2")

            # Verify movement was successful
            assert success is True

            # Verify player was removed from room_1 (service uses UUID objects)
            import uuid as uuid_module

            player_id_uuid = uuid_module.UUID(test_player_id)
            assert not room_1.has_player(player_id_uuid)

            # Verify player was added to room_2
            assert room_2.has_player(player_id_uuid)

            # Verify save_player was called with updated player
            mock_persistence.save_player.assert_called_once()
            saved_player = mock_persistence.save_player.call_args[0][0]
            assert saved_player.current_room_id == "room_2"
            assert saved_player.player_id == test_player_id

    def test_move_player_updates_player_current_room_id(self):
        """Test that the player's current_room_id is updated during movement."""
        # Create mock persistence layer
        mock_persistence = Mock()

        # Create test player (use proper UUID format)
        test_player_id = str(uuid4())
        test_user_id = str(uuid4())
        player = Player(
            player_id=test_player_id, user_id=test_user_id, name="TestPlayer2", current_room_id="start_room"
        )

        # Create test rooms
        start_room = Room(
            {"id": "start_room", "name": "Start Room", "description": "Starting room", "exits": {"east": "end_room"}}
        )
        end_room = Room(
            {"id": "end_room", "name": "End Room", "description": "Ending room", "exits": {"west": "start_room"}}
        )

        # Configure mocks
        mock_persistence.get_player.return_value = player
        mock_persistence.get_room.side_effect = lambda room_id: start_room if room_id == "start_room" else end_room

        # Create movement service with mocked persistence
        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            movement_service = MovementService()

            # Add player to start_room
            start_room.player_entered(test_player_id)

            # Verify initial state
            assert player.current_room_id == "start_room"

            # Move player
            success = movement_service.move_player(test_player_id, "start_room", "end_room")

            # Verify movement was successful
            assert success is True

            # Verify player's current_room_id was updated
            assert player.current_room_id == "end_room"

            # Verify save_player was called
            mock_persistence.save_player.assert_called_once_with(player)

    def test_move_player_handles_player_not_found_by_id(self):
        """Test that move_player handles case where player is not found by ID but found by name."""
        # Create mock persistence layer
        mock_persistence = Mock()

        # Create test player
        player = Player(
            player_id="test-player-789", user_id="test-user-789", name="TestPlayer3", current_room_id="room_a"
        )

        # Create test rooms
        room_a = Room({"id": "room_a", "name": "Room A", "description": "Room A", "exits": {"south": "room_b"}})
        room_b = Room({"id": "room_b", "name": "Room B", "description": "Room B", "exits": {"north": "room_a"}})

        # Configure mocks - player not found by ID but found by name
        mock_persistence.get_player.return_value = None
        mock_persistence.get_player_by_name.return_value = player
        mock_persistence.get_room.side_effect = lambda room_id: room_a if room_id == "room_a" else room_b

        # Create movement service with mocked persistence
        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            movement_service = MovementService()

            # Add player to room_a
            room_a.player_entered("test-player-789")

            # Move player (using player name as ID)
            success = movement_service.move_player("TestPlayer3", "room_a", "room_b")

            # Verify movement was successful
            assert success is True

            # Verify save_player was called
            mock_persistence.save_player.assert_called_once()
            saved_player = mock_persistence.save_player.call_args[0][0]
            assert saved_player.current_room_id == "room_b"

    def test_move_player_fails_when_player_not_found(self):
        """Test that move_player fails when player cannot be found."""
        # Create mock persistence layer
        mock_persistence = Mock()

        # Create test rooms
        room_1 = Room({"id": "room_1", "name": "Room 1", "description": "First room", "exits": {"north": "room_2"}})
        room_2 = Room({"id": "room_2", "name": "Room 2", "description": "Second room", "exits": {"south": "room_1"}})

        # Configure mocks - player not found
        mock_persistence.get_player.return_value = None
        mock_persistence.get_player_by_name.return_value = None
        mock_persistence.get_room.side_effect = lambda room_id: room_1 if room_id == "room_1" else room_2

        # Create movement service with mocked persistence
        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            movement_service = MovementService()

            # Add player to room_1
            room_1.player_entered("unknown-player")

            # Try to move player - should raise DatabaseError
            with pytest.raises(DatabaseError, match="Error moving player unknown-player"):
                movement_service.move_player("unknown-player", "room_1", "room_2")

            # Verify save_player was not called
            mock_persistence.save_player.assert_not_called()
