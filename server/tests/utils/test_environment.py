"""
Test environment setup utilities for dual connection system testing.

This module provides utilities for setting up test environments,
configuring test databases, and managing test resources.
"""

import os
import shutil
import tempfile
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from typing import Any

import pytest
import structlog

from server.config_loader import get_config
from server.database import close_db, init_db
from server.realtime.connection_manager import ConnectionManager


class TestEnvironment:
    """Test environment manager for dual connection system"""

    def __init__(self, test_name: str = "default"):
        self.test_name = test_name
        self.temp_dir = None
        self.database_path = None
        self.connection_manager = None
        self.config = None
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
        self.database_path = os.path.join(self.temp_dir, "test_players.db")

        # Create database directory
        os.makedirs(os.path.dirname(self.database_path), exist_ok=True)

        # Set environment variable for database URL
        os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{self.database_path}"

        # Initialize database
        await init_db()

        self.logger.info("Database setup complete", db_path=self.database_path)

    async def _setup_config(self, config_override: dict[str, Any] | None = None):
        """Set up test configuration"""
        # Load base test configuration
        self.config = get_config("server/tests/test_server_config.yaml")

        # Override with test-specific settings
        if config_override:
            self._merge_config(self.config, config_override)

        # Set test-specific paths
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
        await close_db()

    def _merge_config(self, base_config: dict[str, Any], override_config: dict[str, Any]):
        """Merge configuration dictionaries"""
        for key, value in override_config.items():
            if isinstance(value, dict) and key in base_config and isinstance(base_config[key], dict):
                self._merge_config(base_config[key], value)
            else:
                base_config[key] = value

    def get_test_config(self) -> dict[str, Any]:
        """Get test configuration"""
        return self.config.copy()

    def get_database_path(self) -> str:
        """Get test database path"""
        return self.database_path

    def get_temp_dir(self) -> str:
        """Get temporary directory path"""
        return self.temp_dir


class TestEnvironmentManager:
    """Manager for multiple test environments"""

    def __init__(self):
        self.environments: dict[str, TestEnvironment] = {}
        self.logger = structlog.get_logger("test_env_manager")

    async def create_environment(
        self, test_name: str, config_override: dict[str, Any] | None = None
    ) -> TestEnvironment:
        """Create a new test environment"""
        if test_name in self.environments:
            raise ValueError(f"Test environment '{test_name}' already exists")

        env = TestEnvironment(test_name)
        await env.setup(config_override)
        self.environments[test_name] = env

        self.logger.info("Created test environment", test_name=test_name)
        return env

    async def get_environment(self, test_name: str) -> TestEnvironment:
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
test_env_manager = TestEnvironmentManager()


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
async def test_environment_context(test_name: str, config_override: dict[str, Any] | None = None):
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

    async with test_environment_context(test_name, config_override) as env:
        yield env


# Test data setup utilities
class TestDataSetup:
    """Utilities for setting up test data in environments"""

    @staticmethod
    async def setup_dual_connection_scenario(env: TestEnvironment, player_id: str = "test_player"):
        """Set up dual connection scenario"""
        # Create WebSocket connection
        ws_connection_id = await env.connection_manager.connect_websocket(mock_websocket(), player_id, "test_session")

        # Create SSE connection
        sse_connection_id = await env.connection_manager.connect_sse(player_id, "test_session")

        return {
            "player_id": player_id,
            "websocket_connection_id": ws_connection_id,
            "sse_connection_id": sse_connection_id,
            "session_id": "test_session",
        }

    @staticmethod
    async def setup_multiple_players(env: TestEnvironment, count: int = 10):
        """Set up multiple players with dual connections"""
        players = []

        for i in range(count):
            player_id = f"test_player_{i}"
            scenario = await TestDataSetup.setup_dual_connection_scenario(env, player_id)
            players.append(scenario)

        return players

    @staticmethod
    async def setup_session_switch_scenario(env: TestEnvironment, player_id: str = "session_test_player"):
        """Set up session switch scenario"""
        # Create initial session with connections
        initial_scenario = await TestDataSetup.setup_dual_connection_scenario(env, player_id)

        # Switch to new session
        new_session_id = "new_test_session"
        await env.connection_manager.handle_new_game_session(player_id, new_session_id)

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
    async def setup_monitoring_endpoints(env: TestEnvironment):
        """Set up monitoring endpoints for testing"""
        # This would typically set up Prometheus metrics, health checks, etc.
        # For now, we'll just ensure the connection manager has monitoring enabled
        env.connection_manager.enable_monitoring = True

        return {
            "monitoring_enabled": True,
            "metrics_endpoint": "/metrics",
            "health_endpoint": "/health",
            "connection_stats_endpoint": "/api/connections/stats",
        }

    @staticmethod
    async def setup_performance_monitoring(env: TestEnvironment):
        """Set up performance monitoring for testing"""
        # Enable performance tracking
        env.connection_manager.performance_monitoring = True

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
    async def cleanup_all_connections(env: TestEnvironment):
        """Clean up all connections in test environment"""
        await env.connection_manager.cleanup_all_connections()

    @staticmethod
    async def cleanup_player_data(env: TestEnvironment, player_id: str):
        """Clean up data for specific player"""
        await env.connection_manager.force_disconnect_player(player_id)

    @staticmethod
    async def cleanup_old_sessions(env: TestEnvironment, hours: int = 1):
        """Clean up old sessions"""
        # This would typically clean up sessions older than specified hours
        # Implementation depends on session cleanup logic
        pass


# Export utilities
__all__ = [
    "TestEnvironment",
    "TestEnvironmentManager",
    "test_env_manager",
    "test_environment",
    "dual_connection_environment",
    "performance_test_environment",
    "error_test_environment",
    "test_environment_context",
    "isolated_test_environment",
    "TestDataSetup",
    "TestMonitoringSetup",
    "TestCleanup",
    "mock_websocket",
]
