"""Unit tests for the admin hallucinate command (#714)."""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import admin_hallucinate_command as cmd


def test_extract_args_from_fields() -> None:
    target, htype = cmd.extract_args({"target_player": "Alice", "hallucination_type": "phantom"})
    assert target == "Alice"
    assert htype == "phantom"


def test_extract_args_from_args_list() -> None:
    target, htype = cmd.extract_args({"args": ["Bob", "overlay"]})
    assert target == "Bob"
    assert htype == "overlay"


async def _async_session_gen(session: AsyncMock):
    yield session


@pytest.mark.asyncio
async def test_get_current_lcd_or_error_raises_when_session_unavailable() -> None:
    """#714: an empty session generator raises HallucinateCommandError, not a bare None."""

    async def empty_gen():
        for _ in ():  # loop never runs; keeps this a reachable (not statically-dead) async generator
            yield None

    with patch.object(cmd, "get_async_session", return_value=empty_gen()):
        with pytest.raises(cmd.HallucinateCommandError) as exc_info:
            _ = await cmd.get_current_lcd_or_error(uuid.uuid4())
    assert "Database session could not be established" in exc_info.value.result["result"]


@pytest.mark.asyncio
async def test_resolve_hallucinate_target_raises_when_current_player_not_found() -> None:
    """#714: check_admin_permissions returning (None, None) still surfaces a clear error."""
    player_service = MagicMock()
    with (
        patch.object(cmd, "get_player_service_from_app", return_value=player_service),
        patch.object(cmd, "check_admin_permissions", AsyncMock(return_value=(None, None))),
    ):
        with pytest.raises(cmd.HallucinateCommandError) as exc_info:
            _ = await cmd.resolve_hallucinate_target(MagicMock(), "Admin", "Alice")
    assert exc_info.value.result["result"] == "Current player not found."


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_missing_app() -> None:
    result = await cmd._handle_admin_hallucinate_command({}, {}, None, None, "Admin")
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_missing_args() -> None:
    request = MagicMock()
    request.app = MagicMock()
    result = await cmd._handle_admin_hallucinate_command({}, {}, request, None, "Admin")
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_invalid_type() -> None:
    request = MagicMock()
    request.app = MagicMock()
    result = await cmd._handle_admin_hallucinate_command(
        {"target_player": "Alice", "hallucination_type": "nonsense"}, {}, request, None, "Admin"
    )
    assert "Unknown hallucination type" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_no_player_service() -> None:
    request = MagicMock()
    request.app = MagicMock()
    with patch.object(cmd, "get_player_service_from_app", return_value=None):
        result = await cmd._handle_admin_hallucinate_command(
            {"target_player": "Alice", "hallucination_type": "phantom"}, {}, request, None, "Admin"
        )
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_permission_denied() -> None:
    request = MagicMock()
    request.app = MagicMock()
    with (
        patch.object(cmd, "get_player_service_from_app", return_value=MagicMock()),
        patch.object(cmd, "check_admin_permissions", AsyncMock(return_value=(None, {"result": "not admin"}))),
    ):
        result = await cmd._handle_admin_hallucinate_command(
            {"target_player": "Alice", "hallucination_type": "phantom"}, {}, request, None, "Admin"
        )
    assert result["result"] == "not admin"


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_target_not_found() -> None:
    request = MagicMock()
    request.app = MagicMock()
    with (
        patch.object(cmd, "get_player_service_from_app", return_value=MagicMock()),
        patch.object(cmd, "check_admin_permissions", AsyncMock(return_value=(MagicMock(), None))),
        patch.object(cmd, "resolve_target_player", AsyncMock(return_value=(None, {"result": "not found"}))),
    ):
        result = await cmd._handle_admin_hallucinate_command(
            {"target_player": "Ghost", "hallucination_type": "phantom"}, {}, request, None, "Admin"
        )
    assert result["result"] == "not found"


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_target_no_room() -> None:
    request = MagicMock()
    request.app = MagicMock()
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=MagicMock(current_room_id=None))
    with (
        patch.object(cmd, "get_player_service_from_app", return_value=player_service),
        patch.object(cmd, "check_admin_permissions", AsyncMock(return_value=(MagicMock(), None))),
        patch.object(cmd, "resolve_target_player", AsyncMock(return_value=(uuid.uuid4(), None))),
    ):
        result = await cmd._handle_admin_hallucinate_command(
            {"target_player": "Alice", "hallucination_type": "phantom"}, {}, request, None, "Admin"
        )
    assert "not currently in a room" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_delivers_phantom() -> None:
    request = MagicMock()
    request.app = MagicMock()
    target_id = uuid.uuid4()
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=MagicMock(current_room_id="room-a"))
    session = AsyncMock()
    with (
        patch.object(cmd, "get_player_service_from_app", return_value=player_service),
        patch.object(cmd, "check_admin_permissions", AsyncMock(return_value=(MagicMock(), None))),
        patch.object(cmd, "resolve_target_player", AsyncMock(return_value=(target_id, None))),
        patch.object(cmd, "get_async_session", return_value=_async_session_gen(session)),
        patch.object(cmd, "get_current_lcd", AsyncMock(return_value=25)),
        patch.object(cmd, "deliver_forced_hallucination", AsyncMock()) as deliver,
        patch.object(cmd, "get_admin_actions_logger") as log_cls,
    ):
        cast(MagicMock, log_cls.return_value).log_admin_command = MagicMock()
        result = await cmd._handle_admin_hallucinate_command(
            {"target_player": "Alice", "hallucination_type": "phantom"}, {}, request, None, "Admin"
        )
    assert "Forced 'phantom' hallucination on Alice" in result["result"]
    deliver.assert_awaited_once_with("phantom", target_id, "room-a", "fractured", 25)


