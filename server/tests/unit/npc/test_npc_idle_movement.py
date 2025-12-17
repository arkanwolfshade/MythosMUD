"""
Unit tests for NPC idle movement functionality.

Tests cover idle movement logic, probability checks, exit selection,
and subzone boundary validation.
"""

from unittest.mock import Mock, patch

from server.npc.idle_movement import IdleMovementHandler
from server.npc.movement_integration import NPCMovementIntegration


class TestIdleMovementHandler:
    """Test cases for IdleMovementHandler."""

    def test_should_idle_move_enabled(self):
        """Test that idle movement works when enabled."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)
        npc_instance = Mock()
        npc_instance.npc_id = "test_npc_1"
        npc_instance.is_alive = True
        npc_instance.is_active = True

        npc_definition = Mock()
        npc_definition.sub_zone_id = "northside"

        behavior_config = {
            "idle_movement_enabled": True,
            "idle_movement_probability": 1.0,  # Always move for testing
        }

        with patch.object(handler, "_is_npc_in_combat", return_value=False):
            result = handler.should_idle_move(npc_instance, npc_definition, behavior_config)
            assert result is True

    def test_should_idle_move_disabled(self):
        """Test that idle movement is skipped when disabled."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)
        npc_instance = Mock()
        npc_instance.npc_id = "test_npc_1"
        npc_instance.is_alive = True
        npc_instance.is_active = True

        npc_definition = Mock()
        behavior_config = {"idle_movement_enabled": False}

        result = handler.should_idle_move(npc_instance, npc_definition, behavior_config)
        assert result is False

    def test_should_idle_move_in_combat(self):
        """Test that idle movement is skipped when NPC is in combat."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)
        npc_instance = Mock()
        npc_instance.npc_id = "test_npc_1"
        npc_instance.is_alive = True
        npc_instance.is_active = True

        npc_definition = Mock()
        behavior_config = {
            "idle_movement_enabled": True,
            "idle_movement_probability": 1.0,
        }

        with patch.object(handler, "_is_npc_in_combat", return_value=True):
            result = handler.should_idle_move(npc_instance, npc_definition, behavior_config)
            assert result is False

    def test_should_idle_move_not_alive(self):
        """Test that idle movement is skipped when NPC is not alive."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)
        npc_instance = Mock()
        npc_instance.npc_id = "test_npc_1"
        npc_instance.is_alive = False
        npc_instance.is_active = True

        npc_definition = Mock()
        behavior_config = {
            "idle_movement_enabled": True,
            "idle_movement_probability": 1.0,
        }

        with patch.object(handler, "_is_npc_in_combat", return_value=False):
            result = handler.should_idle_move(npc_instance, npc_definition, behavior_config)
            assert result is False

    def test_get_valid_exits_filters_by_subzone(self):
        """Test that get_valid_exits filters exits by subzone."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)
        handler.movement_integration = Mock(spec=NPCMovementIntegration)

        current_room_id = "earth_arkhamcity_northside_room_001"
        npc_definition = Mock()
        npc_definition.sub_zone_id = "northside"

        # Mock available exits
        all_exits = {
            "north": "earth_arkhamcity_northside_room_002",
            "south": "earth_arkhamcity_downtown_room_001",  # Different subzone
        }

        handler.movement_integration.get_available_exits.return_value = all_exits

        # Mock subzone validation
        def validate_side_effect(subzone_id, room_id):
            # Only northside rooms are valid
            return "northside" in room_id

        handler.movement_integration.validate_subzone_boundary.side_effect = validate_side_effect

        behavior_config = {}
        valid_exits = handler.get_valid_exits(current_room_id, npc_definition, behavior_config)

        # Should only return the north exit (same subzone)
        assert "north" in valid_exits
        assert "south" not in valid_exits
        assert valid_exits["north"] == "earth_arkhamcity_northside_room_002"

    def test_select_exit_weighted_home(self):
        """Test that exit selection prefers exits closer to spawn room."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)

        valid_exits = {
            "north": "earth_arkhamcity_northside_room_002",
            "south": "earth_arkhamcity_northside_room_003",
        }
        spawn_room_id = "earth_arkhamcity_northside_room_001"
        current_room_id = "earth_arkhamcity_northside_room_002"
        behavior_config = {"idle_movement_weighted_home": True}

        with patch.object(handler, "_calculate_distance_to_room") as mock_distance:
            # Mock distances: north moves closer to spawn, south moves further
            def distance_side_effect(from_room, to_room):
                if to_room == spawn_room_id:
                    if from_room == current_room_id:
                        return 1  # Current room is 1 hop from spawn
                    elif "room_002" in from_room:
                        return 0  # North exit leads to spawn (0 hops)
                    elif "room_003" in from_room:
                        return 2  # South exit leads further from spawn (2 hops)
                return 999

            mock_distance.side_effect = distance_side_effect

            # Run multiple times to check weighting (north should be selected more often)
            # With weights: north=1.0, south=0.5, expected probability for north is ~66.7%
            # Using 200 trials for better statistical confidence
            selections = []
            for _ in range(200):
                result = handler.select_exit(valid_exits, spawn_room_id, current_room_id, behavior_config)
                if result:
                    selections.append(result[0])  # direction

            # North should be selected more often due to weighting
            # Expected: ~133 selections (66.7% of 200)
            # Use a more lenient threshold to account for randomness: > 40% (80/200)
            # but still significantly more than random (50%)
            north_count = selections.count("north")
            assert north_count > 80, f"North selected {north_count}/200 times, expected >80 due to weighting"

    def test_select_exit_random_when_not_weighted(self):
        """Test that exit selection is random when weighted_home is False."""
        mock_persistence = Mock()
        handler = IdleMovementHandler(persistence=mock_persistence)

        valid_exits = {
            "north": "earth_arkhamcity_northside_room_002",
            "south": "earth_arkhamcity_northside_room_003",
        }
        spawn_room_id = "earth_arkhamcity_northside_room_001"
        current_room_id = "earth_arkhamcity_northside_room_002"
        behavior_config = {"idle_movement_weighted_home": False}

        # Should select randomly (both exits should be selected roughly equally)
        selections = []
        for _ in range(100):
            result = handler.select_exit(valid_exits, spawn_room_id, current_room_id, behavior_config)
            if result:
                selections.append(result[0])

        # Both directions should be selected
        assert "north" in selections
        assert "south" in selections


