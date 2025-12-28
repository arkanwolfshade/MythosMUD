"""
Unit tests for lifespan startup functions.

Tests the application startup initialization functions.
"""

from unittest.mock import MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.lifespan_startup import (
    initialize_chat_service,
    initialize_combat_services,
    initialize_container_and_legacy_services,
    initialize_magic_services,
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
async def test_initialize_container_and_legacy_services(mock_app, mock_container):
    """Test initialize_container_and_legacy_services() initializes container."""
    mock_container.item_prototype_registry.all = MagicMock(return_value=[])
    await initialize_container_and_legacy_services(mock_app, mock_container)
    assert mock_app.state.container == mock_container
    assert mock_app.state.persistence == mock_container.async_persistence


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services_no_item_factory(mock_app, mock_container):
    """Test initialize_container_and_legacy_services() handles missing item factory."""
    mock_container.item_factory = None
    mock_container.item_prototype_registry = None
    await initialize_container_and_legacy_services(mock_app, mock_container)
    assert mock_app.state.container == mock_container


@pytest.mark.asyncio
async def test_initialize_container_and_legacy_services_async_registry(mock_app, mock_container):
    """Test initialize_container_and_legacy_services() handles async registry."""

    async def async_all():
        return []

    mock_container.item_prototype_registry.all = async_all
    await initialize_container_and_legacy_services(mock_app, mock_container)
    assert mock_app.state.container == mock_container


@pytest.mark.asyncio
async def test_setup_connection_manager(mock_app, mock_container):
    """Test setup_connection_manager() sets up connection manager."""
    mock_container.connection_manager.message_queue = MagicMock()
    mock_container.connection_manager.message_queue.pending_messages = MagicMock()
    await setup_connection_manager(mock_app, mock_container)
    assert mock_container.connection_manager.async_persistence == mock_container.async_persistence
    assert mock_container.connection_manager.app == mock_app


@pytest.mark.asyncio
async def test_setup_connection_manager_no_manager(mock_app, mock_container):
    """Test setup_connection_manager() raises error when manager is None."""
    mock_container.connection_manager = None
    with pytest.raises(RuntimeError, match="Connection manager not initialized"):
        await setup_connection_manager(mock_app, mock_container)


@pytest.mark.asyncio
async def test_initialize_npc_services(mock_app, mock_container):
    """Test initialize_npc_services() initializes NPC services."""
    await initialize_npc_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "npc_spawning_service")
    assert hasattr(mock_app.state, "npc_lifecycle_manager")
    assert hasattr(mock_app.state, "npc_population_controller")


@pytest.mark.asyncio
async def test_initialize_combat_services(mock_app, mock_container):
    """Test initialize_combat_services() initializes combat services."""
    await initialize_combat_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "combat_service") or hasattr(mock_app.state, "combat_configuration_service")


@pytest.mark.asyncio
async def test_initialize_mythos_time_consumer(mock_app, mock_container):
    """Test initialize_mythos_time_consumer() initializes time consumer."""
    with patch("server.app.lifespan_startup.get_mythos_chronicle") as mock_chronicle:
        mock_chronicle.return_value = MagicMock()
        await initialize_mythos_time_consumer(mock_app, mock_container)
        # Should not raise


@pytest.mark.asyncio
async def test_initialize_npc_startup_spawning(mock_app):
    """Test initialize_npc_startup_spawning() initializes NPC spawning."""
    mock_app.state.npc_spawning_service = MagicMock()
    await initialize_npc_startup_spawning(mock_app)
    # Should not raise


@pytest.mark.asyncio
async def test_initialize_nats_and_combat_services(mock_app, mock_container):
    """Test initialize_nats_and_combat_services() initializes NATS and combat."""
    await initialize_nats_and_combat_services(mock_app, mock_container)
    # Should not raise


@pytest.mark.asyncio
async def test_initialize_chat_service(mock_app, mock_container):
    """Test initialize_chat_service() initializes chat service."""
    await initialize_chat_service(mock_app, mock_container)
    assert hasattr(mock_app.state, "chat_service")


@pytest.mark.asyncio
async def test_initialize_magic_services(mock_app, mock_container):
    """Test initialize_magic_services() initializes magic services."""
    await initialize_magic_services(mock_app, mock_container)
    assert hasattr(mock_app.state, "magic_service") or hasattr(mock_app.state, "spell_registry")
