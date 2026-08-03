"""Unit tests for lucidity trigger handlers."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services import lucidity_trigger_handlers as handlers
from server.services.lucidity_trigger_handlers import (
    handle_catatonia_transitions,
    handle_delirium_and_sanitarium_triggers,
    handle_delirium_trigger,
    handle_sanitarium_trigger,
)


@pytest.fixture
def player_id() -> uuid.UUID:
    return uuid.uuid4()


@pytest.fixture
def lucidity_record() -> MagicMock:
    record = MagicMock()
    record.catatonia_entered_at = None
    return record


@pytest.mark.asyncio
async def test_handle_catatonia_transitions_enters_catatonia(lucidity_record: MagicMock, player_id: uuid.UUID) -> None:
    observer = MagicMock()
    with patch("server.services.lucidity_trigger_handlers.send_catatonia_event", new=AsyncMock()) as send_event:
        await handle_catatonia_transitions(
            record=lucidity_record,
            player_id=player_id,
            new_tier="catatonic",
            previous_tier="disturbed",
            new_lcd=0,
            catatonia_observer=observer,
        )
    assert lucidity_record.catatonia_entered_at is not None
    observer.on_catatonia_entered.assert_called_once()
    send_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_catatonia_transitions_resolves_catatonia(
    lucidity_record: MagicMock, player_id: uuid.UUID
) -> None:
    lucidity_record.catatonia_entered_at = datetime.now(UTC)
    observer = MagicMock()
    with patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()) as send_event:
        await handle_catatonia_transitions(
            record=lucidity_record,
            player_id=player_id,
            new_tier="lucid",
            previous_tier="catatonic",
            new_lcd=20,
            catatonia_observer=observer,
        )
    assert lucidity_record.catatonia_entered_at is None
    observer.on_catatonia_cleared.assert_called_once()
    send_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_delirium_trigger_sends_event(player_id: uuid.UUID) -> None:
    handlers._last_delirium_trigger.clear()
    with patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()) as send_event:
        await handle_delirium_trigger(player_id, new_lcd=-11, previous_lcd=0)
    send_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_delirium_trigger_skips_when_not_crossing_threshold(player_id: uuid.UUID) -> None:
    with patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()) as send_event:
        await handle_delirium_trigger(player_id, new_lcd=-5, previous_lcd=0)
    send_event.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_delirium_trigger_debounced(player_id: uuid.UUID) -> None:
    handlers._last_delirium_trigger.clear()
    handlers._last_delirium_trigger[str(player_id)] = datetime.now(UTC)
    with patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()) as send_event:
        await handle_delirium_trigger(player_id, new_lcd=-11, previous_lcd=0)
    send_event.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_sanitarium_trigger_invokes_observer(player_id: uuid.UUID) -> None:
    observer = MagicMock()
    observer.should_trigger_sanitarium_failover.return_value = True
    with patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()) as send_event:
        await handle_sanitarium_trigger(player_id, new_lcd=-101, previous_lcd=-50, catatonia_observer=observer)
    observer.on_sanitarium_failover.assert_called_once()
    send_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_sanitarium_trigger_skips_without_observer(player_id: uuid.UUID) -> None:
    with patch("server.services.lucidity_trigger_handlers.send_rescue_update_event", new=AsyncMock()) as send_event:
        await handle_sanitarium_trigger(player_id, new_lcd=-101, previous_lcd=-50, catatonia_observer=None)
    send_event.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_delirium_and_sanitarium_triggers_combined(player_id: uuid.UUID) -> None:
    handlers._last_delirium_trigger.clear()
    observer = MagicMock()
    observer.should_trigger_sanitarium_failover.return_value = False
    with (
        patch("server.services.lucidity_trigger_handlers.handle_delirium_trigger", new=AsyncMock()) as delirium,
        patch("server.services.lucidity_trigger_handlers.handle_sanitarium_trigger", new=AsyncMock()) as sanitarium,
    ):
        await handle_delirium_and_sanitarium_triggers(player_id, -101, -50, observer)
    delirium.assert_awaited_once()
    sanitarium.assert_awaited_once()
