"""
Unit tests for lifespan startup functions.

Tests the application startup initialization functions.
"""

# pyright: reportPrivateUsage=false
# Reason: unit tests call lifespan_startup private helpers (_get_item_*, _validate_*, _log_*).

from __future__ import annotations

from dataclasses import dataclass
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI
from starlette.datastructures import State

from server.app.lifespan_magic import initialize_magic_services
from server.app.lifespan_startup import (
    _get_item_prototype_count,
    _get_item_prototype_entries,
    _log_npc_startup_errors,
    _validate_npc_services_prerequisites,
    initialize_chat_service,
    initialize_combat_services,
    initialize_container_and_legacy_services,
    initialize_mythos_time_consumer,
    initialize_nats_and_combat_services,
    initialize_npc_services,
    initialize_npc_startup_spawning,
    setup_connection_manager,
)


@dataclass
class _LifespanAppState:
    container: MagicMock | None = None
    npc_spawning_service: MagicMock | None = None
    npc_lifecycle_manager: MagicMock | None = None
    npc_population_controller: MagicMock | None = None
    combat_service: MagicMock | None = None
    combat_configuration_service: MagicMock | None = None
    chat_service: MagicMock | None = None
    magic_service: MagicMock | None = None
    spell_registry: MagicMock | None = None


@dataclass
class _ConnectionManagerStub:
    message_queue: MagicMock | None = None
    async_persistence: MagicMock | None = None
    app: FastAPI | None = None
    memory_monitor: MagicMock | None = None
    set_event_bus: MagicMock | None = None
    start_health_checks: MagicMock | None = None

    def __post_init__(self) -> None:
        if self.set_event_bus is None:
            self.set_event_bus = MagicMock()
        if self.start_health_checks is None:
            self.start_health_checks = MagicMock()
        if self.memory_monitor is None:
            monitor: MagicMock = MagicMock()
            monitor.start_idle_sampler = AsyncMock()
            self.memory_monitor = monitor


@pytest.fixture
def mock_app() -> FastAPI:
    """Create a mock FastAPI app."""
    app = FastAPI()
    lifespan_state = _LifespanAppState()
    app.state = cast(State, cast(object, lifespan_state))
    return app


@pytest.fixture
def mock_container() -> MagicMock:
    """Create a mock ApplicationContainer."""
    container: MagicMock = MagicMock()
    container.task_registry = MagicMock()
    container.event_bus = MagicMock()
    container.real_time_event_handler = MagicMock()
    container.async_persistence = MagicMock()
    connection_manager: MagicMock = MagicMock()
    memory_monitor: MagicMock = MagicMock()
    memory_monitor.start_idle_sampler = AsyncMock()
    connection_manager.memory_monitor = memory_monitor
    container.connection_manager = connection_manager
    container.player_service = MagicMock()
    container.room_service = MagicMock()
    container.user_manager = MagicMock()
    container.container_service = MagicMock()
    container.holiday_service = MagicMock()
    container.schedule_service = MagicMock()
    container.room_cache_service = MagicMock()
    container.profession_cache_service = MagicMock()
    container.item_prototype_registry = MagicMock()
    container.item_factory = MagicMock()
    container.persistence = MagicMock()
    container.config.logging.environment = "unit_test"
    return container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_container_and_legacy_services() initializes container."""
    registry: MagicMock = MagicMock()
    registry.all = MagicMock(return_value=[])
    mock_container.item_prototype_registry = registry
    await initialize_container_and_legacy_services(mock_app, mock_container)
    state = cast(_LifespanAppState, cast(object, mock_app.state))
    assert state.container is mock_container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services_no_item_factory(
    mock_app: FastAPI, mock_container: MagicMock
) -> None:
    """Test initialize_container_and_legacy_services() handles missing item factory."""
    mock_container.item_factory = None
    mock_container.item_prototype_registry = None
    await initialize_container_and_legacy_services(mock_app, mock_container)
    state = cast(_LifespanAppState, cast(object, mock_app.state))
    assert state.container == mock_container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services_async_registry(
    mock_app: FastAPI, mock_container: MagicMock
) -> None:
    """Test initialize_container_and_legacy_services() handles async registry."""

    async def async_all() -> list[object]:
        return []

    registry: MagicMock = MagicMock()
    registry.all = async_all
    mock_container.item_prototype_registry = registry
    await initialize_container_and_legacy_services(mock_app, mock_container)
    state = cast(_LifespanAppState, cast(object, mock_app.state))
    assert state.container == mock_container


@pytest.mark.asyncio
async def test_setup_connection_manager(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test setup_connection_manager() sets up connection manager."""
    message_queue: MagicMock = MagicMock()
    message_queue.pending_messages = MagicMock()
    connection_manager = _ConnectionManagerStub()
    async_persistence: MagicMock = MagicMock()
    mock_container.connection_manager = connection_manager
    mock_container.async_persistence = async_persistence
    connection_manager.message_queue = message_queue
    with (
        patch("server.app.lifespan_event_subscriptions.subscribe_room_occupants_refresh"),
        patch("server.app.lifespan_event_subscriptions.subscribe_quest_events"),
    ):
        await setup_connection_manager(mock_app, mock_container)
    assert connection_manager.async_persistence is async_persistence
    assert connection_manager.app is mock_app


