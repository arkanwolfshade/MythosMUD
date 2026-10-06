"""Unit tests for the assist command (#833): which foe it picks, the refusals, and the hand-off to the attack path."""

# pyright: reportPrivateUsage=false
# Reason: _assisted_name_from_command is exercised directly for its key/blank handling.

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import combat_assist
from server.commands.combat_assist import AssistCommandHandler, run_handle_assist_command
from server.game.party_service import PartyService
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.player import Player
from server.schemas.shared import TargetType
from server.schemas.shared.target_resolution import TargetMatch

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC
PHANTOM = CombatParticipantType.PHANTOM

ME = uuid.UUID(int=1)
ASHCROFT = uuid.UUID(int=2)
LEADER = uuid.UUID(int=3)
_ATTACK = "server.commands.combat_assist.execute_attack_on_npc"


def _participant(pid: uuid.UUID, name: str, ptype: CombatParticipantType = PLAYER, dp: int = 50) -> CombatParticipant:
    return CombatParticipant(
        participant_id=pid, participant_type=ptype, name=name, current_dp=dp, max_dp=100, dexterity=10
    )


def _fight(
    *, room: str = "r1", foe_type: CombatParticipantType = NPC, foe_dp: int = 50, fighter: uuid.UUID = ASHCROFT
) -> tuple[CombatInstance, CombatParticipant]:
    """A fight in ``room`` between ``fighter`` (a player) and a ghoul."""
    ghoul = _participant(uuid.uuid4(), "Ghoul", foe_type, foe_dp)
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id=room)
    for p in (_participant(fighter, "Ashcroft"), ghoul):
        combat.participants[p.participant_id] = p
    return combat, ghoul


def _match(pid: uuid.UUID, name: str, ttype: TargetType = TargetType.PLAYER) -> TargetMatch:
    return TargetMatch(target_id=str(pid), target_name=name, target_type=ttype, room_id="r1")


async def _assist(
    command_data: dict[str, object],
    *,
    combats: dict[uuid.UUID, CombatInstance] | None = None,
    resolved: TargetMatch | None = None,
    resolve_error: str | None = None,
    party_service: object | None = None,
    alive: bool = True,
    forbids: bool = False,
    rest: dict[str, str] | None = None,
    player_error: dict[str, str] | None = None,
    real_player: bool = True,
    has_combat_service: bool = True,
    npc_string_ids: dict[uuid.UUID, str] | None = None,
    default_npc_id: str | None = "npc_ghoul",
) -> tuple[dict[str, str], AsyncMock]:
    """Run ``assist`` against a scene; returns (result, the mock standing in for the attack path)."""
    player: MagicMock = MagicMock(spec=Player) if real_player else MagicMock()
    player.player_id = ME
    player.current_room_id = "r1"
    player.is_alive = MagicMock(return_value=alive)

    async def _combat_of(participant_id: uuid.UUID) -> CombatInstance | None:
        return (combats or {}).get(participant_id)

    combat_service: MagicMock = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(side_effect=_combat_of)

    resolution: MagicMock = MagicMock()
    resolution.success = resolve_error is None
    resolution.error_message = resolve_error
    resolution.get_single_match = MagicMock(return_value=resolved)
    target_resolution_service: MagicMock = MagicMock()
    target_resolution_service.resolve_target = AsyncMock(return_value=resolution)

    def _string_id(participant_id: uuid.UUID) -> str | None:
        return (npc_string_ids or {}).get(participant_id, default_npc_id)

    mapping: MagicMock = MagicMock()
    mapping.get_original_string_id = MagicMock(side_effect=_string_id)
    npc_combat_service: MagicMock = MagicMock()
    npc_combat_service.get_uuid_mapping = MagicMock(return_value=mapping)

    handler: MagicMock = MagicMock()
    handler.check_and_interrupt_rest = AsyncMock(return_value=rest)
    handler.get_player_and_room = AsyncMock(return_value=(player, MagicMock(), player_error))
    handler.combat_service = combat_service if has_combat_service else None
    handler.party_service = party_service
    handler.room_forbids_combat = MagicMock(return_value=forbids)
    handler.get_npc_instance = MagicMock(return_value="npc-instance")
    handler.npc_combat_service = npc_combat_service
    handler.target_resolution_service = target_resolution_service

    attack: AsyncMock = AsyncMock(return_value={"result": "You attack Ghoul!"})
    with patch(_ATTACK, new=attack):
        result = await run_handle_assist_command(
            cast(AssistCommandHandler, handler), command_data, {"username": "u"}, None, None, "Blackwood"
        )
    return result, attack


