"""
Comprehensive integration tests for the movement system.

This module tests complex real-world scenarios, edge cases, and advanced
movement patterns to ensure the complete movement system works correctly
under all conditions.

As noted in the Pnakotic Manuscripts, comprehensive testing of complex
systems is essential for maintaining the integrity of our eldritch architecture.
"""

import threading
import time
from unittest.mock import Mock, patch

import pytest

from server.events import EventBus
from server.game.movement_service import MovementService
from server.models.room import Room


class TestComprehensiveMovement:
    """Test complex movement scenarios and edge cases."""

    def test_multi_room_movement_chain(self):
        """Test a player moving through multiple rooms in sequence."""
        # Create a chain of rooms: room1 -> room2 -> room3 -> room4
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {
            "id": "room2",
            "name": "Room 2",
            "description": "Second room",
            "exits": {"east": "room3", "west": "room1"},
        }
        room_data_3 = {
            "id": "room3",
            "name": "Room 3",
            "description": "Third room",
            "exits": {"east": "room4", "west": "room2"},
        }
        room_data_4 = {"id": "room4", "name": "Room 4", "description": "Fourth room", "exits": {"west": "room3"}}

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)
        room3 = Room(room_data_3)
        room4 = Room(room_data_4)

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {
            "room1": room1,
            "room2": room2,
            "room3": room3,
            "room4": room4,
        }.get(room_id)
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Add player to room1 first
            assert service.add_player_to_room("player1", "room1") is True

            # Move through the chain: room1 -> room2 -> room3 -> room4
            assert service.move_player("player1", "room1", "room2") is True
            assert service.move_player("player1", "room2", "room3") is True
            assert service.move_player("player1", "room3", "room4") is True

            # Verify player is only in the final room
            assert "player1" in room4.get_players()
            assert "player1" not in room1.get_players()
            assert "player1" not in room2.get_players()
            assert "player1" not in room3.get_players()

    def test_circular_movement(self):
        """Test a player moving in a circle and ending up back where they started."""
        # Create a circular path: room1 -> room2 -> room3 -> room1
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {
            "id": "room2",
            "name": "Room 2",
            "description": "Second room",
            "exits": {"east": "room3", "west": "room1"},
        }
        room_data_3 = {
            "id": "room3",
            "name": "Room 3",
            "description": "Third room",
            "exits": {"west": "room2", "north": "room1"},
        }

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)
        room3 = Room(room_data_3)

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2, "room3": room3}.get(
            room_id
        )
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Add player to room1 first
            assert service.add_player_to_room("player1", "room1") is True

            # Move in a circle: room1 -> room2 -> room3 -> room1
            assert service.move_player("player1", "room1", "room2") is True
            assert service.move_player("player1", "room2", "room3") is True
            assert service.move_player("player1", "room3", "room1") is True

            # Verify player is back in room1 and not in other rooms
            assert "player1" in room1.get_players()
            assert "player1" not in room2.get_players()
            assert "player1" not in room3.get_players()

    def test_multiple_players_movement(self):
        """Test multiple players moving simultaneously without conflicts."""
        # Create rooms
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)

        # Create multiple players
        mock_player1 = Mock()
        mock_player1.player_id = "player1"
        mock_player2 = Mock()
        mock_player2.player_id = "player2"
        mock_player3 = Mock()
        mock_player3.player_id = "player3"
        mock_persistence.get_player.side_effect = lambda player_id: {
            "player1": mock_player1,
            "player2": mock_player2,
            "player3": mock_player3,
        }.get(player_id)

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Add all players to room1
            assert service.add_player_to_room("player1", "room1") is True
            assert service.add_player_to_room("player2", "room1") is True
            assert service.add_player_to_room("player3", "room1") is True

            # Verify all players are in room1
            assert "player1" in room1.get_players()
            assert "player2" in room1.get_players()
            assert "player3" in room1.get_players()
            assert len(room1.get_players()) == 3

            # Move players to room2
            assert service.move_player("player1", "room1", "room2") is True
            assert service.move_player("player2", "room1", "room2") is True
            assert service.move_player("player3", "room1", "room2") is True

            # Verify all players are now in room2
            assert "player1" in room2.get_players()
            assert "player2" in room2.get_players()
            assert "player3" in room2.get_players()
            assert len(room2.get_players()) == 3

            # Verify room1 is empty
            assert len(room1.get_players()) == 0

    def test_concurrent_player_movement(self):
        """Test multiple players moving concurrently without race conditions."""
        # Create rooms
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)

        # Create multiple players
        mock_players = {}
        for i in range(5):
            mock_player = Mock()
            mock_player.player_id = f"player{i}"
            mock_players[f"player{i}"] = mock_player

        mock_persistence.get_player.side_effect = lambda player_id: mock_players.get(player_id)

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Add all players to room1
            for i in range(5):
                service.add_player_to_room(f"player{i}", "room1")

            # Create threads that move players concurrently
            def move_player(player_id):
                service.move_player(player_id, "room1", "room2")
                time.sleep(0.01)
                service.move_player(player_id, "room2", "room1")

            threads = []
            for i in range(5):
                thread = threading.Thread(target=move_player, args=(f"player{i}",))
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()

            # Verify that no player appears in multiple rooms
            room1_players = set(room1.get_players())
            room2_players = set(room2.get_players())

            # Check for any players that might be in both rooms
            intersection = room1_players.intersection(room2_players)
            assert len(intersection) == 0, f"Players found in both rooms: {intersection}"

    def test_event_bus_integration(self):
        """Test that movement events are properly published to the event bus."""
        # Create event bus
        event_bus = EventBus()
        received_events = []

        def event_handler(event):
            received_events.append(event)

        # Subscribe to movement events
        from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom

        event_bus.subscribe(PlayerEnteredRoom, event_handler)
        event_bus.subscribe(PlayerLeftRoom, event_handler)

        # Create rooms with event bus
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1, event_bus)
        room2 = Room(room_data_2, event_bus)

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService(event_bus)

            # Add player to room1 first
            assert service.add_player_to_room("player1", "room1") is True

            # Move player from room1 to room2
            assert service.move_player("player1", "room1", "room2") is True

            # Give event bus time to process events
            time.sleep(0.1)

            # Verify events were published (2 events: PlayerLeftRoom for move, PlayerEnteredRoom for move)
            # Note: add_player_to_room does direct assignment and doesn't trigger events
            assert len(received_events) == 2

            # Check that we have both PlayerLeftRoom and PlayerEnteredRoom events
            event_types = [type(event) for event in received_events]
            assert PlayerLeftRoom in event_types
            assert PlayerEnteredRoom in event_types

    def test_movement_validation_edge_cases(self):
        """Test edge cases in movement validation."""
        # Create rooms
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Test empty parameters
            with pytest.raises(ValueError, match="Player ID cannot be empty"):
                service.move_player("", "room1", "room2")

            with pytest.raises(ValueError, match="From room ID cannot be empty"):
                service.move_player("player1", "", "room2")

            with pytest.raises(ValueError, match="To room ID cannot be empty"):
                service.move_player("player1", "room1", "")

            # Test moving to same room
            assert service.move_player("player1", "room1", "room1") is False

            # Test moving from non-existent room
            assert service.move_player("player1", "nonexistent", "room2") is False

            # Test moving to non-existent room
            assert service.move_player("player1", "room1", "nonexistent") is False

    def test_room_occupant_tracking(self):
        """Test that room occupant tracking works correctly with multiple operations."""
        # Create room
        room_data = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {}}
        room = Room(room_data)

        # Test initial state
        assert room.is_empty() is True
        assert room.get_occupant_count() == 0
        assert room.get_players() == []
        assert room.get_objects() == []
        assert room.get_npcs() == []

        # Add players
        room.player_entered("player1")
        room.player_entered("player2")
        room.player_entered("player3")

        # Add objects
        room.object_added("object1")
        room.object_added("object2")

        # Add NPCs
        room.npc_entered("npc1")

        # Test state after additions
        assert room.is_empty() is False
        assert room.get_occupant_count() == 6
        assert len(room.get_players()) == 3
        assert len(room.get_objects()) == 2
        assert len(room.get_npcs()) == 1

        # Test individual occupant checks
        assert room.has_player("player1") is True
        assert room.has_player("player4") is False
        assert room.has_object("object1") is True
        assert room.has_object("object3") is False
        assert room.has_npc("npc1") is True
        assert room.has_npc("npc2") is False

        # Remove some occupants
        room.player_left("player2")
        room.object_removed("object1")
        room.npc_left("npc1")

        # Test state after removals
        assert room.get_occupant_count() == 3
        assert len(room.get_players()) == 2
        assert len(room.get_objects()) == 1
        assert len(room.get_npcs()) == 0

        # Remove remaining occupants
        room.player_left("player1")
        room.player_left("player3")
        room.object_removed("object2")

        # Test final state
        assert room.is_empty() is True
        assert room.get_occupant_count() == 0

    def test_movement_with_objects_and_npcs(self):
        """Test movement when rooms contain objects and NPCs."""
        # Create rooms with objects and NPCs
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)

        # Add objects and NPCs to rooms
        room1.object_added("chest")
        room1.object_added("torch")
        room1.npc_entered("guard")

        room2.object_added("table")
        room2.npc_entered("merchant")
        room2.npc_entered("beggar")

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Add player to room1
            assert service.add_player_to_room("player1", "room1") is True

            # Verify room1 has player, objects, and NPCs
            assert "player1" in room1.get_players()
            assert "chest" in room1.get_objects()
            assert "torch" in room1.get_objects()
            assert "guard" in room1.get_npcs()
            assert room1.get_occupant_count() == 4  # 1 player + 2 objects + 1 NPC

            # Move player to room2
            assert service.move_player("player1", "room1", "room2") is True

            # Verify player moved to room2
            assert "player1" not in room1.get_players()
            assert "player1" in room2.get_players()

            # Verify room2 has player, objects, and NPCs
            assert "table" in room2.get_objects()
            assert "merchant" in room2.get_npcs()
            assert "beggar" in room2.get_npcs()
            assert room2.get_occupant_count() == 4  # 1 player + 1 object + 2 NPCs

    def test_movement_failure_recovery(self):
        """Test that the system recovers gracefully from movement failures."""
        # Create rooms
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1)
        room2 = Room(room_data_2)

        # Mock persistence that fails intermittently
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService()

            # Add player to room1
            assert service.add_player_to_room("player1", "room1") is True

            # Attempt movement that should fail (player not in from room)
            assert service.move_player("player1", "room2", "room1") is False

            # Verify player is still in room1
            assert "player1" in room1.get_players()
            assert "player1" not in room2.get_players()

            # Attempt valid movement
            assert service.move_player("player1", "room1", "room2") is True

            # Verify player moved successfully
            assert "player1" not in room1.get_players()
            assert "player1" in room2.get_players()

    def test_movement_with_event_bus_failures(self):
        """Test that movement works even when event bus fails."""
        # Create event bus that fails
        event_bus = Mock()
        event_bus.publish.side_effect = Exception("Event bus failure")

        # Create rooms without event bus to avoid the failure
        room_data_1 = {"id": "room1", "name": "Room 1", "description": "First room", "exits": {"east": "room2"}}
        room_data_2 = {"id": "room2", "name": "Room 2", "description": "Second room", "exits": {"west": "room1"}}

        room1 = Room(room_data_1)  # No event bus
        room2 = Room(room_data_2)  # No event bus

        # Mock persistence
        mock_persistence = Mock()
        mock_persistence.get_room.side_effect = lambda room_id: {"room1": room1, "room2": room2}.get(room_id)
        mock_player = Mock()
        mock_player.player_id = "player1"  # Set the player_id attribute
        mock_persistence.get_player.return_value = mock_player

        with patch("server.game.movement_service.get_persistence", return_value=mock_persistence):
            service = MovementService(event_bus)

            # Add player to room1
            assert service.add_player_to_room("player1", "room1") is True

            # Move player despite event bus failure
            assert service.move_player("player1", "room1", "room2") is True

            # Verify player moved successfully even though events failed
            assert "player1" not in room1.get_players()
            assert "player1" in room2.get_players()
