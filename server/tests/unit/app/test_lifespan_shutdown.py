"""Unit tests for application lifespan shutdown helpers."""

# pyright: reportPrivateUsage=false
# Reason: unit tests call lifespan_shutdown private _shutdown_* helpers directly.

from __future__ import annotations

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
    app = FastAPI()
    app.state = MagicMock()
    return app


@pytest.fixture
def mock_container() -> MagicMock:
    container: MagicMock = MagicMock()
    container.task_registry = MagicMock()
    container.event_bus = MagicMock()
    container.shutdown = AsyncMock()
    return container


@pytest.mark.asyncio
async def test_shutdown_mythos_chronicle_success() -> None:
    freeze: MagicMock = MagicMock(return_value=MagicMock())
    chronicle: MagicMock = MagicMock()
    chronicle.freeze = freeze
    with patch("server.app.lifespan_shutdown.get_mythos_chronicle", return_value=chronicle):
        await _shutdown_mythos_chronicle()
    freeze.assert_called_once()


@pytest.mark.asyncio
async def test_shutdown_mythos_chronicle_handles_error() -> None:
    with patch("server.app.lifespan_shutdown.get_mythos_chronicle", side_effect=RuntimeError("fail")):
        await _shutdown_mythos_chronicle()


@pytest.mark.asyncio
async def test_shutdown_nats_handler_from_container(mock_app: FastAPI) -> None:
    stop: AsyncMock = AsyncMock()
    handler: MagicMock = MagicMock()
    handler.stop = stop
    mock_app.state.container = MagicMock(nats_message_handler=handler)
    await _shutdown_nats_handler(mock_app)
    stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_nats_handler_from_app_state(mock_app: FastAPI) -> None:
    stop: AsyncMock = AsyncMock()
    handler: MagicMock = MagicMock()
    handler.stop = stop
    mock_app.state.container = None
    mock_app.state.nats_message_handler = handler
    await _shutdown_nats_handler(mock_app)
    stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_nats_handler_missing(mock_app: FastAPI) -> None:
    mock_app.state.container = None
    del mock_app.state.nats_message_handler
    await _shutdown_nats_handler(mock_app)


@pytest.mark.asyncio
async def test_shutdown_connection_manager(mock_app: FastAPI) -> None:
    stop_idle_sampler: AsyncMock = AsyncMock()
    force_cleanup: AsyncMock = AsyncMock()
    stop_health_checks: MagicMock = MagicMock()
    memory_monitor: MagicMock = MagicMock()
    memory_monitor.stop_idle_sampler = stop_idle_sampler
    cm: MagicMock = MagicMock()
    cm.memory_monitor = memory_monitor
    cm.force_cleanup = force_cleanup
    cm.stop_health_checks = stop_health_checks
    mock_app.state.container = MagicMock(connection_manager=cm)
    await _shutdown_connection_manager(mock_app)
    stop_idle_sampler.assert_awaited_once()
    stop_health_checks.assert_called_once()
    force_cleanup.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_connection_manager_handles_errors(mock_app: FastAPI) -> None:
    stop_idle_sampler: AsyncMock = AsyncMock()
    force_cleanup: AsyncMock = AsyncMock(side_effect=RuntimeError("cleanup"))
    stop_health_checks: MagicMock = MagicMock(side_effect=RuntimeError("health"))
    memory_monitor: MagicMock = MagicMock()
    memory_monitor.stop_idle_sampler = stop_idle_sampler
    cm: MagicMock = MagicMock()
    cm.memory_monitor = memory_monitor
    cm.force_cleanup = force_cleanup
    cm.stop_health_checks = stop_health_checks
    mock_app.state.container = MagicMock(connection_manager=cm)
    await _shutdown_connection_manager(mock_app)


@pytest.mark.asyncio
async def test_shutdown_mythos_tick_scheduler(mock_app: FastAPI) -> None:
    stop: AsyncMock = AsyncMock()
    scheduler: MagicMock = MagicMock()
    scheduler.stop = stop
    mock_app.state.container = MagicMock(mythos_tick_scheduler=scheduler)
    await _shutdown_mythos_tick_scheduler(mock_app)
    stop.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_task_registry_success(mock_container: MagicMock) -> None:
    shutdown_all: AsyncMock = AsyncMock(return_value=True)
    task_registry: MagicMock = MagicMock()
    task_registry.shutdown_all = shutdown_all
    mock_container.task_registry = task_registry
    await _shutdown_task_registry(mock_container)
    shutdown_all.assert_awaited_once_with(timeout=5.0)


@pytest.mark.asyncio
async def test_shutdown_task_registry_timeout(mock_container: MagicMock) -> None:
    shutdown_all: AsyncMock = AsyncMock(return_value=False)
    task_registry: MagicMock = MagicMock()
    task_registry.shutdown_all = shutdown_all
    mock_container.task_registry = task_registry
    await _shutdown_task_registry(mock_container)


@pytest.mark.asyncio
async def test_shutdown_task_registry_missing(mock_container: MagicMock) -> None:
    mock_container.task_registry = None
    await _shutdown_task_registry(mock_container)


@pytest.mark.asyncio
async def test_shutdown_event_bus(mock_container: MagicMock) -> None:
    shutdown: AsyncMock = AsyncMock()
    get_subscriber_stats: MagicMock = MagicMock(
        return_value={
            "total_subscribers": 2,
            "services_tracked": 1,
        }
    )
    event_bus: MagicMock = MagicMock()
    event_bus.get_subscriber_stats = get_subscriber_stats
    event_bus.shutdown = shutdown
    mock_container.event_bus = event_bus
    await _shutdown_event_bus(mock_container)
    shutdown.assert_awaited_once()


@pytest.mark.asyncio
async def test_shutdown_event_bus_missing(mock_container: MagicMock) -> None:
    mock_container.event_bus = None
    await _shutdown_event_bus(mock_container)


@pytest.mark.asyncio
async def test_shutdown_services_orchestrates_all(mock_app: FastAPI, mock_container: MagicMock) -> None:
    container_shutdown: AsyncMock = AsyncMock()
    mock_container.shutdown = container_shutdown
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
    container_shutdown.assert_awaited_once()