# --- the happy paths ------------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_assist_a_named_player_attacks_the_foe_they_are_fighting() -> None:
    combat, _ghoul = _fight()

    result, attack = await _assist(
        {"target_player": "ashcroft"}, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "You attack Ghoul!"}
    attack.assert_awaited_once()
    args = attack.await_args
    assert args is not None
    assert args.args[1:] == ("Blackwood", "npc_ghoul", "r1")  # player, NPC string id, room
    assert args.kwargs == {"npc_instance": "npc-instance"}


def _two_foe_fight() -> tuple[CombatInstance, CombatParticipant, CombatParticipant]:
    combat, ghoul = _fight()
    cultist = _participant(uuid.uuid4(), "Cultist", NPC)
    combat.participants[cultist.participant_id] = cultist
    return combat, ghoul, cultist


@pytest.mark.asyncio
async def test_assist_prefers_the_assisted_players_tracked_target() -> None:
    combat, ghoul, cultist = _two_foe_fight()
    combat.player_current_target[ASHCROFT] = cultist.participant_id
    ids = {ghoul.participant_id: "npc_ghoul", cultist.participant_id: "npc_cultist"}

    _, attack = await _assist(
        {"target_player": "ashcroft"},
        combats={ASHCROFT: combat},
        resolved=_match(ASHCROFT, "Ashcroft"),
        npc_string_ids=ids,
    )

    assert attack.await_args is not None
    assert attack.await_args.args[2] == "npc_cultist"


@pytest.mark.asyncio
async def test_without_a_tracked_target_assist_takes_the_first_living_foe() -> None:
    combat, ghoul, cultist = _two_foe_fight()
    ids = {ghoul.participant_id: "npc_ghoul", cultist.participant_id: "npc_cultist"}

    _, attack = await _assist(
        {"target_player": "ashcroft"},
        combats={ASHCROFT: combat},
        resolved=_match(ASHCROFT, "Ashcroft"),
        npc_string_ids=ids,
    )

    assert attack.await_args is not None
    assert attack.await_args.args[2] == "npc_ghoul"


@pytest.mark.asyncio
async def test_a_dead_tracked_target_falls_back_to_a_living_foe() -> None:
    combat, ghoul, cultist = _two_foe_fight()
    combat.player_current_target[ASHCROFT] = ghoul.participant_id
    ghoul.current_dp = 0  # the tracked foe is already dead
    ids = {ghoul.participant_id: "npc_ghoul", cultist.participant_id: "npc_cultist"}

    _, attack = await _assist(
        {"target_player": "ashcroft"},
        combats={ASHCROFT: combat},
        resolved=_match(ASHCROFT, "Ashcroft"),
        npc_string_ids=ids,
    )

    assert attack.await_args is not None
    assert attack.await_args.args[2] == "npc_cultist"


@pytest.mark.asyncio
async def test_a_bare_assist_follows_the_party_leader() -> None:
    combat, _ = _fight(fighter=LEADER)
    parties = PartyService()
    party_id = cast(str, parties.create_party(LEADER)["party_id"])
    _ = parties.add_member(party_id, ME)

    result, attack = await _assist({}, combats={LEADER: combat}, party_service=parties)

    assert result == {"result": "You attack Ghoul!"}
    attack.assert_awaited_once()


@pytest.mark.asyncio
async def test_the_npc_id_falls_back_to_the_participant_uuid_when_no_string_id_was_mapped() -> None:
    combat, ghoul = _fight()

    _, attack = await _assist(
        {"target_player": "ashcroft"},
        combats={ASHCROFT: combat},
        resolved=_match(ASHCROFT, "Ashcroft"),
        default_npc_id=None,
    )

    assert attack.await_args is not None
    assert attack.await_args.args[2] == str(ghoul.participant_id)


