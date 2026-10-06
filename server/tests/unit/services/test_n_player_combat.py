"""Unit tests for N-player combat (#833 slice 1): join, leave, side-based end, targets, XP recipients."""

# pyright: reportPrivateUsage=false
# Reason: _select_player_target and _xp_recipients are the units under test for the ally-swing and XP rules.

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatStatus
from server.services import aggro_threat, combat_service_attack, combat_service_end, combat_service_start
from server.services.combat_turn_participant_actions import _select_player_target
from server.services.combat_types import CombatParticipantData

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC
PHANTOM = CombatParticipantType.PHANTOM


def _p(name: str, ptype: CombatParticipantType = PLAYER, dp: int = 50, dex: int = 10) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=ptype,
        name=name,
        current_dp=dp,
        max_dp=100,
        dexterity=dex,
    )


def _combat(*participants: CombatParticipant, room_id: str = "room_1") -> CombatInstance:
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id=room_id)
    for p in participants:
        combat.participants[p.participant_id] = p
    combat.turn_order = [p.participant_id for p in participants]
    return combat


def _data(name: str, dex: int = 10) -> CombatParticipantData:
    return CombatParticipantData(
        participant_id=uuid.uuid4(),
        name=name,
        current_dp=50,
        max_dp=100,
        dexterity=dex,
        participant_type=PLAYER,
    )


def _service_for(
    combat: CombatInstance | None,
) -> tuple[MagicMock, AsyncMock, AsyncMock, AsyncMock, AsyncMock]:
    """A CombatService stand-in plus the typed mocks to assert on: (service, by_participant, joined, untrack, ended)."""
    get_by_participant: AsyncMock = AsyncMock(return_value=None)
    register_joined: AsyncMock = AsyncMock()
    untrack: AsyncMock = AsyncMock()
    publish_ended: AsyncMock = AsyncMock()
    service: MagicMock = MagicMock()
    service.get_combat = MagicMock(return_value=combat)
    service.get_combat_by_participant = get_by_participant
    service.register_joined_participant = register_joined
    service.untrack_participant = untrack
    service.notify_player_combat_ended = AsyncMock()
    service.publish_combat_ended_event = publish_ended
    return service, get_by_participant, register_joined, untrack, publish_ended


# --- is_combat_over: side-based -------------------------------------------------------------------------------


def test_combat_continues_with_two_players_and_a_living_npc() -> None:
    assert not _combat(_p("A"), _p("B"), _p("Ghoul", NPC)).is_combat_over()


def test_combat_ends_when_npc_dies_even_with_two_players_left() -> None:
    """The old alive<=1 count would have kept this fight running forever."""
    assert _combat(_p("A"), _p("B"), _p("Ghoul", NPC, dp=0)).is_combat_over()


def test_combat_ends_when_every_player_is_dead() -> None:
    assert _combat(_p("A", dp=-10), _p("B", dp=-12), _p("Ghoul", NPC)).is_combat_over()


def test_mortally_wounded_player_keeps_the_fight_going() -> None:
    """A player at 0 DP is down but not dead: the other player and the NPC still fight."""
    assert not _combat(_p("A", dp=0), _p("B"), _p("Ghoul", NPC)).is_combat_over()


def test_player_versus_player_legacy_rule_is_unchanged() -> None:
    assert not _combat(_p("A"), _p("B")).is_combat_over()
    assert _combat(_p("A"), _p("B", dp=-10)).is_combat_over()


def test_one_on_one_still_ends_when_either_side_dies() -> None:
    assert _combat(_p("A"), _p("Ghoul", NPC, dp=0)).is_combat_over()
    assert _combat(_p("A", dp=-10), _p("Ghoul", NPC)).is_combat_over()


# --- auto-attack target ---------------------------------------------------------------------------------------


def test_auto_attack_never_picks_an_ally() -> None:
    a, b, ghoul = _p("A"), _p("B"), _p("Ghoul", NPC)
    combat = _combat(a, b, ghoul)
    assert _select_player_target(combat, a) is ghoul
    assert _select_player_target(combat, b) is ghoul


