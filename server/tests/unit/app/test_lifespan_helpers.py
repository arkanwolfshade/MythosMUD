"""Unit tests for lifespan helper functions."""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally exercise lifespan private helpers.
# pyright: reportAny=false, reportUnknownMemberType=false, reportUnknownArgumentType=false
# Reason: MagicMock attribute chains are typed Any by unittest.mock; typed locals alone do not erase that.
# pyright: reportUnknownVariableType=false
# Reason: Follows from MagicMock fixture usage in assertions.

from __future__ import annotations

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pytest import MonkeyPatch

from server.app.lifespan import (
    _calculate_metrics_delta,
    _cleanup_container_on_error,
    _cleanup_dead_letter_queue_periodically,
    _persist_metrics_to_file,
    _persist_mythos_state_on_error,
)


def _close_registered_coro(coro: object, *_args: object, **_kwargs: object) -> MagicMock:
    """MagicMock register_task stand-in: close the coro so it is not left unawaited."""
    close = getattr(coro, "close", None)
    if callable(close):
        try:
            _ = close()
        except (RuntimeError, TypeError, AttributeError):
            pass
    return MagicMock()


def _mock_task_registry() -> MagicMock:
    registry: MagicMock = MagicMock()
    register_task: MagicMock = MagicMock(side_effect=_close_registered_coro)
    registry.register_task = register_task
    return registry


def test_calculate_metrics_delta_no_startup() -> None:
    assert _calculate_metrics_delta({"connection": {}}, None) == {}


def test_calculate_metrics_delta_connection_keys() -> None:
    startup = {"connection": {"closed_websockets_count": 1, "active_websockets_count": 5}}
    shutdown = {"connection": {"closed_websockets_count": 3, "active_websockets_count": 2}}
    delta = _calculate_metrics_delta(shutdown, startup)
    assert delta["connection"]["closed_websockets_count"] == 2
    assert delta["connection"]["active_websockets_count"] == -3