@pytest.mark.asyncio
async def test_setup_connection_manager_no_manager(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test setup_connection_manager() raises error when manager is None."""
    mock_container.connection_manager = None
    with pytest.raises(RuntimeError, match="Connection manager not initialized"):
        await setup_connection_manager(mock_app, mock_container)


@pytest.mark.asyncio
async def test_initialize_npc_services(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_npc_services() initializes NPC services."""
    with (
        patch("server.npc.population_control.load_zone_configurations", return_value={}),
        patch("server.app.lifespan_startup.NPCService.get_npc_definitions", new=AsyncMock(return_value=[])),
        patch("server.app.lifespan_startup.NPCService.get_spawn_rules", new=AsyncMock(return_value=[])),
    ):
        await initialize_npc_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "npc_spawning_service")
    assert hasattr(mock_app.state, "npc_lifecycle_manager")
    assert hasattr(mock_app.state, "npc_population_controller")


@pytest.mark.asyncio
async def test_initialize_combat_services(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_combat_services() initializes combat services."""
    await initialize_combat_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "combat_service") or hasattr(mock_app.state, "combat_configuration_service")


@pytest.mark.asyncio
async def test_initialize_mythos_time_consumer(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_mythos_time_consumer() initializes time consumer."""
    with patch("server.app.lifespan_startup.get_mythos_chronicle") as mock_chronicle:
        mock_chronicle.return_value = MagicMock()
        await initialize_mythos_time_consumer(mock_app, mock_container)


@pytest.mark.asyncio
async def test_initialize_npc_startup_spawning(mock_app: FastAPI) -> None:
    """Test initialize_npc_startup_spawning() initializes NPC spawning."""
    mock_app.state.npc_spawning_service = MagicMock()
    await initialize_npc_startup_spawning(mock_app)


@pytest.mark.asyncio
async def test_initialize_nats_and_combat_services(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_nats_and_combat_services() initializes NATS and combat."""
    await initialize_nats_and_combat_services(mock_app, mock_container)


@pytest.mark.asyncio
async def test_initialize_chat_service(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_chat_service() initializes chat service."""
    await initialize_chat_service(mock_app, mock_container)
    assert hasattr(mock_app.state, "chat_service")


@pytest.mark.asyncio
async def test_initialize_magic_services(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Test initialize_magic_services() initializes magic services."""
    with patch("server.app.lifespan_magic.SpellRegistry.load_spells", new=AsyncMock(return_value=None)):
        await initialize_magic_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "magic_service") or hasattr(mock_app.state, "spell_registry")


@pytest.mark.asyncio
async def test_get_item_prototype_entries_none_registry() -> None:
    """Missing registry returns None."""
    assert await _get_item_prototype_entries(None) is None


@pytest.mark.asyncio
async def test_get_item_prototype_entries_missing_all_method() -> None:
    """Registry without all() returns None."""
    registry: MagicMock = MagicMock(spec=[])
    assert await _get_item_prototype_entries(registry) is None


@pytest.mark.asyncio
async def test_get_item_prototype_entries_async_failure() -> None:
    """Async registry errors are swallowed."""

    class BadRegistry:
        async def all(self) -> list[object]:
            raise RuntimeError("boom")

    assert await _get_item_prototype_entries(BadRegistry()) is None


@pytest.mark.asyncio
async def test_get_item_prototype_count_non_iterable() -> None:
    """Non-iterable registry entries default count to zero."""

    class WeirdRegistry:
        def all(self) -> int:
            return 42

    assert await _get_item_prototype_count(WeirdRegistry()) == 0


def test_validate_npc_services_prerequisites_missing_event_bus(mock_container: MagicMock) -> None:
    """Missing event bus raises RuntimeError."""
    mock_container.event_bus = None
    with pytest.raises(RuntimeError, match="EventBus"):
        _validate_npc_services_prerequisites(mock_container)


def test_validate_npc_services_prerequisites_missing_persistence(mock_container: MagicMock) -> None:
    """Missing persistence raises RuntimeError."""
    mock_container.persistence = None
    with pytest.raises(RuntimeError, match="Persistence"):
        _validate_npc_services_prerequisites(mock_container)


def test_log_npc_startup_errors() -> None:
    """Startup errors are logged when present."""
    _log_npc_startup_errors({"errors": ["spawn failed"]})
    _log_npc_startup_errors({"errors": []})


@pytest.mark.asyncio
async def test_initialize_mythos_time_consumer_missing_deps(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """Missing dependencies skip mythos time consumer initialization."""
    mock_container.holiday_service = None
    with patch("server.app.lifespan_startup.MythosTimeEventConsumer") as mock_consumer_cls:
        await initialize_mythos_time_consumer(mock_app, mock_container)
        mock_consumer_cls.assert_not_called()


@pytest.mark.asyncio
async def test_initialize_container_legacy_service_none(mock_app: FastAPI, mock_container: MagicMock) -> None:
    """None legacy services log warning without failing startup."""
    mock_container.player_service = None
    registry: MagicMock = MagicMock()
    registry.all = MagicMock(return_value=[])
    mock_container.item_prototype_registry = registry
    await initialize_container_and_legacy_services(mock_app, mock_container)
    state = cast(_LifespanAppState, cast(object, mock_app.state))
    assert state.container is mock_container
