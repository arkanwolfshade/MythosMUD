"""
Unit tests for FollowService.

Covers: request_follow (self reject, NPC immediate, player muted), accept/decline,
unfollow, get_followers/get_following, movement propagation, auto-unfollow on move failure,
disconnect cleanup.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_types import NPCEnteredRoom, PlayerEnteredRoom
from server.game.follow_service import FOLLOW_REQUEST_TTL_SECONDS, FollowService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def event_bus():
    """No event bus so we don't need to run the loop; we call handlers directly."""
    return None


@pytest.fixture
def movement_service():
    """Mock movement service; move_player returns True by default."""
    m = MagicMock()
    m.move_player = AsyncMock(return_value=True)
    return m


@pytest.fixture
def user_manager():
    """Mock user manager; not muted by default."""
    m = MagicMock()
    m.is_player_muted_async = AsyncMock(return_value=False)
    return m


@pytest.fixture
def connection_manager():
    """Mock connection manager (optional for most tests)."""
    return MagicMock()


@pytest.fixture
def follow_service(event_bus, movement_service, user_manager):
    """FollowService with mocks. connection_manager=None avoids scheduling real send_game_event in sync tests."""
    return FollowService(
        event_bus=event_bus,
        movement_service=movement_service,
        user_manager=user_manager,
        connection_manager=None,
    )


# ---- request_follow ----
@pytest.mark.asyncio
async def test_request_follow_self_rejected(follow_service):
    """Cannot follow yourself."""
    pid = str(uuid.uuid4())
    result = await follow_service.request_follow(pid, pid, "player", "Me")
    assert result["success"] is False
    assert "cannot follow yourself" in result["result"].lower()


@pytest.mark.asyncio
async def test_request_follow_npc_immediate(follow_service):
    """Following an NPC is immediate (no pending request)."""
    requestor_id = str(uuid.uuid4())
    npc_id = "npc_guard_1"
    result = await follow_service.request_follow(requestor_id, npc_id, "npc", "Alice")
    assert result["success"] is True
    assert "now following" in result["result"].lower()
    assert follow_service.get_following(requestor_id) == (npc_id, "npc")
    assert follow_service.get_followers(npc_id) == [requestor_id]


@pytest.mark.asyncio
async def test_request_follow_player_muted_auto_decline(follow_service, user_manager):
    """If target has muted requestor, return error and do not create pending request."""
    user_manager.is_player_muted_async = AsyncMock(return_value=True)
    requestor_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    result = await follow_service.request_follow(requestor_id, target_id, "player", "Alice")
    assert result["success"] is False
    assert "not accepting follow requests" in result["result"].lower()
    assert follow_service.get_following(requestor_id) is None
    assert len(follow_service._pending_requests) == 0


@pytest.mark.asyncio
async def test_request_follow_player_creates_pending(follow_service, user_manager):
    """Requesting to follow a player creates a pending request (target gets event via connection_manager)."""
    user_manager.is_player_muted_async = AsyncMock(return_value=False)
    requestor_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    result = await follow_service.request_follow(requestor_id, target_id, "player", "Alice")
    assert result["success"] is True
    assert "waiting" in result["result"].lower() or "sent" in result["result"].lower()
    assert "request_id" in result
    assert len(follow_service._pending_requests) == 1
    req_id = list(follow_service._pending_requests)[0]
    data = follow_service._pending_requests[req_id]
    assert data["requestor_id"] == requestor_id
    assert data["target_id"] == target_id
    assert data["requestor_name"] == "Alice"


@pytest.mark.asyncio
async def test_request_follow_already_following_rejected(follow_service):
    """If already following someone, request_follow is rejected."""
    requestor_id = str(uuid.uuid4())
    follow_service._follow_target[requestor_id] = ("other_id", "player")
    result = await follow_service.request_follow(requestor_id, str(uuid.uuid4()), "player", "Alice")
    assert result["success"] is False
    assert "already following" in result["result"].lower()


# ---- accept_follow / decline_follow ----
@pytest.mark.asyncio
async def test_accept_follow_success(follow_service, user_manager):
    """Accepting a follow request establishes follow and notifies both."""
    user_manager.is_player_muted_async = AsyncMock(return_value=False)
    requestor_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    await follow_service.request_follow(requestor_id, target_id, "player", "Alice")
    req_id = list(follow_service._pending_requests)[0]
    result = await follow_service.accept_follow(target_id, req_id)
    assert result["success"] is True
    assert follow_service.get_following(requestor_id) == (target_id, "player")
    assert follow_service.get_followers(target_id) == [requestor_id]
    assert req_id not in follow_service._pending_requests