def test_auto_attack_prefers_the_tracked_target_and_skips_a_dead_one() -> None:
    a, ghoul, cultist = _p("A"), _p("Ghoul", NPC), _p("Cultist", NPC)
    combat = _combat(a, ghoul, cultist)
    combat.player_current_target[a.participant_id] = cultist.participant_id
    assert _select_player_target(combat, a) is cultist
    cultist.current_dp = 0
    assert _select_player_target(combat, a) is ghoul


def test_auto_attack_player_versus_player_keeps_legacy_pick() -> None:
    a, b = _p("A"), _p("B")
    assert _select_player_target(_combat(a, b), a) is b


# --- aggro cleanup --------------------------------------------------------------------------------------------


def test_remove_entity_from_aggro_clears_lists_and_target_links() -> None:
    a, b, ghoul = _p("A"), _p("B"), _p("Ghoul", NPC)
    combat = _combat(a, b, ghoul)
    combat.npc_hate_lists[ghoul.participant_id] = {a.participant_id: 5.0, b.participant_id: 3.0}
    combat.npc_current_target[ghoul.participant_id] = a.participant_id
    combat.player_current_target[a.participant_id] = ghoul.participant_id
    combat.player_current_target[b.participant_id] = ghoul.participant_id

    aggro_threat.remove_entity_from_aggro(combat, a.participant_id)

    assert combat.npc_hate_lists[ghoul.participant_id] == {b.participant_id: 3.0}
    assert ghoul.participant_id not in combat.npc_current_target
    assert a.participant_id not in combat.player_current_target
    assert combat.player_current_target[b.participant_id] == ghoul.participant_id


def test_clear_aggro_for_combat_also_clears_player_targets() -> None:
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    combat = _combat(a, ghoul)
    combat.player_current_target[a.participant_id] = ghoul.participant_id
    aggro_threat.clear_aggro_for_combat(combat)
    assert combat.player_current_target == {}


# --- remove_participant ---------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_remove_participant_ends_combat_when_no_other_player_remains() -> None:
    """1v1: behaves exactly like end_combat, leaver stays on the roster for the ended event."""
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    combat = _combat(a, ghoul)
    service, _, _, untrack, publish_ended = _service_for(combat)

    ended = await combat_service_end.remove_participant(service, combat.combat_id, a.participant_id, "A flees")

    assert ended is True
    assert combat.status == CombatStatus.ENDED
    assert a.participant_id in combat.participants
    untrack.assert_not_awaited()
    publish_ended.assert_awaited_once_with(combat, "A flees")


@pytest.mark.asyncio
async def test_remove_participant_drops_only_the_leaver_when_others_remain() -> None:
    a, b, ghoul = _p("A"), _p("B"), _p("Ghoul", NPC)
    combat = _combat(a, b, ghoul)
    combat.npc_hate_lists[ghoul.participant_id] = {a.participant_id: 9.0, b.participant_id: 2.0}
    combat.npc_current_target[ghoul.participant_id] = a.participant_id
    combat.player_current_target[a.participant_id] = ghoul.participant_id
    combat.queued_actions[a.participant_id] = []
    service, _, _, untrack, publish_ended = _service_for(combat)

    ended = await combat_service_end.remove_participant(service, combat.combat_id, a.participant_id, "A flees")

    assert ended is False
    assert combat.status == CombatStatus.ACTIVE
    assert a.participant_id not in combat.participants
    assert a.participant_id not in combat.turn_order
    assert a.participant_id not in combat.queued_actions
    assert combat.npc_hate_lists[ghoul.participant_id] == {b.participant_id: 2.0}
    assert ghoul.participant_id not in combat.npc_current_target
    untrack.assert_awaited_once_with(a.participant_id)
    publish_ended.assert_not_awaited()


@pytest.mark.asyncio
async def test_remove_participant_ignores_unknown_participant_and_combat() -> None:
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    combat = _combat(a, ghoul)
    assert await combat_service_end.remove_participant(_service_for(combat)[0], combat.combat_id, uuid.uuid4()) is False
    assert await combat_service_end.remove_participant(_service_for(None)[0], uuid.uuid4(), a.participant_id) is False


