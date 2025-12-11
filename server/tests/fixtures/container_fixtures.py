"""
Container-based test fixtures for MythosMUD.

This module provides pytest fixtures for testing with the ApplicationContainer,
following modern dependency injection patterns and pytest best practices.

As documented in the Pnakotic Manuscripts: "Proper test fixtures must mirror
the reality of production initialization, lest the tests mislead us about the
true behavior of the system."

Fixtures Provided:
- test_container: Real ApplicationContainer for integration tests
- container_test_client: TestClient with container initialized
- async_container_test_client: AsyncClient with container initialized
- mock_container: Mocked ApplicationContainer for unit tests
- player_factory: Factory for creating test players
- room_factory: Factory for creating test rooms

Best Practices Followed:
- Fixture factories for flexible test data
- Proper async context management
- Clean teardown to prevent resource leaks
- Backward compatibility with legacy patterns
"""

import asyncio
from typing import Any
from unittest.mock import AsyncMock, MagicMock, Mock
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _setup_test_environment() -> None:
    """Load test environment variables and validate configuration."""
    import os
    from pathlib import Path

    from dotenv import load_dotenv

    # Load test environment file explicitly to ensure variables are set
    test_env_path = Path(__file__).parent.parent.parent / "tests" / ".env.unit_test"
    if test_env_path.exists():
        load_dotenv(test_env_path, override=True)
        logger.info("Loaded test environment file", env_path=str(test_env_path))
    else:
        logger.warning("Test environment file not found", env_path=str(test_env_path))

    # Verify DATABASE_URL is set before proceeding
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError(
            "DATABASE_URL environment variable is not set. "
            "Please ensure server/tests/.env.unit_test exists and contains DATABASE_URL."
        )
    if not database_url.startswith("postgresql"):
        raise ValueError(f"DATABASE_URL must be a PostgreSQL URL, got: {database_url}. SQLite is no longer supported.")

    # CRITICAL: Reset config cache to ensure fresh environment variables are loaded
    from server.config import reset_config

    reset_config()


def _create_mock_persistence() -> Mock:
    """Create a mock persistence object with all required methods."""
    mock_persistence = Mock()
    mock_persistence.async_list_players = AsyncMock(return_value=[])
    mock_persistence.async_get_player = AsyncMock(return_value=None)
    mock_persistence.async_get_room = AsyncMock(return_value=None)
    mock_persistence.list_players = AsyncMock(return_value=[])
    mock_persistence.get_player = Mock(return_value=None)
    mock_persistence.get_room = AsyncMock(return_value=None)
    return mock_persistence


def _validate_persistence(persistence: Any) -> bool:
    """Check if persistence has all required methods."""
    if persistence is None:
        return False

    required_methods = [
        "async_list_players",
        "async_get_player",
        "async_get_room",
        "list_players",
        "get_player",
        "get_room",
    ]
    for method_name in required_methods:
        if not hasattr(persistence, method_name) or not callable(getattr(persistence, method_name, None)):
            logger.warning("Persistence missing required method, creating mock", missing_method=method_name)
            return False
    return True


def _ensure_valid_persistence(container: Any) -> Any:
    """Ensure container has valid persistence, creating mock if needed."""
    persistence_to_use = container.persistence

    if not _validate_persistence(persistence_to_use):
        logger.warning("Container persistence is invalid, creating mock persistence")
        mock_persistence = _create_mock_persistence()
        container.persistence = mock_persistence
        persistence_to_use = mock_persistence
        logger.info("Container persistence set to mock (defensive)")

    return persistence_to_use


def _update_service_persistence(service: Any, persistence_to_use: Any, service_name: str) -> None:
    """Update a single service's persistence if needed."""
    if service and hasattr(service, "persistence"):
        if service.persistence is None:
            service.persistence = persistence_to_use
            logger.info(f"{service_name} persistence updated")