@pytest.mark.asyncio
async def test_handle_admin_hallucinate_delivery_error() -> None:
    request = MagicMock()
    request.app = MagicMock()
    target_id = uuid.uuid4()
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=MagicMock(current_room_id="room-a"))
    session = AsyncMock()
    with (
        patch.object(cmd, "get_player_service_from_app", return_value=player_service),
        patch.object(cmd, "check_admin_permissions", AsyncMock(return_value=(MagicMock(), None))),
        patch.object(cmd, "resolve_target_player", AsyncMock(return_value=(target_id, None))),
        patch.object(cmd, "get_async_session", return_value=_async_session_gen(session)),
        patch.object(cmd, "get_current_lcd", AsyncMock(return_value=50)),
        patch.object(cmd, "deliver_forced_hallucination", AsyncMock(side_effect=RuntimeError("boom"))),
    ):
        result = await cmd._handle_admin_hallucinate_command(
            {"target_player": "Alice", "hallucination_type": "overlay"}, {}, request, None, "Admin"
        )
    assert "Error forcing hallucination" in result["result"]


@pytest.mark.asyncio
async def test_deliver_forced_hallucination_phantom() -> None:
    with patch(
        "server.services.passive_lucidity_flux.hallucinations.handle_phantom_hostile_hallucination",
        new_callable=AsyncMock,
    ) as handler:
        await cmd.deliver_forced_hallucination("phantom", uuid.uuid4(), "room-a", "deranged", -50)
    handler.assert_awaited_once()


@pytest.mark.asyncio
async def test_deliver_forced_hallucination_overlay() -> None:
    with patch(
        "server.services.passive_lucidity_flux.hallucinations.handle_room_text_overlay_hallucination",
        new_callable=AsyncMock,
    ) as handler:
        await cmd.deliver_forced_hallucination("overlay", uuid.uuid4(), "room-a", "fractured", -20)
    handler.assert_awaited_once()


@pytest.mark.asyncio
async def test_deliver_forced_hallucination_fake_tell() -> None:
    player_id = uuid.uuid4()
    with (
        patch("server.services.fake_hallucination_service.FakeHallucinationService") as svc_cls,
        patch("server.game.chat_npc_system.deliver_fake_npc_whisper", new_callable=AsyncMock) as deliver,
        patch("server.services.fake_sender_registry.fake_sender_registry.record_fake_whisper") as record,
        patch("server.services.lucidity_event_dispatcher.send_hallucination_event", new_callable=AsyncMock) as send,
    ):
        svc = cast(MagicMock, svc_cls.return_value)
        cast(MagicMock, svc.generate_fake_npc_tell).return_value = {
            "npc_name": "Ghost",
            "message": "Boo.",
            "room_id": "room-a",
            "hallucination_id": "h1",
        }
        await cmd.deliver_forced_hallucination("fake_tell", player_id, "room-a", "fractured", -20)
    deliver.assert_awaited_once_with(player_id, "Ghost", "Boo.")
    record.assert_called_once_with(player_id, "Ghost")
    send.assert_awaited_once()
    assert send.await_args is not None
    assert send.await_args.kwargs["metadata"]["forced"] is True
