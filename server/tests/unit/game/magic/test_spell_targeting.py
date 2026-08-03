"""
Unit tests for spell targeting.

Tests SpellTargetingService, including self-only spell feedback when a target is provided.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_targeting import SpellTargetingService
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType
from server.schemas.shared import TargetMatch, TargetResolutionResult, TargetType

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


@pytest.fixture
def area_spell():
    return Spell(
        spell_id="nova",
        name="Nova",
        description="Area blast.",
        school=SpellSchool.ELEMENTAL,
        mp_cost=10,
        target_type=SpellTargetType.AREA,
        range_type=SpellRangeType.SAME_ROOM,
        effect_type=SpellEffectType.DAMAGE,
        effect_data={"amount": 5},
    )


@pytest.fixture
def entity_spell():
    return Spell(
        spell_id="bolt",
        name="Bolt",
        description="Single target.",
        school=SpellSchool.ELEMENTAL,
        mp_cost=3,
        target_type=SpellTargetType.ENTITY,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.DAMAGE,
        effect_data={"amount": 4},
    )


@pytest.mark.asyncio
async def test_resolve_area_target(spell_targeting_service, area_spell):
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.name = "Caster"
    mock_player.current_room_id = "room_001"
    with patch.object(spell_targeting_service, "_get_player", new=AsyncMock(return_value=mock_player)):
        target_match, error = await spell_targeting_service.resolve_spell_target(player_id, area_spell)
    assert error == ""
    assert target_match is not None
    assert target_match.target_type == TargetType.ROOM


@pytest.mark.asyncio
async def test_resolve_entity_target_success(spell_targeting_service, entity_spell, mock_target_resolution_service):
    player_id = uuid.uuid4()
    match = TargetMatch(
        target_id="npc_1",
        target_name="Ghoul",
        target_type=TargetType.NPC,
        room_id="room_001",
    )
    mock_target_resolution_service.resolve_target = AsyncMock(
        return_value=TargetResolutionResult(
            success=True,
            matches=[match],
            search_term="Ghoul",
            room_id="room_001",
        )
    )
    target_match, error = await spell_targeting_service.resolve_spell_target(
        player_id, entity_spell, target_name="Ghoul"
    )
    assert error == ""
    assert target_match is not None
    assert target_match.target_name == "Ghoul"


@pytest.mark.asyncio
async def test_resolve_entity_target_rejects_location(
    spell_targeting_service, entity_spell, mock_target_resolution_service
):
    player_id = uuid.uuid4()
    match = TargetMatch(
        target_id="room_001",
        target_name="North Door",
        target_type=TargetType.ROOM,
        room_id="room_001",
    )
    mock_target_resolution_service.resolve_target = AsyncMock(
        return_value=TargetResolutionResult(
            success=True,
            matches=[match],
            search_term="Ghoul",
            room_id="room_001",
        )
    )
    target_match, error = await spell_targeting_service.resolve_spell_target(
        player_id, entity_spell, target_name="door"
    )
    assert target_match is None
    assert "entities" in error


@pytest.mark.asyncio
async def test_resolve_spell_target_requires_target(spell_targeting_service, entity_spell):
    player_id = uuid.uuid4()
    target_match, error = await spell_targeting_service.resolve_spell_target(player_id, entity_spell)
    assert target_match is None
    assert "requires a target" in error


@pytest.mark.asyncio
async def test_get_combat_target_auto_selects_opponent():
    target_resolution = MagicMock()
    combat_service = MagicMock()
    player_combat_service = MagicMock()
    svc = SpellTargetingService(target_resolution, combat_service, player_combat_service)
    player_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    combat_state = MagicMock()
    combat_state.is_in_combat = True
    player_combat_service.get_player_combat_state = AsyncMock(return_value=combat_state)
    participant_player = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Caster",
        current_dp=50,
        max_dp=50,
        dexterity=10,
        is_active=True,
    )
    participant_npc = CombatParticipant(
        participant_id=npc_id,
        participant_type=CombatParticipantType.NPC,
        name="Ghoul",
        current_dp=20,
        max_dp=20,
        dexterity=8,
        is_active=True,
    )
    combat = CombatInstance(
        combat_id=uuid.uuid4(),
        room_id="room_1",
        participants={player_id: participant_player, npc_id: participant_npc},
    )
    combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    mock_player = MagicMock()
    mock_player.name = "Caster"
    mock_player.current_room_id = "room_1"
    with patch.object(svc, "_get_player", new=AsyncMock(return_value=mock_player)):
        target_match, error = await svc.resolve_spell_target(
            player_id,
            Spell(
                spell_id="bolt",
                name="Bolt",
                description="Hit",
                school=SpellSchool.ELEMENTAL,
                mp_cost=1,
                target_type=SpellTargetType.ENTITY,
                range_type=SpellRangeType.TOUCH,
                effect_type=SpellEffectType.DAMAGE,
                effect_data={},
            ),
        )
    assert error == ""
    assert target_match is not None
    assert target_match.target_type == TargetType.NPC