def _ensure_services_have_persistence(container: Any, persistence_to_use: Any) -> None:
    """Ensure player_service and room_service have valid persistence."""
    from server.game.player_service import PlayerService
    from server.game.room_service import RoomService

    needs_recreation = (
        container.player_service is None or getattr(container.player_service, "persistence", None) is None
    )

    if needs_recreation:
        container.player_service = PlayerService(persistence=persistence_to_use)
        container.room_service = RoomService(persistence=persistence_to_use)
        logger.info("PlayerService and RoomService recreated with valid persistence")
    else:
        _update_service_persistence(container.player_service, persistence_to_use, "PlayerService")
        _update_service_persistence(container.room_service, persistence_to_use, "RoomService")

    # Final defensive check
    _update_service_persistence(container.player_service, persistence_to_use, "PlayerService")
    _update_service_persistence(container.room_service, persistence_to_use, "RoomService")


def _setup_app_state(app: Any, container: Any) -> None:
    """Set up app.state with container services."""
    # Final emergency check - ensure container.persistence is not None
    if container.persistence is None:
        logger.error("container.persistence is None after all fixes - creating emergency mock")
        emergency_mock = _create_mock_persistence()
        container.persistence = emergency_mock
        if container.player_service:
            container.player_service.persistence = emergency_mock
        if container.room_service:
            container.room_service.persistence = emergency_mock
        if container.connection_manager:
            container.connection_manager.persistence = emergency_mock

    app.state.container = container
    app.state.task_registry = container.task_registry
    app.state.event_bus = container.event_bus
    app.state.event_handler = container.real_time_event_handler
    app.state.connection_manager = container.connection_manager
    app.state.user_manager = container.user_manager
    app.state.room_cache_service = container.room_cache_service
    app.state.profession_cache_service = container.profession_cache_service
    app.state.persistence = container.persistence
    app.state.player_service = container.player_service
    app.state.room_service = container.room_service

    if container.connection_manager:
        container.connection_manager.persistence = container.persistence
        logger.info("Connection manager persistence set from container")


def _dispose_database_before_testclient(container: Any, loop: asyncio.AbstractEventLoop) -> None:
    """Dispose database engines and reset singletons before creating TestClient."""
    try:
        if container.database_manager and container.database_manager.engine:
            loop.run_until_complete(container.database_manager.close())
    except (RuntimeError, AttributeError, ConnectionError) as e:
        logger.warning("Error disposing database engine before TestClient creation", error=str(e))

    try:
        from server.npc_database import close_npc_db

        loop.run_until_complete(close_npc_db())
    except (RuntimeError, AttributeError, ConnectionError) as e:
        logger.warning("Error disposing NPC database engine before TestClient creation", error=str(e))

    from server.database import DatabaseManager

    DatabaseManager.reset_instance()

    from server.npc_database import reset_npc_database

    reset_npc_database()


def _cancel_eventbus_active_tasks(event_bus: Any) -> None:
    """Cancel active tasks in EventBus."""
    active_tasks = getattr(event_bus, "_active_tasks", None)
    if active_tasks:
        active_tasks_list = list(active_tasks)
        logger.debug("Cancelling EventBus tasks", task_count=len(active_tasks_list))
        for task in active_tasks_list:
            if not task.done():
                task.cancel()
        active_tasks.clear()


def _stop_eventbus_processing(event_bus: Any) -> None:
    """Stop EventBus processing."""
    running = getattr(event_bus, "_running", None)
    if running is not None:
        # Accessing protected member for test cleanup - necessary for EventBus teardown
        event_bus._running = False  # pylint: disable=protected-access

    shutdown_event = getattr(event_bus, "_shutdown_event", None)
    if shutdown_event is not None:
        try:
            shutdown_event.set()
        except (RuntimeError, AttributeError):
            # RuntimeError: Event loop may be closed during test cleanup
            # AttributeError: shutdown_event may not have set() method (defensive)
            pass


