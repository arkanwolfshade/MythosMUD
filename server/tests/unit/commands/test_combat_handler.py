"""
Unit tests for server.commands.combat_handler (CombatCommandHandler and validation helpers).
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from enum import Enum
from typing import Protocol, cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.combat_app_protocols import AppWithState
from server.commands.combat_handler import CombatCommandHandler, CombatCommandHandlerExtras
from server.schemas.shared import TargetType
from server.schemas.shared.target_resolution import TargetMatch, TargetResolutionResult

# pylint: disable=protected-access  # Reason: Unit tests exercise handler internals
# pylint: disable=redefined-outer-name  # Reason: pytest fixtures


class _CmdType(Enum):
    """Stub enum for extract_combat_command_data .value branch."""

    STRIKE = "strike"


class _PlayerWithIdForTests(Protocol):  # pylint: disable=too-few-public-methods  # Reason: test Protocol stub
    """Minimal player shape for resolve_combat_target (matches handler Protocol intent)."""

    player_id: str | uuid.UUID


@dataclass
class _AppStatePersistence:
    persistence: MagicMock
    container: None = None


@dataclass
class _AppWithPersistence:
    state: _AppStatePersistence


def _handler_with_persistence(persistence: MagicMock) -> CombatCommandHandler:
    return CombatCommandHandler(async_persistence=persistence)


def _as_app_with_state(app: object) -> AppWithState | None:
    """Widen test doubles to ``object`` before ``cast`` so pyright accepts Protocol arguments."""
    return cast(AppWithState | None, app)


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Async persistence mock with player/room lookups wired for handler tests."""
    p = MagicMock()
    p.get_player_by_name = AsyncMock()
    p.get_room_by_id = MagicMock()
    return p


def test_combat_command_handler_requires_async_persistence() -> None:
    """__init__ raises when async_persistence is None."""
    with pytest.raises(ValueError, match="async_persistence is required"):
        _ = CombatCommandHandler(async_persistence=None)


def test_combat_command_handler_extras_optional(mock_persistence: MagicMock) -> None:
    """Handler wires optional extras without error."""
    h = CombatCommandHandler(
        async_persistence=mock_persistence,
        extras=CombatCommandHandlerExtras(
            movement_service=MagicMock(),
            player_position_service=MagicMock(),
            item_prototype_registry=MagicMock(),
        ),
    )
    assert h.movement_service is not None
    assert h.player_position_service is not None
    assert h.item_prototype_registry is not None


def test_extract_combat_command_data_string_type(mock_persistence: MagicMock) -> None:
    """command_type as string is preserved; target from target_player."""
    h = _handler_with_persistence(mock_persistence)
    cmd, target = h.extract_combat_command_data({"command_type": "kick", "target_player": "goblin"})
    assert cmd == "kick"
    assert target == "goblin"


def test_extract_combat_command_data_enum_value(mock_persistence: MagicMock) -> None:
    """command_type with .value (Enum) is normalized to string."""
    h = _handler_with_persistence(mock_persistence)
    cmd, target = h.extract_combat_command_data({"command_type": _CmdType.STRIKE, "target_player": "x"})
    assert cmd == "strike"
    assert target == "x"


def test_validate_target_name_empty(mock_persistence: MagicMock) -> None:
    """Missing target returns a result dict with a message."""
    h = _handler_with_persistence(mock_persistence)
    err = h.validate_target_name(None)
    assert err is not None
    assert "result" in err
    assert len(err["result"]) > 0


def test_validate_target_name_present(mock_persistence: MagicMock) -> None:
    """Non-empty target passes validation."""
    h = _handler_with_persistence(mock_persistence)
    assert h.validate_target_name("rat") is None


@pytest.mark.asyncio
async def test_get_player_and_room_no_persistence_on_app(mock_persistence: MagicMock) -> None:
    """When app resolves no persistence layer, return cosmic forces error."""
    h = _handler_with_persistence(mock_persistence)
    app = MagicMock()
    state: MagicMock = MagicMock()
    state.container = None
    state.persistence = None
    app.state = state
    player, room, err = await h.get_player_and_room(_as_app_with_state(app), {"username": "u"})
    assert player is None and room is None
    assert err is not None
    assert "unreachable" in err["result"].lower()


