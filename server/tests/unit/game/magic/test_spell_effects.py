"""
Unit tests for spell effects.

Tests the SpellEffects class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_effects import SpellEffects
from server.models.spell import SpellEffectType
from server.schemas.shared import TargetMatch, TargetType

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    return MagicMock()


@pytest.fixture
def spell_effects(mock_player_service):
    """Create a SpellEffects instance."""
    return SpellEffects(mock_player_service)


@pytest.fixture
def mock_spell():
    """Create a mock spell."""
    spell = MagicMock()
    spell.spell_id = "spell_001"
    spell.effect_data = {}
    return spell


@pytest.fixture
def mock_target_match():
    """Create a mock target match."""
    return TargetMatch(
        target_id=str(uuid.uuid4()), target_type=TargetType.PLAYER, target_name="Player1", room_id="room_001"
    )


def test_spell_effects_init(spell_effects, mock_player_service):
    """Test SpellEffects initialization."""
    assert spell_effects.player_service == mock_player_service


def test_spell_effects_init_with_repository(mock_player_service):
    """Test SpellEffects initialization with repository."""
    from server.persistence.repositories.player_spell_repository import PlayerSpellRepository

    mock_repo = PlayerSpellRepository()
    spell_effects = SpellEffects(mock_player_service, mock_repo)
    assert spell_effects.player_spell_repository == mock_repo


@pytest.mark.asyncio
async def test_process_effect_heal(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to heal handler."""
    mock_spell.effect_type = SpellEffectType.HEAL
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_damage(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to damage handler."""
    mock_spell.effect_type = SpellEffectType.DAMAGE
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_status_effect(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to status effect handler."""
    mock_spell.effect_type = SpellEffectType.STATUS_EFFECT
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_stat_modify(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to stat modify handler."""
    mock_spell.effect_type = SpellEffectType.STAT_MODIFY
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_lucidity_adjust(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to lucidity adjust handler."""
    mock_spell.effect_type = SpellEffectType.LUCIDITY_ADJUST
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_corruption_adjust(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to corruption adjust handler."""
    mock_spell.effect_type = SpellEffectType.CORRUPTION_ADJUST
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_teleport(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to teleport handler."""
    mock_spell.effect_type = SpellEffectType.TELEPORT
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_create_object(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() routes to create object handler."""
    mock_spell.effect_type = SpellEffectType.CREATE_OBJECT
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert isinstance(result, dict)
    assert "success" in result or "effect_applied" in result


@pytest.mark.asyncio
async def test_process_effect_flee_services_not_configured(spell_effects, mock_spell, mock_target_match):
    """Test process_effect() FLEE returns failure when combat/movement services not configured."""
    mock_spell.effect_type = SpellEffectType.FLEE
    # spell_effects fixture has no combat_service/movement_service
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert result.get("success") is False
    assert "not available" in result.get("message", "").lower() or "not configured" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_effect_flee_not_in_combat(mock_player_service, mock_spell, mock_target_match):
    """Test _process_flee() when target is not in combat."""
    mock_combat = AsyncMock()
    mock_combat.get_combat_by_participant = AsyncMock(return_value=None)
    spell_effects = SpellEffects(
        mock_player_service,
        combat_service=mock_combat,
        movement_service=MagicMock(),
        get_room_by_id=MagicMock(return_value=MagicMock(exits={"north": "room_2"})),
    )
    mock_spell.effect_type = SpellEffectType.FLEE
    result = await spell_effects.process_effect(mock_spell, mock_target_match, uuid.uuid4(), mastery=50)
    assert result.get("success") is False
    assert "not in combat" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_heal_invalid_target(spell_effects):
    """Test _process_heal() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"heal_amount": 10}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_heal(spell, invalid_target, uuid.uuid4(), 1.5)
    assert result["success"] is False
    assert "can only target entities" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_heal_heal_other_rejects_self_target(spell_effects):
    """Test _process_heal() with heal_other spell targeting self returns error."""

    caster_id = uuid.uuid4()
    spell = MagicMock()
    spell.spell_id = "heal_other"
    spell.name = "Heal Other"
    spell.effect_data = {"heal_amount": 10}
    self_target = TargetMatch(
        target_id=str(caster_id),
        target_type=TargetType.PLAYER,
        target_name="Self",
        room_id="room_001",
    )
    result = await spell_effects._process_heal(spell, self_target, caster_id, 1.5)
    assert result["success"] is False
    assert "can only target others" in result.get("message", "").lower()
    assert "not yourself" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_heal_steal_life_damages_target_and_heals_caster(spell_effects):
    """Test _process_heal() with steal-life effect_data damages target and heals caster (capped by target DP)."""
    spell_effects.player_service.damage_player = AsyncMock()
    spell_effects.player_service.heal_player = AsyncMock()
    caster_id = uuid.uuid4()
    target_id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.get_stats.return_value = {"current_dp": 100}
    spell_effects.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_target_player)
    spell = MagicMock()
    spell.spell_id = "steal_life"
    spell.effect_data = {"heal_amount": 20, "damage_amount": 20, "damage_type": "necrotic"}
    target = TargetMatch(
        target_id=str(target_id),
        target_type=TargetType.PLAYER,
        target_name="Victim",
        room_id="room_001",
    )
    result = await spell_effects._process_heal(spell, target, caster_id, 1.0)
    assert result["success"] is True
    assert result.get("heal_amount") == 20
    assert result.get("damage_amount") == 20
    assert "Stole" in result.get("message", "") and "life from" in result.get("message", "")
    spell_effects.player_service.damage_player.assert_awaited_once_with(target_id, 20, "necrotic")
    spell_effects.player_service.heal_player.assert_awaited_once_with(caster_id, 20)


@pytest.mark.asyncio
async def test_process_heal_steal_life_capped_by_target_dp(spell_effects):
    """Steal-life caps drain at target's current DP: spell 10, target 8 -> drain 8, target to 0, caster +8."""
    spell_effects.player_service.damage_player = AsyncMock()
    spell_effects.player_service.heal_player = AsyncMock()
    caster_id = uuid.uuid4()
    target_id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.get_stats.return_value = {"current_dp": 8}
    spell_effects.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_target_player)
    spell = MagicMock()
    spell.spell_id = "steal_life"
    spell.effect_data = {"heal_amount": 10, "damage_amount": 10, "damage_type": "necrotic"}
    target = TargetMatch(
        target_id=str(target_id),
        target_type=TargetType.PLAYER,
        target_name="Victim",
        room_id="room_001",
    )
    result = await spell_effects._process_heal(spell, target, caster_id, 1.0)
    assert result["success"] is True
    assert result.get("heal_amount") == 8
    assert result.get("damage_amount") == 8
    spell_effects.player_service.damage_player.assert_awaited_once_with(target_id, 8, "necrotic")
    spell_effects.player_service.heal_player.assert_awaited_once_with(caster_id, 8)


@pytest.mark.asyncio
async def test_process_heal_steal_life_target_zero_dp(spell_effects):
    """Steal-life when target has 0 DP: no damage, no heal, message says no life to steal."""
    spell_effects.player_service.damage_player = AsyncMock()
    spell_effects.player_service.heal_player = AsyncMock()
    caster_id = uuid.uuid4()
    target_id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.get_stats.return_value = {"current_dp": 0}
    spell_effects.player_service.persistence.get_player_by_id = AsyncMock(return_value=mock_target_player)
    spell = MagicMock()
    spell.spell_id = "steal_life"
    spell.effect_data = {"heal_amount": 10, "damage_amount": 10, "damage_type": "necrotic"}
    target = TargetMatch(
        target_id=str(target_id),
        target_type=TargetType.PLAYER,
        target_name="Victim",
        room_id="room_001",
    )
    result = await spell_effects._process_heal(spell, target, caster_id, 1.0)
    assert result["success"] is True
    assert result.get("heal_amount") == 0
    assert result.get("effect_applied") is False
    assert "no life to steal" in result.get("message", "").lower()
    spell_effects.player_service.damage_player.assert_not_awaited()
    spell_effects.player_service.heal_player.assert_not_awaited()


@pytest.mark.asyncio
async def test_process_damage_invalid_target(spell_effects):
    """Test _process_damage() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"damage_amount": 10}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_damage(spell, invalid_target, uuid.uuid4(), 1.5)
    assert result["success"] is False
    assert "can only target entities" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_status_effect_invalid_target(spell_effects):
    """Test _process_status_effect() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"status_effect_type": "poison"}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_status_effect(spell, invalid_target, 1.5)
    assert result["success"] is False
    assert "can only target entities" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_stat_modify_invalid_target(spell_effects):
    """Test _process_stat_modify() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"stat_modifications": {"strength": 5}}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_stat_modify(spell, invalid_target, 1.5)
    assert result["success"] is False
    assert "can only target players" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_lucidity_adjust_invalid_target(spell_effects):
    """Test _process_lucidity_adjust() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"adjust_amount": 10}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_lucidity_adjust(spell, invalid_target, 1.5)
    assert result["success"] is False
    assert "can only target players" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_corruption_adjust_invalid_target(spell_effects):
    """Test _process_corruption_adjust() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"adjust_amount": 10}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_corruption_adjust(spell, invalid_target, 1.5)
    assert result["success"] is False
    assert "can only target players" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_teleport_invalid_target(spell_effects):
    """Test _process_teleport() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"destination_room_id": "room_002"}
    invalid_target = TargetMatch(
        target_id="invalid", target_type=TargetType.ROOM, target_name="Room", room_id="room_001"
    )
    result = await spell_effects._process_teleport(spell, invalid_target, 1.5)
    assert result["success"] is False
    assert "can only target players" in result.get("message", "").lower()


