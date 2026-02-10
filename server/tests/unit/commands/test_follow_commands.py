"""
Unit tests for follow command handlers.

Tests: follow (self rejected, same-room player/NPC, no target, no container),
unfollow, following output. Follow uses TargetResolutionService (same as combat).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.follow_commands import (
    handle_follow_command,
    handle_following_command,
    handle_unfollow_command,
)
from server.schemas.target_resolution import TargetMatch, TargetResolutionResult
from server.schemas.target_resolution import TargetType as SchemaTargetType


def _make_container(follow_service=None, async_persistence=None, npc_lifecycle_manager=None, player_service=None):
    """Build a mock container with optional follow_service, persistence, and player_service."""
    c = MagicMock()
    c.follow_service = follow_service
    c.async_persistence = async_persistence
    c.npc_lifecycle_manager = npc_lifecycle_manager or MagicMock(active_npcs={})
    c.player_service = player_service
    return c


def _make_request(container):
    """Build request with app.state.container."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.container = container
    return request


@pytest.mark.asyncio
async def test_handle_follow_no_container():
    """Follow when container or follow_service missing returns not available."""
    request = MagicMock()
    request.app = None
    result = await handle_follow_command({"target": "Bob"}, {"name": "Alice"}, request, None, "Alice")
    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_follow_no_persistence():
    """Follow when async_persistence missing returns not available."""
    container = _make_container(follow_service=MagicMock(), async_persistence=None)
    request = _make_request(container)
    result = await handle_follow_command({"target": "Bob"}, {"name": "Alice"}, request, None, "Alice")
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_follow_no_target():
    """Follow with no target asks 'Follow who?'."""
    follow_svc = MagicMock()
    persistence = AsyncMock()
    container = _make_container(follow_service=follow_svc, async_persistence=persistence)
    request = _make_request(container)
    result = await handle_follow_command({}, {"name": "Alice"}, request, None, "Alice")
    assert "follow who" in result["result"].lower() or "usage" in result["result"].lower()
    follow_svc.request_follow.assert_not_called()


@pytest.mark.asyncio
async def test_handle_follow_player_not_in_game():
    """Follow when player not found (not in game) returns error."""
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    container = _make_container(follow_service=MagicMock(), async_persistence=persistence)
    request = _make_request(container)
    result = await handle_follow_command({"target": "Bob"}, {"name": "Alice"}, request, None, "Alice")
    assert "not in the game" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_follow_self_rejected():
    """Following yourself (same room, same player) is rejected."""
    player_id = str(uuid.uuid4())
    mock_player = MagicMock()
    mock_player.player_id = player_id
    mock_player.name = "Alice"
    mock_player.current_room_id = "room_1"

    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    persistence.get_players_in_room = AsyncMock(return_value=[mock_player])

    follow_svc = MagicMock()
    follow_svc.request_follow = AsyncMock(return_value={"success": False, "result": "You cannot follow yourself."})

    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
        player_service=MagicMock(),
    )
    request = _make_request(container)
    match_self = TargetMatch(
        target_id=player_id,
        target_name="Alice",
        target_type=SchemaTargetType.PLAYER,
        room_id="room_1",
    )
    with patch("server.commands.follow_commands.TargetResolutionService") as mock_trs_class:
        mock_trs = MagicMock()
        mock_trs.resolve_target = AsyncMock(
            return_value=TargetResolutionResult(
                success=True, matches=[match_self], search_term="Alice", room_id="room_1"
            )
        )
        mock_trs_class.return_value = mock_trs
        result = await handle_follow_command({"target": "Alice"}, {"name": "Alice"}, request, None, "Alice")
    assert "cannot follow yourself" in result["result"].lower()
    follow_svc.request_follow.assert_called_once()


@pytest.mark.asyncio
async def test_handle_follow_same_room_player_sends_request():
    """Follow same-room player calls request_follow and returns result (uses TargetResolutionService)."""
    my_id = str(uuid.uuid4())
    other_id = str(uuid.uuid4())
    mock_me = MagicMock()
    mock_me.player_id = my_id
    mock_me.name = "Alice"
    mock_me.current_room_id = "room_1"
    mock_other = MagicMock()
    mock_other.player_id = other_id
    mock_other.name = "Bob"

    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_me)
    persistence.get_players_in_room = AsyncMock(return_value=[mock_me, mock_other])

    follow_svc = MagicMock()
    follow_svc.request_follow = AsyncMock(
        return_value={
            "success": True,
            "result": "Follow request sent. Waiting for them to accept.",
        }
    )

    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
        player_service=MagicMock(),
    )
    request = _make_request(container)
    match_bob = TargetMatch(
        target_id=other_id,
        target_name="Bob",
        target_type=SchemaTargetType.PLAYER,
        room_id="room_1",
    )
    with patch("server.commands.follow_commands.TargetResolutionService") as mock_trs_class:
        mock_trs = MagicMock()
        mock_trs.resolve_target = AsyncMock(
            return_value=TargetResolutionResult(success=True, matches=[match_bob], search_term="Bob", room_id="room_1")
        )
        mock_trs_class.return_value = mock_trs
        result = await handle_follow_command({"target": "Bob"}, {"name": "Alice"}, request, None, "Alice")
    assert "result" in result
    follow_svc.request_follow.assert_called_once()
    call_kw = follow_svc.request_follow.call_args
    assert call_kw[0][0] == my_id or str(call_kw[0][0]) == my_id
    assert call_kw[0][1] == other_id
    assert call_kw[0][2] == "player"
    assert call_kw[0][3] == "Alice"
    assert call_kw[1].get("target_display_name") == "Bob"