@pytest.mark.asyncio
async def test_get_player_and_room_unknown_player(mock_persistence: MagicMock) -> None:
    """Unknown player yields recognition error."""
    h = _handler_with_persistence(mock_persistence)
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    app = _AppWithPersistence(state=_AppStatePersistence(persistence=mock_persistence))
    err = (await h.get_player_and_room(_as_app_with_state(app), {"username": "nobody"}))[2]
    assert err is not None
    assert "not recognized" in err["result"].lower()


@pytest.mark.asyncio
async def test_get_player_and_room_no_current_room(mock_persistence: MagicMock) -> None:
    """Player without current_room_id fails."""
    h = _handler_with_persistence(mock_persistence)
    pl = MagicMock()
    pl.current_room_id = None
    mock_persistence.get_player_by_name = AsyncMock(return_value=pl)
    app = _AppWithPersistence(state=_AppStatePersistence(persistence=mock_persistence))
    err = (await h.get_player_and_room(_as_app_with_state(app), {"username": "p"}))[2]
    assert err is not None
    assert "not in a room" in err["result"].lower()


@pytest.mark.asyncio
async def test_get_player_and_room_unknown_room(mock_persistence: MagicMock) -> None:
    """Missing room record fails."""
    h = _handler_with_persistence(mock_persistence)
    pl = MagicMock()
    pl.current_room_id = "r1"
    mock_persistence.get_player_by_name = AsyncMock(return_value=pl)
    mock_persistence.get_room_by_id = MagicMock(return_value=None)
    app = _AppWithPersistence(state=_AppStatePersistence(persistence=mock_persistence))
    err = (await h.get_player_and_room(_as_app_with_state(app), {"username": "p"}))[2]
    assert err is not None
    assert "unknown room" in err["result"].lower()


@pytest.mark.asyncio
async def test_get_player_and_room_success(mock_persistence: MagicMock) -> None:
    """Happy path returns player, room, no error."""
    h = _handler_with_persistence(mock_persistence)
    pl = MagicMock()
    pl.current_room_id = "r1"
    rm = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=pl)
    mock_persistence.get_room_by_id = MagicMock(return_value=rm)
    app = _AppWithPersistence(state=_AppStatePersistence(persistence=mock_persistence))
    player, room, err = await h.get_player_and_room(_as_app_with_state(app), {"username": "p"})
    assert err is None
    assert player is pl
    assert room is rm


def test_room_forbids_combat_true(mock_persistence: MagicMock) -> None:
    """no_combat attribute in room mapping blocks combat."""
    h = _handler_with_persistence(mock_persistence)
    room = MagicMock()
    room.attributes = {"no_combat": True}
    mock_persistence.get_room_by_id = MagicMock(return_value=room)
    assert h.room_forbids_combat("arena") is True


def test_room_forbids_combat_false_no_attrs(mock_persistence: MagicMock) -> None:
    """Room without mapping attributes allows combat."""
    h = _handler_with_persistence(mock_persistence)
    room = MagicMock()
    room.attributes = None
    mock_persistence.get_room_by_id = MagicMock(return_value=room)
    assert h.room_forbids_combat("arena") is False


@pytest.mark.asyncio
async def test_resolve_combat_target_failure_message(mock_persistence: MagicMock) -> None:
    """Failed resolution surfaces error_message."""
    h = _handler_with_persistence(mock_persistence)
    h.target_resolution_service.resolve_target = AsyncMock(
        return_value=TargetResolutionResult(
            success=False,
            matches=[],
            error_message="nothing here",
            disambiguation_required=False,
            search_term="x",
            room_id="r",
        )
    )
    player = MagicMock()
    player.player_id = uuid.uuid4()
    match, err = await h.resolve_combat_target(cast(_PlayerWithIdForTests, player), "x")
    assert match is None and err is not None
    assert err["result"] == "nothing here"


