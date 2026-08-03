"""Unit tests for connection_error_methods delegation wrappers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.connection_error_methods import (
    detect_and_handle_error_state_impl,
    handle_authentication_error_impl,
    handle_security_violation_impl,
    handle_websocket_error_impl,
    recover_from_error_impl,
)


@pytest.fixture
def manager() -> MagicMock:
    mgr = MagicMock()
    mgr.error_handler = MagicMock()
    mgr.error_handler.detect_and_handle_error_state = AsyncMock(return_value={"success": True})
    mgr.error_handler.handle_websocket_error = AsyncMock(return_value={"success": True})
    mgr.error_handler.handle_authentication_error = AsyncMock(return_value={"success": True})
    mgr.error_handler.handle_security_violation = AsyncMock(return_value={"success": True})
    mgr.error_handler.recover_from_error = AsyncMock(return_value={"success": True})
    return mgr


@pytest.mark.asyncio
async def test_detect_and_handle_error_state_impl_delegates(manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    result = await detect_and_handle_error_state_impl(manager, player_id, "MINOR", "detail", "conn-1")
    assert result["success"] is True
    manager.error_handler.detect_and_handle_error_state.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_websocket_error_impl_delegates(manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    await handle_websocket_error_impl(manager, player_id, "conn-1", "PROTOCOL", "bad frame")
    manager.error_handler.handle_websocket_error.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_authentication_error_impl_delegates(manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    await handle_authentication_error_impl(manager, player_id, "TOKEN", "expired")
    manager.error_handler.handle_authentication_error.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_security_violation_impl_delegates(manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    await handle_security_violation_impl(manager, player_id, "INJECTION", "payload")
    manager.error_handler.handle_security_violation.assert_awaited_once()


@pytest.mark.asyncio
async def test_recover_from_error_impl_delegates(manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    await recover_from_error_impl(manager, player_id, recovery_type="FULL")
    manager.error_handler.recover_from_error.assert_awaited_once()


@pytest.mark.asyncio
async def test_error_impl_returns_default_when_handler_missing() -> None:
    manager = MagicMock()
    manager.error_handler = None
    player_id = uuid.uuid4()
    result = await detect_and_handle_error_state_impl(manager, player_id, "MINOR", "detail")
    assert result["success"] is False
    assert "Error handler not initialized" in result["errors"]