@pytest.mark.asyncio
async def test_decline_follow_success(follow_service, user_manager):
    """Declining removes pending request and does not add follow."""
    user_manager.is_player_muted_async = AsyncMock(return_value=False)
    requestor_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    await follow_service.request_follow(requestor_id, target_id, "player", "Alice")
    req_id = list(follow_service._pending_requests)[0]
    result = await follow_service.decline_follow(target_id, req_id)
    assert result["success"] is True
    assert follow_service.get_following(requestor_id) is None
    assert req_id not in follow_service._pending_requests


@pytest.mark.asyncio
async def test_accept_follow_invalid_request_id(follow_service):
    """Accept with wrong or expired request_id returns error."""
    result = await follow_service.accept_follow(str(uuid.uuid4()), "no-such-id")
    assert result["success"] is False
    assert "invalid" in result["result"].lower() or "expired" in result["result"].lower()


# ---- unfollow ----
def test_unfollow_was_following(follow_service):
    """Unfollow when following returns success and clears state."""
    fid = str(uuid.uuid4())
    follow_service._follow_target[fid] = ("target_id", "player")
    result = follow_service.unfollow(fid)
    assert result["success"] is True
    assert "no longer following" in result["result"].lower()
    assert follow_service.get_following(fid) is None


def test_unfollow_was_not_following(follow_service):
    """Unfollow when not following returns friendly message."""
    result = follow_service.unfollow(str(uuid.uuid4()))
    assert result["success"] is True
    assert "weren't following" in result["result"].lower()


# ---- get_followers / get_following ----
def test_get_followers_empty(follow_service):
    """get_followers returns empty list when no followers."""
    assert follow_service.get_followers("any_id") == []


def test_get_followers_multiple(follow_service):
    """get_followers returns all follower ids for a target."""
    target_id = "target_1"
    follow_service._follow_target["f1"] = (target_id, "player")
    follow_service._follow_target["f2"] = (target_id, "player")
    follow_service._follow_target["f3"] = ("other", "player")
    assert set(follow_service.get_followers(target_id)) == {"f1", "f2"}


def test_get_following_none(follow_service):
    """get_following returns None when not following anyone."""
    assert follow_service.get_following(str(uuid.uuid4())) is None


def test_get_following_returns_tuple(follow_service):
    """get_following returns (target_id, target_type)."""
    fid = str(uuid.uuid4())
    follow_service._follow_target[fid] = ("npc_1", "npc")
    assert follow_service.get_following(fid) == ("npc_1", "npc")


# ---- movement propagation and auto-unfollow ----
@pytest.mark.asyncio
async def test_on_player_entered_room_moves_followers(follow_service, movement_service):
    """When followed player moves, followers are moved same from_room -> to_room."""
    leader_id = "leader_1"
    follower_id = "follower_1"
    follow_service._follow_target[follower_id] = (leader_id, "player")
    event = PlayerEnteredRoom(
        player_id=leader_id,
        room_id="room_b",
        from_room_id="room_a",
    )
    await follow_service._on_player_entered_room(event)
    movement_service.move_player.assert_called_once_with(follower_id, "room_a", "room_b")
    assert follow_service.get_following(follower_id) == (leader_id, "player")


@pytest.mark.asyncio
async def test_on_player_entered_room_move_failure_auto_unfollow(follow_service, movement_service):
    """When follower move fails, follower is auto-unfollowed and notified."""
    movement_service.move_player = AsyncMock(return_value=False)
    leader_id = "leader_1"
    follower_id = "follower_1"
    follow_service._follow_target[follower_id] = (leader_id, "player")
    event = PlayerEnteredRoom(
        player_id=leader_id,
        room_id="room_b",
        from_room_id="room_a",
    )
    await follow_service._on_player_entered_room(event)
    assert follow_service.get_following(follower_id) is None
    assert follow_service.get_followers(leader_id) == []


@pytest.mark.asyncio
async def test_on_npc_entered_room_moves_followers(follow_service, movement_service):
    """When followed NPC moves, followers are moved."""
    npc_id = "npc_1"
    follower_id = "follower_1"
    follow_service._follow_target[follower_id] = (npc_id, "npc")
    event = NPCEnteredRoom(
        npc_id=npc_id,
        room_id="room_b",
        from_room_id="room_a",
    )
    await follow_service._on_npc_entered_room(event)
    movement_service.move_player.assert_called_once_with(follower_id, "room_a", "room_b")


