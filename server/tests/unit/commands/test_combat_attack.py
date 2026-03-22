"""
Unit tests for server.commands.combat_attack (attack preconditions and execution helpers).
"""

from __future__ import annotations

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import combat_attack

# pylint: disable=redefined-outer-name,protected-access
# Reason: pytest fixtures; tests call combat_attack private helpers (no public test seam).
# pyright: reportPrivateUsage=false
# Reason: Same as pylint protected-access - intentional access to module-private helpers under test.


@pytest.fixture
def mock_handler() -> MagicMock:
    """Return a handler-shaped MagicMock for combat_attack unit tests."""
    h = MagicMock()
    h.validate_target_name = MagicMock(return_value=None)
    h.get_player_and_room = AsyncMock()
    h.room_forbids_combat = MagicMock(return_value=False)
    h.resolve_combat_target = AsyncMock()
    h.get_npc_instance = MagicMock()
    h.validate_combat_action = AsyncMock(return_value={"valid": True})
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = AsyncMock()
    h.persistence = persistence
    npc_combat_service: MagicMock = MagicMock()
    npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=True)
    h.npc_combat_service = npc_combat_service
    h.item_prototype_registry = None
    h.check_and_interrupt_rest = AsyncMock(return_value=None)
    h.extract_combat_command_data = MagicMock(return_value=("punch", "goblin"))
    return h


@pytest.mark.asyncio
async def test_validate_attack_player_and_room_missing_target(mock_handler: MagicMock) -> None:
    """Empty target_name after handler validation still yields error tuple."""
    mock_handler.validate_target_name = MagicMock(return_value={"result": "need target"})
    row = await combat_attack._validate_attack_player_and_room(mock_handler, MagicMock(), {"username": "u"}, None)
    player = cast(object | None, row[0])
    room_id = cast(object | None, row[1])
    err = row[2]
    assert player is None and room_id is None and err == {"result": "need target"}


