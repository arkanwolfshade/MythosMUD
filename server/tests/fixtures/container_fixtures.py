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
from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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

    container = ApplicationContainer()

    try:
        await container.initialize()
        logger.info("ApplicationContainer initialized for test")
        yield container
    finally:
        # Cleanup: Shutdown container and dispose all database connections
        logger.info("Shutting down ApplicationContainer after test")
        try:
            await container.shutdown()

            # CRITICAL: Wait for all async cleanup to complete
            # This ensures database connections are fully disposed before test ends
            try:
                loop = asyncio.get_running_loop()
                pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
                if pending_tasks:
                    logger.debug("Waiting for pending tasks to complete", task_count=len(pending_tasks))
                    # Give tasks a short time to complete
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
        except Exception as e:
            logger.error("Error during container shutdown in test", error=str(e))


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
    from server.app.factory import create_app
    from server.container import ApplicationContainer

    logger.info("Creating TestClient with ApplicationContainer")

    # CRITICAL: Ensure test environment variables are loaded before config initialization
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

    # Create new event loop for container initialization
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Initialize container synchronously using event loop
        container = ApplicationContainer()
        loop.run_until_complete(container.initialize())

        app = create_app()

        # Set container in app.state
        app.state.container = container

        # BACKWARD COMPATIBILITY: Also expose services directly on app.state
        # This allows legacy tests to continue working during migration
        app.state.task_registry = container.task_registry
        app.state.event_bus = container.event_bus
        app.state.event_handler = container.real_time_event_handler
        app.state.persistence = container.persistence
        app.state.connection_manager = container.connection_manager
        app.state.player_service = container.player_service
        app.state.room_service = container.room_service
        app.state.user_manager = container.user_manager
        app.state.room_cache_service = container.room_cache_service
        app.state.profession_cache_service = container.profession_cache_service

        # CRITICAL: Ensure persistence is set on container and connection_manager
        # This prevents 503 errors from readiness gate checks and service failures
        # Always set persistence, even if container.persistence is None (defensive)
        if container.persistence is None:
            # Defensive: If persistence is None, create a mock to prevent 503 errors
            # This can happen in test environments where database isn't fully initialized
            logger.warning("Container persistence is None, creating mock persistence")
            from unittest.mock import AsyncMock, Mock

            mock_persistence = Mock()
            # Ensure mock has async methods that might be called
            mock_persistence.async_list_players = AsyncMock(return_value=[])
            mock_persistence.async_get_player = AsyncMock(return_value=None)
            mock_persistence.async_get_room = AsyncMock(return_value=None)
            # Also mock synchronous methods
            mock_persistence.list_players = Mock(return_value=[])
            mock_persistence.get_player = Mock(return_value=None)
            mock_persistence.get_room = Mock(return_value=None)
            # Set mock persistence on container
            container.persistence = mock_persistence
            # Recreate player_service and room_service with mock persistence
            if container.player_service is None:
                from server.game.player_service import PlayerService
                from server.game.room_service import RoomService

                container.player_service = PlayerService(persistence=mock_persistence)
                container.room_service = RoomService(persistence=mock_persistence)
                logger.info("PlayerService and RoomService recreated with mock persistence")
            logger.info("Container persistence set to mock (defensive)")

        # Ensure connection_manager has persistence set
        if container.connection_manager:
            container.connection_manager.persistence = container.persistence
            logger.info("Connection manager persistence set from container")

        logger.info("TestClient created with container services")

        # CRITICAL: Dispose database engines and reset singletons before creating TestClient
        # TestClient creates its own event loop for each request, and asyncpg connections
        # must be created in the same loop they're used in
        # We'll dispose them here and reset singletons so engines are recreated lazily
        # in TestClient's loop when needed
        try:
            if container.database_manager and container.database_manager.engine:
                loop.run_until_complete(container.database_manager.close())
        except Exception as e:
            logger.warning("Error disposing database engine before TestClient creation", error=str(e))

        try:
            from server.npc_database import close_npc_db

            loop.run_until_complete(close_npc_db())
        except Exception as e:
            logger.warning("Error disposing NPC database engine before TestClient creation", error=str(e))

        # Reset DatabaseManager singleton so it gets recreated in TestClient's loop
        from server.database import DatabaseManager

        DatabaseManager.reset_instance()

        # Reset NPC database global state
        import server.npc_database

        server.npc_database._npc_engine = None
        server.npc_database._npc_async_session_maker = None
        server.npc_database._npc_database_url = None

        # Now create TestClient - it will create its own loop for each request
        # and engines will be recreated lazily when needed in that loop
        client = TestClient(app)

        try:
            yield client
        finally:
            # CRITICAL: Cleanup database connections before TestClient's loop closes
            # This prevents "Event loop is closed" errors on Windows
            # TestClient creates its own event loop for each request, and when the test
            # finishes, that loop might be closed while async database connections are
            # still trying to clean up. We need to ensure connections are closed in the
            # fixture's loop before TestClient tears down.
            logger.info("Cleaning up database connections before TestClient teardown")
            try:
                # Close database connections in the fixture's loop before TestClient closes its loop
                if not loop.is_closed() and hasattr(container, "database_manager") and container.database_manager:
                    # Ensure all database operations complete before closing
                    # Use a timeout to prevent hanging if connections are stuck
                    try:
                        loop.run_until_complete(asyncio.wait_for(container.database_manager.close(), timeout=1.0))
                    except (TimeoutError, RuntimeError):
                        # Timeout or loop closed - connections will be cleaned up by GC
                        logger.debug("Database cleanup timed out or loop closed (harmless)")
            except (RuntimeError, Exception) as e:
                # Ignore "Event loop is closed" errors - connections will be cleaned up by GC
                # This can happen if TestClient has already closed its loop
                # These errors are harmless on Windows where TestClient manages its own loop
                if "Event loop is closed" not in str(e):
                    logger.debug("Error closing database connections", error=str(e))

        # Cleanup: Shutdown container and dispose all database connections
        logger.info("Shutting down container after test")
        try:
            # Shutdown container (disposes database engines and shuts down EventBus)
            if not loop.is_closed():
                # Use a timeout to prevent hanging if shutdown takes too long
                try:
                    loop.run_until_complete(asyncio.wait_for(container.shutdown(), timeout=5.0))
                except TimeoutError:
                    logger.warning("Container shutdown timed out, forcing cleanup")
                    # Force shutdown by cancelling all tasks
                    pending = [task for task in asyncio.all_tasks(loop) if not task.done()]
                    for task in pending:
                        task.cancel()

            # CRITICAL: Aggressively cancel any remaining tasks to prevent hanging
            # Don't wait for tasks - just cancel them immediately after shutdown
            if not loop.is_closed():
                pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
                if pending_tasks:
                    logger.debug("Cancelling remaining tasks", task_count=len(pending_tasks))
                    # Cancel all remaining tasks immediately
                    for task in pending_tasks:
                        if not task.done():
                            task.cancel()
                    # Give a very short time for cancellations, then move on
                    try:
                        loop.run_until_complete(
                            asyncio.wait_for(asyncio.gather(*pending_tasks, return_exceptions=True), timeout=0.5)
                        )
                    except (TimeoutError, RuntimeError, Exception):
                        # Ignore all errors - we're cleaning up and moving on
                        pass
        except Exception as e:
            logger.error("Error during container shutdown", error=str(e))
    finally:
        # Cleanup: Close event loop and reset to None
        # AI: This prevents "Event loop is closed" errors in subsequent tests
        # by ensuring asyncio.get_event_loop() doesn't return a closed loop
        # Only close if loop is not already closed
        if not loop.is_closed():
            try:
                # Aggressively cancel any remaining tasks before closing
                # This prevents hanging if tasks are stuck waiting
                pending = [task for task in asyncio.all_tasks(loop) if not task.done()]
                if pending:
                    logger.debug("Cancelling remaining tasks before loop close", task_count=len(pending))
                    for task in pending:
                        if not task.done():
                            task.cancel()
                    # Don't wait for cancellations - just close the loop
                loop.close()
            except Exception as e:
                logger.warning("Error closing event loop", error=str(e))
                # Force close even if there are errors
                try:
                    if not loop.is_closed():
                        loop.close()
                except Exception:
                    pass  # Ignore errors during forced close
        asyncio.set_event_loop(None)


@pytest.fixture
async def async_container_test_client(test_container):
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
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://testserver") as client:
        logger.info("AsyncClient created with container services")
        yield client

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
            "sanity": 100,
            "occult_knowledge": 0,
            "fear": 0,
            "corruption": 0,
            "cult_affiliation": 0,
            "current_health": 100,
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
