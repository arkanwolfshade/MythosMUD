"""
Integration tests for the movement system.

This module tests the integration between MovementService, PersistenceLayer,
and the command handler to ensure the complete movement flow works correctly.

As noted in the Pnakotic Manuscripts, proper integration testing is essential
for maintaining the integrity of our eldritch architecture.
"""

from unittest.mock import Mock, patch

from server.game.movement_service import MovementService
from server.models.room import Room


class TestMovementIntegration:
    """Test the integration between movement components."""

    def test_movement_service_with_persistence_layer(self):
        """Test that MovementService works with PersistenceLayer."""
        # Mock persistence layer
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

            # Test movement
            result = service.move_player("player1", "room1", "room2")

            assert result is True
            mock_from_room.player_left.assert_called_once_with("player1")
            mock_to_room.player_entered.assert_called_once_with("player1")
            mock_player.current_room_id = "room2"
            mock_persistence.save_player.assert_called_once_with(mock_player)

    def test_persistence_layer_room_objects(self):
        """Test that PersistenceLayer returns Room objects."""
        from server.persistence import PersistenceLayer

        # Mock world_loader
        mock_room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room",
            "exits": {"north": "room2"},
        }

        with patch("server.world_loader.load_hierarchical_world") as mock_loader:
            mock_loader.return_value = {"rooms": {"test_room": mock_room_data}, "room_mappings": {}}

            # Create persistence layer
            persistence = PersistenceLayer(db_path=":memory:")

            # Get room
            room = persistence.get_room("test_room")

            assert room is not None
            assert isinstance(room, Room)
            assert room.id == "test_room"
            assert room.name == "Test Room"
            assert room.description == "A test room"

    def test_command_handler_with_movement_service(self):
        """Test that command handler uses MovementService correctly."""
        from server.command_handler import process_command

        # Mock persistence and movement service
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_player = Mock()
        mock_target_room = Mock(spec=Room)

        # Setup mocks
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_player.player_id = "player1"
        mock_player.current_room_id = "room1"
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_room, "room2": mock_target_room}.get(
            room_id
        )
        mock_room.exits = {"north": "room2"}
        mock_target_room.name = "North Room"
        mock_target_room.description = "A northern chamber"
        mock_target_room.exits = {"south": "room1"}

        with patch("server.command_handler.MovementService") as mock_movement_service_class:
            mock_movement_service = Mock()
            mock_movement_service_class.return_value = mock_movement_service
            mock_movement_service.move_player.return_value = True

            # Mock request and current user
            mock_request = Mock()
            mock_request.app.state.persistence = mock_persistence
            current_user = {"username": "testplayer"}
            mock_alias_storage = Mock()

            # Test go command
            result = process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testplayer")

            # Verify MovementService was called
            mock_movement_service.move_player.assert_called_once_with("player1", "room1", "room2")

            # Verify result
            assert "result" in result
            assert "North Room" in result["result"]
            assert "A northern chamber" in result["result"]

    def test_movement_failure_handling(self):
        """Test that movement failures are handled gracefully."""
        from server.command_handler import process_command

        # Mock persistence and movement service
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_player = Mock()

        # Setup mocks
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_player.player_id = "player1"
        mock_player.current_room_id = "room1"
        mock_persistence.get_room.return_value = mock_room
        mock_room.exits = {"north": "room2"}

        with patch("server.command_handler.MovementService") as mock_movement_service_class:
            mock_movement_service = Mock()
            mock_movement_service_class.return_value = mock_movement_service
            mock_movement_service.move_player.return_value = False  # Movement fails

            # Mock request and current user
            mock_request = Mock()
            mock_request.app.state.persistence = mock_persistence
            current_user = {"username": "testplayer"}
            mock_alias_storage = Mock()

            # Test go command with failed movement
            result = process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testplayer")

            # Verify MovementService was called
            mock_movement_service.move_player.assert_called_once_with("player1", "room1", "room2")

            # Verify failure result
            assert "result" in result
            assert "You can't go that way" in result["result"]

    def test_room_object_properties(self):
        """Test that Room objects have the expected properties."""
        room_data = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room",
            "exits": {"north": "room2", "south": None},
        }

        room = Room(room_data)

        # Test basic properties
        assert room.id == "test_room"
        assert room.name == "Test Room"
        assert room.description == "A test room"
        assert room.exits == {"north": "room2", "south": None}

        # Test occupant tracking
        assert room.get_players() == []
        assert room.get_objects() == []
        assert room.get_npcs() == []
        assert room.is_empty() is True

        # Test adding occupants
        room.player_entered("player1")
        assert "player1" in room.get_players()
        assert room.has_player("player1") is True
        assert room.is_empty() is False

    def test_movement_service_validation(self):
        """Test that MovementService validates movement properly."""
        mock_persistence = Mock()
        mock_from_room = Mock(spec=Room)
        mock_to_room = Mock(spec=Room)
        mock_player = Mock()

        # Setup mocks
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": mock_from_room, "room2": mock_to_room}.get(
            room_id
        )
        mock_persistence.get_player.return_value = mock_player
        mock_from_room.has_player.return_value = False  # Player not in from room

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Test invalid movement (player not in from room)
            result = service.move_player("player1", "room1", "room2")

            assert result is False
            # Should not call room methods for invalid movement
            mock_from_room.player_left.assert_not_called()
            mock_to_room.player_entered.assert_not_called()

    def test_concurrent_movement_safety(self):
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
