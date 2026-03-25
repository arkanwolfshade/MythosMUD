"""Unit tests for aggro/threat module (ADR-016)."""

import uuid
from unittest.mock import MagicMock, patch

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services import aggro_threat


def _make_combat() -> CombatInstance:
    return CombatInstance(combat_id=uuid.uuid4(), room_id="room_1", participants={})


def _make_participant(
    name: str,
    participant_type: CombatParticipantType = CombatParticipantType.PLAYER,
    current_dp: int = 50,
    npc_type: str | None = None,
    aggression_level: int | None = None,
) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=participant_type,
        name=name,
        current_dp=current_dp,
        max_dp=100,
        dexterity=10,
        npc_type=npc_type,
        aggression_level=aggression_level,
    )


def test_get_or_create_hate_list_creates_empty() -> None:
    """get_or_create_hate_list creates empty list for NPC and returns same dict."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    hate = aggro_threat.get_or_create_hate_list(combat, npc_id)
    assert hate == {}
    assert combat.npc_hate_lists[npc_id] is hate
    hate2 = aggro_threat.get_or_create_hate_list(combat, npc_id)
    assert hate2 is hate


def test_add_damage_threat_accumulates() -> None:
    """add_damage_threat adds amount * multiplier to source entity."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    source_id = uuid.uuid4()
    aggro_threat.add_damage_threat(combat, npc_id, source_id, 10.0, multiplier=1.0)
    assert combat.npc_hate_lists[npc_id][source_id] == 10.0
    aggro_threat.add_damage_threat(combat, npc_id, source_id, 5.0, multiplier=1.0)
    assert combat.npc_hate_lists[npc_id][source_id] == 15.0


def test_add_damage_threat_ignores_zero() -> None:
    """add_damage_threat does nothing for amount <= 0."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    source_id = uuid.uuid4()
    aggro_threat.add_damage_threat(combat, npc_id, source_id, 0.0)
    assert npc_id not in combat.npc_hate_lists or source_id not in combat.npc_hate_lists.get(npc_id, {})


def test_add_heal_threat_accumulates_with_factor() -> None:
    """add_heal_threat adds amount * factor (e.g. 0.5)."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    healer_id = uuid.uuid4()
    aggro_threat.add_heal_threat(combat, npc_id, healer_id, 20.0, factor=0.5)
    assert combat.npc_hate_lists[npc_id][healer_id] == 10.0


def test_apply_taunt_same_room_sets_threat_above_top() -> None:
    """apply_taunt in same room sets taunter threat to current_top + margin."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    other_id = uuid.uuid4()
    taunter_id = uuid.uuid4()
    aggro_threat.get_or_create_hate_list(combat, npc_id)[other_id] = 100.0
    result = aggro_threat.apply_taunt(combat, npc_id, taunter_id, "room_1", "room_1")
    assert result is True
    assert combat.npc_hate_lists[npc_id][taunter_id] >= 111.0  # 100 + 10% + 1


def test_apply_taunt_different_room_no_op() -> None:
    """apply_taunt from different room does nothing and returns False."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    taunter_id = uuid.uuid4()
    aggro_threat.get_or_create_hate_list(combat, npc_id)[taunter_id] = 50.0
    result = aggro_threat.apply_taunt(combat, npc_id, taunter_id, "room_1", "room_2")
    assert result is False
    assert combat.npc_hate_lists[npc_id][taunter_id] == 50.0


def test_apply_stealth_wipe_removes_entity() -> None:
    """apply_stealth_wipe removes entity from NPC hate list."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    entity_id = uuid.uuid4()
    aggro_threat.get_or_create_hate_list(combat, npc_id)[entity_id] = 80.0
    aggro_threat.apply_stealth_wipe(combat, npc_id, entity_id)
    assert entity_id not in combat.npc_hate_lists.get(npc_id, {})


def test_apply_stealth_wipe_no_list_no_op() -> None:
    """apply_stealth_wipe when NPC has no hate list does not raise."""
    combat = _make_combat()
    aggro_threat.apply_stealth_wipe(combat, uuid.uuid4(), uuid.uuid4())


def test_clear_aggro_for_combat_clears_both() -> None:
    """clear_aggro_for_combat clears npc_hate_lists and npc_current_target."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    combat.npc_hate_lists[npc_id] = {uuid.uuid4(): 1.0}
    combat.npc_current_target[npc_id] = uuid.uuid4()
    aggro_threat.clear_aggro_for_combat(combat)
    assert not combat.npc_hate_lists
    assert not combat.npc_current_target


