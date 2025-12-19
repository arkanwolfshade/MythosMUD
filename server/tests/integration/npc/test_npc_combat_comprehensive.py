"""
Comprehensive tests for NPC Combat Integration.

This module provides additional test coverage for the NPC combat integration
module to improve coverage from 55% to 80%+.
"""

from typing import Any
from unittest.mock import Mock, patch
from uuid import uuid4

import pytest

from server.events.event_types import NPCAttacked
from server.exceptions import DatabaseError
from server.npc.combat_integration import NPCCombatIntegration


class TestNPCCombatIntegrationComprehensive:
    """Comprehensive test cases for NPC Combat Integration."""

    # pylint: disable=attribute-defined-outside-init
    # Attributes are defined in setup_method, which is the pytest pattern for test fixtures.
    # This is intentional and follows pytest best practices.
    def setup_method(self) -> None:
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.game_mechanics = Mock()

        with (
            patch("server.npc.combat_integration.GameMechanicsService") as mock_game_mechanics,
        ):
            mock_game_mechanics.return_value = self.game_mechanics

            self.integration = NPCCombatIntegration(self.event_bus, async_persistence=self.persistence)

    def test_calculate_damage_physical_attack(self) -> None:
        """Test damage calculation for physical attacks."""
        attacker_stats = {"strength": 75}
        target_stats = {"constitution": 50}
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Strength 75 = +12 bonus ((75-50)//2), constitution 50 = 0 reduction ((50-50)//4)
        # Expected: 5 (base) + 12 (strength) - 0 (constitution) = 17
        assert damage == 17

    def test_calculate_damage_high_strength_attacker(self) -> None:
        """Test damage calculation with high strength attacker."""
        attacker_stats = {"strength": 90}
        target_stats = {"constitution": 50}
        weapon_damage = 3

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Strength 90 = +20 bonus ((90-50)//2), constitution 50 = 0 reduction ((50-50)//4)
        # Expected: 3 (base) + 20 (strength) - 0 (constitution) = 23
        assert damage == 23

    def test_calculate_damage_high_constitution_target(self) -> None:
        """Test damage calculation against high constitution target."""
        attacker_stats = {"strength": 60}
        target_stats = {"constitution": 90}
        weapon_damage = 8

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Strength 60 = +5 bonus ((60-50)//2), constitution 90 = +10 reduction ((90-50)//4)
        # Expected: 8 (base) + 5 (strength) - 10 (constitution) = 3
        assert damage == 3

    def test_calculate_damage_non_physical_attack(self) -> None:
        """Test damage calculation for non-physical attacks."""
        attacker_stats = {"strength": 15}
        target_stats = {"constitution": 10}
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "mental")

        # Non-physical attacks don't get strength bonus
        # Expected: 5 (base) - 0 (constitution) = 5
        assert damage == 5

    def test_calculate_damage_minimum_damage(self) -> None:
        """Test that damage is always at least 1."""
        attacker_stats = {"strength": 8}  # Low strength
        target_stats = {"constitution": 20}  # Very high constitution
        weapon_damage = 1

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should be minimum 1 damage
        assert damage == 1

    def test_calculate_damage_exception_handling(self) -> None:
        """Test damage calculation handles exceptions gracefully."""
        attacker_stats = {"strength": "invalid"}  # Invalid strength
        target_stats = {"constitution": 10}
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should return minimum damage on error
        assert damage == 1

    @pytest.mark.asyncio
    async def test_apply_combat_effects_player_success(self) -> None:
        """Test applying combat effects to a player successfully."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "physical"
        source_id = str(uuid4())

        # Mock player - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)
        self.game_mechanics.damage_player = AsyncMock(return_value=(True, "Damage applied"))

        result = await self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)

    @pytest.mark.asyncio
    async def test_apply_combat_effects_player_with_Lucidity_loss(self) -> None:
        """Test applying combat effects with lucidity loss for mental damage."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "mental"
        source_id = str(uuid4())

        # Mock player - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)
        self.game_mechanics.damage_player = AsyncMock(return_value=(True, "Damage applied"))
        self.game_mechanics.apply_lucidity_loss = AsyncMock()

        result = await self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)
        # Should apply lucidity loss for mental damage
        self.game_mechanics.apply_lucidity_loss.assert_called_once()

    @pytest.mark.asyncio
    async def test_apply_combat_effects_player_with_fear_gain(self) -> None:
        """Test applying combat effects with fear gain for occult damage."""
        target_id = str(uuid4())
        damage = 15
        damage_type = "occult"
        source_id = str(uuid4())

        # Mock player - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)
        self.game_mechanics.damage_player = AsyncMock(return_value=(True, "Damage applied"))
        # Occult damage triggers both lucidity loss and fear
        self.game_mechanics.apply_lucidity_loss = AsyncMock()
        self.game_mechanics.apply_fear = AsyncMock()

        result = await self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)
        # Should apply lucidity loss for occult damage (occult is in ["mental", "occult"])
        self.game_mechanics.apply_lucidity_loss.assert_called_once()
        # Should apply fear for occult damage (occult is in ["occult", "eldritch"])
        self.game_mechanics.apply_fear.assert_called_once()

    @pytest.mark.asyncio
    async def test_apply_combat_effects_player_with_eldritch_damage(self) -> None:
        """Test applying combat effects with fear gain for eldritch damage."""
        target_id = str(uuid4())
        damage = 20
        damage_type = "eldritch"
        source_id = str(uuid4())

        # Mock player - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)
        self.game_mechanics.damage_player = AsyncMock(return_value=(True, "Damage applied"))
        self.game_mechanics.apply_fear = AsyncMock()

        result = await self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        self.game_mechanics.damage_player.assert_called_once_with(target_id, damage, damage_type)
        # Should apply fear for eldritch damage
        self.game_mechanics.apply_fear.assert_called_once()

    @pytest.mark.asyncio
    async def test_apply_combat_effects_non_player(self) -> None:
        """Test applying combat effects to non-player entity."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "physical"
        source_id = str(uuid4())

        # Mock no player found - use AsyncMock for async method
        from unittest.mock import AsyncMock

        self.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

        assert result is True
        if hasattr(self.game_mechanics, "damage_player"):
            self.game_mechanics.damage_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_apply_combat_effects_exception_handling(self) -> None:
        """Test applying combat effects re-raises exceptions (CRITICAL FIX)."""
        target_id = str(uuid4())
        damage = 10
        damage_type = "physical"
        source_id = str(uuid4())

        # Mock exception - use AsyncMock for async method
        from unittest.mock import AsyncMock

        self.persistence.get_player_by_id = AsyncMock(side_effect=Exception("Database error"))

        # CRITICAL FIX: Exceptions should be re-raised, not silently caught
        # This ensures errors are visible in logs and monitoring
        with pytest.raises(Exception, match="Database error"):
            await self.integration.apply_combat_effects(target_id, damage, damage_type, source_id)

    @pytest.mark.asyncio
    async def test_handle_npc_attack_with_player_target(self) -> None:
        """Test handling NPC attack on player target."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 8
        attack_type = "physical"
        npc_stats = {"strength": 14, "constitution": 12}

        # Mock player target - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        player.stats.model_dump.return_value = {"constitution": 10}
        self.persistence.get_player_by_id = AsyncMock(return_value=player)

        with patch.object(
            self.integration, "apply_combat_effects", new_callable=AsyncMock, return_value=True
        ) as mock_apply:
            result = await self.integration.handle_npc_attack(
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

    @pytest.mark.asyncio
    async def test_handle_npc_attack_with_npc_target(self) -> None:
        """Test handling NPC attack on NPC target."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 8
        attack_type = "physical"
        npc_stats = {"strength": 14, "constitution": 12}

        # Mock no player found (NPC target) - use AsyncMock for async method
        from unittest.mock import AsyncMock

        self.persistence.get_player_by_id = AsyncMock(return_value=None)

        with patch.object(
            self.integration, "apply_combat_effects", new_callable=AsyncMock, return_value=True
        ) as mock_apply:
            result = await self.integration.handle_npc_attack(
                npc_id, target_id, room_id, attack_damage, attack_type, npc_stats
            )

        assert result is True
        mock_apply.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_npc_attack_with_default_stats(self) -> None:
        """Test handling NPC attack with default stats."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 5
        attack_type = "physical"

        # Mock player target - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        player.stats.model_dump.return_value = {"constitution": 10}
        self.persistence.get_player_by_id = AsyncMock(return_value=player)

        with patch.object(
            self.integration, "apply_combat_effects", new_callable=AsyncMock, return_value=True
        ) as mock_apply:
            result = await self.integration.handle_npc_attack(npc_id, target_id, room_id, attack_damage, attack_type)

        assert result is True
        mock_apply.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_npc_attack_exception_handling(self) -> None:
        """Test handling NPC attack with exception."""
        npc_id = str(uuid4())
        target_id = str(uuid4())
        room_id = "test_room_001"
        attack_damage = 5
        attack_type = "physical"

        # Mock exception in _get_target_stats - use regular Mock since it's not async
        # The exception happens in get_player which is called synchronously in _get_target_stats
        # Note: handle_npc_attack only catches specific exceptions, so we need to raise one of those
        self.persistence.get_player = Mock(side_effect=AttributeError("Database error"))

        result = await self.integration.handle_npc_attack(npc_id, target_id, room_id, attack_damage, attack_type)

        assert result is False

    @pytest.mark.asyncio
    async def test_handle_npc_death_with_player_killer(self) -> None:
        """Test handling NPC death with player killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "combat"
        killer_id = str(uuid4())

        # Mock player killer - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)

        # Mock NPC
        npc = Mock()
        npc.npc_type.value = "aggressive_mob"
        self.persistence.get_npc = Mock(return_value=npc)

        # Mock async game mechanics methods
        self.game_mechanics.gain_occult_knowledge = AsyncMock()
        self.game_mechanics.apply_lucidity_loss = AsyncMock()

        result = await self.integration.handle_npc_death(npc_id, room_id, cause, killer_id)

        assert result is True
        self.game_mechanics.gain_occult_knowledge.assert_called_once()
        self.game_mechanics.apply_lucidity_loss.assert_called_once()
        # Note: NPCDied event is now published by CombatService via NATS, not by this integration service

    @pytest.mark.asyncio
    async def test_handle_npc_death_without_killer(self) -> None:
        """Test handling NPC death without killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "timeout"

        result = await self.integration.handle_npc_death(npc_id, room_id, cause)

        assert result is True
        if hasattr(self.game_mechanics, "gain_occult_knowledge"):
            self.game_mechanics.gain_occult_knowledge.assert_not_called()
        if hasattr(self.game_mechanics, "apply_lucidity_loss"):
            self.game_mechanics.apply_lucidity_loss.assert_not_called()
        # Note: NPCDied event is now published by CombatService via NATS, not by this integration service

    @pytest.mark.asyncio
    async def test_handle_npc_death_with_non_player_killer(self) -> None:
        """Test handling NPC death with non-player killer."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "combat"
        killer_id = str(uuid4())

        # Mock no player found - use AsyncMock for async method
        from unittest.mock import AsyncMock

        self.persistence.get_player_by_id = AsyncMock(return_value=None)

        result = await self.integration.handle_npc_death(npc_id, room_id, cause, killer_id)

        assert result is True
        if hasattr(self.game_mechanics, "gain_occult_knowledge"):
            self.game_mechanics.gain_occult_knowledge.assert_not_called()
        if hasattr(self.game_mechanics, "apply_lucidity_loss"):
            self.game_mechanics.apply_lucidity_loss.assert_not_called()
        # Note: NPCDied event is now published by CombatService via NATS, not by this integration service

    @pytest.mark.asyncio
    async def test_handle_npc_death_exception_handling(self) -> None:
        """Test handling NPC death with exception."""
        npc_id = str(uuid4())
        room_id = "test_room_001"
        cause = "combat"
        killer_id = str(uuid4())

        # Mock exception - use AsyncMock for async method
        # Note: handle_npc_death only catches specific exceptions (ValueError, TypeError, AttributeError, ValidationError)
        # So we need to raise one of those, not a generic Exception
        from unittest.mock import AsyncMock

        self.persistence.get_player_by_id = AsyncMock(side_effect=AttributeError("Database error"))

        result = await self.integration.handle_npc_death(npc_id, room_id, cause, killer_id)

        assert result is False

    def test_get_combat_stats_player(self) -> None:
        """Test getting combat stats for player."""
        entity_id = str(uuid4())

        # Mock player
        player = Mock()
        player.stats.model_dump.return_value = {
            "current_dp": 75,
            "max_dp": 100,
            "strength": 12,
            "constitution": 14,
            "lucidity": 80,
            "fear": 20,
            "corruption": 5,
        }
        self.persistence.get_player.return_value = player

        result = self.integration.get_combat_stats(entity_id)

        assert result["dp"] == 75
        assert result["max_dp"] == 100
        assert result["strength"] == 12
        assert result["constitution"] == 14
        assert result["lucidity"] == 80
        assert result["fear"] == 20
        assert result["corruption"] == 5

    def test_get_combat_stats_npc_with_stats(self) -> None:
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

    def test_get_combat_stats_npc_without_stats(self) -> None:
        """Test getting combat stats for NPC without stats."""
        entity_id = str(uuid4())

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.get_combat_stats(entity_id)

        assert result == {}

    def test_get_combat_stats_database_error_with_npc_stats(self) -> None:
        """Test getting combat stats with database error but NPC stats provided."""
        entity_id = str(uuid4())
        npc_stats = {"hp": 50, "max_hp": 50}

        # Mock database error - the method should catch it and return npc_stats
        self.persistence.get_player.side_effect = DatabaseError("Database error")

        result = self.integration.get_combat_stats(entity_id, npc_stats)

        assert result == npc_stats

    def test_get_combat_stats_database_error_without_npc_stats(self) -> None:
        """Test getting combat stats with database error and no NPC stats."""
        entity_id = str(uuid4())

        # Mock database error
        self.persistence.get_player.side_effect = DatabaseError("Database error")

        result = self.integration.get_combat_stats(entity_id)

        assert result == {}

    def test_get_combat_stats_entity_not_found(self) -> None:
        """Test getting combat stats for entity not found."""
        entity_id = str(uuid4())

        # Mock no player found
        self.persistence.get_player.return_value = None

        result = self.integration.get_combat_stats(entity_id)

        assert result == {}


class TestNPCCombatIntegrationEdgeCases:
    """Test edge cases for NPC Combat Integration."""

    def __init__(self) -> None:
        """Initialize test class attributes."""
        # Initialize attributes to satisfy linter (attributes-defined-outside-init)
        # These are set up properly in setup_method per pytest conventions
        self.event_bus: Mock | None = None
        self.persistence: Mock | None = None
        self.game_mechanics: Mock | None = None
        self.integration: NPCCombatIntegration | None = None

    def setup_method(self) -> None:
        """Set up test environment."""
        self.event_bus = Mock()
        self.persistence = Mock()
        self.game_mechanics = Mock()

        with (
            patch("server.npc.combat_integration.GameMechanicsService") as mock_game_mechanics,
        ):
            mock_game_mechanics.return_value = self.game_mechanics

            self.integration = NPCCombatIntegration(self.event_bus, async_persistence=self.persistence)

    def test_calculate_damage_extreme_values(self) -> None:
        """Test damage calculation with extreme values."""
        assert self.integration is not None
        attacker_stats = {"strength": 1}  # Minimum strength
        target_stats = {"constitution": 20}  # Maximum constitution
        weapon_damage = 0  # No weapon damage

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should still return minimum 1 damage
        assert damage == 1

    def test_calculate_damage_missing_stats(self) -> None:
        """Test damage calculation with missing stats."""
        assert self.integration is not None
        attacker_stats: dict[str, Any] = {}  # No stats
        target_stats: dict[str, Any] = {}  # No stats
        weapon_damage = 5

        damage = self.integration.calculate_damage(attacker_stats, target_stats, weapon_damage, "physical")

        # Should use default values (10 for strength/constitution)
        assert damage == 5

    @pytest.mark.asyncio
    async def test_apply_combat_effects_capped_Lucidity_loss(self) -> None:
        """Test that lucidity loss is capped appropriately."""
        assert self.integration is not None
        assert self.persistence is not None
        assert self.game_mechanics is not None
        target_id = str(uuid4())
        damage = 50  # High damage
        damage_type = "mental"

        # Mock player - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)
        self.game_mechanics.damage_player = AsyncMock(return_value=(True, "Damage applied"))
        self.game_mechanics.apply_lucidity_loss = AsyncMock()

        await self.integration.apply_combat_effects(target_id, damage, damage_type)

        # Should apply capped lucidity loss (max 10)
        self.game_mechanics.apply_lucidity_loss.assert_called_once()
        call_args = self.game_mechanics.apply_lucidity_loss.call_args
        assert call_args[0][1] <= 10  # lucidity loss should be capped

    @pytest.mark.asyncio
    async def test_apply_combat_effects_capped_fear_gain(self) -> None:
        """Test that fear gain is capped appropriately."""
        assert self.integration is not None
        assert self.persistence is not None
        assert self.game_mechanics is not None
        target_id = str(uuid4())
        damage = 50  # High damage
        damage_type = "occult"

        # Mock player - use AsyncMock for async method
        from unittest.mock import AsyncMock

        player = Mock()
        self.persistence.get_player_by_id = AsyncMock(return_value=player)
        self.game_mechanics.damage_player = AsyncMock(return_value=(True, "Damage applied"))
        # Occult damage triggers both lucidity loss and fear
        self.game_mechanics.apply_lucidity_loss = AsyncMock()
        self.game_mechanics.apply_fear = AsyncMock()

        await self.integration.apply_combat_effects(target_id, damage, damage_type)

        # Should apply capped fear gain (max 5)
        self.game_mechanics.apply_fear.assert_called_once()
        call_args = self.game_mechanics.apply_fear.call_args
        assert call_args[0][1] <= 5  # Fear gain should be capped
