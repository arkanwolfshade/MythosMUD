"""
Test for NPC spawn condition fix.

This test verifies that the fix for NPC spawning conditions works correctly.
The issue was that spawn conditions with "any" values were failing when
the corresponding game state keys didn't exist.
"""

from server.models.npc import NPCSpawnRule


class TestNPCSpawnFix:
    """Test the NPC spawn condition fix."""

    def test_spawn_conditions_with_any_values(self):
        """Test that spawn conditions with 'any' values work correctly."""
        # Create a spawn rule with "any" conditions
        spawn_rule = NPCSpawnRule(
            id=1,
            npc_definition_id=1,
            sub_zone_id="arkhamcity/downtown",
            min_players=1,
            max_players=5,
            spawn_conditions='{"time_of_day": "any", "weather": "any", "special_events": []}',
        )

        # Test with game state that has all required keys
        game_state_with_all_keys = {"time_of_day": "day", "weather": "clear", "player_count": 1, "player_level_min": 1}

        # Should return True since conditions are "any"
        assert spawn_rule.check_spawn_conditions(game_state_with_all_keys)

        # Test with game state that's missing some keys (the bug scenario)
        game_state_missing_keys = {
            "player_count": 1,
            "player_level_min": 1,
            # Missing 'time_of_day' and 'weather' keys
        }

        # Should return True since conditions are "any" (this was failing before the fix)
        assert spawn_rule.check_spawn_conditions(game_state_missing_keys)

    def test_spawn_conditions_with_specific_values(self):
        """Test that spawn conditions with specific values still work correctly."""
        # Create a spawn rule with specific conditions
        spawn_rule = NPCSpawnRule(
            id=2,
            npc_definition_id=2,
            sub_zone_id="arkhamcity/sanitarium",
            min_players=1,
            max_players=5,
            spawn_conditions='{"time_of_day": "night", "weather": "storm"}',
        )

        # Test with matching game state
        matching_game_state = {"time_of_day": "night", "weather": "storm", "player_count": 1, "player_level_min": 1}

        assert spawn_rule.check_spawn_conditions(matching_game_state)

        # Test with non-matching game state
        non_matching_game_state = {"time_of_day": "day", "weather": "clear", "player_count": 1, "player_level_min": 1}

        assert not spawn_rule.check_spawn_conditions(non_matching_game_state)

        # Test with missing keys (should fail for specific conditions)
        missing_keys_game_state = {"player_count": 1, "player_level_min": 1}

        assert not spawn_rule.check_spawn_conditions(missing_keys_game_state)

    def test_spawn_conditions_with_empty_list(self):
        """Test that spawn conditions with empty lists work correctly."""
        # Create a spawn rule with empty list condition
        spawn_rule = NPCSpawnRule(
            id=3,
            npc_definition_id=3,
            sub_zone_id="arkhamcity/warehouse",
            min_players=1,
            max_players=5,
            spawn_conditions='{"special_events": []}',
        )

        # Test with game state that has the key
        game_state_with_key = {"special_events": [], "player_count": 1, "player_level_min": 1}

        assert spawn_rule.check_spawn_conditions(game_state_with_key)

        # Test with game state missing the key (should pass for empty list)
        game_state_missing_key = {"player_count": 1, "player_level_min": 1}

        assert spawn_rule.check_spawn_conditions(game_state_missing_key)

    def test_spawn_conditions_mixed_any_and_specific(self):
        """Test spawn conditions with mixed 'any' and specific values."""
        spawn_rule = NPCSpawnRule(
            id=4,
            npc_definition_id=4,
            sub_zone_id="arkhamcity/port",
            min_players=1,
            max_players=5,
            spawn_conditions='{"time_of_day": "any", "weather": "clear", "special_events": []}',
        )

        # Test with game state that matches specific conditions
        matching_game_state = {
            "weather": "clear",
            "player_count": 1,
            "player_level_min": 1,
            # Missing 'time_of_day' and 'special_events' but they're "any" or empty list
        }

        assert spawn_rule.check_spawn_conditions(matching_game_state)

        # Test with game state that doesn't match specific conditions
        non_matching_game_state = {"weather": "storm", "player_count": 1, "player_level_min": 1}

        assert not spawn_rule.check_spawn_conditions(non_matching_game_state)