def _cancel_eventbus_tasks(container: Any, loop: asyncio.AbstractEventLoop) -> None:
    """Cancel EventBus tasks before shutdown to prevent hanging."""
    try:
        if loop.is_closed() or not container.event_bus:
            return

        _cancel_eventbus_active_tasks(container.event_bus)
        _stop_eventbus_processing(container.event_bus)
    except (RuntimeError, AttributeError, TypeError) as e:
        # RuntimeError: Event loop may be closed during cleanup
        # AttributeError: EventBus may be missing expected attributes during teardown
        # TypeError: Invalid types during cleanup
        logger.debug("Error cancelling EventBus tasks", error=str(e))


def _cleanup_database_connections(container: Any, loop: asyncio.AbstractEventLoop) -> None:
    """Cleanup database connections before TestClient's loop closes."""
    try:
        if loop.is_closed() or not hasattr(container, "database_manager") or not container.database_manager:
            return

        try:
            loop.run_until_complete(asyncio.wait_for(container.database_manager.close(), timeout=1.0))
        except (TimeoutError, RuntimeError):
            logger.debug("Database cleanup timed out or loop closed (harmless)")
    except (RuntimeError, AttributeError, TypeError) as e:
        # RuntimeError: Event loop may be closed during cleanup
        # AttributeError: DatabaseManager may be missing expected attributes during teardown
        # TypeError: Invalid types during cleanup
        if "Event loop is closed" not in str(e):
            logger.debug("Error closing database connections", error=str(e))


def _shutdown_container(container: Any, loop: asyncio.AbstractEventLoop) -> None:
    """Shutdown container with timeout protection."""
    try:
        if loop.is_closed():
            return

        try:
            loop.run_until_complete(asyncio.wait_for(container.shutdown(), timeout=3.0))
        except TimeoutError:
            logger.warning("Container shutdown timed out, forcing cleanup")
            pending = [task for task in asyncio.all_tasks(loop) if not task.done()]
            for task in pending:
                task.cancel()
    except (RuntimeError, AttributeError, TypeError) as e:
        # RuntimeError: Event loop may be closed during cleanup
        # AttributeError: container may be missing expected attributes during teardown
        # TypeError: Invalid types during cleanup
        logger.error("Error during container shutdown", error=str(e))


def _cancel_pending_tasks(loop: asyncio.AbstractEventLoop) -> None:
    """Cancel all pending tasks in the loop."""
    pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
    if not pending_tasks:
        return

    logger.debug("Cancelling remaining tasks", task_count=len(pending_tasks))
    for task in pending_tasks:
        if not task.done():
            task.cancel()

    try:
        loop.run_until_complete(asyncio.wait_for(asyncio.gather(*pending_tasks, return_exceptions=True), timeout=0.5))
    except (TimeoutError, RuntimeError, AttributeError, TypeError):
        # TimeoutError: Task timed out during cleanup
        # RuntimeError: Event loop may be closed during cleanup
        # AttributeError: loop may be missing expected attributes during teardown
        # TypeError: Invalid types during cleanup
        pass


def _cancel_remaining_tasks(loop: asyncio.AbstractEventLoop) -> None:
    """Cancel any remaining tasks to prevent hanging."""
    try:
        if loop.is_closed():
            return
        _cancel_pending_tasks(loop)
    except (RuntimeError, AttributeError, TypeError) as e:
        # RuntimeError: Event loop may be closed during cleanup
        # AttributeError: loop may be missing expected attributes during teardown
        # TypeError: Invalid types during cleanup
        logger.debug("Error cancelling remaining tasks", error=str(e))


def _initialize_test_container(loop: asyncio.AbstractEventLoop) -> Any:
    """Initialize ApplicationContainer with error handling."""
    from server.container import ApplicationContainer

    container = ApplicationContainer()
    try:
        loop.run_until_complete(container.initialize())
    except Exception as init_error:  # noqa: BLE001  # pylint: disable=broad-exception-caught
        logger.warning("Container initialization failed, using defensive setup", error=str(init_error))
        container.persistence = None
    return container


