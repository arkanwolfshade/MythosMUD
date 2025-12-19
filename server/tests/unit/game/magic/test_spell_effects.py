"""
Tests for spell effects processing engine.

This module tests the SpellEffects class and its methods for applying
various spell effects to targets.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.game.magic.spell_effects import SpellEffects
from server.models.game import StatusEffectType
from server.models.spell import SpellEffectType
from server.schemas.target_resolution import TargetType


class TestSpellEffectsInit:
    """Test SpellEffects initialization."""

    def test_spell_effects_init_defaults(self) -> None:
        """Test initialization with required service only."""
        mock_player_service = MagicMock()

        with patch("server.game.magic.spell_effects.logger"):
            effects = SpellEffects(mock_player_service)

            assert effects.player_service == mock_player_service
            assert effects.player_spell_repository is not None

    def test_spell_effects_init_with_repository(self) -> None:
        """Test initialization with custom repository."""
        mock_player_service = MagicMock()
        mock_repository = MagicMock()

        with patch("server.game.magic.spell_effects.logger"):
            effects = SpellEffects(mock_player_service, player_spell_repository=mock_repository)

            assert effects.player_spell_repository == mock_repository


class TestProcessEffect:
    """Test process_effect routing method."""

    @pytest.mark.asyncio
    async def test_process_effect_heal(self) -> None:
        """Test routing to heal effect."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_type = SpellEffectType.HEAL
        spell.spell_id = "spell-1"
        spell.effect_data = {"heal_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        with patch.object(effects, "_process_heal", new_callable=AsyncMock) as mock_heal:
            mock_heal.return_value = {"success": True, "message": "Healed"}
            result = await effects.process_effect(spell, target, uuid4(), mastery=50)

            mock_heal.assert_called_once()
            assert result["success"] is True

    @pytest.mark.asyncio
    async def test_process_effect_damage(self) -> None:
        """Test routing to damage effect."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_type = SpellEffectType.DAMAGE
        spell.spell_id = "spell-1"
        spell.effect_data = {"damage_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        with patch.object(effects, "_process_damage", new_callable=AsyncMock) as mock_damage:
            mock_damage.return_value = {"success": True, "message": "Damaged"}
            result = await effects.process_effect(spell, target, uuid4(), mastery=50)

            mock_damage.assert_called_once()
            assert result["success"] is True

    @pytest.mark.asyncio
    async def test_process_effect_mastery_modifier(self) -> None:
        """Test mastery modifier calculation."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_type = SpellEffectType.HEAL
        spell.spell_id = "spell-1"
        spell.effect_data = {"heal_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        with patch.object(effects, "_process_heal", new_callable=AsyncMock) as mock_heal:
            await effects.process_effect(spell, target, uuid4(), mastery=100)

            # Mastery 100 should give modifier 2.0
            call_args = mock_heal.call_args[0]
            assert call_args[2] == 2.0  # mastery_modifier


class TestProcessHeal:
    """Test _process_heal method."""

    @pytest.mark.asyncio
    async def test_process_heal_player_success(self) -> None:
        """Test successful healing of a player."""
        mock_player_service = MagicMock()
        mock_player_service.heal_player = AsyncMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"heal_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_heal(spell, target, 1.5)

        assert result["success"] is True
        assert result["heal_amount"] == 15  # 10 * 1.5
        mock_player_service.heal_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_heal_invalid_target(self) -> None:
        """Test healing with invalid target type."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"heal_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.ROOM
        target.target_name = "Room"

        result = await effects._process_heal(spell, target, 1.0)

        assert result["success"] is False
        assert "can only target entities" in result["message"]

    @pytest.mark.asyncio
    async def test_process_heal_invalid_amount(self) -> None:
        """Test healing with invalid heal amount."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"heal_amount": 0}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_heal(spell, target, 1.0)

        assert result["success"] is False
        assert "Invalid heal amount" in result["message"]

    @pytest.mark.asyncio
    async def test_process_heal_player_error(self) -> None:
        """Test healing when player service raises error."""
        mock_player_service = MagicMock()
        mock_player_service.heal_player = AsyncMock(side_effect=OSError("Connection error"))
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"heal_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        with patch("server.game.magic.spell_effects.logger"):
            result = await effects._process_heal(spell, target, 1.0)

            assert result["success"] is False
            assert "Failed to heal" in result["message"]


class TestProcessDamage:
    """Test _process_damage method."""

    @pytest.mark.asyncio
    async def test_process_damage_player_success(self) -> None:
        """Test successful damage to a player."""
        mock_player_service = MagicMock()
        mock_player_service.damage_player = AsyncMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"damage_amount": 10, "damage_type": "fire"}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_damage(spell, target, 1.5)

        assert result["success"] is True
        assert result["damage_amount"] == 15  # 10 * 1.5
        assert result["damage_type"] == "fire"
        mock_player_service.damage_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_damage_default_type(self) -> None:
        """Test damage with default damage type."""
        mock_player_service = MagicMock()
        mock_player_service.damage_player = AsyncMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"damage_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_damage(spell, target, 1.0)

        assert result["damage_type"] == "magical"

    @pytest.mark.asyncio
    async def test_process_damage_invalid_target(self) -> None:
        """Test damage with invalid target type."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"damage_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.ROOM

        result = await effects._process_damage(spell, target, 1.0)

        assert result["success"] is False
        assert "can only target entities" in result["message"]


class TestProcessStatusEffect:
    """Test _process_status_effect method."""

    @pytest.mark.asyncio
    async def test_process_status_effect_player_success(self) -> None:
        """Test successful status effect application."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        # Return a mutable list that can be modified
        status_effects_list: list[Any] = []
        mock_player.get_status_effects.return_value = status_effects_list
        mock_player.set_status_effects = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.spell_id = "spell-1"
        spell.effect_data = {"status_effect_type": StatusEffectType.POISONED.value, "duration": 10, "intensity": 5}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target_id = uuid4()
        target.target_id = str(target_id)
        target.target_name = "TestPlayer"

        result = await effects._process_status_effect(spell, target, 1.5)

        assert result["success"] is True
        assert result["status_effect"] == "poisoned"
        # Verify that set_status_effects was called
        mock_player.set_status_effects.assert_called_once()
        # Verify save_player was called
        mock_persistence.save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_process_status_effect_invalid_type(self) -> None:
        """Test status effect with invalid type."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"status_effect_type": "invalid_type", "duration": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_status_effect(spell, target, 1.0)

        assert result["success"] is False
        assert "Invalid status effect type" in result["message"]

    @pytest.mark.asyncio
    async def test_process_status_effect_player_not_found(self) -> None:
        """Test status effect when player is not found."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=None)
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"status_effect_type": StatusEffectType.POISONED.value, "duration": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_status_effect(spell, target, 1.0)

        assert result["success"] is False
        assert "Target player not found" in result["message"]


class TestProcessStatModify:
    """Test _process_stat_modify method."""

    @pytest.mark.asyncio
    async def test_process_stat_modify_success(self) -> None:
        """Test successful stat modification."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"strength": 50, "intelligence": 50}
        mock_player.get_status_effects.return_value = []
        mock_player.set_stats = MagicMock()
        mock_player.set_status_effects = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.spell_id = "spell-1"
        spell.effect_data = {"stat_modifications": {"strength": 10, "intelligence": -5}, "duration": 0}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_stat_modify(spell, target, 1.0)

        assert result["success"] is True
        assert "strength" in result["stat_changes"]
        assert "intelligence" in result["stat_changes"]
        mock_player.set_stats.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_stat_modify_invalid_target(self) -> None:
        """Test stat modification with invalid target."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"stat_modifications": {"strength": 10}}

        target = MagicMock()
        target.target_type = TargetType.ROOM

        result = await effects._process_stat_modify(spell, target, 1.0)

        assert result["success"] is False
        assert "can only target players" in result["message"]

    @pytest.mark.asyncio
    async def test_process_stat_modify_no_modifications(self) -> None:
        """Test stat modification with no modifications specified."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_stat_modify(spell, target, 1.0)

        assert result["success"] is False
        assert "No stat modifications specified" in result["message"]


class TestProcessLucidityAdjust:
    """Test _process_lucidity_adjust method."""

    @pytest.mark.asyncio
    async def test_process_lucidity_adjust_gain(self) -> None:
        """Test successful lucidity gain."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.apply_lucidity_gain = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.spell_id = "spell-1"
        spell.effect_data = {"adjust_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_lucidity_adjust(spell, target, 1.0)

        assert result["success"] is True
        assert result["lucidity_adjust"] == 10
        mock_persistence.apply_lucidity_gain.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_lucidity_adjust_loss(self) -> None:
        """Test successful lucidity loss."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.apply_lucidity_loss = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.spell_id = "spell-1"
        spell.effect_data = {"adjust_amount": -10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_lucidity_adjust(spell, target, 1.0)

        assert result["success"] is True
        assert result["lucidity_adjust"] == -10
        mock_persistence.apply_lucidity_loss.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_lucidity_adjust_invalid_amount(self) -> None:
        """Test lucidity adjustment with zero amount."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"adjust_amount": 0}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_lucidity_adjust(spell, target, 1.0)

        assert result["success"] is False
        assert "Invalid lucidity adjustment amount" in result["message"]


class TestProcessCorruptionAdjust:
    """Test _process_corruption_adjust method."""

    @pytest.mark.asyncio
    async def test_process_corruption_adjust_increase(self) -> None:
        """Test successful corruption increase."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"corruption": 10}
        mock_player.set_stats = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"adjust_amount": 5}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_corruption_adjust(spell, target, 1.0)

        assert result["success"] is True
        assert result["corruption_adjust"] == 5
        assert result["new_corruption"] == 15
        assert "Increased" in result["message"]

    @pytest.mark.asyncio
    async def test_process_corruption_adjust_decrease(self) -> None:
        """Test successful corruption decrease."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"corruption": 20}
        mock_player.set_stats = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"adjust_amount": -10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_corruption_adjust(spell, target, 1.0)

        assert result["success"] is True
        assert result["corruption_adjust"] == -10
        assert result["new_corruption"] == 10
        assert "Decreased" in result["message"]

    @pytest.mark.asyncio
    async def test_process_corruption_adjust_bounded(self) -> None:
        """Test corruption adjustment is bounded to 0-100."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"corruption": 95}
        mock_player.set_stats = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"adjust_amount": 10}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_corruption_adjust(spell, target, 1.0)

        assert result["new_corruption"] == 100  # Bounded at 100


class TestProcessTeleport:
    """Test _process_teleport method."""

    @pytest.mark.asyncio
    async def test_process_teleport_success(self) -> None:
        """Test successful teleport."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_player.current_room_id = "room-1"
        mock_player.name = "TestPlayer"
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_player_service.persistence = mock_persistence
        mock_player_service.update_player_location = AsyncMock(return_value=True)

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"destination_room_id": "room-2"}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_teleport(spell, target, 1.0)

        assert result["success"] is True
        assert result["destination_room_id"] == "room-2"
        assert result["original_room_id"] == "room-1"

    @pytest.mark.asyncio
    async def test_process_teleport_no_destination(self) -> None:
        """Test teleport with no destination specified."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_teleport(spell, target, 1.0)

        assert result["success"] is False
        assert "No destination room specified" in result["message"]


class TestProcessCreateObject:
    """Test _process_create_object method."""

    @pytest.mark.asyncio
    async def test_process_create_object_player_success(self) -> None:
        """Test successful object creation in player inventory."""
        mock_player_service = MagicMock()
        mock_persistence = AsyncMock()
        mock_player = MagicMock()
        mock_player.get_inventory.return_value = []
        mock_player.set_inventory = MagicMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_persistence.save_player = AsyncMock()
        mock_player_service.persistence = mock_persistence

        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {"prototype_id": "item-1", "quantity": 1}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_create_object(spell, target, 1.0)

        assert result["success"] is True
        assert result["prototype_id"] == "item-1"
        assert result["quantity"] == 1
        mock_player.set_inventory.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_create_object_no_prototype(self) -> None:
        """Test object creation with no prototype ID."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.effect_data = {}

        target = MagicMock()
        target.target_type = TargetType.PLAYER
        target.target_id = str(uuid4())
        target.target_name = "TestPlayer"

        result = await effects._process_create_object(spell, target, 1.0)

        assert result["success"] is False
        assert "No prototype ID specified" in result["message"]

    @pytest.mark.asyncio
    async def test_process_create_object_room_target(self) -> None:
        """Test object creation with room target (not implemented)."""
        mock_player_service = MagicMock()
        effects = SpellEffects(mock_player_service)

        spell = MagicMock()
        spell.spell_id = "spell-1"
        spell.effect_data = {"prototype_id": "item-1"}

        target = MagicMock()
        target.target_type = TargetType.ROOM
        target.room_id = "room-1"

        with patch("server.game.magic.spell_effects.logger"):
            result = await effects._process_create_object(spell, target, 1.0)

            assert result["success"] is False
            assert "requires additional services" in result["message"]
