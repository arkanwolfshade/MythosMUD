"""Unit tests for follow_movement helpers (coverage for extracted module)."""

# pyright: reportPrivateUsage=false
# Reason: Helpers intentionally take a host Protocol with private FollowService fields.
# pyright: reportAny=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
# Reason: MagicMock host/player fixtures; typing each access adds no safety.

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.events.event_types import NPCEnteredRoom
from server.game import follow_movement


def _host(**overrides: object) -> MagicMock:
    host: MagicMock = MagicMock()
    host._async_persistence = overrides.get("persistence", MagicMock())
    host._player_position_service = overrides.get("position_service", MagicMock())
    host._connection_manager = overrides.get("connection_manager", MagicMock())
    host._movement_service = overrides.get("movement_service", MagicMock())
    host._logger = MagicMock()
    host.get_followers = MagicMock(return_value=overrides.get("followers", []))
    host.unfollow = MagicMock(return_value={"success": True, "result": "ok"})
    host._send_result_to_player = MagicMock()
    host._send_follow_state_to_player = MagicMock()
    return host


def test_follower_needs_stand_rejects_non_string_position() -> None:
    player: MagicMock = MagicMock()
    player.get_stats = MagicMock(return_value={"position": 3})
    assert follow_movement.follower_needs_stand(player) is False


@pytest.mark.asyncio
async def test_stand_follower_no_position_service_returns_true() -> None:
    host = _host(position_service=None)
    player: MagicMock = MagicMock()
    player.name = "Alice"
    assert await follow_movement.stand_follower_for_move(host, str(uuid.uuid4()), player) is True


@pytest.mark.asyncio
async def test_ensure_follower_standing_swallows_lookup_errors() -> None:
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_id = AsyncMock(side_effect=ValueError("bad id"))
    host = _host(persistence=persistence)
    assert await follow_movement.ensure_follower_standing(host, "not-a-uuid") is True
    host._logger.warning.assert_called()


@pytest.mark.asyncio
async def test_follower_already_in_room_true_and_false() -> None:
    follower_id = str(uuid.uuid4())
    player: MagicMock = MagicMock()
    player.current_room_id = "room_b"
    persistence: MagicMock = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=player)
    host = _host(persistence=persistence)
    assert await follow_movement.follower_already_in_room(host, follower_id, "room_b") is True
    assert await follow_movement.follower_already_in_room(host, follower_id, "room_a") is False


@pytest.mark.asyncio
async def test_follower_already_in_room_missing_persistence() -> None:
    host = _host(persistence=None)
    assert await follow_movement.follower_already_in_room(host, str(uuid.uuid4()), "room_a") is False


@pytest.mark.asyncio
async def test_propagate_unfollow_when_cannot_stand() -> None:
    follower_id = str(uuid.uuid4())
    movement: MagicMock = MagicMock()
    movement.move_player = AsyncMock()
    host = _host(movement_service=movement)
    with patch("server.game.follow_movement.ensure_follower_standing", new_callable=AsyncMock) as ensure:
        ensure.return_value = False
        await follow_movement.propagate_follower_move(
            host,
            follower_id,
            "room_a",
            "room_b",
            log_extra={"target_id": "t1"},
            already_in_room_msg="already",
            move_failed_msg="failed",
            error_msg="error",
        )
    host.unfollow.assert_called_once_with(follower_id)
    movement.move_player.assert_not_called()


@pytest.mark.asyncio
async def test_propagate_skips_when_already_in_room() -> None:
    follower_id = str(uuid.uuid4())
    movement: MagicMock = MagicMock()
    movement.move_player = AsyncMock()
    host = _host(movement_service=movement)
    with (
        patch("server.game.follow_movement.ensure_follower_standing", new_callable=AsyncMock) as ensure,
        patch("server.game.follow_movement.follower_already_in_room", new_callable=AsyncMock) as already,
    ):
        ensure.return_value = True
        already.return_value = True
        await follow_movement.propagate_follower_move(
            host,
            follower_id,
            "room_a",
            "room_b",
            log_extra={},
            already_in_room_msg="already",
            move_failed_msg="failed",
            error_msg="error",
        )
    movement.move_player.assert_not_called()


@pytest.mark.asyncio
async def test_propagate_exception_drops_follower() -> None:
    follower_id = str(uuid.uuid4())
    movement: MagicMock = MagicMock()
    movement.move_player = AsyncMock(side_effect=RuntimeError("boom"))
    host = _host(movement_service=movement)
    with patch("server.game.follow_movement.ensure_follower_standing", new_callable=AsyncMock) as ensure:
        ensure.return_value = True
        with patch("server.game.follow_movement.follower_already_in_room", new_callable=AsyncMock) as already:
            already.return_value = False
            await follow_movement.propagate_follower_move(
                host,
                follower_id,
                "room_a",
                "room_b",
                log_extra={},
                already_in_room_msg="already",
                move_failed_msg="failed",
                error_msg="error",
            )
    host.unfollow.assert_called_once_with(follower_id)


@pytest.mark.asyncio
async def test_on_npc_entered_room_skips_without_movement_service() -> None:
    host = _host(movement_service=None, followers=["f1"])
    event = NPCEnteredRoom(npc_id="npc_1", room_id="room_b", from_room_id="room_a")
    await follow_movement.on_npc_entered_room(host, event)
    host.get_followers.assert_not_called()