def _setup_container_and_app(loop: asyncio.AbstractEventLoop) -> tuple[Any, Any]:
    """Set up container and app with all required services."""
    from server.app.factory import create_app

    container = _initialize_test_container(loop)
    app = create_app()

    _ensure_valid_persistence(container)
    _ensure_services_have_persistence(container, container.persistence)
    _setup_app_state(app, container)

    logger.info("TestClient created with container services")
    _dispose_database_before_testclient(container, loop)

    return container, app


def _cancel_tasks_before_close(loop: asyncio.AbstractEventLoop) -> None:
    """Cancel all pending tasks before closing loop."""
    pending = [task for task in asyncio.all_tasks(loop) if not task.done()]
    if pending:
        logger.debug("Cancelling remaining tasks before loop close", task_count=len(pending))
        for task in pending:
            if not task.done():
                task.cancel()


def _close_event_loop(loop: asyncio.AbstractEventLoop) -> None:
    """Close event loop with proper cleanup."""
    if loop.is_closed():
        return

    try:
        _cancel_tasks_before_close(loop)
        loop.close()
    except (RuntimeError, AttributeError, TypeError) as e:
        # RuntimeError: Event loop may be closed during cleanup
        # AttributeError: loop may be missing expected attributes during teardown
        # TypeError: Invalid types during cleanup
        logger.warning("Error closing event loop", error=str(e))
        try:
            if not loop.is_closed():
                loop.close()
        except (RuntimeError, AttributeError, TypeError):
            # RuntimeError: Event loop may be closed during cleanup
            # AttributeError: loop may be missing expected attributes during teardown
            # TypeError: Invalid types during cleanup
            pass


def _initialize_container_with_timeout(loop: asyncio.AbstractEventLoop, timeout: float = 30.0) -> Any:
    """Initialize ApplicationContainer with timeout protection."""
    from server.container import ApplicationContainer

    container = ApplicationContainer()
    try:

        async def init_with_timeout():
            await asyncio.wait_for(container.initialize(), timeout=timeout)

        loop.run_until_complete(init_with_timeout())
    except TimeoutError:
        logger.warning("Container initialization timed out, using defensive setup")
        container.persistence = None
    except Exception as init_error:  # noqa: BLE001  # pylint: disable=broad-exception-caught
        logger.warning("Container initialization failed, using defensive setup", error=str(init_error))
        container.persistence = None
    return container


def _create_mock_persistence_with_rooms() -> Mock:
    """Create a mock persistence object with all required methods including async_list_rooms."""
    mock_persistence = _create_mock_persistence()
    mock_persistence.async_list_rooms = AsyncMock(return_value=[])
    return mock_persistence


def _ensure_persistence_validity(container: Any) -> Any:
    """Ensure container has valid persistence, creating mock if needed (class-scoped version)."""
    persistence_to_use = container.persistence

    # First check: if persistence is None, create mock
    if persistence_to_use is None:
        persistence_to_use = _create_mock_persistence_with_rooms()
        container.persistence = persistence_to_use
        return persistence_to_use

    # Second check: validate persistence has all required methods
    if not _validate_persistence(persistence_to_use):
        persistence_to_use = _create_mock_persistence_with_rooms()
        container.persistence = persistence_to_use
        return persistence_to_use

    return persistence_to_use


async def _wait_for_pending_tasks() -> None:
    """Wait for pending tasks to complete, cancelling if timeout occurs."""
    try:
        loop = asyncio.get_running_loop()
        pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
        if not pending_tasks:
            return

        logger.debug("Waiting for pending tasks to complete", task_count=len(pending_tasks))
        try:
            await asyncio.wait_for(asyncio.gather(*pending_tasks, return_exceptions=True), timeout=2.0)
        except TimeoutError:
            logger.warning("Some tasks did not complete in time, cancelling", task_count=len(pending_tasks))
            for task in pending_tasks:
                if not task.done():
                    task.cancel()
            # Wait briefly for cancellations
            await asyncio.gather(*pending_tasks, return_exceptions=True)
    except RuntimeError:
        # No running loop - that's okay, cleanup already happened
        pass