@pytest.mark.asyncio
async def test_handle_follow_same_room_npc_immediate():
    """Follow same-room NPC returns immediate success with display name (uses TargetResolutionService)."""
    my_id = str(uuid.uuid4())
    mock_me = MagicMock()
    mock_me.player_id = my_id
    mock_me.name = "Alice"
    mock_me.current_room_id = "room_1"

    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_me)

    follow_svc = MagicMock()
    follow_svc.request_follow = AsyncMock(return_value={"success": True, "result": "You are now following Guard."})

    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
        player_service=MagicMock(),
    )
    request = _make_request(container)
    match_guard = TargetMatch(
        target_id="npc_guard_1",
        target_name="Guard",
        target_type=SchemaTargetType.NPC,
        room_id="room_1",
    )
    with patch("server.commands.follow_commands.TargetResolutionService") as mock_trs_class:
        mock_trs = MagicMock()
        mock_trs.resolve_target = AsyncMock(
            return_value=TargetResolutionResult(
                success=True, matches=[match_guard], search_term="Guard", room_id="room_1"
            )
        )
        mock_trs_class.return_value = mock_trs
        result = await handle_follow_command({"target": "Guard"}, {"name": "Alice"}, request, None, "Alice")
    assert "now following" in result["result"].lower()
    follow_svc.request_follow.assert_called_once()
    call_args = follow_svc.request_follow.call_args[0]
    assert call_args[2] == "npc"
    assert follow_svc.request_follow.call_args[1].get("target_display_name") == "Guard"


@pytest.mark.asyncio
async def test_handle_follow_no_such_player_or_npc():
    """Follow when target not in room returns error from TargetResolutionService."""
    mock_me = MagicMock()
    my_id = str(uuid.uuid4())
    mock_me.player_id = my_id
    mock_me.name = "Alice"
    mock_me.current_room_id = "room_1"

    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_me)

    follow_svc = MagicMock()
    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
        player_service=MagicMock(),
    )
    request = _make_request(container)
    with patch("server.commands.follow_commands.TargetResolutionService") as mock_trs_class:
        mock_trs = MagicMock()
        mock_trs.resolve_target = AsyncMock(
            return_value=TargetResolutionResult(
                success=False,
                error_message="No targets found matching 'NobodyHere'",
                search_term="NobodyHere",
                room_id="room_1",
            )
        )
        mock_trs_class.return_value = mock_trs
        result = await handle_follow_command({"target": "NobodyHere"}, {"name": "Alice"}, request, None, "Alice")
    assert (
        "no such" in result["result"].lower()
        or "not here" in result["result"].lower()
        or "no target" in result["result"].lower()
    )
    follow_svc.request_follow.assert_not_called()


# ---- unfollow ----
@pytest.mark.asyncio
async def test_handle_unfollow_no_container():
    """Unfollow when container missing returns not available."""
    request = MagicMock()
    request.app = None
    result = await handle_unfollow_command({}, {"name": "Alice"}, request, None, "Alice")
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_unfollow_success():
    """Unfollow calls service and returns result."""
    player_id = str(uuid.uuid4())
    mock_player = MagicMock()
    mock_player.player_id = player_id

    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)

    follow_svc = MagicMock()
    follow_svc.unfollow = MagicMock(return_value={"success": True, "result": "You are no longer following anyone."})

    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
    )
    request = _make_request(container)
    result = await handle_unfollow_command({}, {"name": "Alice"}, request, None, "Alice")
    assert "no longer following" in result["result"].lower()
    follow_svc.unfollow.assert_called_once_with(player_id)


@pytest.mark.asyncio
async def test_handle_unfollow_was_not_following():
    """Unfollow when not following returns friendly message."""
    mock_player = MagicMock()
    mock_player.player_id = str(uuid.uuid4())
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    follow_svc = MagicMock()
    follow_svc.unfollow = MagicMock(return_value={"success": True, "result": "You weren't following anyone."})
    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
    )
    request = _make_request(container)
    result = await handle_unfollow_command({}, {"name": "Alice"}, request, None, "Alice")
    assert "weren't following" in result["result"].lower()


# ---- following ----
@pytest.mark.asyncio
async def test_handle_following_no_container():
    """Following when container missing returns not available."""
    request = MagicMock()
    request.app = None
    result = await handle_following_command({}, {"name": "Alice"}, request, None, "Alice")
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_following_display():
    """Following returns display from service (who you follow, who follows you)."""
    mock_player = MagicMock()
    mock_player.player_id = str(uuid.uuid4())
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    follow_svc = MagicMock()
    display_text = "You are not following anyone.\nNo one is following you."
    follow_svc.get_following_display = AsyncMock(return_value=display_text)
    container = _make_container(
        follow_service=follow_svc,
        async_persistence=persistence,
    )
    request = _make_request(container)
    result = await handle_following_command({}, {"name": "Alice"}, request, None, "Alice")
    assert result["result"] == display_text
    follow_svc.get_following_display.assert_called_once()