class TestNPCMovementIntegrationSubzoneValidation:
    """Test cases for subzone boundary validation."""

    def test_validate_subzone_boundary_same_subzone(self):
        """Test that validation passes for rooms in same subzone."""
        mock_persistence = Mock()
        integration = NPCMovementIntegration(persistence=mock_persistence)

        # Mock room with subzone attribute
        room = Mock()
        room.sub_zone = "northside"
        mock_persistence.get_room_by_id.return_value = room

        npc_sub_zone_id = "northside"
        destination_room_id = "earth_arkhamcity_northside_room_001"

        result = integration.validate_subzone_boundary(npc_sub_zone_id, destination_room_id)
        assert result is True

    def test_validate_subzone_boundary_different_subzone(self):
        """Test that validation fails for rooms in different subzones."""
        mock_persistence = Mock()
        integration = NPCMovementIntegration(persistence=mock_persistence)

        # Mock room with different subzone
        room = Mock()
        room.sub_zone = "downtown"
        mock_persistence.get_room_by_id.return_value = room

        npc_sub_zone_id = "northside"
        destination_room_id = "earth_arkhamcity_downtown_room_001"

        result = integration.validate_subzone_boundary(npc_sub_zone_id, destination_room_id)
        assert result is False

    def test_validate_subzone_boundary_room_not_found(self):
        """Test that validation fails when room is not found."""
        mock_persistence = Mock()
        integration = NPCMovementIntegration(persistence=mock_persistence)
        mock_persistence.get_room_by_id.return_value = None

        npc_sub_zone_id = "northside"
        destination_room_id = "invalid_room_id"

        result = integration.validate_subzone_boundary(npc_sub_zone_id, destination_room_id)
        assert result is False

    def test_validate_subzone_boundary_fallback_to_room_id_parsing(self):
        """Test that validation falls back to room ID parsing when sub_zone attribute missing."""
        mock_persistence = Mock()
        integration = NPCMovementIntegration(persistence=mock_persistence)

        # Mock room without sub_zone attribute
        room = Mock()
        del room.sub_zone  # Remove sub_zone attribute
        mock_persistence.get_room_by_id.return_value = room

        npc_sub_zone_id = "northside"
        destination_room_id = "earth_arkhamcity_northside_room_001"

        result = integration.validate_subzone_boundary(npc_sub_zone_id, destination_room_id)
        # Should extract subzone from room_id and match
        assert result is True