def test_persist_metrics_to_file_writes_json(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    _persist_metrics_to_file({"a": 1}, {"b": 2}, {"delta": 1}, [])
    metrics_file = tmp_path / "logs" / "local" / "memory_leak_metrics.json"
    assert metrics_file.exists()
    assert b"delta" in metrics_file.read_bytes()


def test_persist_mythos_state_on_error_handles_failure() -> None:
    with patch("server.app.lifespan.get_mythos_chronicle", side_effect=RuntimeError("fail")):
        _persist_mythos_state_on_error()


@pytest.mark.asyncio
async def test_cleanup_container_on_error_with_container() -> None:
    container: MagicMock = MagicMock()
    shutdown: AsyncMock = AsyncMock()
    container.shutdown = shutdown
    await _cleanup_container_on_error(container)
    shutdown.assert_awaited_once()


@pytest.mark.asyncio
async def test_cleanup_container_on_error_none() -> None:
    await _cleanup_container_on_error(None)


@pytest.mark.asyncio
async def test_cleanup_dead_letter_queue_periodically_runs_cleanup() -> None:
    """Each wake-up should invoke cleanup_old_messages via to_thread; cancellation re-raises."""
    mock_dlq: MagicMock = MagicMock()
    cleanup_old_messages: MagicMock = MagicMock(return_value=3)
    mock_dlq.cleanup_old_messages = cleanup_old_messages

    call_count = 0

    async def fake_sleep(_seconds: float) -> None:
        nonlocal call_count
        call_count += 1
        if call_count > 1:
            raise asyncio.CancelledError()

    with patch("server.app.lifespan.asyncio.sleep", new=fake_sleep):
        with pytest.raises(asyncio.CancelledError):
            await _cleanup_dead_letter_queue_periodically(mock_dlq, interval_seconds=0)

    cleanup_old_messages.assert_called_once()


@pytest.mark.asyncio
async def test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors() -> None:
    """A failing cleanup run must be logged and not crash/raise out of the periodic task."""
    mock_dlq: MagicMock = MagicMock()
    cleanup_old_messages: MagicMock = MagicMock(side_effect=RuntimeError("disk error"))
    mock_dlq.cleanup_old_messages = cleanup_old_messages

    async def fake_sleep(_seconds: float) -> None:
        return None

    with patch("server.app.lifespan.asyncio.sleep", new=fake_sleep):
        await _cleanup_dead_letter_queue_periodically(mock_dlq, interval_seconds=0)

    cleanup_old_messages.assert_called_once()


@pytest.mark.asyncio
async def test_initialize_enhanced_systems() -> None:
    from server.app.lifespan import _initialize_enhanced_systems

    mock_aggregator: MagicMock = MagicMock()
    with (
        patch("server.app.lifespan.get_performance_monitor"),
        patch("server.app.lifespan.get_exception_tracker"),
        patch("server.app.lifespan.get_monitoring_dashboard"),
        patch("server.app.lifespan.get_log_aggregator", return_value=mock_aggregator),
    ):
        result = await _initialize_enhanced_systems()
    assert result is mock_aggregator


@pytest.mark.asyncio
async def test_startup_application_minimal() -> None:
    from server.app.lifespan import _startup_application

    mock_app: MagicMock = MagicMock()
    mock_app.state = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.event_bus = MagicMock()
    task_registry = _mock_task_registry()
    mock_container.task_registry = task_registry
    mock_container.mythos_tick_scheduler = None
    mock_container.nats_message_handler = None
    mock_container.initialize = AsyncMock()
    mock_container.player_service = MagicMock()

    with (
        patch("server.app.lifespan.ApplicationContainer", return_value=mock_container),
        patch("server.app.lifespan.set_auth_epoch"),
        patch("server.app.lifespan.initialize_container_and_legacy_services", new=AsyncMock()),
        patch("server.app.lifespan.setup_connection_manager", new=AsyncMock()),
        patch("server.app.lifespan.initialize_npc_startup_spawning", new=AsyncMock()),
        patch("server.app.lifespan.update_logging_with_player_service"),
        patch("server.app.lifespan.game_tick_loop", return_value=AsyncMock()),
    ):
        result = await _startup_application(mock_app)
    assert result is mock_container
    # nats_message_handler is None (NATS disabled) -> no dlq_cleanup task registered
    register_task: MagicMock = task_registry.register_task
    registered_task_names = [call.args[1] for call in register_task.call_args_list]
    assert "lifecycle/dlq_cleanup" not in registered_task_names


@pytest.mark.asyncio
async def test_startup_application_registers_dlq_cleanup_when_nats_available() -> None:
    from server.app.lifespan import _startup_application

    mock_app: MagicMock = MagicMock()
    mock_app.state = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.event_bus = MagicMock()
    task_registry = _mock_task_registry()
    mock_container.task_registry = task_registry
    mock_container.mythos_tick_scheduler = None
    mock_container.nats_message_handler = MagicMock()
    mock_container.initialize = AsyncMock()
    mock_container.player_service = MagicMock()

    with (
        patch("server.app.lifespan.ApplicationContainer", return_value=mock_container),
        patch("server.app.lifespan.set_auth_epoch"),
        patch("server.app.lifespan.initialize_container_and_legacy_services", new=AsyncMock()),
        patch("server.app.lifespan.setup_connection_manager", new=AsyncMock()),
        patch("server.app.lifespan.initialize_npc_startup_spawning", new=AsyncMock()),
        patch("server.app.lifespan.update_logging_with_player_service"),
        patch("server.app.lifespan.game_tick_loop", return_value=AsyncMock()),
    ):
        _ = await _startup_application(mock_app)
    register_task: MagicMock = task_registry.register_task
    registered_task_names = [call.args[1] for call in register_task.call_args_list]
    assert "lifecycle/dlq_cleanup" in registered_task_names


@pytest.mark.asyncio
async def test_shutdown_with_error_handling() -> None:
    from server.app.lifespan import _shutdown_with_error_handling

    mock_app: MagicMock = MagicMock()
    mock_collector: MagicMock = MagicMock()
    collect_all_metrics: MagicMock = MagicMock(return_value={"connection": {"active_websockets_count": 0}})
    check_alerts: MagicMock = MagicMock(return_value=[])
    mock_collector.collect_all_metrics = collect_all_metrics
    mock_collector.check_alerts = check_alerts
    # #679: collector is container-owned, not a module-level global
    mock_container: MagicMock = MagicMock(memory_leak_collector=mock_collector)

    with (
        patch("server.app.lifespan._startup_metrics", {"connection": {"active_websockets_count": 0}}),
        patch("server.app.lifespan._persist_metrics_to_file"),
        patch("server.app.lifespan.shutdown_services", new=AsyncMock()),
    ):
        await _shutdown_with_error_handling(mock_app, mock_container)


def test_persist_mythos_state_on_error_success() -> None:
    mock_chronicle: MagicMock = MagicMock()
    freeze: MagicMock = MagicMock()
    mock_chronicle.freeze = freeze
    with patch("server.app.lifespan.get_mythos_chronicle", return_value=mock_chronicle):
        _persist_mythos_state_on_error()
    freeze.assert_called_once()


@pytest.mark.asyncio
async def test_lifespan_happy_path() -> None:
    from server.app.lifespan import lifespan

    mock_app: MagicMock = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_aggregator: MagicMock = MagicMock()
    shutdown: MagicMock = MagicMock()
    mock_aggregator.shutdown = shutdown

    with (
        patch("server.app.lifespan._initialize_enhanced_systems", new=AsyncMock(return_value=mock_aggregator)),
        patch("server.app.lifespan._startup_application", new=AsyncMock(return_value=mock_container)),
        patch("server.app.lifespan._shutdown_with_error_handling", new=AsyncMock()),
    ):
        async with lifespan(mock_app):
            pass

    shutdown.assert_called_once()
