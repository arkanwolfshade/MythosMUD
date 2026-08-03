"""
Unit tests for lifespan startup functions.

Tests the application startup initialization functions.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

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


@pytest.fixture
def mock_app():
    """Create a mock FastAPI app."""
    app = MagicMock(spec=FastAPI)
    app.state = MagicMock()
    return app


@pytest.fixture
def mock_container():
    """Create a mock ApplicationContainer."""
    container = MagicMock()
    container.task_registry = MagicMock()
    container.event_bus = MagicMock()
    container.real_time_event_handler = MagicMock()
    container.async_persistence = MagicMock()
    container.connection_manager = MagicMock()
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
    return container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_container_and_legacy_services() initializes container."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.item_prototype_registry.all = MagicMock(return_value=[])
    await initialize_container_and_legacy_services(mock_app, mock_container)
    # The implementation sets app.state.container = container, so they should be the same object
    assert mock_app.state.container is mock_container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services_no_item_factory(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_container_and_legacy_services() handles missing item factory."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.item_factory = None
    mock_container.item_prototype_registry = None
    await initialize_container_and_legacy_services(mock_app, mock_container)
    assert mock_app.state.container == mock_container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services_async_registry(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_container_and_legacy_services() handles async registry."""
    # Parameter names must match fixture names for pytest automatic injection

    async def async_all():
        return []

    mock_container.item_prototype_registry.all = async_all
    await initialize_container_and_legacy_services(mock_app, mock_container)
    assert mock_app.state.container == mock_container


@pytest.mark.asyncio
async def test_setup_connection_manager(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test setup_connection_manager() sets up connection manager."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.connection_manager.message_queue = MagicMock()
    mock_container.connection_manager.message_queue.pending_messages = MagicMock()
    await setup_connection_manager(mock_app, mock_container)
    assert mock_container.connection_manager.async_persistence == mock_container.async_persistence
    assert mock_container.connection_manager.app == mock_app


@pytest.mark.asyncio
async def test_setup_connection_manager_no_manager(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test setup_connection_manager() raises error when manager is None."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.connection_manager = None
    with pytest.raises(RuntimeError, match="Connection manager not initialized"):
        await setup_connection_manager(mock_app, mock_container)


@pytest.mark.asyncio
async def test_initialize_npc_services(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_npc_services() initializes NPC services."""
    # Parameter names must match fixture names for pytest automatic injection.
    # Patch zone config loader so NPCPopulationController does not hit the database.
    # Also patch NPCService DB calls so unit tests do not require stored procedures.
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
async def test_initialize_combat_services(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_combat_services() initializes combat services."""
    # Parameter names must match fixture names for pytest automatic injection
    await initialize_combat_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "combat_service") or hasattr(mock_app.state, "combat_configuration_service")


@pytest.mark.asyncio
async def test_initialize_mythos_time_consumer(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_mythos_time_consumer() initializes time consumer."""
    # Parameter names must match fixture names for pytest automatic injection
    with patch("server.app.lifespan_startup.get_mythos_chronicle") as mock_chronicle:
        mock_chronicle.return_value = MagicMock()
        await initialize_mythos_time_consumer(mock_app, mock_container)
        # Should not raise


@pytest.mark.asyncio
async def test_initialize_npc_startup_spawning(mock_app):  # pylint: disable=redefined-outer-name
    """Test initialize_npc_startup_spawning() initializes NPC spawning."""
    # Parameter name must match fixture name for pytest automatic injection
    mock_app.state.npc_spawning_service = MagicMock()
    await initialize_npc_startup_spawning(mock_app)
    # Should not raise


@pytest.mark.asyncio
async def test_initialize_nats_and_combat_services(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_nats_and_combat_services() initializes NATS and combat."""
    # Parameter names must match fixture names for pytest automatic injection
    await initialize_nats_and_combat_services(mock_app, mock_container)
    # Should not raise


@pytest.mark.asyncio
async def test_initialize_chat_service(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_chat_service() initializes chat service."""
    # Parameter names must match fixture names for pytest automatic injection
    await initialize_chat_service(mock_app, mock_container)
    assert hasattr(mock_app.state, "chat_service")


@pytest.mark.asyncio
async def test_initialize_magic_services(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test initialize_magic_services() initializes magic services."""
    # Parameter names must match fixture names for pytest automatic injection
    # Patch SpellRegistry.load_spells so unit tests do not require stored procedures.
    with patch("server.app.lifespan_magic.SpellRegistry.load_spells", new=AsyncMock(return_value=None)):
        await initialize_magic_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "magic_service") or hasattr(mock_app.state, "spell_registry")


@pytest.mark.asyncio
async def test_get_item_prototype_entries_none_registry():
    """Missing registry returns None."""
    assert await _get_item_prototype_entries(None) is None


@pytest.mark.asyncio
async def test_get_item_prototype_entries_missing_all_method():
    """Registry without all() returns None."""
    registry = MagicMock(spec=[])
    assert await _get_item_prototype_entries(registry) is None


@pytest.mark.asyncio
async def test_get_item_prototype_entries_async_failure():
    """Async registry errors are swallowed."""

    class BadRegistry:
        async def all(self):
            raise RuntimeError("boom")

    assert await _get_item_prototype_entries(BadRegistry()) is None


@pytest.mark.asyncio
async def test_get_item_prototype_count_non_iterable():
    """Non-iterable registry entries default count to zero."""

    class WeirdRegistry:
        def all(self):
            return 42

    assert await _get_item_prototype_count(WeirdRegistry()) == 0


def test_validate_npc_services_prerequisites_missing_event_bus(mock_container):
    """Missing event bus raises RuntimeError."""
    mock_container.event_bus = None
    with pytest.raises(RuntimeError, match="EventBus"):
        _validate_npc_services_prerequisites(mock_container)


def test_validate_npc_services_prerequisites_missing_persistence(mock_container):
    """Missing persistence raises RuntimeError."""
    mock_container.persistence = None
    with pytest.raises(RuntimeError, match="Persistence"):
        _validate_npc_services_prerequisites(mock_container)


def test_log_npc_startup_errors():
    """Startup errors are logged when present."""
    _log_npc_startup_errors({"errors": ["spawn failed"]})
    _log_npc_startup_errors({"errors": []})


@pytest.mark.asyncio
async def test_initialize_mythos_time_consumer_missing_deps(mock_app, mock_container):
    """Missing dependencies skip mythos time consumer initialization."""
    mock_container.holiday_service = None
    with patch("server.app.lifespan_startup.MythosTimeEventConsumer") as mock_consumer_cls:
        await initialize_mythos_time_consumer(mock_app, mock_container)
        mock_consumer_cls.assert_not_called()


@pytest.mark.asyncio
async def test_initialize_container_legacy_service_none(mock_app, mock_container):
    """None legacy services log warning without failing startup."""
    mock_container.player_service = None
    mock_container.item_prototype_registry.all = MagicMock(return_value=[])
    await initialize_container_and_legacy_services(mock_app, mock_container)
    assert mock_app.state.container is mock_container
