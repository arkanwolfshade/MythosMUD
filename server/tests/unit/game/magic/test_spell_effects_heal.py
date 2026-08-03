"""Unit tests for spell_effects_heal helpers."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic import spell_effects_heal as heal_mod
from server.models.spell import Spell
from server.schemas.shared import TargetMatch, TargetType


def test_coerce_effect_int_variants() -> None:
    assert heal_mod._coerce_effect_int(True) == 0
    assert heal_mod._coerce_effect_int(7) == 7
    assert heal_mod._coerce_effect_int(3.9) == 3
    assert heal_mod._coerce_effect_int(" 12 ") == 12
    assert heal_mod._coerce_effect_int("bad") == 0
    assert heal_mod._coerce_effect_int(None) == 0


def test_is_heal_other_self_target() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal_other"
    caster_id = uuid.uuid4()
    target = TargetMatch(
        target_id=str(caster_id),
        target_type=TargetType.PLAYER,
        target_name="Self",
        room_id="room_001",
    )
    assert heal_mod._is_heal_other_self_target(spell, target, caster_id) is True


def test_is_steal_life_spell() -> None:
    spell = MagicMock(spec=Spell)
    spell.effect_data = {"damage_amount": 10, "heal_amount": 8}
    assert heal_mod._is_steal_life_spell(spell) is True
    spell.effect_data = {"damage_amount": 0, "heal_amount": 8}
    assert heal_mod._is_steal_life_spell(spell) is False


@pytest.mark.asyncio
async def test_run_heal_effect_standard_player() -> None:
    caster_id = uuid.uuid4()
    target_id = uuid.uuid4()
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal"
    spell.name = "Minor Heal"
    spell.effect_data = {"heal_amount": 10}
    target = TargetMatch(
        target_id=str(target_id),
        target_type=TargetType.PLAYER,
        target_name="Patient",
        room_id="room_001",
    )
    engine = MagicMock()
    engine.player_service.heal_player = AsyncMock()

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, caster_id, 1.0, None)

    assert result["success"] is True
    engine.player_service.heal_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_run_heal_effect_invalid_target_type() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal"
    spell.effect_data = {"heal_amount": 5}
    target = TargetMatch(
        target_id="room_001",
        target_type=TargetType.ROOM,
        target_name="Room",
        room_id="room_001",
    )
    engine = MagicMock()

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)

    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_heal_effect_heal_other_self_rejected() -> None:
    caster_id = uuid.uuid4()
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal_other"
    spell.name = "Heal Other"
    spell.effect_data = {"heal_amount": 10}
    target = TargetMatch(
        target_id=str(caster_id),
        target_type=TargetType.PLAYER,
        target_name="Self",
        room_id="room_001",
    )
    engine = MagicMock()

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, caster_id, 1.0, None)

    assert result["success"] is False
    assert "others" in result["message"]


def test_get_npc_instance_for_steal_life_none() -> None:
    with patch.object(heal_mod, "_get_npc_lifecycle_manager", return_value=None):
        assert heal_mod.get_npc_instance_for_steal_life("npc_001", None) is None


def test_add_healing_threat_if_in_combat() -> None:
    caster_id = uuid.uuid4()
    npc_id = uuid.uuid4()
    combat_service = MagicMock()
    combat_service.get_combat_id_for_participant.return_value = "combat-1"
    combat = MagicMock()
    npc_participant = MagicMock()
    npc_participant.participant_type = MagicMock()
    combat.participants = {npc_id: npc_participant}
    combat_service.get_combat.return_value = combat

    with (
        patch("server.models.combat.CombatParticipantType") as mock_type,
        patch("server.services.aggro_threat.add_heal_threat") as mock_threat,
    ):
        mock_type.NPC = npc_participant.participant_type
        heal_mod._add_healing_threat_if_in_combat(combat_service, caster_id, 15)
        mock_threat.assert_called_once()


def test_add_healing_threat_skips_zero_heal() -> None:
    combat_service = MagicMock()
    heal_mod._add_healing_threat_if_in_combat(combat_service, uuid.uuid4(), 0)
    combat_service.get_combat_id_for_participant.assert_not_called()


@pytest.mark.asyncio
async def test_run_standard_heal_npc_target() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal"
    spell.effect_data = {"heal_amount": 5}
    target = TargetMatch(
        target_id="npc_001",
        target_type=TargetType.NPC,
        target_name="Ghoul",
        room_id="room_001",
    )
    engine = MagicMock()

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)

    assert result["success"] is True
    assert result["heal_amount"] == 5


@pytest.mark.asyncio
async def test_run_heal_effect_invalid_heal_amount() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal"
    spell.effect_data = {"heal_amount": 0}
    target = TargetMatch(
        target_id=str(uuid.uuid4()),
        target_type=TargetType.PLAYER,
        target_name="Patient",
        room_id="room_001",
    )
    engine = MagicMock()

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)

    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_steal_life_no_target_dp() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "steal_life"
    spell.name = "Steal Life"
    spell.effect_data = {"damage_amount": 10, "heal_amount": 10, "damage_type": "necrotic"}
    target = TargetMatch(
        target_id=str(uuid.uuid4()),
        target_type=TargetType.PLAYER,
        target_name="Victim",
        room_id="room_001",
    )
    engine = MagicMock()
    engine.player_service.persistence.get_player_by_id = AsyncMock(return_value=None)

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)

    assert result["success"] is False
    assert "not found" in result["message"].lower()


@pytest.mark.asyncio
async def test_run_steal_life_zero_dp_message() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "steal_life"
    spell.name = "Steal Life"
    spell.effect_data = {"damage_amount": 10, "heal_amount": 10}
    target_id = uuid.uuid4()
    target = TargetMatch(
        target_id=str(target_id),
        target_type=TargetType.PLAYER,
        target_name="Empty",
        room_id="room_001",
    )
    player = MagicMock()
    player.get_stats.return_value = {"current_dp": 0}
    engine = MagicMock()
    engine.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)

    assert result["success"] is True
    assert result["heal_amount"] == 0


@pytest.mark.asyncio
async def test_run_steal_life_success_player_target() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "steal_life"
    spell.name = "Steal Life"
    spell.effect_data = {"damage_amount": 10, "heal_amount": 10, "damage_type": "necrotic"}
    target_id = uuid.uuid4()
    caster_id = uuid.uuid4()
    target = TargetMatch(
        target_id=str(target_id),
        target_type=TargetType.PLAYER,
        target_name="Victim",
        room_id="room_001",
    )
    player = MagicMock()
    player.get_stats.return_value = {"current_dp": 20}
    engine = MagicMock()
    engine.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    engine.player_service.damage_player = AsyncMock()
    engine.player_service.heal_player = AsyncMock()

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, caster_id, 1.0, None)

    assert result["success"] is True
    assert result["heal_amount"] == 10
    engine.player_service.damage_player.assert_awaited_once()
    engine.player_service.heal_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_run_heal_player_oserror() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "heal"
    spell.effect_data = {"heal_amount": 5}
    target = TargetMatch(
        target_id=str(uuid.uuid4()),
        target_type=TargetType.PLAYER,
        target_name="Patient",
        room_id="room_001",
    )
    engine = MagicMock()
    engine.player_service.heal_player = AsyncMock(side_effect=OSError("db down"))

    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)

    assert result["success"] is False


def test_get_npc_instance_for_steal_life_active_npc() -> None:
    npc = MagicMock()
    npc.is_alive = True
    lm = MagicMock()
    lm.active_npcs = {"npc_001": npc}
    with patch.object(heal_mod, "_get_npc_lifecycle_manager", return_value=lm):
        result = heal_mod.get_npc_instance_for_steal_life("npc_001", None)
    assert result is npc


def test_resolve_npc_id_for_event_uuid() -> None:
    npc = MagicMock()
    npc.npc_id = "npc_001"
    target = TargetMatch(
        target_id=str(uuid.uuid4()),
        target_type=TargetType.NPC,
        target_name="Ghoul",
        room_id="room_001",
    )
    resolved = heal_mod._resolve_npc_id_for_event(npc, target)
    assert isinstance(resolved, uuid.UUID)


@pytest.mark.asyncio
async def test_run_steal_life_npc_target() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "steal_life"
    spell.name = "Steal Life"
    spell.effect_data = {"damage_amount": 8, "heal_amount": 8, "damage_type": "necrotic"}
    caster_id = uuid.uuid4()
    target = TargetMatch(
        target_id="npc_001",
        target_type=TargetType.NPC,
        target_name="Ghoul",
        room_id="room_001",
    )
    npc = MagicMock()
    npc.is_alive = True
    npc.get_combat_stats.return_value = {"current_dp": 12, "max_dp": 20}
    npc.take_damage.return_value = True
    npc.current_room = "room_001"
    npc.npc_id = "npc_001"
    engine = MagicMock()
    engine.player_service.heal_player = AsyncMock()

    with (
        patch.object(heal_mod, "get_combat_service", return_value=None),
        patch.object(heal_mod, "get_npc_instance_for_steal_life", return_value=npc),
        patch.object(heal_mod, "_steal_life_publish_npc_events", new_callable=AsyncMock),
    ):
        result = await heal_mod.run_heal_effect(engine, spell, target, caster_id, 1.0, None)

    assert result["success"] is True
    assert result["heal_amount"] == 8
    npc.take_damage.assert_called_once()


@pytest.mark.asyncio
async def test_steal_life_apply_player_damage_oserror() -> None:
    engine = MagicMock()
    engine.player_service.damage_player = AsyncMock(side_effect=OSError("fail"))
    target = TargetMatch(
        target_id=str(uuid.uuid4()),
        target_type=TargetType.PLAYER,
        target_name="Victim",
        room_id="room_001",
    )
    result = await heal_mod._steal_life_apply_player_damage(engine, target, 5, "necrotic")
    assert result is not None
    assert result["success"] is False


def test_steal_life_apply_npc_damage_only_failure() -> None:
    npc = MagicMock()
    npc.take_damage.return_value = False
    result = heal_mod._steal_life_apply_npc_damage_only(npc, 5, "necrotic", uuid.uuid4())
    assert result is not None
    assert result["success"] is False


@pytest.mark.asyncio
async def test_run_steal_life_invalid_amounts() -> None:
    spell = MagicMock(spec=Spell)
    spell.spell_id = "steal_life"
    spell.effect_data = {"damage_amount": 0, "heal_amount": 0}
    target = TargetMatch(
        target_id=str(uuid.uuid4()),
        target_type=TargetType.PLAYER,
        target_name="X",
        room_id="room_001",
    )
    engine = MagicMock()
    with patch.object(heal_mod, "get_combat_service", return_value=None):
        result = await heal_mod.run_heal_effect(engine, spell, target, uuid.uuid4(), 1.0, None)
    assert result["success"] is False


def test_lookup_npc_by_id_or_uuid_direct() -> None:
    lm = MagicMock()
    npc = MagicMock()
    lm.active_npcs = {"npc_001": npc}
    assert heal_mod._lookup_npc_by_id_or_uuid(lm, "npc_001", None) is npc