# --- who can be assisted --------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_a_player_who_is_not_here_is_reported_by_the_resolver() -> None:
    result, attack = await _assist({"target_player": "nobody"}, resolve_error="You don't see 'nobody' here.")

    assert result == {"result": "You don't see 'nobody' here."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_only_players_can_be_assisted() -> None:
    result, attack = await _assist({"target_player": "ghoul"}, resolved=_match(uuid.uuid4(), "Ghoul", TargetType.NPC))

    assert result == {"result": "You can only assist players."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_you_cannot_assist_yourself() -> None:
    result, attack = await _assist({"target_player": "me"}, resolved=_match(ME, "Blackwood"))

    assert result == {"result": "You can't assist yourself."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("party_service", [None, "not-a-party-service"])
async def test_a_bare_assist_without_a_party_asks_for_a_name(party_service: object | None) -> None:
    result, attack = await _assist({}, party_service=party_service)

    assert result == {"result": "You are not in a party. Name the player you want to assist."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_bare_assist_from_the_party_leader_asks_for_a_name() -> None:
    parties = PartyService()
    _ = parties.create_party(ME)

    result, attack = await _assist({}, party_service=parties)

    assert result == {"result": "You lead your party. Name the player you want to assist."}
    attack.assert_not_awaited()


# --- when there is nothing to assist --------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_an_idle_player_is_not_fighting_anything() -> None:
    result, attack = await _assist({"target_player": "ashcroft"}, combats={}, resolved=_match(ASHCROFT, "Ashcroft"))

    assert result == {"result": "Ashcroft isn't fighting anything."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_fight_with_no_living_foe_is_not_a_fight_to_join() -> None:
    combat, _ = _fight(foe_dp=0)

    result, attack = await _assist(
        {"target_player": "ashcroft"}, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "Ashcroft isn't fighting anything."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_fight_in_another_room_is_not_here() -> None:
    combat, _ = _fight(room="r2")

    result, attack = await _assist(
        {"target_player": "ashcroft"}, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "Ashcroft isn't here."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_phantom_fight_cannot_be_joined() -> None:
    """ADR-024: hallucinated hostiles exist for their owner only."""
    combat, _ = _fight(foe_type=PHANTOM)

    result, attack = await _assist(
        {"target_player": "ashcroft"}, combats={ASHCROFT: combat}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "You see nothing there to fight."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_you_are_told_when_you_are_already_in_that_fight() -> None:
    combat, _ = _fight()
    combat.participants[ME] = _participant(ME, "Blackwood")

    result, attack = await _assist(
        {"target_player": "ashcroft"}, combats={ASHCROFT: combat, ME: combat}, resolved=_match(ASHCROFT, "Ashcroft")
    )

    assert result == {"result": "You are already fighting Ghoul."}
    attack.assert_not_awaited()


# --- preconditions --------------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_an_incapacitated_player_cannot_assist() -> None:
    result, attack = await _assist({"target_player": "ashcroft"}, alive=False)

    assert result == {"result": "You are incapacitated and cannot attack."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_no_assisting_where_violence_is_forbidden() -> None:
    result, attack = await _assist({"target_player": "ashcroft"}, forbids=True)

    assert result == {"result": "The cosmic forces forbid violence in this place."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_resting_blocks_the_command() -> None:
    result, attack = await _assist({"target_player": "ashcroft"}, rest={"result": "You are resting."})

    assert result == {"result": "You are resting."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_player_lookup_error_is_passed_through() -> None:
    result, attack = await _assist({"target_player": "ashcroft"}, player_error={"result": "You are not in a room."})

    assert result == {"result": "You are not in a room."}
    attack.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize(("real_player", "has_combat_service"), [(False, True), (True, False)])
async def test_assist_needs_a_real_player_and_a_combat_service(real_player: bool, has_combat_service: bool) -> None:
    result, attack = await _assist(
        {"target_player": "ashcroft"}, real_player=real_player, has_combat_service=has_combat_service
    )

    assert result == {"result": "You cannot assist anyone right now."}
    attack.assert_not_awaited()


# --- reading the command --------------------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("command_data", "expected"),
    [
        ({"target_player": "Ashcroft"}, "Ashcroft"),
        ({"target": "Ashcroft"}, "Ashcroft"),
        ({"target_player": "  Ashcroft  "}, "Ashcroft"),
        ({"target_player": "   "}, None),
        ({"target_player": None, "target": None}, None),
        ({}, None),
    ],
)
def test_the_assisted_name_is_read_from_either_key_and_blank_means_bare(
    command_data: dict[str, object], expected: str | None
) -> None:
    assert combat_assist._assisted_name_from_command(command_data) == expected
