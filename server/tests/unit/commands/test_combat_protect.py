"""Unit tests for the protect command (#991): joining, queuing, and every refusal."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.combat_assist import AssistCommandHandler
from server.commands.combat_protect import run_handle_protect_command
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.models.player import Player
from server.schemas.shared import TargetType
from server.schemas.shared.target_resolution import TargetMatch

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC
PHANTOM = CombatParticipantType.PHANTOM

ME = uuid.UUID(int=1)
ASHCROFT = uuid.UUID(int=2)


def _participant(pid: uuid.UUID, name: str, ptype: CombatParticipantType = PLAYER, dp: int = 50) -> CombatParticipant:
    return CombatParticipant(
        participant_id=pid, participant_type=ptype, name=name, current_dp=dp, max_dp=100, dexterity=10
    )


def _fight(*, room: str = "r1", foe_type: CombatParticipantType = NPC, with_me: bool = False) -> CombatInstance:
    """A fight in ``room`` between Ashcroft (a player) and a ghoul, optionally with the protector already in it."""
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id=room)
    members = [_participant(ASHCROFT, "Ashcroft"), _participant(uuid.uuid4(), "Ghoul", foe_type)]
    if with_me:
        members.append(_participant(ME, "Blackwood"))
    for p in members:
        combat.participants[p.participant_id] = p
    return combat


def _match(pid: uuid.UUID, name: str, ttype: TargetType = TargetType.PLAYER) -> TargetMatch:
    return TargetMatch(target_id=str(pid), target_name=name, target_type=ttype, room_id="r1")


async def _protect(
    command_data: Mapping[str, object],
    *,
    combats: dict[uuid.UUID, CombatInstance] | None = None,
    resolved: TargetMatch | None = None,
    resolve_error: str | None = None,
    alive: bool = True,
    forbids: bool = False,
    rest: dict[str, str] | None = None,
    player_error: dict[str, str] | None = None,
    real_player: bool = True,
    has_combat_service: bool = True,
    join_error: bool = False,
    queued: bool = True,
) -> tuple[dict[str, str], AsyncMock, AsyncMock]:
    """Run ``protect`` against a scene; returns (result, the join mock, the queue mock) to assert on."""
    player: MagicMock = MagicMock(spec=Player) if real_player else MagicMock()
    player.player_id = ME
    player.current_room_id = "r1"
    player.is_alive = MagicMock(return_value=alive)

    async def _combat_of(participant_id: uuid.UUID) -> CombatInstance | None:
        return (combats or {}).get(participant_id)

    queue: AsyncMock = AsyncMock(return_value=queued)
    combat_service: MagicMock = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(side_effect=_combat_of)
    combat_service.queue_combat_action = queue

    resolution: MagicMock = MagicMock()
    resolution.success = resolve_error is None
    resolution.error_message = resolve_error
    resolution.get_single_match = MagicMock(return_value=resolved)
    target_resolution_service: MagicMock = MagicMock()
    target_resolution_service.resolve_target = AsyncMock(return_value=resolution)

    join: AsyncMock = AsyncMock(side_effect=ValueError("Participant is already in combat") if join_error else None)
    npc_combat_service: MagicMock = MagicMock()
    npc_combat_service.join_player_to_combat = join

    handler: MagicMock = MagicMock()
    handler.check_and_interrupt_rest = AsyncMock(return_value=rest)
    handler.get_player_and_room = AsyncMock(return_value=(player, MagicMock(), player_error))
    handler.combat_service = combat_service if has_combat_service else None
    handler.room_forbids_combat = MagicMock(return_value=forbids)
    handler.npc_combat_service = npc_combat_service
    handler.target_resolution_service = target_resolution_service

    result = await run_handle_protect_command(
        cast(AssistCommandHandler, handler), command_data, {"username": "u"}, None, None, "Blackwood"
    )
    return result, join, queue


_ASH: dict[str, object] = {"target_player": "ashcroft"}


# --- the happy paths ----------------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_protect_a_fighting_ally_you_are_already_fighting_beside_queues_the_action() -> None:
    combat = _fight(with_me=True)

    result, join, queue = await _protect(
        _ASH, combats={ASHCROFT: combat, ME: combat}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "You move to cover Ashcroft."}
    join.assert_not_awaited()
    queue.assert_awaited_once_with(
        combat_id=combat.combat_id, participant_id=ME, action_type="protect", target_id=ASHCROFT
    )


@pytest.mark.asyncio
async def test_protect_joins_the_allys_fight_when_you_are_not_in_it_yet() -> None:
    combat = _fight()

    result, join, queue = await _protect(_ASH, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft"))

    assert result == {"result": "You move to cover Ashcroft."}
    join.assert_awaited_once_with(str(ME), "r1", ME, combat, "Ghoul")
    queue.assert_awaited_once()


@pytest.mark.asyncio
async def test_protect_replaces_whatever_you_had_queued_for_the_next_round() -> None:
    combat = _fight(with_me=True)
    next_round = combat.combat_round + 1
    combat.queued_actions[ME] = [CombatAction(attacker_id=ME, action_type="attack", round=next_round)]

    result, _, _ = await _protect(_ASH, combats={ASHCROFT: combat, ME: combat}, resolved=_match(ASHCROFT, "Ashcroft"))

    assert result == {"result": "You move to cover Ashcroft."}
    assert not any(a.round == next_round for a in combat.queued_actions.get(ME, []))


# --- refusals about joining and queuing ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_you_cannot_protect_from_inside_a_different_fight() -> None:
    allys_fight, other_fight = _fight(), _fight()

    result, join, queue = await _protect(
        _ASH, combats={ASHCROFT: allys_fight, ME: other_fight}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "You are already in another fight."}
    join.assert_not_awaited()
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_refused_join_stops_the_protect() -> None:
    combat = _fight()

    result, _, queue = await _protect(
        _ASH, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft"), join_error=True
    )

    assert result == {"result": "You cannot join that fight."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_failed_queue_is_reported() -> None:
    combat = _fight(with_me=True)

    result, _, _ = await _protect(
        _ASH, combats={ASHCROFT: combat, ME: combat}, resolved=_match(ASHCROFT, "Ashcroft"), queued=False
    )

    assert result == {"result": "You cannot protect right now."}


# --- who can be protected -----------------------------------------------------------------------------------------


@pytest.mark.asyncio
@pytest.mark.parametrize("command_data", [{}, {"target_player": "   "}])
async def test_protect_needs_a_name(command_data: Mapping[str, object]) -> None:
    result, _, queue = await _protect(command_data)

    assert result == {"result": "Protect whom? Name the player you want to cover."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_an_unknown_player_is_reported() -> None:
    result, _, queue = await _protect({"target_player": "nobody"}, resolve_error="You don't see 'nobody' here.")

    assert result == {"result": "You don't see 'nobody' here."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_only_players_can_be_protected() -> None:
    result, _, queue = await _protect(
        {"target_player": "ghoul"}, resolved=_match(uuid.uuid4(), "Ghoul", TargetType.NPC)
    )

    assert result == {"result": "You can only protect players."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_you_cannot_protect_yourself() -> None:
    result, _, queue = await _protect({"target_player": "me"}, resolved=_match(ME, "Blackwood"))

    assert result == {"result": "You can't protect yourself."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_an_idle_player_has_nothing_to_be_protected_from() -> None:
    result, _, queue = await _protect(_ASH, combats={}, resolved=_match(ASHCROFT, "Ashcroft"))

    assert result == {"result": "Ashcroft isn't fighting anything."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_fight_in_another_room_is_not_here() -> None:
    combat = _fight(room="r2")

    result, _, queue = await _protect(_ASH, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft"))

    assert result == {"result": "Ashcroft isn't here."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_phantom_fight_cannot_be_covered() -> None:
    """ADR-024: hallucinated hostiles exist for their owner only."""
    combat = _fight(foe_type=PHANTOM)

    result, join, queue = await _protect(_ASH, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft"))

    assert result == {"result": "You see nothing there to fight."}
    join.assert_not_awaited()
    queue.assert_not_awaited()


# --- preconditions ------------------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_an_incapacitated_player_cannot_protect() -> None:
    result, _, queue = await _protect(_ASH, alive=False)

    assert result == {"result": "You are incapacitated and cannot attack."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_no_protecting_where_violence_is_forbidden() -> None:
    result, _, queue = await _protect(_ASH, forbids=True)

    assert result == {"result": "The cosmic forces forbid violence in this place."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_resting_blocks_the_command() -> None:
    result, _, queue = await _protect(_ASH, rest={"result": "You are resting."})

    assert result == {"result": "You are resting."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_player_lookup_error_is_passed_through() -> None:
    """The login-grace gate lives in get_player_and_room, so it reaches protect through this same path."""
    result, _, queue = await _protect(_ASH, player_error={"result": "You are still warded by protective energies."})

    assert result == {"result": "You are still warded by protective energies."}
    queue.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize(("real_player", "has_combat_service"), [(False, True), (True, False)])
async def test_protect_needs_a_real_player_and_a_combat_service(real_player: bool, has_combat_service: bool) -> None:
    result, _, queue = await _protect(_ASH, real_player=real_player, has_combat_service=has_combat_service)

    assert result == {"result": "You cannot protect anyone right now."}
    queue.assert_not_awaited()
