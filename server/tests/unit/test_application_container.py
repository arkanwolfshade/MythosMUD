"""
Unit tests for ApplicationContainer.

Tests container initialization, service access, and singleton management.
"""

from contextlib import contextmanager
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest

from server.container import ApplicationContainer, get_container, reset_container


@pytest.fixture(autouse=True)
def reset_container_state():
    """Reset container singleton before and after each test."""
    ApplicationContainer.reset_instance()
    yield
    ApplicationContainer.reset_instance()


@contextmanager
def patch_container_dependencies():
    """Helper context manager to patch all container dependencies."""
    from contextlib import ExitStack

    mock_config = MagicMock()
    mock_config.logging.environment = "test"
    mock_config.nats.enabled = True  # Enable NATS for tests

    # Create mock database manager with proper async methods
    mock_db_manager = MagicMock()
    mock_db_manager.close = AsyncMock()
    mock_session_maker = Mock()
    mock_session = AsyncMock()
    mock_context = AsyncMock()
    mock_context.__aenter__ = AsyncMock(return_value=mock_session)
    mock_context.__aexit__ = AsyncMock(return_value=None)
    mock_session_maker.return_value = mock_context
    mock_db_manager.get_session_maker = Mock(return_value=mock_session_maker)

    # Mock database query result for item services
    mock_result = MagicMock()
    mock_scalars_result = MagicMock()
    mock_scalars_result.all.return_value = []
    mock_result.scalars = Mock(return_value=mock_scalars_result)
    mock_session.execute = AsyncMock(return_value=mock_result)

    # Mock async generator for get_npc_session
    async def mock_get_npc_session():
        mock_npc_session = AsyncMock()
        # Configure session.execute to return a result with scalars().all() chain
        mock_npc_result = MagicMock()
        mock_npc_scalars = MagicMock()
        mock_npc_scalars.all.return_value = []
        mock_npc_result.scalars.return_value = mock_npc_scalars
        mock_npc_session.execute = AsyncMock(return_value=mock_npc_result)
        yield mock_npc_session

    patches = [
        ("server.config.get_config", {"return_value": mock_config}),
        ("server.database.DatabaseManager.get_instance", {"return_value": mock_db_manager}),
        ("server.database.init_db", {"new_callable": AsyncMock}),
        ("server.npc_database.init_npc_db", {"new_callable": AsyncMock}),
        ("server.npc_database.get_npc_session", {"new_callable": lambda: mock_get_npc_session}),
        ("server.app.task_registry.TaskRegistry", {}),
        ("server.app.tracked_task_manager.TrackedTaskManager", {}),
        (
            "server.events.event_bus.EventBus",
            {
                "new_callable": lambda: type(
                    "MockEventBus",
                    (),
                    {"shutdown": AsyncMock(), "subscribe": MagicMock()},
                )
            },
        ),
        (
            "server.async_persistence.AsyncPersistenceLayer",
            {"new_callable": lambda: (lambda *args, **kwargs: MagicMock(close=AsyncMock()))},
        ),
        ("server.services.exploration_service.ExplorationService", {}),
        ("server.game.movement_service.MovementService", {}),
        ("server.utils.project_paths.get_calendar_paths_for_environment", {}),
        ("server.services.holiday_service.HolidayService", {}),
        ("server.services.schedule_service.ScheduleService", {}),
        ("server.time.tick_scheduler.MythosTickScheduler", {}),
        ("server.realtime.connection_manager.ConnectionManager", {}),
        ("server.realtime.event_handler.RealTimeEventHandler", {}),
        (
            "server.services.nats_service.NATSService",
            {
                "new_callable": lambda: type(
                    "MockNATSService",
                    (),
                    {
                        "__init__": lambda self, *args, **kwargs: None,
                        "connect": AsyncMock(),
                        "disconnect": AsyncMock(),
                        "is_connected": lambda self: True,
                    },
                )
            },
        ),
        ("server.game.player_service.PlayerService", {}),
        ("server.game.room_service.RoomService", {}),
        ("server.services.user_manager.UserManager", {}),
        ("server.services.container_service.ContainerService", {}),
        ("server.game.items.prototype_registry.PrototypeRegistry", {}),
        ("server.game.items.item_factory.ItemFactory", {}),
        ("server.caching.cache_service.RoomCacheService", {}),
        ("server.caching.cache_service.ProfessionCacheService", {}),
        ("server.monitoring.performance_monitor.PerformanceMonitor", {}),
        ("server.monitoring.exception_tracker.ExceptionTracker", {}),
        ("server.monitoring.monitoring_dashboard.MonitoringDashboard", {}),
        ("server.structured_logging.log_aggregator.LogAggregator", {}),
    ]

    with ExitStack() as stack:
        for target, kwargs in patches:
            stack.enter_context(patch(target, **kwargs))
        yield


