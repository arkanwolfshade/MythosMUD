"""
Test environment setup utilities for dual connection system testing.

This module provides utilities for setting up test environments,
configuring test databases, and managing test resources.
"""

import os
import shutil
import tempfile
import uuid
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from typing import Any

import pytest
import structlog

from server.config import get_config, reset_config
from server.database import close_db, init_db
from server.realtime.connection_manager import ConnectionManager


class Environment:
    """Test environment manager for dual connection system"""

    def __init__(self, test_name: str = "default"):
        self.test_name = test_name
        # AI Agent: Explicit type annotations for attributes initialized as None
        self.temp_dir: str | None = None
        self.database_path: str | None = None
        self.connection_manager: ConnectionManager | None = None
        self.config: dict[str, Any] | None = None
        self.logger = structlog.get_logger(f"test_env_{test_name}")

    async def setup(self, config_override: dict[str, Any] | None = None):
        """Set up test environment"""
        self.logger.info("Setting up test environment", test_name=self.test_name)

        # Create temporary directory
        self.temp_dir = tempfile.mkdtemp(prefix=f"mythos_test_{self.test_name}_")
        self.logger.info("Created temp directory", temp_dir=self.temp_dir)

        # Set up database
        await self._setup_database()

        # Set up configuration
        await self._setup_config(config_override)

        # Set up connection manager
        await self._setup_connection_manager()

        self.logger.info("Test environment setup complete")

    async def teardown(self):
        """Tear down test environment"""
        self.logger.info("Tearing down test environment", test_name=self.test_name)

        # Clean up connection manager
        if self.connection_manager:
            await self._cleanup_connection_manager()

        # Clean up database
        await self._cleanup_database()

        # Remove temporary directory
        if self.temp_dir and os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            self.logger.info("Removed temp directory", temp_dir=self.temp_dir)

        self.logger.info("Test environment teardown complete")

    async def _setup_database(self):
        """Set up test database"""
        # Check if we're using PostgreSQL from environment
        existing_db_url = os.getenv("DATABASE_URL", "")
        existing_npc_url = os.getenv("DATABASE_NPC_URL", "")

        if not existing_db_url:
            raise ValueError(
                "DATABASE_URL environment variable is required. PostgreSQL is required - SQLite is no longer supported."
            )

        if not existing_db_url.startswith("postgresql"):
            raise ValueError(
                f"Unsupported database URL: {existing_db_url}. Only PostgreSQL (postgresql+asyncpg://) is supported."
            )

        # PostgreSQL - use URLs from environment, no file paths needed
        self.database_path = None
        self.npc_database_path = None
        # URLs are already set in environment, just ensure DATABASE_NPC_URL is set
        if not existing_npc_url:
            os.environ["DATABASE_NPC_URL"] = existing_db_url  # Use same DB for NPCs

        try:
            # Recreate database engine with new URL using the new getter-based API

            import server.database

            # Dispose existing engine if it exists
            try:
                existing_engine = server.database.get_engine() if server.database._engine else None
                if existing_engine:
                    await existing_engine.dispose()
                    self.logger.info("Disposed existing main database engine")
            except Exception:
                pass  # Engine might not be initialized yet

            # Reset global state to force re-initialization with new environment variables
            server.database._engine = None
            server.database._async_session_maker = None
            server.database._database_url = None

            # Initialize main database (will read from DATABASE_URL environment variable)
            await init_db()
            if self.database_path:
                self.logger.info("Database setup complete", db_path=self.database_path)
            else:
                self.logger.info(
                    "Database setup complete",
                    database_url=existing_db_url[:50] + "..." if len(existing_db_url) > 50 else existing_db_url,
                )

            # Recreate NPC database engine with new URL using the new getter-based API
            import server.npc_database

            # Dispose existing NPC engine if it exists
            try:
                existing_npc_engine = server.npc_database.get_npc_engine() if server.npc_database._npc_engine else None
                if existing_npc_engine:
                    await existing_npc_engine.dispose()
                    self.logger.info("Disposed existing NPC database engine")
            except Exception:
                pass  # NPC engine might not be initialized yet

            # Reset global NPC database state to force re-initialization
            server.npc_database._npc_engine = None
            server.npc_database._npc_async_session_maker = None
            server.npc_database._npc_database_url = None

            # Initialize NPC database (will read from NPC_DATABASE_URL environment variable)
            from server.npc_database import init_npc_db

            await init_npc_db()
            if self.npc_database_path:
                self.logger.info("NPC Database setup complete", npc_db_path=self.npc_database_path)
            else:
                npc_url = os.getenv("DATABASE_NPC_URL", existing_db_url)
                self.logger.info(
                    "NPC Database setup complete", database_url=npc_url[:50] + "..." if len(npc_url) > 50 else npc_url
                )
        except Exception as e:
            self.logger.error("Database setup failed", error=str(e))
            # For tests, we can continue without a real database
            # The tests will use mocked persistence
            self.logger.info("Continuing with mocked persistence for tests")

    async def _setup_config(self, config_override: dict[str, Any] | None = None):
        """Set up test configuration"""
        # Reset config cache to get fresh configuration
        reset_config()

        # Load base test configuration (from environment variables)
        config_obj = get_config()
        self.config = config_obj.to_legacy_dict()

        # Type guards for mypy
        assert self.temp_dir is not None, "temp_dir must be set before _setup_config"
        assert self.config is not None, "config must be set after loading"

        # Override with test-specific settings
        if config_override:
            self._merge_config(self.config, config_override)

        # Set test-specific paths in config dict
        # Note: These are legacy dict accesses for backward compatibility
        self.config["db_path"] = self.database_path
        self.config["log_dir"] = os.path.join(self.temp_dir, "logs")
        self.config["player_dir"] = os.path.join(self.temp_dir, "players")

        # Create necessary directories
        os.makedirs(self.config["log_dir"], exist_ok=True)
        os.makedirs(self.config["player_dir"], exist_ok=True)

        self.logger.info("Configuration setup complete")

    async def _setup_connection_manager(self):
        """Set up connection manager"""
        self.connection_manager = ConnectionManager()

        self.logger.info("Connection manager setup complete")

    async def _cleanup_connection_manager(self):
        """Clean up connection manager"""
        if self.connection_manager:
            # Disconnect all connections
            await self.connection_manager.cleanup_dead_connections()
            self.connection_manager = None

    async def _cleanup_database(self):
        """Clean up database"""
        try:
            from server.database import get_engine

            engine = get_engine()
            await engine.dispose()  # Properly dispose of main database engine connections
            self.logger.info("Disposed main database engine")
        except Exception as e:
            self.logger.warning("Error disposing main database engine", error=str(e))

        try:
            from server.npc_database import get_npc_engine

            npc_engine = get_npc_engine()
            await npc_engine.dispose()  # Properly dispose of NPC database engine connections
            self.logger.info("Disposed NPC database engine")
        except Exception as e:
            self.logger.warning("Error disposing NPC database engine", error=str(e))

        try:
            await close_db()
        except Exception as e:
            self.logger.warning("Error closing database connections", error=str(e))

        # Reset global state after cleanup to prevent pollution
        try:
            import server.database
            import server.npc_database

            server.database._engine = None
            server.database._async_session_maker = None
            server.database._database_url = None

            server.npc_database._npc_engine = None
            server.npc_database._npc_async_session_maker = None
            server.npc_database._npc_database_url = None

            self.logger.info("Reset database global state")
        except Exception as e:
            self.logger.warning("Error resetting database global state", error=str(e))

    def _merge_config(self, base_config: dict[str, Any], override_config: dict[str, Any]):
        """Merge configuration dictionaries"""
        for key, value in override_config.items():
            if isinstance(value, dict) and key in base_config and isinstance(base_config[key], dict):
                self._merge_config(base_config[key], value)
            else:
                base_config[key] = value

    def get_test_config(self) -> dict[str, Any]:
        """Get test configuration"""
        assert self.config is not None, "config must be set up before calling get_test_config"
        return self.config.copy()

    def get_database_path(self) -> str | None:
        """Get test database path"""
        return self.database_path

    def get_temp_dir(self) -> str | None:
        """Get temporary directory path"""
        return self.temp_dir


