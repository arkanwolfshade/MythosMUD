"""Unit tests for application lifespan shutdown helpers."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.lifespan_shutdown import (
    _shutdown_connection_manager,
    _shutdown_event_bus,
    _shutdown_mythos_chronicle,
    _shutdown_mythos_tick_scheduler,
    _shutdown_nats_handler,
    _shutdown_task_registry,
    shutdown_services,
)


@pytest.fixture
def mock_app() -> FastAPI:
    app = MagicMock(spec=FastAPI)
    app.state = MagicMock()
    return app


@pytest.fixture
def mock_container() -> MagicMock:
    container = MagicMock()
    container.task_registry = MagicMock()
    container.event_bus = MagicMock()
    container.shutdown = AsyncMock()
    return container


@pytest.mark.asyncio
async def test_shutdown_mythos_chronicle_success() -> None:
    frozen = MagicMock()
    frozen.real_timestamp.isoformat.return_value = "2026-01-01T00:00:00"
    frozen.mythos_timestamp.isoformat.return_value = "1926-01-01T00:00:00"
    chronicle = MagicMock()
    chronicle.freeze.return_value = frozen
    with patch("server.app.lifespan_shutdown.get_mythos_chronicle", return_value=chronicle):
        await _shutdown_mythos_chronicle()
    chronicle.freeze.assert_called_once()


@pytest.mark.asyncio
async def test_shutdown_mythos_chronicle_handles_error() -> None:
    with patch("server.app.lifespan_shutdown.get_mythos_chronicle", side_effect=RuntimeError("fail")):
        await _shutdown_mythos_chronicle()


@pytest.mark.asyncio
async def test_shutdown_nats_handler_from_container(mock_app: FastAPI) -> None:
    handler = MagicMock()
    handler.stop = AsyncMock()
    mock_app.state.container = MagicMock(nats_message_handler=handler)
    await _shutdown_nats_handler(mock_app)
    handler.stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_nats_handler_from_app_state(mock_app: FastAPI) -> None:
    handler = MagicMock()
    handler.stop = AsyncMock()
    mock_app.state.container = None
    mock_app.state.nats_message_handler = handler
    await _shutdown_nats_handler(mock_app)
    handler.stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_nats_handler_missing(mock_app: FastAPI) -> None:
    mock_app.state.container = None
    del mock_app.state.nats_message_handler
    await _shutdown_nats_handler(mock_app)


@pytest.mark.asyncio
async def test_shutdown_connection_manager(mock_app: FastAPI) -> None:
    cm = MagicMock()
    cm.force_cleanup = AsyncMock()
    mock_app.state.container = MagicMock(connection_manager=cm)
    await _shutdown_connection_manager(mock_app)
    cm.stop_health_checks.assert_called_once()
    cm.force_cleanup.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_connection_manager_handles_errors(mock_app: FastAPI) -> None:
    cm = MagicMock()
    cm.stop_health_checks.side_effect = RuntimeError("health")
    cm.force_cleanup = AsyncMock(side_effect=RuntimeError("cleanup"))
    mock_app.state.container = MagicMock(connection_manager=cm)
    await _shutdown_connection_manager(mock_app)


@pytest.mark.asyncio
async def test_shutdown_mythos_tick_scheduler(mock_app: FastAPI) -> None:
    scheduler = MagicMock()
    scheduler.stop = AsyncMock()
    mock_app.state.container = MagicMock(mythos_tick_scheduler=scheduler)
    await _shutdown_mythos_tick_scheduler(mock_app)
    scheduler.stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_task_registry_success(mock_container: MagicMock) -> None:
    mock_container.task_registry.shutdown_all = AsyncMock(return_value=True)
    await _shutdown_task_registry(mock_container)
    mock_container.task_registry.shutdown_all.assert_awaited_once_with(timeout=5.0)


@pytest.mark.asyncio
async def test_shutdown_task_registry_timeout(mock_container: MagicMock) -> None:
    mock_container.task_registry.shutdown_all = AsyncMock(return_value=False)
    await _shutdown_task_registry(mock_container)


@pytest.mark.asyncio
async def test_shutdown_task_registry_missing(mock_container: MagicMock) -> None:
    mock_container.task_registry = None
    await _shutdown_task_registry(mock_container)


@pytest.mark.asyncio
async def test_shutdown_event_bus(mock_container: MagicMock) -> None:
    mock_container.event_bus.get_subscriber_stats.return_value = {
        "total_subscribers": 2,
        "services_tracked": 1,
    }
    mock_container.event_bus.shutdown = AsyncMock()
    await _shutdown_event_bus(mock_container)
    mock_container.event_bus.shutdown.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_event_bus_missing(mock_container: MagicMock) -> None:
    mock_container.event_bus = None
    await _shutdown_event_bus(mock_container)


@pytest.mark.asyncio
async def test_shutdown_services_orchestrates_all(mock_app: FastAPI, mock_container: MagicMock) -> None:
    with (
        patch("server.app.lifespan_shutdown._shutdown_mythos_chronicle", new_callable=AsyncMock) as chronicle,
        patch("server.app.lifespan_shutdown._shutdown_nats_handler", new_callable=AsyncMock) as nats,
        patch("server.app.lifespan_shutdown._shutdown_connection_manager", new_callable=AsyncMock) as conn,
        patch("server.app.lifespan_shutdown._shutdown_mythos_tick_scheduler", new_callable=AsyncMock) as tick,
        patch("server.app.lifespan_shutdown._shutdown_task_registry", new_callable=AsyncMock) as tasks,
        patch("server.app.lifespan_shutdown._shutdown_event_bus", new_callable=AsyncMock) as bus,
    ):
        await shutdown_services(mock_app, mock_container)

    chronicle.assert_awaited_once()
    nats.assert_awaited_once_with(mock_app)
    conn.assert_awaited_once_with(mock_app)
    tick.assert_awaited_once_with(mock_app)
    tasks.assert_awaited_once_with(mock_container)
    bus.assert_awaited_once_with(mock_container)
    mock_container.shutdown.assert_awaited_once()