def test_update_aggro_no_hate_list_clears_target() -> None:
    """update_aggro with empty hate list clears current target and returns (None, True) if had target."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    combat.participants[npc.participant_id] = npc
    combat.npc_current_target[npc.participant_id] = npc.participant_id  # invalid self, but state exists
    with patch.object(aggro_threat, "_get_aggro_config", return_value=MagicMock(aggro_stability_margin=0.10)):
        target_id, did_switch = aggro_threat.update_aggro(
            combat, npc, "room_1", combat.participants, stability_margin=0.10
        )
    assert target_id is None
    assert did_switch is True
    assert npc.participant_id not in combat.npc_current_target


def test_update_aggro_one_entity_sets_target() -> None:
    """update_aggro with one alive entity in hate list sets them as target and returns (id, True)."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    player = _make_participant("Player", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[player.participant_id] = player
    aggro_threat.get_or_create_hate_list(combat, npc.participant_id)[player.participant_id] = 100.0
    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == player.participant_id
    assert did_switch is True
    assert combat.npc_current_target[npc.participant_id] == player.participant_id


def test_update_aggro_stability_no_switch_when_below_threshold() -> None:
    """update_aggro does not switch when candidate is below 110% of current target."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    tank = _make_participant("Tank", CombatParticipantType.PLAYER)
    healer = _make_participant("Healer", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[tank.participant_id] = tank
    combat.participants[healer.participant_id] = healer
    hate = aggro_threat.get_or_create_hate_list(combat, npc.participant_id)
    hate[tank.participant_id] = 100.0
    hate[healer.participant_id] = 109.0  # 109 < 110 (100 * 1.10)
    combat.npc_current_target[npc.participant_id] = tank.participant_id
    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == tank.participant_id
    assert did_switch is False


def test_update_aggro_stability_switch_when_at_or_above_threshold() -> None:
    """update_aggro switches when candidate >= 110% of current target."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    tank = _make_participant("Tank", CombatParticipantType.PLAYER)
    healer = _make_participant("Healer", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[tank.participant_id] = tank
    combat.participants[healer.participant_id] = healer
    hate = aggro_threat.get_or_create_hate_list(combat, npc.participant_id)
    hate[tank.participant_id] = 100.0
    hate[healer.participant_id] = 110.0
    combat.npc_current_target[npc.participant_id] = tank.participant_id
    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == healer.participant_id
    assert did_switch is True
    assert combat.npc_current_target[npc.participant_id] == healer.participant_id


def test_update_aggro_excludes_dead_from_candidate() -> None:
    """update_aggro does not choose dead participant as candidate."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    dead_player = _make_participant("Dead", CombatParticipantType.PLAYER, current_dp=-10)
    combat.participants[npc.participant_id] = npc
    combat.participants[dead_player.participant_id] = dead_player
    aggro_threat.get_or_create_hate_list(combat, npc.participant_id)[dead_player.participant_id] = 999.0
    target_id, _did_switch = aggro_threat.update_aggro(
        combat, npc, "room_1", combat.participants, stability_margin=0.10
    )
    assert target_id is None
    assert combat.npc_current_target.get(npc.participant_id) is None


def test_on_player_entered_stealth_wipes_from_all_npcs() -> None:
    """on_player_entered_stealth removes player from every NPC hate list in combat."""
    combat = _make_combat()
    npc1 = _make_participant("Mob1", CombatParticipantType.NPC)
    npc2 = _make_participant("Mob2", CombatParticipantType.NPC)
    player = _make_participant("Player", CombatParticipantType.PLAYER)
    combat.participants[npc1.participant_id] = npc1
    combat.participants[npc2.participant_id] = npc2
    combat.participants[player.participant_id] = player
    aggro_threat.get_or_create_hate_list(combat, npc1.participant_id)[player.participant_id] = 50.0
    aggro_threat.get_or_create_hate_list(combat, npc2.participant_id)[player.participant_id] = 30.0
    aggro_threat.on_player_entered_stealth(combat, player.participant_id)
    assert player.participant_id not in combat.npc_hate_lists.get(npc1.participant_id, {})
    assert player.participant_id not in combat.npc_hate_lists.get(npc2.participant_id, {})


def test_get_npc_current_target_returns_none_when_unset() -> None:
    """get_npc_current_target returns None when NPC has no current target."""
    combat = _make_combat()
    assert aggro_threat.get_npc_current_target(combat, uuid.uuid4()) is None


def test_get_npc_current_target_returns_set_target() -> None:
    """get_npc_current_target returns the set target UUID."""
    combat = _make_combat()
    npc_id = uuid.uuid4()
    target_id = uuid.uuid4()
    combat.npc_current_target[npc_id] = target_id
    assert aggro_threat.get_npc_current_target(combat, npc_id) == target_id


def test_add_damage_threat_passive_mob_skipped() -> None:
    """add_damage_threat does not add threat when NPC is passive_mob (only taunt/heal add threat)."""
    combat = _make_combat()
    npc = _make_participant("PassiveMob", CombatParticipantType.NPC, npc_type="passive_mob")
    source_id = uuid.uuid4()
    combat.participants[npc.participant_id] = npc
    aggro_threat.add_damage_threat(combat, npc.participant_id, source_id, 10.0, multiplier=1.0, npc_participant=npc)
    assert npc.participant_id not in combat.npc_hate_lists or source_id not in combat.npc_hate_lists.get(
        npc.participant_id, {}
    )


def test_add_damage_threat_aggressive_mob_adds() -> None:
    """add_damage_threat adds threat when NPC is aggressive_mob."""
    combat = _make_combat()
    npc = _make_participant("AggressiveMob", CombatParticipantType.NPC, npc_type="aggressive_mob")
    source_id = uuid.uuid4()
    combat.participants[npc.participant_id] = npc
    aggro_threat.add_damage_threat(combat, npc.participant_id, source_id, 10.0, multiplier=1.0, npc_participant=npc)
    assert combat.npc_hate_lists[npc.participant_id][source_id] == 10.0


def test_aggression_level_scales_damage_threat() -> None:
    """add_damage_threat scales multiplier by aggression_level: 0 -> 0.5x, 10 -> 1.0x."""
    source_id = uuid.uuid4()
    # aggression_level 0: scale 0.5 + 0.05*0 = 0.5
    npc0 = _make_participant("Mob0", CombatParticipantType.NPC, npc_type="aggressive_mob", aggression_level=0)
    combat0 = _make_combat()
    combat0.participants[npc0.participant_id] = npc0
    aggro_threat.add_damage_threat(combat0, npc0.participant_id, source_id, 10.0, multiplier=1.0, npc_participant=npc0)
    assert combat0.npc_hate_lists[npc0.participant_id][source_id] == 5.0  # 10 * 0.5
    # aggression_level 10: scale 1.0
    npc10 = _make_participant("Mob10", CombatParticipantType.NPC, npc_type="aggressive_mob", aggression_level=10)
    combat10 = _make_combat()
    combat10.participants[npc10.participant_id] = npc10
    aggro_threat.add_damage_threat(
        combat10, npc10.participant_id, source_id, 10.0, multiplier=1.0, npc_participant=npc10
    )
    assert combat10.npc_hate_lists[npc10.participant_id][source_id] == 10.0


def test_aggression_level_scales_heal_threat() -> None:
    """add_heal_threat scales factor by aggression_level: 0 -> 0.5x, 10 -> 1.0x."""
    combat = _make_combat()
    healer_id = uuid.uuid4()
    npc0 = _make_participant("Mob0", CombatParticipantType.NPC, npc_type="aggressive_mob", aggression_level=0)
    combat.participants[npc0.participant_id] = npc0
    aggro_threat.add_heal_threat(combat, npc0.participant_id, healer_id, 20.0, factor=0.5, npc_participant=npc0)
    # 20 * 0.5 (factor) * 0.5 (scale for level 0) = 5.0
    assert combat.npc_hate_lists[npc0.participant_id][healer_id] == 5.0