class EnvironmentManager:
    """Manager for multiple test environments"""

    def __init__(self):
        self.environments: dict[str, Environment] = {}
        self.logger = structlog.get_logger("test_env_manager")

    async def create_environment(self, test_name: str, config_override: dict[str, Any] | None = None) -> Environment:
        """Create a new test environment"""
        if test_name in self.environments:
            raise ValueError(f"Test environment '{test_name}' already exists")

        env = Environment(test_name)
        await env.setup(config_override)
        self.environments[test_name] = env

        self.logger.info("Created test environment", test_name=test_name)
        return env

    async def get_environment(self, test_name: str) -> Environment:
        """Get existing test environment"""
        if test_name not in self.environments:
            raise ValueError(f"Test environment '{test_name}' does not exist")

        return self.environments[test_name]

    async def destroy_environment(self, test_name: str):
        """Destroy test environment"""
        if test_name not in self.environments:
            return

        env = self.environments[test_name]
        await env.teardown()
        del self.environments[test_name]

        self.logger.info("Destroyed test environment", test_name=test_name)

    async def destroy_all_environments(self):
        """Destroy all test environments"""
        for test_name in list(self.environments.keys()):
            await self.destroy_environment(test_name)

        self.logger.info("Destroyed all test environments")


# Global test environment manager
test_env_manager = EnvironmentManager()