@pytest.mark.asyncio
async def test_remove_participant_does_not_count_a_dead_player_as_remaining() -> None:
    a, dead, ghoul = _p("A"), _p("Dead", dp=-10), _p("Ghoul", NPC)
    combat = _combat(a, dead, ghoul)
    ended = await combat_service_end.remove_participant(
        _service_for(combat)[0], combat.combat_id, a.participant_id, "A flees"
    )
    assert ended is True


# --- join_existing_combat -------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_join_existing_combat_adds_player_and_rebuilds_initiative() -> None:
    a, ghoul = _p("A", dex=10), _p("Ghoul", NPC, dex=5)
    combat = _combat(a, ghoul)
    service, _, register_joined, _, _ = _service_for(combat)
    joiner = _data("B", dex=15)

    await combat_service_start.join_existing_combat(service, combat, joiner, "room_1")

    assert joiner.participant_id in combat.participants
    assert combat.participants[joiner.participant_id].participant_type == PLAYER
    assert combat.turn_order[0] == joiner.participant_id  # highest dexterity acts first
    assert set(combat.turn_order) == set(combat.participants)
    register_joined.assert_awaited_once_with(combat, joiner.participant_id, "room_1")


@pytest.mark.asyncio
async def test_join_existing_combat_refuses_another_room() -> None:
    combat = _combat(_p("A"), _p("Ghoul", NPC), room_id="room_1")
    with pytest.raises(ValueError, match="another room"):
        await combat_service_start.join_existing_combat(_service_for(combat)[0], combat, _data("B"), "room_2")


@pytest.mark.asyncio
async def test_join_existing_combat_refuses_phantom_encounters() -> None:
    combat = _combat(_p("A"), _p("Haunt", PHANTOM))
    with pytest.raises(ValueError, match="phantom"):
        await combat_service_start.join_existing_combat(_service_for(combat)[0], combat, _data("B"), "room_1")


@pytest.mark.asyncio
async def test_join_existing_combat_refuses_a_player_already_fighting_elsewhere() -> None:
    combat = _combat(_p("A"), _p("Ghoul", NPC))
    service, get_by_participant, register_joined, _, _ = _service_for(combat)
    get_by_participant.return_value = MagicMock()
    with pytest.raises(ValueError, match="already in combat"):
        await combat_service_start.join_existing_combat(service, combat, _data("B"), "room_1")
    register_joined.assert_not_awaited()


# --- XP recipients and target tracking ------------------------------------------------------------------------


def test_xp_recipients_pays_every_living_player_including_mortally_wounded() -> None:
    a, b, down, dead = _p("A"), _p("B"), _p("Down", dp=0), _p("Dead", dp=-10)
    ghoul = _p("Ghoul", NPC, dp=0)
    combat = _combat(a, b, down, dead, ghoul)
    recipients = combat_service_attack._xp_recipients(combat, a, ghoul)
    assert {p.name for p in recipients} == {"A", "B", "Down"}


def test_xp_recipients_solo_fight_pays_only_the_killer() -> None:
    a, ghoul = _p("A"), _p("Ghoul", NPC, dp=0)
    assert combat_service_attack._xp_recipients(_combat(a, ghoul), a, ghoul) == [a]


def test_xp_recipients_for_a_player_death_is_just_the_killer() -> None:
    ghoul, a = _p("Ghoul", NPC), _p("A", dp=-10)
    assert combat_service_attack._xp_recipients(_combat(ghoul, a), ghoul, a) == [ghoul]


@pytest.mark.asyncio
async def test_queue_attack_records_player_target_but_not_npc_target() -> None:
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    combat = _combat(a, ghoul)
    service = _service_for(combat)[0]

    assert await combat_service_attack.queue_combat_action(
        service, combat.combat_id, a.participant_id, "attack", target_id=ghoul.participant_id
    )
    assert await combat_service_attack.queue_combat_action(
        service, combat.combat_id, ghoul.participant_id, "attack", target_id=a.participant_id
    )

    assert combat.player_current_target == {a.participant_id: ghoul.participant_id}