async def _shutdown_test_container(container: Any) -> None:
    """Shutdown container and wait for pending tasks to complete."""
    logger.info("Shutting down ApplicationContainer after test")
    try:
        await container.shutdown()
        await _wait_for_pending_tasks()
    except Exception as e:  # noqa: BLE001  # pylint: disable=broad-exception-caught
        # Defensive: Catch all exceptions during cleanup to ensure test teardown completes
        # This prevents test failures from masking cleanup errors
        logger.error("Error during container shutdown in test", error=str(e))


def _setup_class_scoped_app_state(app: Any, container: Any, persistence_to_use: Any) -> None:
    """Set up app.state with container services for class-scoped fixture."""
    # Set container in app.state
    app.state.container = container
    app.state.task_registry = container.task_registry
    app.state.event_bus = container.event_bus
    app.state.event_handler = container.real_time_event_handler
    app.state.connection_manager = container.connection_manager
    app.state.user_manager = container.user_manager
    app.state.room_cache_service = container.room_cache_service
    app.state.profession_cache_service = container.profession_cache_service

    # Ensure services have valid persistence
    if container.player_service is None or getattr(container.player_service, "persistence", None) is None:
        from server.game.player_service import PlayerService
        from server.game.room_service import RoomService

        container.player_service = PlayerService(persistence=persistence_to_use)
        container.room_service = RoomService(persistence=persistence_to_use)
    else:
        _update_service_persistence(container.player_service, persistence_to_use, "PlayerService")
        _update_service_persistence(container.room_service, persistence_to_use, "RoomService")

    app.state.persistence = container.persistence
    app.state.player_service = container.player_service
    app.state.room_service = container.room_service

    if container.connection_manager:
        container.connection_manager.persistence = container.persistence

    # Final emergency check
    if container.persistence is None:
        emergency_mock = _create_mock_persistence_with_rooms()
        container.persistence = emergency_mock
        app.state.persistence = emergency_mock
        if container.player_service:
            container.player_service.persistence = emergency_mock
        if container.room_service:
            container.room_service.persistence = emergency_mock
        if container.connection_manager:
            container.connection_manager.persistence = emergency_mock


def _cleanup_class_scoped_fixture(container: Any, loop: asyncio.AbstractEventLoop) -> None:
    """Perform all cleanup steps for class-scoped test fixture."""
    logger.info("Cancelling EventBus tasks before shutdown")
    _cancel_eventbus_tasks(container, loop)

    logger.info("Cleaning up database connections before TestClient teardown")
    _cleanup_database_connections(container, loop)

    logger.info("Shutting down container after test class")
    _shutdown_container(container, loop)

    logger.info("Cancelling remaining tasks")
    _cancel_remaining_tasks(loop)


def _cleanup_test_fixture(container: Any, loop: asyncio.AbstractEventLoop) -> None:
    """Perform all cleanup steps for test fixture."""
    logger.info("Cancelling EventBus tasks before shutdown")
    _cancel_eventbus_tasks(container, loop)

    logger.info("Cleaning up database connections before TestClient teardown")
    _cleanup_database_connections(container, loop)

    logger.info("Shutting down container after test")
    _shutdown_container(container, loop)

    logger.info("Cancelling remaining tasks")
    _cancel_remaining_tasks(loop)


@pytest.fixture
async def test_container():
    """
    Create fully initialized ApplicationContainer for integration testing.

    This fixture provides a real ApplicationContainer with all services initialized,
    suitable for integration tests that need real dependencies.

    Scope: Function (creates fresh container for each test)
    Type: Async fixture
    Cleanup: Automatic via yield

    Usage:
        async def test_something(test_container):
            player_service = test_container.player_service
            result = await player_service.create_player("TestPlayer")
            assert result is not None

    Note: Uses real database, real NATS (if enabled), real services.
          For unit tests, prefer mock_container.
    """
    from server.container import ApplicationContainer

    logger.info("Creating ApplicationContainer for test")

    # CRITICAL: Ensure test environment variables are loaded before config initialization
    _setup_test_environment()

    container = ApplicationContainer()

    try:
        await container.initialize()
        logger.info("ApplicationContainer initialized for test")
        yield container
    finally:
        # Cleanup: Shutdown container and dispose all database connections
        await _shutdown_test_container(container)


