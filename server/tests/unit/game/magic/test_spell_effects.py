"""
Unit tests for spell effects.

Tests the SpellEffects class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.magic.spell_effects import SpellEffects
from server.models.spell import SpellEffectType
from server.schemas.target_resolution import TargetMatch, TargetType


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    return MagicMock()


@pytest.fixture
def spell_effects(mock_player_service):
    """Create a SpellEffects instance."""
    return SpellEffects(mock_player_service)


def test_spell_effects_init(spell_effects, mock_player_service):
    """Test SpellEffects initialization."""
    assert spell_effects.player_service == mock_player_service
    assert spell_effects.player_spell_repository is not None


@pytest.mark.asyncio
async def test_process_effect_heal(spell_effects):
    """Test process_effect() with HEAL effect type."""
    spell = MagicMock()
    spell.effect_type = SpellEffectType.HEAL
    spell.spell_id = "spell_001"
    spell.effect_data = {"heal_amount": 10}
    target = TargetMatch(
        target_id=str(uuid.uuid4()), target_type=TargetType.PLAYER, target_name="Player1", room_id="room_001"
    )
    caster_id = uuid.uuid4()
    spell_effects.player_service.heal_player = AsyncMock()
    result = await spell_effects.process_effect(spell, target, caster_id, mastery=50)
    assert "success" in result
    assert "message" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_damage(spell_effects):
    """Test process_effect() with DAMAGE effect type."""
    spell = MagicMock()
    spell.effect_type = SpellEffectType.DAMAGE
    spell.spell_id = "spell_002"
    spell.effect_data = {"damage_amount": 10, "damage_type": "magical"}
    target = TargetMatch(
        target_id=str(uuid.uuid4()), target_type=TargetType.PLAYER, target_name="Player1", room_id="room_001"
    )
    caster_id = uuid.uuid4()
    spell_effects.player_service.damage_player = AsyncMock()
    result = await spell_effects.process_effect(spell, target, caster_id, mastery=50)
    assert "success" in result


@pytest.mark.asyncio
async def test_process_effect_status_effect(spell_effects):
    """Test process_effect() with STATUS_EFFECT effect type."""
    spell = MagicMock()
    spell.effect_type = SpellEffectType.STATUS_EFFECT
    spell.spell_id = "spell_003"
    target = TargetMatch(
        target_id=str(uuid.uuid4()), target_type=TargetType.PLAYER, target_name="Player1", room_id="room_001"
    )
    caster_id = uuid.uuid4()
    result = await spell_effects.process_effect(spell, target, caster_id, mastery=50)
    assert "success" in result
