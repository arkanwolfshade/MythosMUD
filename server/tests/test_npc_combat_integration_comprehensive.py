"""
Comprehensive tests for NPC Combat Integration.

This module provides additional test coverage for the NPC combat integration
module to improve coverage from 55% to 80%+.
"""

from unittest.mock import Mock, patch
from uuid import uuid4

from server.events.event_types import NPCAttacked, NPCDied
from server.npc.combat_integration import NPCCombatIntegration


class TestNPCCombatIntegrationComprehensive:
    """Comprehensive test cases for NPC Combat Integration."""

    def setup_method(self):
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.game_mechanics = Mock()

        with (
            patch("server.npc.combat_integration.get_persistence") as mock_get_persistence,
            patch("server.npc.combat_integration.GameMechanicsService") as mock_game_mechanics,
        ):
            mock_get_persistence.return_value = self.persistence
            mock_game_mechanics.return_value = self.game_mechanics

            self.integration = NPCCombatIntegration(self.event_bus)

    def test_calculate_damage_physical_attack(self):
        """Test damage calculation for physical attacks."""
        attacker_stats = {"strength": 15}
        target_stats = {"constitution": 10}
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Strength 15 = +2 bonus, constitution 10 = 0 reduction
        # Expected: 5 (base) + 2 (strength) - 0 (constitution) = 7
        assert damage == 7

    def test_calculate_damage_high_strength_attacker(self):
        """Test damage calculation with high strength attacker."""
        attacker_stats = {"strength": 18}
        target_stats = {"constitution": 10}
        weapon_damage = 3

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Strength 18 = +4 bonus, constitution 10 = 0 reduction
        # Expected: 3 (base) + 4 (strength) - 0 (constitution) = 7
        assert damage == 7

    def test_calculate_damage_high_constitution_target(self):
        """Test damage calculation against high constitution target."""
        attacker_stats = {"strength": 12}
        target_stats = {"constitution": 18}
        weapon_damage = 8

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Strength 12 = +1 bonus, constitution 18 = +2 reduction
        # Expected: 8 (base) + 1 (strength) - 2 (constitution) = 7
        assert damage == 7

    def test_calculate_damage_non_physical_attack(self):
        """Test damage calculation for non-physical attacks."""
        attacker_stats = {"strength": 15}
        target_stats = {"constitution": 10}
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "mental")

        # Non-physical attacks don't get strength bonus
        # Expected: 5 (base) - 0 (constitution) = 5
        assert damage == 5

    def test_calculate_damage_minimum_damage(self):
        """Test that damage is always at least 1."""
        attacker_stats = {"strength": 8}  # Low strength
        target_stats = {"constitution": 20}  # Very high constitution
        weapon_damage = 1

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should be minimum 1 damage
        assert damage == 1

    def test_calculate_damage_exception_handling(self):
        """Test damage calculation handles exceptions gracefully."""
        attacker_stats = {"strength": "invalid"}  # Invalid strength
        target_stats = {"constitution": 10}
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should return minimum damage on error
        assert damage == 1

    def test_apply_combat_effects_player_success(self):
        """Test applying combat effects to a player successfully."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "physical"
        source_id = str(uuid4())

        # Mock player
        player = Mock()
        self.persistence.get_player.return_value = player
        self.game_mechanics.damage_player.return_value = (True, "Damage applied")

        result = self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)

    def test_apply_combat_effects_player_with_sanity_loss(self):
        """Test applying combat effects with sanity loss for mental damage."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "mental"
        source_id = str(uuid4())

        # Mock player
        player = Mock()
        self.persistence.get_player.return_value = player
        self.game_mechanics.damage_player.return_value = (True, "Damage applied")

        result = self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)
        # Should apply sanity loss for mental damage
        self.game_mechanics.apply_sanity_loss.assert_called_once()

    def test_apply_combat_effects_player_with_fear_gain(self):
        """Test applying combat effects with fear gain for occult damage."""
        target_id = str(uuid4())
        damage = 15
        damage_type = "occult"
        source_id = str(uuid4())

        # Mock player
        player = Mock()
        self.persistence.get_player.return_value = player
        self.game_mechanics.damage_player.return_value = (True, "Damage applied")

        result = self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)
        # Should apply fear for occult damage
        self.game_mechanics.apply_fear.assert_called_once()

    def test_apply_combat_effects_player_with_eldritch_damage(self):
        """Test applying combat effects with fear gain for eldritch damage."""
        target_id = str(uuid4())
        damage = 20
        damage_type = "eldritch"
        source_id = str(uuid4())

        # Mock player
        player = Mock()
        self.persistence.get_player.return_value = player
        self.game_mechanics.damage_player.return_value = (True, "Damage applied")

        result = self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)
        # Should apply fear for eldritch damage
        self.game_mechanics.apply_fear.assert_called_once()

    def test_apply_combat_effects_non_player(self):
        """Test applying combat effects to non-player entity."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "physical"
        source_id = str(uuid4())

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_not_called()

    def test_apply_combat_effects_exception_handling(self):
        """Test applying combat effects handles exceptions gracefully."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "physical"
        source_id = str(uuid4())

        # Mock exception
        self.persistence.get_player.side_effect = Exception("Database error")

        result = self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is False

    def test_handle_npc_attack_with_player_target(self):
        """Test handling NPC attack on player target."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 8
        attack_type = "physical"
        npc_stats = {"strength": 14, "constitution": 12}

        # Mock player target
        player = Mock()
        player.stats.model_dump.return_value = {"constitution": 10}
        self.persistence.get_player.return_value = player

        with patch.object(self.integration, "apply_combat_effects", return_value=True) as mock_apply:
            result = self.integration.handle_npc_attack(
                npc_id, target_id, room_id, attack_damage, attack_type, npc_stats
            )

        assert result is True
        mock_apply.assert_called_once()
        self.event_bus.publish.assert_called_once()

        # Verify event was published
        published_event = self.event_bus.publish.call_args[0][0]
        assert isinstance(published_event, NPCAttacked)
        assert published_event.npc_id == npc_id
        assert published_event.target_id == target_id
        assert published_event.room_id == room_id

    def test_handle_npc_attack_with_npc_target(self):
        """Test handling NPC attack on NPC target."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 8
        attack_type = "physical"
        npc_stats = {"strength": 14, "constitution": 12}

        # Mock no player found (NPC target)
        self.persistence.get_player.return_value = None

        with patch.object(self.integration, "apply_combat_effects", return_value=True) as mock_apply:
            result = self.integration.handle_npc_attack(
                npc_id, target_id, room_id, attack_damage, attack_type, npc_stats
            )

        assert result is True
        mock_apply.assert_called_once()

    def test_handle_npc_attack_with_default_stats(self):
        """Test handling NPC attack with default stats."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 5
        attack_type = "physical"

        # Mock player target
        player = Mock()
        player.stats.model_dump.return_value = {"constitution": 10}
        self.persistence.get_player.return_value = player

        with patch.object(self.integration, "apply_combat_effects", return_value=True) as mock_apply:
            result = self.integration.handle_npc_attack(npc_id, target_id, room_id, attack_damage, attack_type)

        assert result is True
        mock_apply.assert_called_once()

    def test_handle_npc_attack_exception_handling(self):
        """Test handling NPC attack with exception."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 5
        attack_type = "physical"

        # Mock exception
        self.persistence.get_player.side_effect = Exception("Database error")

        result = self.integration.handle_npc_attack(npc_id, target_id, room_id, attack_damage, attack_type)

        assert result is False

    def test_handle_npc_death_with_player_killer(self):
        """Test handling NPC death with player killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "combat"
        killer_id = str(uuid4())

        # Mock player killer
        player = Mock()
        self.persistence.get_player.return_value = player

        # Mock NPC
        npc = Mock()
        npc.npc_type.value = "aggressive_mob"
        self.persistence.get_npc.return_value = npc

        result = self.integration.handle_npc_death(npc_id, room_id, cause, killer_id)

        assert result is True
        self.game_mechanics.gain_occult_knowledge.assert_called_once()
        self.game_mechanics.apply_sanity_loss.assert_called_once()
        self.event_bus.publish.assert_called_once()

        # Verify event was published
        published_event = self.event_bus.publish.call_args[0][0]
        assert isinstance(published_event, NPCDied)
        assert published_event.npc_id == npc_id
        assert published_event.room_id == room_id
        assert published_event.cause == cause
        assert published_event.killer_id == killer_id

    def test_handle_npc_death_without_killer(self):
        """Test handling NPC death without killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "timeout"

        result = self.integration.handle_npc_death(npc_id, room_id, cause)

        assert result is True
        self.game_mechanics.gain_occult_knowledge.assert_not_called()
        self.game_mechanics.apply_sanity_loss.assert_not_called()
        self.event_bus.publish.assert_called_once()

    def test_handle_npc_death_with_non_player_killer(self):
        """Test handling NPC death with non-player killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "combat"
        killer_id = str(uuid4())

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.handle_npc_death(npc_id, room_id, cause, killer_id)

        assert result is True
        self.game_mechanics.gain_occult_knowledge.assert_not_called()
        self.game_mechanics.apply_sanity_loss.assert_not_called()
        self.event_bus.publish.assert_called_once()

    def test_handle_npc_death_exception_handling(self):
        """Test handling NPC death with exception."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "combat"
        killer_id = str(uuid4())

        # Mock exception
        self.persistence.get_player.side_effect = Exception("Database error")

        result = self.integration.handle_npc_death(npc_id, room_id, cause, killer_id)

        assert result is False

    def test_get_combat_stats_player(self):
        """Test getting combat stats for player."""
        entity_id = str(uuid4())

        # Mock player
        player = Mock()
        player.stats.model_dump.return_value = {
            "current_health": 75,
            "max_health": 100,
            "strength": 12,
            "constitution": 14,
            "sanity": 80,
            "fear": 20,
            "corruption": 5,
        }
        self.persistence.get_player.return_value = player

        result = self.integration.get_combat_stats(entity_id)

        assert result["hp"] == 75
        assert result["max_hp"] == 100
        assert result["strength"] == 12
        assert result["constitution"] == 14
        assert result["sanity"] == 80
        assert result["fear"] == 20
        assert result["corruption"] == 5

    def test_get_combat_stats_npc_with_stats(self):
        """Test getting combat stats for NPC with provided stats."""
        entity_id = str(uuid4())
        npc_stats = {
            "hp": 50,
            "max_hp": 50,
            "strength": 10,
            "constitution": 8,
        }

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.get_combat_stats(entity_id, npc_stats)

        assert result == npc_stats

    def test_get_combat_stats_npc_without_stats(self):
        """Test getting combat stats for NPC without stats."""
        entity_id = str(uuid4())

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.get_combat_stats(entity_id)

        assert result == {}

    def test_get_combat_stats_database_error_with_npc_stats(self):
        """Test getting combat stats with database error but NPC stats provided."""
        entity_id = str(uuid4())
        npc_stats = {"hp": 50, "max_hp": 50}

        # Mock database error
        self.persistence.get_player.side_effect = Exception("Database error")

        result = self.integration.get_combat_stats(entity_id, npc_stats)

        assert result == npc_stats

    def test_get_combat_stats_database_error_without_npc_stats(self):
        """Test getting combat stats with database error and no NPC stats."""
        entity_id = str(uuid4())

        # Mock database error
        self.persistence.get_player.side_effect = Exception("Database error")

        result = self.integration.get_combat_stats(entity_id)

        assert result == {}

    def test_get_combat_stats_entity_not_found(self):
        """Test getting combat stats for entity not found."""
        entity_id = str(uuid4())

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.get_combat_stats(entity_id)

        assert result == {}


