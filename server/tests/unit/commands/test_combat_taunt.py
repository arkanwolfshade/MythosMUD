"""
Unit tests for server.commands.combat_taunt.
"""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import combat_taunt
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.schemas.shared import TargetType
from server.schemas.shared.target_resolution import TargetMatch

# pylint: disable=redefined-outer-name,protected-access
# pyright: reportPrivateUsage=false
# Reason: pytest fixtures; tests call combat_taunt private helpers (no public test seam).


@pytest.fixture
def mock_handler() -> MagicMock:
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
    npc_svc._messaging_integration = None
    h.npc_combat_service = npc_svc
    return h


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


def test_validate_taunt_target_not_npc(mock_handler: MagicMock) -> None:
    """Non-NPC target returns error."""
    tm = MagicMock()
    tm.target_type = TargetType.PLAYER
    err = combat_taunt._validate_taunt_target(mock_handler, tm)
    assert err is not None
    assert "only taunt npcs" in err["result"].lower()


def test_validate_taunt_target_dead(mock_handler: MagicMock) -> None:
    """Missing or dead NPC returns error."""
    tm = MagicMock()
    tm.target_type = TargetType.NPC
    tm.target_id = "n1"
    mock_handler.get_npc_instance = MagicMock(return_value=None)
    err = combat_taunt._validate_taunt_target(mock_handler, tm)
    assert err is not None


def test_validate_taunt_target_name_from_target_key(mock_handler: MagicMock) -> None:
    """command_data['target'] is accepted."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    out = combat_taunt._validate_taunt_target_name(mock_handler, {"target": "beast"})
    assert out == "beast"


@pytest.mark.asyncio
async def test_run_handle_taunt_no_combat_service(mock_handler: MagicMock) -> None:
    """Without combat_service, taunt is unavailable."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    mock_handler.combat_service = None
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
async def test_run_handle_taunt_not_in_combat(mock_handler: MagicMock) -> None:
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
    mock_handler.combat_service = combat_svc
    req = MagicMock()
    req.app = None
    out = await combat_taunt.run_handle_taunt_command(
        mock_handler, {"target_player": "beast"}, {"username": "u"}, req, None, "u"
    )
    assert "must be in combat" in out["result"].lower()


@pytest.mark.asyncio
async def test_run_handle_taunt_success(mock_handler: MagicMock) -> None:
    """Successful taunt returns flavor message."""
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

    async def _gcbp(participant_id: uuid.UUID):
        if participant_id == pid:
            return combat
        return None

    combat_svc: MagicMock = MagicMock()
    combat_svc.get_combat_by_participant = AsyncMock(side_effect=_gcbp)
    mock_handler.combat_service = combat_svc

    with (
        patch("server.commands.combat_taunt.find_participant_uuid_by_string_id", return_value=npc_uuid),
        patch("server.commands.combat_taunt.apply_taunt", return_value=True),
        patch("server.commands.combat_taunt.update_aggro", return_value=(None, False)),
    ):
        req = MagicMock()
        req.app = None
        out = await combat_taunt.run_handle_taunt_command(
            mock_handler, {"target_player": "beast"}, {"username": "u"}, req, None, "hero"
        )
    assert "taunt" in out["result"].lower()
    assert "beast" in out["result"].lower()