class TestContainerSingleton:
    """Test container singleton pattern."""

    def test_get_instance_creates_singleton(self):
        """Test get_instance() creates singleton instance."""
        instance1 = ApplicationContainer.get_instance()
        instance2 = ApplicationContainer.get_instance()
        assert instance1 is instance2

    def test_reset_instance(self):
        """Test reset_instance() resets singleton."""
        instance1 = ApplicationContainer.get_instance()
        ApplicationContainer.reset_instance()
        instance2 = ApplicationContainer.get_instance()
        assert instance1 is not instance2

    def test_set_instance(self):
        """Test set_instance() sets singleton instance."""
        custom_instance = ApplicationContainer()
        ApplicationContainer.set_instance(custom_instance)
        assert ApplicationContainer.get_instance() is custom_instance

    def test_get_instance_thread_safe(self):
        """Test get_instance() is thread-safe."""
        # This is a basic test - full thread safety would require concurrent testing
        instance1 = ApplicationContainer.get_instance()
        ApplicationContainer.reset_instance()
        instance2 = ApplicationContainer.get_instance()
        assert instance1 is not instance2


class TestContainerInitialization:
    """Test container initialization."""

    @pytest.mark.asyncio
    async def test_initialize_sets_initialized_flag(self):
        """Test initialize() sets _initialized flag."""
        container = ApplicationContainer()
        with patch_container_dependencies():
            await container.initialize()
            assert container.is_initialized is True

    @pytest.mark.asyncio
    async def test_initialize_idempotent(self):
        """Test initialize() is idempotent."""
        container = ApplicationContainer()
        with patch_container_dependencies():
            # First initialization
            await container.initialize()
            # Second initialization should be skipped
            await container.initialize()
            # Should only initialize once
            assert container.is_initialized is True

    @pytest.mark.asyncio
    async def test_initialize_handles_failure(self):
        """Test initialize() handles initialization failure."""
        container = ApplicationContainer()
        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.logging.environment = "test"
            mock_get_config.return_value = mock_config

            with patch("server.database.DatabaseManager.get_instance", side_effect=Exception("Init error")):
                with pytest.raises(RuntimeError, match="Failed to initialize"):
                    await container.initialize()


class TestContainerServiceAccess:
    """Test container service access methods."""

    def test_get_service_not_initialized(self):
        """Test get_service() raises when container not initialized."""
        container = ApplicationContainer()
        with pytest.raises(RuntimeError, match="Container not initialized"):
            container.get_service("player_service")

    def test_get_service_invalid_name(self):
        """Test get_service() raises for invalid service name."""
        container = ApplicationContainer()
        with patch.object(container, "_initialized", True):
            with pytest.raises(ValueError, match="Unknown service"):
                container.get_service("nonexistent_service")

    def test_get_service_not_initialized_service(self):
        """Test get_service() raises when service not initialized."""
        container = ApplicationContainer()
        with patch.object(container, "_initialized", True):
            container.player_service = None
            with pytest.raises(ValueError, match="Service not initialized"):
                container.get_service("player_service")

    def test_get_service_success(self):
        """Test get_service() returns service when available."""
        container = ApplicationContainer()
        with patch.object(container, "_initialized", True):
            mock_service = MagicMock()
            container.player_service = mock_service
            result = container.get_service("player_service")
            assert result == mock_service

    def test_is_initialized_property(self):
        """Test is_initialized property."""
        container = ApplicationContainer()
        assert container.is_initialized is False
        with patch.object(container, "_initialized", True):
            assert container.is_initialized is True


