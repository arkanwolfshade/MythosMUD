"""Unit tests for the automatic player turn (#833): who a player's default attack lands on, and its failure paths."""

# pyright: reportPrivateUsage=false
# Reason: _should_skip_for_casting is exercised directly for its error path.

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType, CombatResult
from server.services import combat_turn_participant_actions as actions

PLAYER = CombatParticipantType.PLAYER
NPC = CombatParticipantType.NPC
_RESOLVE_DAMAGE = "server.services.combat_turn_participant_actions.resolve_player_attack_damage"


def _p(name: str, ptype: CombatParticipantType = PLAYER, dp: int = 50) -> CombatParticipant:
    return CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=ptype,
        name=name,
        current_dp=dp,
        max_dp=100,
        dexterity=10,
    )


def _combat(*participants: CombatParticipant) -> CombatInstance:
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="room_1")
    for p in participants:
        combat.participants[p.participant_id] = p
    return combat


def _result(success: bool = True) -> CombatResult:
    return CombatResult(
        success=success, damage=5, target_died=False, combat_ended=False, message="ok", combat_id=uuid.uuid4()
    )


def _service(process_attack: AsyncMock, *, casting: bool = False) -> MagicMock:
    """A CombatService stand-in whose magic service reports ``casting`` for every participant."""
    is_casting: MagicMock = MagicMock(return_value=casting)
    get_state: MagicMock = MagicMock(return_value=None)
    manager: MagicMock = MagicMock()
    manager.is_casting = is_casting
    manager.get_casting_state = get_state
    magic: MagicMock = MagicMock()
    magic.casting_state_manager = manager
    service: MagicMock = MagicMock()
    service.process_attack = process_attack
    service.magic_service = magic
    return service


@pytest.mark.asyncio
async def test_automatic_attack_lands_on_the_npc_not_the_ally() -> None:
    """#833: with two players and a ghoul, each player's default attack goes to the ghoul."""
    a, b, ghoul = _p("A"), _p("B"), _p("Ghoul", NPC)
    combat = _combat(a, b, ghoul)
    process_attack: AsyncMock = AsyncMock(return_value=_result())

    with patch(_RESOLVE_DAMAGE, new=AsyncMock(return_value=(7, "physical"))):
        await actions.process_player_turn(_service(process_attack), combat, a, current_tick=42)

    process_attack.assert_awaited_once_with(
        attacker_id=a.participant_id, target_id=ghoul.participant_id, damage=7, damage_type="physical"
    )
    assert a.last_action_tick == 42


@pytest.mark.asyncio
async def test_automatic_attack_follows_the_tracked_target() -> None:
    a, ghoul, cultist = _p("A"), _p("Ghoul", NPC), _p("Cultist", NPC)
    combat = _combat(a, ghoul, cultist)
    combat.player_current_target[a.participant_id] = cultist.participant_id
    process_attack: AsyncMock = AsyncMock(return_value=_result())

    with patch(_RESOLVE_DAMAGE, new=AsyncMock(return_value=(3, "physical"))):
        await actions.process_player_turn(_service(process_attack), combat, a, current_tick=1)

    process_attack.assert_awaited_once()
    assert process_attack.await_args is not None
    assert process_attack.await_args.kwargs["target_id"] == cultist.participant_id


@pytest.mark.asyncio
async def test_no_automatic_attack_when_no_foe_is_left() -> None:
    a, dead_ghoul = _p("A"), _p("Ghoul", NPC, dp=0)
    process_attack: AsyncMock = AsyncMock(return_value=_result())

    await actions.process_player_turn(_service(process_attack), _combat(a, dead_ghoul), a, current_tick=5)

    process_attack.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_casting_player_skips_the_automatic_attack() -> None:
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    process_attack: AsyncMock = AsyncMock(return_value=_result())

    await actions.process_player_turn(_service(process_attack, casting=True), _combat(a, ghoul), a, current_tick=9)

    process_attack.assert_not_awaited()
    assert a.last_action_tick == 9


@pytest.mark.asyncio
async def test_a_failed_automatic_attack_still_spends_the_turn() -> None:
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    process_attack: AsyncMock = AsyncMock(return_value=_result(success=False))

    with patch(_RESOLVE_DAMAGE, new=AsyncMock(return_value=(4, "physical"))):
        await actions.process_player_turn(_service(process_attack), _combat(a, ghoul), a, current_tick=11)

    process_attack.assert_awaited_once()
    assert a.last_action_tick == 11


@pytest.mark.asyncio
async def test_an_error_during_the_player_turn_is_contained() -> None:
    """A failing attack must not escape and break the whole combat round."""
    a, ghoul = _p("A"), _p("Ghoul", NPC)
    process_attack: AsyncMock = AsyncMock(side_effect=RuntimeError("boom"))

    with patch(_RESOLVE_DAMAGE, new=AsyncMock(return_value=(4, "physical"))):
        await actions.process_player_turn(_service(process_attack), _combat(a, ghoul), a, current_tick=12)

    process_attack.assert_awaited_once()


def test_casting_check_failure_does_not_block_the_attack() -> None:
    """If the casting state cannot be read, the player is treated as not casting."""
    a = _p("A")
    broken: MagicMock = MagicMock(side_effect=AttributeError("no casting manager"))
    manager: MagicMock = MagicMock()
    manager.is_casting = broken
    magic: MagicMock = MagicMock()
    magic.casting_state_manager = manager
    service: MagicMock = MagicMock()
    service.magic_service = magic

    assert actions._should_skip_for_casting(service, a, current_tick=3) is False