@pytest.mark.asyncio
async def test_resolve_combat_target_rejects_non_npc(mock_persistence: MagicMock) -> None:
    """Single match that is not an NPC is rejected."""
    h = _handler_with_persistence(mock_persistence)
    pid = str(uuid.uuid4())
    tm = TargetMatch(
        target_id=pid,
        target_name="Bob",
        target_type=TargetType.PLAYER,
        room_id="r1",
    )
    h.target_resolution_service.resolve_target = AsyncMock(
        return_value=TargetResolutionResult(
            success=True,
            matches=[tm],
            error_message=None,
            disambiguation_required=False,
            search_term="bob",
            room_id="r1",
        )
    )
    player = MagicMock()
    player.player_id = uuid.uuid4()
    match, err = await h.resolve_combat_target(cast(_PlayerWithIdForTests, player), "bob")
    assert match is None and err is not None
    assert "only attack npcs" in err["result"].lower()


@pytest.mark.asyncio
async def test_resolve_combat_target_rejects_dead_npc(mock_persistence: MagicMock) -> None:
    """Dead NPC in lifecycle yields already dead message."""
    h = _handler_with_persistence(mock_persistence)
    tm = TargetMatch(
        target_id="npc_dead",
        target_name="Zombie",
        target_type=TargetType.NPC,
        room_id="r1",
    )
    h.target_resolution_service.resolve_target = AsyncMock(
        return_value=TargetResolutionResult(
            success=True,
            matches=[tm],
            error_message=None,
            disambiguation_required=False,
            search_term="z",
            room_id="r1",
        )
    )
    npc = MagicMock()
    npc.is_alive = False
    npc.name = "Zombie"
    lm = MagicMock()
    lm.active_npcs = {"npc_dead": npc}
    svc = MagicMock()
    svc.lifecycle_manager = lm
    with patch("server.commands.combat_handler.get_npc_instance_service", return_value=svc):
        player = MagicMock()
        player.player_id = uuid.uuid4()
        player.player_name = "hero"
        match, err = await h.resolve_combat_target(cast(_PlayerWithIdForTests, player), "z")
    assert match is None and err is not None
    assert "dead" in err["result"].lower()


@pytest.mark.asyncio
async def test_validate_combat_action(mock_persistence: MagicMock) -> None:
    """_validate_combat_action returns valid flag for well-formed args."""
    h = _handler_with_persistence(mock_persistence)
    out = await h.validate_combat_action("p", "npc1", "punch")
    assert out["valid"] is True


@pytest.mark.asyncio
async def test_validate_combat_action_empty_name(mock_persistence: MagicMock) -> None:
    """Empty player_name fails validation."""
    h = _handler_with_persistence(mock_persistence)
    out = await h.validate_combat_action("", "npc1", "punch")
    assert out["valid"] is False


@pytest.mark.asyncio
async def test_handle_flee_command_delegates(mock_persistence: MagicMock) -> None:
    """handle_flee_command calls combat_flee.run_handle_flee_command."""
    h = _handler_with_persistence(mock_persistence)
    with patch("server.commands.combat_flee.run_handle_flee_command", new_callable=AsyncMock) as run_flee:
        run_flee.return_value = {"result": "ok"}
        out = await h.handle_flee_command({}, {"username": "u"}, None, None, "u")
    assert out == {"result": "ok"}
    run_flee.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_taunt_command_delegates(mock_persistence: MagicMock) -> None:
    """handle_taunt_command calls run_handle_taunt_command."""
    h = _handler_with_persistence(mock_persistence)
    with patch("server.commands.combat_handler.run_handle_taunt_command", new_callable=AsyncMock) as run_taunt:
        run_taunt.return_value = {"result": "taunted"}
        out = await h.handle_taunt_command({}, {"username": "u"}, None, None, "u")
    assert out == {"result": "taunted"}
    run_taunt.assert_awaited_once()