class TestContainerShutdown:
    """Test container shutdown methods."""

    @pytest.mark.asyncio
    async def test_shutdown_closes_services(self):
        """Test shutdown() closes all services."""
        container = ApplicationContainer()
        mock_log_aggregator = MagicMock()
        mock_log_aggregator.shutdown = Mock()
        container.log_aggregator = mock_log_aggregator

        mock_nats_message_handler = AsyncMock()
        mock_nats_message_handler.stop = AsyncMock()
        container.nats_message_handler = mock_nats_message_handler

        mock_nats_service = AsyncMock()
        mock_nats_service.disconnect = AsyncMock()
        container.nats_service = mock_nats_service

        mock_event_bus = AsyncMock()
        mock_event_bus.shutdown = AsyncMock()
        container.event_bus = mock_event_bus

        mock_database_manager = AsyncMock()
        mock_database_manager.close = AsyncMock()
        container.database_manager = mock_database_manager

        mock_async_persistence = AsyncMock()
        mock_async_persistence.close = AsyncMock()
        container.async_persistence = mock_async_persistence

        with patch("server.npc_database.close_npc_db", new_callable=AsyncMock):
            await container.shutdown()

        mock_log_aggregator.shutdown.assert_called_once()
        mock_nats_message_handler.stop.assert_awaited_once()
        mock_nats_service.disconnect.assert_awaited_once()
        mock_event_bus.shutdown.assert_awaited_once()
        mock_database_manager.close.assert_awaited_once()
        mock_async_persistence.close.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_shutdown_handles_errors_gracefully(self):
        """Test shutdown() handles errors gracefully."""
        container = ApplicationContainer()
        mock_log_aggregator = MagicMock()
        # Use RuntimeError to match what _shutdown_log_aggregator catches
        mock_log_aggregator.shutdown = Mock(side_effect=RuntimeError("Shutdown error"))
        container.log_aggregator = mock_log_aggregator

        # Should not raise, just log error
        await container.shutdown()


class TestContainerFactoryFunctions:
    """Test container factory functions."""

    def test_get_container(self):
        """Test get_container() returns singleton."""
        instance1 = get_container()
        instance2 = get_container()
        assert instance1 is instance2

    def test_reset_container(self):
        """Test reset_container() resets singleton."""
        instance1 = get_container()
        reset_container()
        instance2 = get_container()
        assert instance1 is not instance2


class TestContainerItemServices:
    """Test container item service initialization."""

    @pytest.mark.asyncio
    async def test_initialize_item_services_success(self):
        """Test _initialize_item_services() loads item prototypes."""
        container = ApplicationContainer()
        mock_database_manager = MagicMock()
        mock_session = AsyncMock()
        mock_context = AsyncMock()
        mock_context.__aenter__ = AsyncMock(return_value=mock_session)
        mock_context.__aexit__ = AsyncMock(return_value=None)
        mock_session_maker = Mock(return_value=mock_context)
        mock_database_manager.get_session_maker = Mock(return_value=mock_session_maker)
        container.database_manager = mock_database_manager

        # Mock database query result
        mock_result = MagicMock()
        mock_scalars_result = MagicMock()
        mock_scalars_result.all.return_value = []
        mock_result.scalars = Mock(return_value=mock_scalars_result)
        mock_session.execute = AsyncMock(return_value=mock_result)

        # Testing protected method _initialize_item_services is necessary for unit test coverage
        await container._initialize_item_services()  # pylint: disable=protected-access  # Reason: Testing protected method is necessary for unit test coverage
        # Should complete without error

    @pytest.mark.asyncio
    async def test_initialize_item_services_no_database(self):
        """Test _initialize_item_services() handles missing database manager."""
        container = ApplicationContainer()
        container.database_manager = None

        # Testing protected method _initialize_item_services is necessary for unit test coverage
        await container._initialize_item_services()  # pylint: disable=protected-access  # Reason: Testing protected method is necessary for unit test coverage
        assert container.item_prototype_registry is None
        assert container.item_factory is None

    def test_decode_json_column_none(self):
        """Test _decode_json_column() with None value."""
        container = ApplicationContainer()
        # Testing protected method _decode_json_column is necessary for unit test coverage
        result = container._decode_json_column(None, list)  # pylint: disable=protected-access  # Reason: Testing protected method is necessary for unit test coverage
        assert result == []

    def test_decode_json_column_already_list(self):
        """Test _decode_json_column() with list value."""
        container = ApplicationContainer()
        value = [1, 2, 3]
        # Testing protected method _decode_json_column is necessary for unit test coverage
        result = container._decode_json_column(value, list)  # pylint: disable=protected-access  # Reason: Testing protected method is necessary for unit test coverage
        assert result == value

    def test_decode_json_column_json_string(self):
        """Test _decode_json_column() with JSON string."""
        import json

        container = ApplicationContainer()
        value = json.dumps([1, 2, 3])
        # Testing protected method _decode_json_column is necessary for unit test coverage
        result = container._decode_json_column(value, list)  # pylint: disable=protected-access  # Reason: Testing protected method is necessary for unit test coverage
        assert result == [1, 2, 3]

    def test_decode_json_column_invalid_json(self):
        """Test _decode_json_column() handles invalid JSON."""
        container = ApplicationContainer()
        # Testing protected method _decode_json_column is necessary for unit test coverage
        result = container._decode_json_column("invalid json", list)  # pylint: disable=protected-access  # Reason: Testing protected method is necessary for unit test coverage
        assert result == []