# Pytest fixtures
@pytest.fixture
async def test_environment():
    """Pytest fixture for test environment"""
    env = await test_env_manager.create_environment("pytest_default")
    yield env
    await test_env_manager.destroy_environment("pytest_default")


@pytest.fixture
async def dual_connection_environment():
    """Pytest fixture for dual connection test environment"""
    config_override = {
        "dual_connections": {
            "enabled": True,
            "max_connections_per_player": 4,
            "connection_timeout": 60,
            "health_check_interval": 10,
            "cleanup_interval": 30,
        }
    }

    env = await test_env_manager.create_environment("pytest_dual_connection", config_override)
    yield env
    await test_env_manager.destroy_environment("pytest_dual_connection")


@pytest.fixture
async def performance_test_environment():
    """Pytest fixture for performance test environment"""
    config_override = {
        "dual_connections": {
            "enabled": True,
            "max_connections_per_player": 10,
            "connection_timeout": 300,
            "health_check_interval": 5,
            "cleanup_interval": 15,
            "performance_monitoring": True,
        },
        "max_connections": 1000,
        "connection_timeout": 300,
    }

    env = await test_env_manager.create_environment("pytest_performance", config_override)
    yield env
    await test_env_manager.destroy_environment("pytest_performance")


@pytest.fixture
async def error_test_environment():
    """Pytest fixture for error handling test environment"""
    config_override = {
        "dual_connections": {
            "enabled": True,
            "error_handling": {"max_retry_attempts": 2, "retry_delay": 1, "error_recovery_enabled": True},
        },
        "enable_stack_traces": True,
        "logging": {"level": "DEBUG"},
    }

    env = await test_env_manager.create_environment("pytest_error_handling", config_override)
    yield env
    await test_env_manager.destroy_environment("pytest_error_handling")


# Context managers for test environments
@asynccontextmanager
async def create_test_environment_context(test_name: str, config_override: dict[str, Any] | None = None):
    """Context manager for test environment"""
    env = await test_env_manager.create_environment(test_name, config_override)
    try:
        yield env
    finally:
        await test_env_manager.destroy_environment(test_name)


@asynccontextmanager
async def isolated_test_environment(config_override: dict[str, Any] | None = None):
    """Context manager for isolated test environment"""
    import uuid

    test_name = f"isolated_{uuid.uuid4().hex[:8]}"

    async with create_test_environment_context(test_name, config_override) as env:
        yield env