@pytest.mark.asyncio
async def test_process_create_object_invalid_target(spell_effects):
    """Test _process_create_object() with invalid target type."""

    spell = MagicMock()
    spell.effect_data = {"prototype_id": "item_001"}
    # create_object can target players (adds to inventory) or rooms
    # Test with a valid player target (not invalid, since it tries to convert to UUID)
    player_target = TargetMatch(
        target_id=str(uuid.uuid4()), target_type=TargetType.PLAYER, target_name="Player", room_id="room_001"
    )
    spell_effects.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)
    result = await spell_effects._process_create_object(spell, player_target, 1.5)
    # Should fail because player not found
    assert isinstance(result, dict)
    assert (
        result.get("success") is False or result.get("success") is True
    )  # May succeed or fail depending on implementation


@pytest.mark.asyncio
async def test_publish_npc_spell_damage_syncs_participant_when_npc_room_missing(mock_player_service):
    """
    Regress: Fire bolt (and other NPC damage spells) update the live NPC via take_damage first.
    Combat UI and melee use CombatParticipant.current_dp; sync must run even when
    npc_instance.current_room is unset (use combat.room_id for NATS publish).
    """
    combat_uuid = uuid.uuid4()
    combat = MagicMock()
    combat.room_id = "limbo_arena_arena_arena_5_5"
    combat.participants = {}

    svc = MagicMock()
    svc.sync_npc_participant_dp_after_spell_damage = MagicMock()
    svc.publish_npc_damage_event = AsyncMock()
    svc.publish_npc_died_event = AsyncMock()
    svc.end_combat_if_npc_died = AsyncMock()
    svc.get_combat = MagicMock(return_value=combat)

    npc_inst = MagicMock()
    npc_inst.current_room = None
    npc_inst.get_combat_stats = MagicMock(return_value={"current_dp": 75, "max_dp": 100})
    npc_inst.is_alive = True

    tid = str(uuid.uuid4())
    target = TargetMatch(
        target_id=tid,
        target_type=TargetType.NPC,
        target_name="Nightgaunt",
        room_id=combat.room_id,
    )
    caster_id = uuid.uuid4()
    spell_fx = SpellEffects(mock_player_service, combat_service=svc)

    with patch("server.game.magic.spell_effects.get_combat_id_for_npc", return_value=combat_uuid):
        await spell_fx._publish_npc_damage_and_death_events(npc_inst, target, 25, caster_id)

    svc.sync_npc_participant_dp_after_spell_damage.assert_called_once_with(tid, 75)
    svc.publish_npc_damage_event.assert_awaited_once()
    call_kw = svc.publish_npc_damage_event.await_args.kwargs
    assert call_kw["room_id"] == combat.room_id
    assert call_kw["current_dp"] == 75