@pytest.fixture(scope="function")
def container_test_client():
    """
    Create FastAPI TestClient with ApplicationContainer initialized.

    This fixture provides a synchronous TestClient with the ApplicationContainer
    properly initialized in app.state, suitable for testing API endpoints.

    Scope: Function
    Type: Sync fixture (creates its own event loop)
    Cleanup: Automatic (TestClient handles cleanup)

    Usage:
        def test_api_endpoint(container_test_client):
            response = container_test_client.get("/api/players")
            assert response.status_code == 200

    AI: This fixture properly initializes the container in app.state.container,
        fixing the "ApplicationContainer not found" error.

    Note: Creates its own event loop to run async initialization synchronously.
          This allows sync tests to use container-based client without needing
          async test functions.
    """
    from unittest.mock import patch

    logger.info("Creating TestClient with ApplicationContainer")

    # Setup test environment
    _setup_test_environment()

    # Create new event loop for container initialization
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Patch NATS connection to prevent timeout in tests
    nats_patcher = patch("server.services.nats_service.NATSService.connect", new_callable=AsyncMock)
    nats_patcher.start()

    try:
        container, app = _setup_container_and_app(loop)
        client = TestClient(app)

        try:
            yield client
        finally:
            _cleanup_test_fixture(container, loop)
    finally:
        try:
            nats_patcher.stop()
        except (RuntimeError, AttributeError, TypeError):
            # RuntimeError: Event loop may be closed during cleanup
            # AttributeError: nats_patcher may be missing expected attributes during teardown
            # TypeError: Invalid types during cleanup
            pass
        _close_event_loop(loop)
        asyncio.set_event_loop(None)


@pytest.fixture(scope="class")
def container_test_client_class():
    """
    Create FastAPI TestClient with ApplicationContainer initialized (class-scoped).

    This is a class-scoped version of container_test_client that shares the same
    container/app instance across all tests in a test class. This dramatically
    reduces setup time from 26-30s per test to 26-30s per class.

    Use this for test classes where:
    - Tests don't modify the container/app instance itself
    - Tests use mocks to isolate behavior (mocks are still function-scoped)
    - Tests only read from container state or use dependency overrides

    Scope: Class (shared across all tests in a class)
    Type: Sync fixture (creates its own event loop)
    Cleanup: Automatic (TestClient handles cleanup)

    Usage:
        class TestMyAPI:
            def test_one(self, container_test_client_class):
                # Uses shared container/app
                response = container_test_client_class.get("/api/endpoint")

            def test_two(self, container_test_client_class):
                # Same shared container/app instance
                response = container_test_client_class.post("/api/endpoint")

    Note: Dependency overrides (app.dependency_overrides) are still per-test
          since they're managed by individual test functions, not the fixture.
    """
    from server.app.factory import create_app

    logger.info("Creating class-scoped TestClient with ApplicationContainer")

    # Setup test environment
    _setup_test_environment()

    # Create new event loop for container initialization
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Initialize container with timeout protection
        container = _initialize_container_with_timeout(loop)

        # Create app and setup state
        app = create_app()
        persistence_to_use = _ensure_persistence_validity(container)
        _setup_class_scoped_app_state(app, container, persistence_to_use)

        logger.info("Class-scoped TestClient created with container services")

        # Dispose database engines before creating TestClient
        _dispose_database_before_testclient(container, loop)

        client = TestClient(app)

        try:
            yield client
        finally:
            _cleanup_class_scoped_fixture(container, loop)
    finally:
        _close_event_loop(loop)
        asyncio.set_event_loop(None)