@pytest.mark.asyncio
async def test_validate_attack_player_and_room_incapacitated(mock_handler: MagicMock) -> None:
    """current_dp <= 0 blocks attack."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    pl = MagicMock()
    pl.get_stats = MagicMock(return_value={"current_dp": 0})
    mock_handler.get_player_and_room = AsyncMock(return_value=(pl, MagicMock(), None))
    row2 = await combat_attack._validate_attack_player_and_room(mock_handler, MagicMock(), {"username": "u"}, "goblin")
    _player = cast(object | None, row2[0])
    _room_id = cast(object | None, row2[1])
    err = row2[2]
    assert err is not None
    assert "incapacitated" in err["result"].lower()
    assert _player is None


@pytest.mark.asyncio
async def test_validate_attack_player_and_room_no_combat_zone(mock_handler: MagicMock) -> None:
    """room_forbids_combat blocks attack."""
    mock_handler.validate_target_name = MagicMock(return_value=None)
    pl = MagicMock()
    pl.get_stats = MagicMock(return_value={"current_dp": 10})
    pl.current_room_id = "sanctuary"
    mock_handler.get_player_and_room = AsyncMock(return_value=(pl, MagicMock(), None))
    mock_handler.room_forbids_combat = MagicMock(return_value=True)
    row3 = await combat_attack._validate_attack_player_and_room(mock_handler, MagicMock(), {"username": "u"}, "goblin")
    _player = cast(object | None, row3[0])
    _room_id = cast(object | None, row3[1])
    err = row3[2]
    assert err is not None
    assert "forbid" in err["result"].lower()


@pytest.mark.asyncio
async def test_validate_attack_target_and_action_invalid(mock_handler: MagicMock) -> None:
    """validate_combat_action invalid returns message."""
    target_match = MagicMock()
    target_match.target_id = "n1"
    mock_handler.resolve_combat_target = AsyncMock(return_value=(target_match, None))
    mock_handler.validate_combat_action = AsyncMock(return_value={"valid": False, "message": "nope"})
    player = MagicMock()
    out = await combat_attack._validate_attack_target_and_action(mock_handler, player, "goblin", "hero", "punch")
    assert out[0] is None and out[1] is None and out[2] == {"result": "nope"}


@pytest.mark.asyncio
async def test_get_combat_action_context_missing_player(mock_handler: MagicMock) -> None:
    """_get_combat_action_context errors when player not in persistence."""
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_handler.persistence = persistence
    ctx = await combat_attack._get_combat_action_context(mock_handler, "missing", "n1", MagicMock())
    _player = cast(object | None, ctx[0])
    _npc = cast(object | None, ctx[1])
    name = ctx[2]
    err = ctx[3]
    assert _player is None and err is not None
    assert "not recognized" in err["result"].lower()
    assert name == ""


def test_resolve_combat_damage_unarmed_fallback(mock_handler: MagicMock) -> None:
    """Without registry, damage comes from config unarmed value."""
    pl = MagicMock()
    pl.get_equipped_items = MagicMock(return_value={})

    class _GameSection:
        basic_unarmed_damage: int = 7

    class _ConfigRoot:
        game: _GameSection = _GameSection()

    with patch("server.commands.combat_attack.get_config", return_value=_ConfigRoot()):
        dmg = combat_attack._resolve_combat_damage(mock_handler, pl)
    assert dmg == 7


@pytest.mark.asyncio
async def test_execute_combat_action_failure_message(mock_handler: MagicMock) -> None:
    """When npc_combat_service returns False, user sees cannot attack message."""
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=MagicMock(player_id="pid"))
    mock_handler.persistence = persistence
    npc_combat_service: MagicMock = MagicMock()
    npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=False)
    mock_handler.npc_combat_service = npc_combat_service
    npc = MagicMock()
    npc.name = "Orc"
    with patch("server.commands.combat_attack._resolve_combat_damage", return_value=5):
        out = await combat_attack._execute_combat_action(mock_handler, "hero", "n1", "punch", "r1", npc_instance=npc)
    assert "cannot attack" in out["result"].lower()


@pytest.mark.asyncio
async def test_run_handle_attack_command_blocked_by_rest(mock_handler: MagicMock) -> None:
    """check_and_interrupt_rest non-None short-circuits attack."""
    mock_handler.check_and_interrupt_rest = AsyncMock(return_value={"result": "warded"})
    req = MagicMock()
    req.app = MagicMock()
    out = await combat_attack.run_handle_attack_command(
        mock_handler, {"target_player": "x"}, {"username": "u"}, req, None, "u"
    )
    assert out == {"result": "warded"}
    gpr = cast(AsyncMock, mock_handler.get_player_and_room)
    gpr.assert_not_called()


@pytest.mark.asyncio
async def test_run_handle_attack_command_success_path(mock_handler: MagicMock) -> None:
    """Happy path returns combat result string."""
    mock_handler.check_and_interrupt_rest = AsyncMock(return_value=None)
    mock_handler.extract_combat_command_data = MagicMock(return_value=("slap", "orc"))
    pl = MagicMock()
    pl.get_stats = MagicMock(return_value={"current_dp": 5})
    pl.current_room_id = "r9"
    pl.player_id = "uuid-here"
    tm = MagicMock()
    tm.target_id = "orc_npc"
    mock_handler.get_player_and_room = AsyncMock(return_value=(pl, MagicMock(), None))
    mock_handler.resolve_combat_target = AsyncMock(return_value=(tm, None))
    npc = MagicMock()
    npc.name = "Orc"
    mock_handler.get_npc_instance = MagicMock(return_value=npc)
    npc_combat_service: MagicMock = MagicMock()
    npc_combat_service.handle_player_attack_on_npc = AsyncMock(return_value=True)
    mock_handler.npc_combat_service = npc_combat_service
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=pl)
    mock_handler.persistence = persistence
    req = MagicMock()
    req.app = MagicMock()
    with patch("server.commands.combat_attack._resolve_combat_damage", return_value=3):
        out = await combat_attack.run_handle_attack_command(
            mock_handler,
            {"target_player": "orc"},
            {"username": "u"},
            req,
            None,
            "hero",
        )
    assert "slap" in out["result"].lower() and "orc" in out["result"].lower()