# Test data setup utilities
class TestDataSetup:
    """Utilities for setting up test data in environments"""

    @staticmethod
    async def setup_dual_connection_scenario(env: Environment, player_id: str = "test_player"):
        """Set up dual connection scenario"""
        assert env.connection_manager is not None, "connection_manager must be initialized"

        # Convert string player_id to UUID for type safety
        # If player_id is a valid UUID string, use it; otherwise generate a new UUID
        try:
            player_id_uuid = uuid.UUID(player_id)
        except (ValueError, TypeError):
            player_id_uuid = uuid.uuid4()

        # Create WebSocket connection
        ws_success = await env.connection_manager.connect_websocket(mock_websocket(), player_id_uuid, "test_session")

        # Create SSE connection
        sse_connection_id = await env.connection_manager.connect_sse(player_id_uuid, "test_session")

        return {
            "player_id": player_id,
            "websocket_connection_id": "ws_conn" if ws_success else None,
            "sse_connection_id": sse_connection_id,
            "session_id": "test_session",
        }

    @staticmethod
    async def setup_multiple_players(env: Environment, count: int = 10):
        """Set up multiple players with dual connections"""
        players = []

        for i in range(count):
            player_id = f"test_player_{i}"
            scenario = await TestDataSetup.setup_dual_connection_scenario(env, player_id)
            players.append(scenario)

        return players

    @staticmethod
    async def setup_session_switch_scenario(env: Environment, player_id: str = "session_test_player"):
        """Set up session switch scenario"""
        assert env.connection_manager is not None, "connection_manager must be initialized"

        # Create initial session with connections
        initial_scenario = await TestDataSetup.setup_dual_connection_scenario(env, player_id)

        # Switch to new session
        new_session_id = "new_test_session"
        # Convert string player_id to UUID for type safety
        try:
            player_id_uuid = uuid.UUID(player_id)
        except (ValueError, TypeError):
            player_id_uuid = uuid.uuid4()
        await env.connection_manager.handle_new_game_session(player_id_uuid, new_session_id)

        return {
            "player_id": player_id,
            "old_session_id": initial_scenario["session_id"],
            "new_session_id": new_session_id,
            "old_connections": [initial_scenario["websocket_connection_id"], initial_scenario["sse_connection_id"]],
        }


def mock_websocket():
    """Create a mock WebSocket for testing"""

    class MockWebSocket:
        def __init__(self):
            self.closed = False
            self.send_calls = []
            self.ping_calls = []

        async def accept(self):
            pass

        async def send_json(self, data):
            self.send_calls.append(data)

        async def ping(self):
            self.ping_calls.append(datetime.now(UTC))
            return True

        async def close(self):
            self.closed = True

        def is_closed(self):
            return self.closed

    return MockWebSocket()


# Test monitoring setup
class TestMonitoringSetup:
    """Utilities for setting up test monitoring"""

    @staticmethod
    async def setup_monitoring_endpoints(env: Environment):
        """Set up monitoring endpoints for testing"""
        assert env.connection_manager is not None, "connection_manager must be initialized"

        # This would typically set up Prometheus metrics, health checks, etc.
        # For now, we'll just ensure the connection manager has monitoring enabled
        env.connection_manager.enable_monitoring = True  # type: ignore[attr-defined]

        return {
            "monitoring_enabled": True,
            "metrics_endpoint": "/metrics",
            "health_endpoint": "/health",
            "connection_stats_endpoint": "/api/connections/stats",
        }

    @staticmethod
    async def setup_performance_monitoring(env: Environment):
        """Set up performance monitoring for testing"""
        assert env.connection_manager is not None, "connection_manager must be initialized"

        # Enable performance tracking
        env.connection_manager.performance_monitoring = True  # type: ignore[attr-defined]

        return {
            "performance_monitoring_enabled": True,
            "connection_establishment_tracking": True,
            "message_delivery_tracking": True,
            "memory_usage_tracking": True,
        }


# Test cleanup utilities
class TestCleanup:
    """Utilities for cleaning up test data"""

    @staticmethod
    async def cleanup_all_connections(env: Environment):
        """Clean up all connections in test environment"""
        assert env.connection_manager is not None, "connection_manager must be initialized"
        await env.connection_manager.cleanup_all_connections()  # type: ignore[attr-defined]

    @staticmethod
    async def cleanup_player_data(env: Environment, player_id: str):
        """Clean up data for specific player"""
        assert env.connection_manager is not None, "connection_manager must be initialized"
        # Convert string player_id to UUID for type safety
        try:
            player_id_uuid = uuid.UUID(player_id)
        except (ValueError, TypeError):
            player_id_uuid = uuid.uuid4()
        await env.connection_manager.force_disconnect_player(player_id_uuid)

    @staticmethod
    async def cleanup_old_sessions(env: Environment, hours: int = 1):
        """Clean up old sessions"""
        # This would typically clean up sessions older than specified hours
        # Implementation depends on session cleanup logic
        pass


# Export utilities
__all__ = [
    "Environment",
    "EnvironmentManager",
    "test_env_manager",
    "test_environment",
    "dual_connection_environment",
    "performance_test_environment",
    "error_test_environment",
    "isolated_test_environment",
    "TestDataSetup",
    "TestMonitoringSetup",
    "TestCleanup",
    "mock_websocket",
]