class TestNPCCombatIntegrationEdgeCases:
    """Test edge cases for NPC Combat Integration."""

    def setup_method(self):
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.game_mechanics = Mock()

        with (
            patch("server.npc.combat_integration.get_persistence") as mock_get_persistence,
            patch("server.npc.combat_integration.GameMechanicsService") as mock_game_mechanics,
        ):
            mock_get_persistence.return_value = self.persistence
            mock_game_mechanics.return_value = self.game_mechanics

            self.integration = NPCCombatIntegration(self.event_bus)

    def test_calculate_damage_extreme_values(self):
        """Test damage calculation with extreme values."""
        attacker_stats = {"strength": 1}  # Minimum strength
        target_stats = {"constitution": 20}  # Maximum constitution
        weapon_damage = 0  # No weapon damage

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should still return minimum 1 damage
        assert damage == 1

    def test_calculate_damage_missing_stats(self):
        """Test damage calculation with missing stats."""
        attacker_stats = {}  # No stats
        target_stats = {}  # No stats
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should use default values (10 for strength/constitution)
        assert damage == 5

    def test_apply_combat_effects_capped_sanity_loss(self):
        """Test that sanity loss is capped appropriately."""
        target_id = str(uuid4())
        damage = 50  # High damage
        damage_type = "mental"

        # Mock player
        player = Mock()
        self.persistence.get_player.return_value = player
        self.game_mechanics.damage_player.return_value = (True, "Damage applied")

        self.integration.apply_combat_effects(target_id, damage, damage_type)

        # Should apply capped sanity loss (max 10)
        self.game_mechanics.apply_sanity_loss.assert_called_once()
        call_args = self.game_mechanics.apply_sanity_loss.call_args
        assert call_args[0][1] <= 10  # Sanity loss should be capped

    def test_apply_combat_effects_capped_fear_gain(self):
        """Test that fear gain is capped appropriately."""
        target_id = str(uuid4())
        damage = 50  # High damage
        damage_type = "occult"

        # Mock player
        player = Mock()
        self.persistence.get_player.return_value = player
        self.game_mechanics.damage_player.return_value = (True, "Damage applied")

        self.integration.apply_combat_effects(target_id, damage, damage_type)

        # Should apply capped fear gain (max 5)
        self.game_mechanics.apply_fear.assert_called_once()
        call_args = self.game_mechanics.apply_fear.call_args
        assert call_args[0][1] <= 5  # Fear gain should be capped
