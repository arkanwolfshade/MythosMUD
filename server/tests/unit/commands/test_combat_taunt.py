"""
Unit tests for server.commands.combat_taunt.
"""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import combat_taunt
from server.commands.combat_taunt import TauntCommandHandler
from server.models.combat import CombatAction, CombatInstance, CombatParticipant, CombatParticipantType
from server.schemas.shared import TargetType
from server.schemas.shared.target_resolution import TargetMatch

# pylint: disable=redefined-outer-name,protected-access
# pyright: reportPrivateUsage=false
# Reason: pytest fixtures; tests call combat_taunt private helpers (no public test seam).


@pytest.fixture
def mock_handler() -> TauntCommandHandler:
    """Return a handler-shaped MagicMock for taunt command tests."""
    h = MagicMock()
    h.validate_target_name = MagicMock(return_value=None)
    h.get_player_and_room = AsyncMock()
    h.resolve_combat_target = AsyncMock()
    h.get_npc_instance = MagicMock()
    combat_svc: MagicMock = MagicMock()
    combat_svc.get_combat_by_participant = AsyncMock()
    h.combat_service = combat_svc
    h.check_and_interrupt_rest = AsyncMock(return_value=None)
    npc_svc: MagicMock = MagicMock()
    h.npc_combat_service = npc_svc
    return cast(TauntCommandHandler, h)


def test_resolve_taunt_room_and_player_uses_room_id_attr() -> None:
    """room_id from room.room_id when present."""
    room = MagicMock()
    room.room_id = "limbo_1"
    pid = uuid.uuid4()
    pl = MagicMock()
    pl.player_id = pid
    out = combat_taunt._resolve_taunt_room_and_player(pl, room)
    assert out == ("limbo_1", pid)


class _RoomWithIdOnly:
    """Room-like object with only ``id`` (no ``room_id``)."""

    id: str

    def __init__(self, room_id: str) -> None:
        self.id = room_id


def test_resolve_taunt_room_and_player_falls_back_to_id() -> None:
    """Falls back to room.id when room_id missing."""
    room = _RoomWithIdOnly("fallback_r")
    pid = uuid.uuid4()
    pl = MagicMock()
    pl.player_id = pid
    out = combat_taunt._resolve_taunt_room_and_player(pl, room)
    assert out == ("fallback_r", pid)


def test_validate_taunt_target_not_npc(mock_handler: TauntCommandHandler) -> None:
    """Non-NPC target returns error."""
    tm = TargetMatch(
        target_id="p1",
        target_name="Hero",
        target_type=TargetType.PLAYER,
        room_id="r1",
    )
    err = combat_taunt._validate_taunt_target(mock_handler, tm)
    assert err is not None
    assert "only taunt npcs" in err["result"].lower()


def test_validate_taunt_target_dead(mock_handler: TauntCommandHandler) -> None:
    """Missing or dead NPC returns error."""
    tm = TargetMatch(
        target_id="n1",
        target_name="Beast",
        target_type=TargetType.NPC,
        room_id="r1",
    )
    mock_handler.get_npc_instance = MagicMock(return_value=None)
    err = combat_taunt._validate_taunt_target(mock_handler, tm)
    assert err is not None


def test_validate_taunt_target_name_from_target_key(mock_handler: TauntCommandHandler) -> None:
    """command_data['target'] is accepted."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    out = combat_taunt._validate_taunt_target_name(mock_handler, {"target": "beast"})
    assert out == "beast"


@pytest.mark.asyncio
async def test_run_handle_taunt_no_combat_service(mock_handler: TauntCommandHandler) -> None:
    """Without combat_service, taunt is unavailable."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    cast(MagicMock, mock_handler).combat_service = None
    pl = MagicMock()
    pl.player_id = uuid.uuid4()
    room = MagicMock()
    room.room_id = "r1"
    mock_handler.get_player_and_room = AsyncMock(return_value=(pl, room, None))
    tm = TargetMatch(
        target_id="n1",
        target_name="Beast",
        target_type=TargetType.NPC,
        room_id="r1",
    )
    mock_handler.resolve_combat_target = AsyncMock(return_value=(tm, None))
    npc = MagicMock()
    npc.is_alive = True
    mock_handler.get_npc_instance = MagicMock(return_value=npc)
    req = MagicMock()
    req.app = None
    out = await combat_taunt.run_handle_taunt_command(
        mock_handler, {"target_player": "beast"}, {"username": "u"}, req, None, "u"
    )
    assert "not available" in out["result"].lower()