@pytest.mark.asyncio
async def test_on_player_entered_room_no_from_room_id_skips_propagation(follow_service, movement_service):
    """If from_room_id is None, no follower movement."""
    follow_service._follow_target["f1"] = ("leader_1", "player")
    event = PlayerEnteredRoom(
        player_id="leader_1",
        room_id="room_b",
        from_room_id=None,
    )
    await follow_service._on_player_entered_room(event)
    movement_service.move_player.assert_not_called()


# ---- get_following_display ----
@pytest.mark.asyncio
async def test_get_following_display_not_following(follow_service):
    """Display when not following anyone."""
    text = await follow_service.get_following_display(str(uuid.uuid4()))
    assert "not following anyone" in text
    assert "No one is following you" in text or "following you" in text.lower()


@pytest.mark.asyncio
async def test_get_following_display_following_npc(follow_service):
    """Display shows who you follow (NPC)."""
    fid = str(uuid.uuid4())
    follow_service._follow_target[fid] = ("npc_1", "npc")
    text = await follow_service.get_following_display(fid)
    assert "npc_1" in text
    assert "npc" in text


@pytest.mark.asyncio
async def test_get_following_display_following_player_resolves_name(follow_service):
    """When following a player, display uses resolved name from persistence, not UUID."""
    fid = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    follow_service._follow_target[fid] = (target_id, "player")
    mock_player = type("Player", (), {"name": "ArkanWolfshade"})()
    async_persistence = AsyncMock()
    async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    text = await follow_service.get_following_display(fid, async_persistence=async_persistence)
    assert "ArkanWolfshade" in text
    assert "player" in text
    assert target_id not in text


# ---- disconnect cleanup ----
def test_on_player_disconnect_clears_follow_state(follow_service):
    """Disconnect removes player from follow target and follower lists."""
    pid = str(uuid.uuid4())
    other = str(uuid.uuid4())
    follow_service._follow_target[pid] = ("target_1", "player")
    follow_service._follow_target[other] = (pid, "player")
    follow_service.on_player_disconnect(pid)
    assert pid not in follow_service._follow_target
    assert follow_service._follow_target.get(other) != (pid, "player")
    assert other not in follow_service._follow_target or follow_service._follow_target[other][0] != pid


@pytest.mark.asyncio
async def test_on_player_disconnect_cancels_pending_requests(follow_service, user_manager):
    """Disconnect cancels pending requests where player is requestor or target."""
    user_manager.is_player_muted_async = AsyncMock(return_value=False)
    requestor_id = str(uuid.uuid4())
    target_id = str(uuid.uuid4())
    await follow_service.request_follow(requestor_id, target_id, "player", "Alice")
    assert len(follow_service._pending_requests) >= 1
    follow_service.on_player_disconnect(target_id)
    assert len(follow_service._pending_requests) == 0


# ---- _ensure_follower_standing (auto-stand when following) ----
@pytest.mark.asyncio
async def test_ensure_follower_standing_already_standing(follow_service):
    """If follower is already standing, _ensure_follower_standing returns True."""
    fid = str(uuid.uuid4())
    result = await follow_service._ensure_follower_standing(fid)
    assert result is True


@pytest.mark.asyncio
async def test_ensure_follower_standing_sitting_stands(follow_service):
    """If follower is sitting and position service stands them, returns True."""
    fid = str(uuid.uuid4())
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(return_value={"position": "sitting"})
    mock_player.name = "Alice"
    follow_service._async_persistence = MagicMock()
    follow_service._async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    follow_service._player_position_service = MagicMock()
    follow_service._player_position_service.change_position = AsyncMock(
        return_value={"success": True, "position": "standing"}
    )
    result = await follow_service._ensure_follower_standing(fid)
    assert result is True
    follow_service._player_position_service.change_position.assert_called_once_with("Alice", "standing")


@pytest.mark.asyncio
async def test_ensure_follower_standing_fails_to_stand(follow_service):
    """If follower is prone and stand fails, returns False."""
    fid = str(uuid.uuid4())
    mock_player = MagicMock()
    mock_player.get_stats = MagicMock(return_value={"position": "lying"})
    mock_player.name = "Bob"
    follow_service._async_persistence = MagicMock()
    follow_service._async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    follow_service._player_position_service = MagicMock()
    follow_service._player_position_service.change_position = AsyncMock(
        return_value={"success": False, "message": "Cannot stand."}
    )
    result = await follow_service._ensure_follower_standing(fid)
    assert result is False


# ---- TTL constant ----
def test_follow_request_ttl_constant():
    """Pending requests use 60s TTL as per plan."""
    assert FOLLOW_REQUEST_TTL_SECONDS == 60
