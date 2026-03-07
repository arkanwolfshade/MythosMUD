"""
Integration tests for aggro/threat flow (ADR-016).

Scenarios: healer overpull, tank swap, taunt from next room, stealth wipe.
Uses real CombatInstance and aggro_threat module; no full combat service or NATS.
"""

import uuid

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services import aggro_threat


def _make_combat(room_id: str = "room_1") -> CombatInstance:
    return CombatInstance(combat_id=uuid.uuid4(), room_id=room_id, participants={})


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


def test_aggro_healer_overpull_switches_target() -> None:
    """Tank has threat; healer does one big heal; after UpdateAggro mob switches to healer."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    tank = _make_participant("Tank", CombatParticipantType.PLAYER)
    healer = _make_participant("Healer", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[tank.participant_id] = tank
    combat.participants[healer.participant_id] = healer

    aggro_threat.add_damage_threat(combat, npc.participant_id, tank.participant_id, 100.0)
    combat.npc_current_target[npc.participant_id] = tank.participant_id

    # Healer heals for enough to exceed 110% of tank (100): need >= 110 threat from heal
    # heal_amount * 0.5 >= 110 -> heal_amount >= 220
    aggro_threat.add_heal_threat(combat, npc.participant_id, healer.participant_id, 220.0, factor=0.5)

    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)

    assert target_id == healer.participant_id
    assert did_switch is True
    assert combat.npc_current_target[npc.participant_id] == healer.participant_id


def test_aggro_tank_swap_taunt_sequence() -> None:
    """Tank A taunts (room-local), gets top. Tank B taunts, gets top. Mob switches to B."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    tank_a = _make_participant("TankA", CombatParticipantType.PLAYER)
    tank_b = _make_participant("TankB", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[tank_a.participant_id] = tank_a
    combat.participants[tank_b.participant_id] = tank_b

    # Tank A taunts (same room) -> becomes top
    applied_a = aggro_threat.apply_taunt(combat, npc.participant_id, tank_a.participant_id, "room_1", "room_1")
    assert applied_a is True
    target_id, _ = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == tank_a.participant_id

    # Tank B taunts (same room) -> becomes top
    applied_b = aggro_threat.apply_taunt(combat, npc.participant_id, tank_b.participant_id, "room_1", "room_1")
    assert applied_b is True
    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == tank_b.participant_id
    assert did_switch is True
    assert combat.npc_current_target[npc.participant_id] == tank_b.participant_id


def test_aggro_taunt_from_next_room_no_effect() -> None:
    """Taunt from adjacent room has no effect; mob does not switch."""
    combat = _make_combat("room_1")
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    tank = _make_participant("Tank", CombatParticipantType.PLAYER)
    taunter_other_room = _make_participant("Taunter", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[tank.participant_id] = tank
    combat.participants[taunter_other_room.participant_id] = taunter_other_room

    aggro_threat.get_or_create_hate_list(combat, npc.participant_id)[tank.participant_id] = 100.0
    combat.npc_current_target[npc.participant_id] = tank.participant_id

    # Taunt from room_2 (combat is in room_1) -> no-op
    applied = aggro_threat.apply_taunt(
        combat,
        npc.participant_id,
        taunter_other_room.participant_id,
        "room_1",
        "room_2",
    )
    assert applied is False

    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == tank.participant_id
    assert did_switch is False


def test_aggro_stealth_wipe_switches_to_next() -> None:
    """Player in combat enters stealth; that player removed from NPC hate list; mob switches to next."""
    combat = _make_combat()
    npc = _make_participant("Mob", CombatParticipantType.NPC)
    player_a = _make_participant("PlayerA", CombatParticipantType.PLAYER)
    player_b = _make_participant("PlayerB", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[player_a.participant_id] = player_a
    combat.participants[player_b.participant_id] = player_b

    hate = aggro_threat.get_or_create_hate_list(combat, npc.participant_id)
    hate[player_a.participant_id] = 200.0
    hate[player_b.participant_id] = 100.0
    combat.npc_current_target[npc.participant_id] = player_a.participant_id

    aggro_threat.on_player_entered_stealth(combat, player_a.participant_id)

    assert player_a.participant_id not in hate or hate.get(player_a.participant_id, 0) == 0
    assert hate.get(player_b.participant_id) == 100.0

    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == player_b.participant_id
    assert did_switch is True


def test_aggro_passive_mob_no_damage_threat_taunt_switches() -> None:
    """passive_mob: attack adds no threat; taunt adds threat and UpdateAggro switches to taunter."""
    combat = _make_combat()
    npc = _make_participant("PassiveMob", CombatParticipantType.NPC, npc_type="passive_mob")
    player = _make_participant("Player", CombatParticipantType.PLAYER)
    taunter = _make_participant("Taunter", CombatParticipantType.PLAYER)
    combat.participants[npc.participant_id] = npc
    combat.participants[player.participant_id] = player
    combat.participants[taunter.participant_id] = taunter

    # Player attacks passive mob -> no damage threat (passive_mob ignores damage)
    aggro_threat.add_damage_threat(combat, npc.participant_id, player.participant_id, 100.0, npc_participant=npc)
    assert npc.participant_id not in combat.npc_hate_lists or combat.npc_hate_lists[npc.participant_id] == {}

    # Taunter taunts (same room) -> gets threat above zero
    applied = aggro_threat.apply_taunt(combat, npc.participant_id, taunter.participant_id, "room_1", "room_1")
    assert applied is True
    target_id, did_switch = aggro_threat.update_aggro(combat, npc, "room_1", combat.participants, stability_margin=0.10)
    assert target_id == taunter.participant_id
    assert did_switch is True
    assert combat.npc_current_target[npc.participant_id] == taunter.participant_id