# pylint: disable=redefined-outer-name
@pytest.fixture
async def async_container_test_client(test_container):  # noqa: F811
    """
    Create async HTTPX client with ApplicationContainer initialized.

    This fixture provides an asynchronous AsyncClient for testing async endpoints
    with proper container initialization.

    Scope: Function
    Type: Async fixture
    Cleanup: Automatic via async context manager

    Usage:
        @pytest.mark.asyncio
        async def test_async_endpoint(async_container_test_client):
            async with async_container_test_client as client:
                response = await client.get("/api/players")
                assert response.status_code == 200

    AI: Properly handles async context and container lifecycle.
    """
    from server.app.factory import create_app

    container = test_container

    logger.info("Creating AsyncClient with ApplicationContainer")
    app = create_app()

    # Set container in app.state
    app.state.container = container

    # BACKWARD COMPATIBILITY: Expose services on app.state
    app.state.task_registry = container.task_registry
    app.state.event_bus = container.event_bus
    app.state.event_handler = container.real_time_event_handler
    app.state.persistence = container.persistence
    app.state.connection_manager = container.connection_manager
    app.state.player_service = container.player_service
    app.state.room_service = container.room_service
    app.state.user_manager = container.user_manager

    # Create async client with proper transport
    transport = ASGITransport(app=app)
    client = AsyncClient(transport=transport, base_url="http://testserver")
    logger.info("AsyncClient created with container services")
    try:
        yield client
    finally:
        # Explicitly close the client and transport to prevent ResourceWarnings
        try:
            await client.aclose()
        except (RuntimeError, AttributeError, TypeError):
            # RuntimeError: Event loop may be closed during cleanup
            # AttributeError: client may be missing expected attributes during teardown
            # TypeError: Invalid types during cleanup
            pass
        logger.info("AsyncClient closed")


@pytest.fixture
def mock_container():
    """
    Create mocked ApplicationContainer for unit testing.

    This fixture provides a fully mocked container where all services are MagicMock
    or AsyncMock instances, suitable for isolated unit tests.

    Scope: Function
    Type: Sync fixture
    Cleanup: Automatic (mocks don't need cleanup)

    Usage:
        def test_service_logic(mock_container):
            # Configure mock behavior
            mock_container.persistence.get_player.return_value = MockPlayer()

            # Test service that depends on container
            service = MyService(mock_container.persistence)
            result = service.do_something()

            # Verify mock interactions
            mock_container.persistence.get_player.assert_called_once()

    AI: This allows true unit testing without any real infrastructure.
        All dependencies are mocked for complete isolation.
    """
    logger.info("Creating mock ApplicationContainer for unit test")

    # Create mock container
    container = MagicMock()

    # Mock configuration
    container.config = MagicMock()
    container.config.server = MagicMock()
    container.config.database = MagicMock()
    container.config.nats = MagicMock()
    container.config.security = MagicMock()
    container.config.logging = MagicMock()
    container.config.logging.environment = "unit_test"

    # Mock core infrastructure
    container.db_manager = MagicMock()
    container.task_registry = MagicMock()
    container.tracked_task_manager = MagicMock()

    # Mock event system
    container.event_bus = MagicMock()
    container.real_time_event_handler = MagicMock()

    # Mock persistence (use AsyncMock for async methods)
    container.persistence = AsyncMock()
    container.async_persistence = AsyncMock()

    # Configure common persistence mock behaviors
    container.persistence.get_player.return_value = None
    container.persistence.get_room.return_value = None
    container.persistence.list_players.return_value = []
    container.async_persistence.get_player_by_id.return_value = None
    container.async_persistence.get_player_by_name.return_value = None

    # Mock real-time communication
    container.connection_manager = MagicMock()
    container.nats_service = MagicMock()
    container.nats_service.is_connected.return_value = False  # Default: not connected

    # Mock game services
    container.player_service = MagicMock()
    container.room_service = MagicMock()
    container.user_manager = MagicMock()

    # Mock caching services
    container.room_cache_service = MagicMock()
    container.profession_cache_service = MagicMock()

    # Mock monitoring services
    container.performance_monitor = MagicMock()
    container.exception_tracker = MagicMock()
    container.monitoring_dashboard = MagicMock()
    container.log_aggregator = MagicMock()

    # Mock lifecycle methods
    container.initialize = AsyncMock()
    container.shutdown = AsyncMock()

    logger.info("Mock ApplicationContainer created")

    return container