@pytest.mark.asyncio
async def test_run_handle_taunt_not_in_combat(mock_handler: TauntCommandHandler) -> None:
    """Player not in combat cannot taunt."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    pl = MagicMock()
    pl.player_id = uuid.uuid4()
    room = MagicMock()
    room.room_id = "r1"
    mock_handler.get_player_and_room = AsyncMock(return_value=(pl, room, None))
    tm = TargetMatch(
        target_id="n1",
        target_name="Beast",
        target_type=TargetType.NPC,
        room_id="r1",
    )
    mock_handler.resolve_combat_target = AsyncMock(return_value=(tm, None))
    npc = MagicMock()
    npc.is_alive = True
    mock_handler.get_npc_instance = MagicMock(return_value=npc)
    combat_svc: MagicMock = MagicMock()
    combat_svc.get_combat_by_participant = AsyncMock(return_value=None)
    cast(MagicMock, mock_handler).combat_service = combat_svc
    req = MagicMock()
    req.app = None
    out = await combat_taunt.run_handle_taunt_command(
        mock_handler, {"target_player": "beast"}, {"username": "u"}, req, None, "u"
    )
    assert "must be in combat" in out["result"].lower()


@pytest.mark.asyncio
async def test_run_handle_taunt_success_queues_the_taunt_as_the_rounds_action(
    mock_handler: TauntCommandHandler,
) -> None:
    """#833: taunt no longer resolves instantly; it queues a 'taunt' action and acknowledges with one line."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    pid = uuid.uuid4()
    pl = MagicMock()
    pl.player_id = pid
    room = MagicMock()
    room.room_id = "r1"
    mock_handler.get_player_and_room = AsyncMock(return_value=(pl, room, None))
    tm = TargetMatch(
        target_id="str_npc",
        target_name="Beast",
        target_type=TargetType.NPC,
        room_id="r1",
    )
    mock_handler.resolve_combat_target = AsyncMock(return_value=(tm, None))
    npc_inst = MagicMock()
    npc_inst.is_alive = True
    mock_handler.get_npc_instance = MagicMock(return_value=npc_inst)

    npc_uuid = uuid.uuid4()
    npc_part = CombatParticipant(
        participant_id=npc_uuid,
        participant_type=CombatParticipantType.NPC,
        name="Beast",
        current_dp=10,
        max_dp=10,
        dexterity=10,
        is_active=True,
    )
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="r1", participants={npc_uuid: npc_part})

    async def _gcbp(participant_id: uuid.UUID) -> CombatInstance | None:
        return combat if participant_id == pid else None

    queue_action: AsyncMock = AsyncMock(return_value=True)
    combat_svc: MagicMock = MagicMock()
    combat_svc.get_combat_by_participant = AsyncMock(side_effect=_gcbp)
    combat_svc.queue_combat_action = queue_action
    cast(MagicMock, mock_handler).combat_service = combat_svc

    with patch("server.commands.combat_taunt.find_participant_uuid_by_string_id", return_value=npc_uuid):
        req = MagicMock()
        req.app = None
        out = await combat_taunt.run_handle_taunt_command(
            mock_handler, {"target_player": "beast"}, {"username": "u"}, req, None, "hero"
        )

    assert out["result"] == "You square up to Beast."
    queue_action.assert_awaited_once_with(
        combat_id=combat.combat_id, participant_id=pid, action_type="taunt", target_id=npc_uuid
    )


def _ghoul_fight() -> tuple[CombatInstance, uuid.UUID, CombatParticipant]:
    pid = uuid.uuid4()
    ghoul = CombatParticipant(
        participant_id=uuid.uuid4(),
        participant_type=CombatParticipantType.NPC,
        name="Ghoul",
        current_dp=10,
        max_dp=10,
        dexterity=10,
    )
    return CombatInstance(combat_id=uuid.uuid4(), room_id="r1", participants={ghoul.participant_id: ghoul}), pid, ghoul


def _handler_with(combat_service: MagicMock | None) -> TauntCommandHandler:
    handler: MagicMock = MagicMock()
    handler.combat_service = combat_service
    return cast(TauntCommandHandler, handler)


@pytest.mark.asyncio
async def test_queue_taunt_replaces_whatever_was_already_queued_for_the_round() -> None:
    """A player has one action per round: a taunt clears an attack queued for the same round."""
    combat, pid, ghoul = _ghoul_fight()
    stale = CombatAction(combat_id=combat.combat_id, attacker_id=pid, target_id=ghoul.participant_id)
    combat.queue_action(pid, stale)
    queue_action: AsyncMock = AsyncMock(return_value=True)
    combat_svc: MagicMock = MagicMock()
    combat_svc.queue_combat_action = queue_action

    err = await combat_taunt._queue_taunt(_handler_with(combat_svc), combat, ghoul, pid)

    assert err is None
    assert combat.get_queued_actions(pid) == []  # the stale attack is gone; the taunt is queued via the service
    queue_action.assert_awaited_once()


@pytest.mark.asyncio
async def test_queue_taunt_reports_a_failed_queue() -> None:
    combat, pid, ghoul = _ghoul_fight()
    combat_svc: MagicMock = MagicMock()
    combat_svc.queue_combat_action = AsyncMock(return_value=False)

    err = await combat_taunt._queue_taunt(_handler_with(combat_svc), combat, ghoul, pid)

    assert err == {"result": "You cannot taunt right now."}


@pytest.mark.asyncio
async def test_queue_taunt_without_a_combat_service() -> None:
    combat, pid, ghoul = _ghoul_fight()

    err = await combat_taunt._queue_taunt(_handler_with(None), combat, ghoul, pid)

    assert err == {"result": "Combat is not available."}
