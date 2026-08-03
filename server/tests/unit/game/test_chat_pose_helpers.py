"""Unit tests for chat pose helpers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.chat_pose_helpers import (
    clear_player_pose,
    get_player_pose,
    get_room_poses,
    normalize_player_id,
    set_player_pose,
)


def test_normalize_player_id():
    uid = uuid.uuid4()
    assert normalize_player_id(uid) == str(uid)


@pytest.mark.asyncio
async def test_set_player_pose_empty():
    result = await set_player_pose(uuid.uuid4(), "  ", MagicMock(), MagicMock(), MagicMock(), None)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_set_player_pose_too_long():
    result = await set_player_pose(uuid.uuid4(), "x" * 101, MagicMock(), MagicMock(), MagicMock(), None)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_set_player_pose_player_not_found():
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=None)
    result = await set_player_pose(uuid.uuid4(), "leaning", player_service, MagicMock(), MagicMock(), None)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_set_player_pose_no_room():
    player = MagicMock(current_room_id=None)
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=player)
    result = await set_player_pose(uuid.uuid4(), "leaning", player_service, MagicMock(), MagicMock(), None)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_set_player_pose_success():
    player = MagicMock(name="Armitage", current_room_id="room-1")
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=player)
    pose_manager = MagicMock()
    with patch("server.game.chat_pose_helpers.publish_chat_message_to_nats", new_callable=AsyncMock) as mock_pub:
        mock_pub.return_value = True
        result = await set_player_pose(uuid.uuid4(), "  reading  ", player_service, pose_manager, MagicMock(), None)
    assert result["success"] is True
    pose_manager.set_pose.assert_called_once()
    mock_pub.assert_awaited_once()


@pytest.mark.asyncio
async def test_set_player_pose_nats_failure():
    player = MagicMock(name="Armitage", current_room_id="room-1")
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=player)
    with patch("server.game.chat_pose_helpers.publish_chat_message_to_nats", new_callable=AsyncMock) as mock_pub:
        mock_pub.return_value = False
        result = await set_player_pose(uuid.uuid4(), "reading", player_service, MagicMock(), MagicMock(), None)
    assert result["success"] is False


def _player(name: str = "Armitage"):
    p = MagicMock()
    p.name = name
    return p


def test_get_and_clear_player_pose():
    pose_manager = MagicMock()
    pose_manager.get_pose.return_value = "reading"
    pose_manager.clear_pose.return_value = True
    uid = uuid.uuid4()
    assert get_player_pose(uid, pose_manager) == "reading"
    assert clear_player_pose(uid, pose_manager) is True


@pytest.mark.asyncio
async def test_get_room_poses():
    pose_manager = MagicMock()
    pose_manager.get_pose.side_effect = lambda pid: "posing" if pid == "p1" else None
    room_service = MagicMock()
    room_service.get_room_occupants = AsyncMock(return_value=["p1", "p2"])
    player_service = MagicMock()
    player_service.get_player_by_id = AsyncMock(return_value=_player("Armitage"))
    poses = await get_room_poses("room-1", room_service, player_service, pose_manager)
    assert poses == {"Armitage": "posing"}
