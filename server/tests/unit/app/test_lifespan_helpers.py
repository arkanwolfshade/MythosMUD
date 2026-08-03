"""Unit tests for lifespan helper functions."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.lifespan import (
    _calculate_metrics_delta,
    _cleanup_container_on_error,
    _persist_metrics_to_file,
    _persist_mythos_state_on_error,
)


def test_calculate_metrics_delta_no_startup() -> None:
    assert _calculate_metrics_delta({"connection": {}}, None) == {}


def test_calculate_metrics_delta_connection_keys() -> None:
    startup = {"connection": {"closed_websockets_count": 1, "active_websockets_count": 5}}
    shutdown = {"connection": {"closed_websockets_count": 3, "active_websockets_count": 2}}
    delta = _calculate_metrics_delta(shutdown, startup)
    assert delta["connection"]["closed_websockets_count"] == 2
    assert delta["connection"]["active_websockets_count"] == -3


def test_persist_metrics_to_file_writes_json(tmp_path, monkeypatch) -> None:
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
    container = MagicMock()
    container.shutdown = AsyncMock()
    await _cleanup_container_on_error(container)
    container.shutdown.assert_awaited_once()


@pytest.mark.asyncio
async def test_cleanup_container_on_error_none() -> None:
    await _cleanup_container_on_error(None)


@pytest.mark.asyncio
async def test_initialize_enhanced_systems() -> None:
    from server.app.lifespan import _initialize_enhanced_systems

    mock_aggregator = MagicMock()
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

    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.event_bus = MagicMock()
    mock_container.task_registry = MagicMock()
    mock_container.mythos_tick_scheduler = None
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


@pytest.mark.asyncio
async def test_shutdown_with_error_handling() -> None:
    from server.app.lifespan import _shutdown_with_error_handling

    mock_app = MagicMock()
    mock_container = MagicMock()
    mock_collector = MagicMock()
    mock_collector.collect_all_metrics.return_value = {"connection": {"active_websockets_count": 0}}
    mock_collector.check_alerts.return_value = []

    with (
        patch("server.app.lifespan._metrics_collector", mock_collector),
        patch("server.app.lifespan._startup_metrics", {"connection": {"active_websockets_count": 0}}),
        patch("server.app.lifespan._persist_metrics_to_file"),
        patch("server.app.lifespan.shutdown_services", new=AsyncMock()),
    ):
        await _shutdown_with_error_handling(mock_app, mock_container)


def test_persist_mythos_state_on_error_success() -> None:
    mock_chronicle = MagicMock()
    with patch("server.app.lifespan.get_mythos_chronicle", return_value=mock_chronicle):
        _persist_mythos_state_on_error()
    mock_chronicle.freeze.assert_called_once()


@pytest.mark.asyncio
async def test_lifespan_happy_path() -> None:
    from server.app.lifespan import lifespan

    mock_app = MagicMock()
    mock_container = MagicMock()
    mock_aggregator = MagicMock()

    with (
        patch("server.app.lifespan._initialize_enhanced_systems", new=AsyncMock(return_value=mock_aggregator)),
        patch("server.app.lifespan._startup_application", new=AsyncMock(return_value=mock_container)),
        patch("server.app.lifespan._shutdown_with_error_handling", new=AsyncMock()),
    ):
        async with lifespan(mock_app):
            pass

    mock_aggregator.shutdown.assert_called_once()