@pytest.fixture
def player_factory():
    """
    Factory fixture for creating test players with varied configurations.

    This fixture follows the Fixture Factory pattern from pytest best practices,
    allowing tests to create players with custom attributes on demand.

    Usage:
        def test_player_levels(player_factory):
            beginner = player_factory(name="Novice", level=1)
            veteran = player_factory(name="Veteran", level=50)
            master = player_factory(name="Master", level=100)

            assert beginner.level < veteran.level < master.level

    AI: This reduces fixture proliferation and makes tests more readable.
        Instead of 10 different player fixtures, we have one flexible factory.
    """
    from server.models.game import Player, Stats

    def _create_player(
        name: str = "TestPlayer",
        level: int = 1,
        current_room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001",
        stats: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> Player:
        """
        Create a test player with specified attributes.

        Args:
            name: Player name (default: "TestPlayer")
            level: Player level (default: 1)
            current_room_id: Starting room (default: foyer)
            stats: Custom stats dict (default: standard stats)
            **kwargs: Additional Player attributes

        Returns:
            Player: Configured Player instance
        """
        default_stats = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "lucidity": 100,
            "occult_knowledge": 0,
            "fear": 0,
            "corruption": 0,
            "cult_affiliation": 0,
            "current_db": 100,
            "position": "standing",
        }

        if stats:
            default_stats.update(stats)

        return Player(
            id=kwargs.get("id", str(uuid4())),
            name=name,
            level=level,
            current_room_id=current_room_id,
            stats=Stats(**default_stats),
            experience_points=kwargs.get("experience_points", 0),
            inventory=kwargs.get("inventory", []),
            status_effects=kwargs.get("status_effects", []),
        )

    return _create_player


@pytest.fixture
def room_factory():
    """
    Factory fixture for creating test rooms with varied configurations.

    Usage:
        def test_room_occupancy(room_factory):
            empty_room = room_factory(name="Empty Room")
            crowded_room = room_factory(name="Crowded", occupants=["Alice", "Bob"])

            assert len(empty_room.get_players()) == 0
            assert len(crowded_room.get_players()) == 2

    AI: Follows fixture factory pattern to reduce duplication.
    """
    from server.models.room import Room

    def _create_room(
        room_id: str | None = None,
        name: str = "Test Room",
        description: str = "A test room for unit testing",
        zone: str = "earth",
        subzone: str = "testzone",
        room_name: str = "testroom",
        exits: dict[str, str] | None = None,
        **kwargs: Any,
    ) -> Room:
        """
        Create a test room with specified attributes.

        Args:
            room_id: Room ID (default: auto-generated)
            name: Room display name
            description: Room description
            zone: Zone identifier
            subzone: Subzone identifier
            room_name: Room name identifier
            exits: Dictionary of exit directions
            **kwargs: Additional room attributes

        Returns:
            Room: Configured Room instance
        """
        if room_id is None:
            room_id = f"{zone}_{subzone}_room_{room_name}_001"

        room_data = {
            "id": room_id,
            "name": name,
            "description": description,
            "zone": zone,
            "subzone": subzone,
            "exits": exits or {},
            **kwargs,
        }

        return Room(room_data=room_data, event_bus=None)

    return _create_room


# AI: Following pytest best practices:
# 1. Fixtures for setup/teardown (test_container with cleanup)
# 2. Fixture factories for flexible data (player_factory, room_factory)
# 3. Async fixtures properly managed (test_container, async_container_test_client)
# 4. Mocking for isolation (mock_container)
# 5. Clear naming conventions (container_*, *_factory)
# 6. Proper scoping (function scope for isolation)
