"""
Unit tests for spell targeting.

Tests SpellTargetingService, including self-only spell feedback when a target is provided.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_targeting import SpellTargetingService
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType
from server.schemas.shared import TargetType

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_target_resolution_service():
    """Create a mock target resolution service."""
    return MagicMock()


@pytest.fixture
def spell_targeting_service(mock_target_resolution_service):
    """Create SpellTargetingService with mocks."""
    return SpellTargetingService(
        target_resolution_service=mock_target_resolution_service,
        combat_service=None,
        player_combat_service=None,
    )


@pytest.fixture
def self_spell():
    """Spell that can only target self (e.g. heal)."""
    return Spell(
        spell_id="heal",
        name="Heal",
        description="Restore health.",
        school=SpellSchool.CLERICAL,
        mp_cost=5,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
        effect_data={"amount": 10},
    )


@pytest.mark.asyncio
async def test_resolve_spell_target_self_spell_with_target_returns_error(spell_targeting_service, self_spell):
    """When spell is self-only and player provides a target, return clear error."""
    player_id = uuid.uuid4()
    target_match, error = await spell_targeting_service.resolve_spell_target(
        player_id, self_spell, target_name="Ithaqua"
    )
    assert target_match is None
    assert error == "Heal can only be cast on yourself."


@pytest.mark.asyncio
async def test_resolve_spell_target_self_spell_no_target_resolves_self(spell_targeting_service, self_spell):
    """Self-only spell with no target name resolves to caster (when persistence available)."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "Caster"
    mock_player.player_id = player_id
    mock_player.current_room_id = "room_001"

    with patch.object(spell_targeting_service, "_get_player", new=AsyncMock(return_value=mock_player)):
        target_match, error = await spell_targeting_service.resolve_spell_target(
            player_id, self_spell, target_name=None
        )
    assert error == ""
    assert target_match is not None
    assert target_match.target_type == TargetType.PLAYER
    assert target_match.target_name == "Caster"
