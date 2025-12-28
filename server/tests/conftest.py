"""
Test configuration and fixtures for MythosMUD greenfield test suite.

This module provides core fixtures and test isolation for the new test suite.
"""

"""
Test configuration and fixtures for MythosMUD greenfield test suite.

This module provides core fixtures and test isolation for the new test suite.
"""

import asyncio
import os
import random
from collections.abc import Generator
from pathlib import Path
from typing import Any

import pytest

# Set critical environment variables immediately to prevent module-level config loading failures
os.environ.setdefault("MYTHOSMUD_ADMIN_PASSWORD", "test-admin-password-for-development")
os.environ.setdefault("MYTHOSMUD_JWT_SECRET", "test-jwt-secret-key-for-testing-only")
os.environ.setdefault("SERVER_PORT", "54731")
os.environ.setdefault("SERVER_HOST", "127.0.0.1")
os.environ.setdefault("LOGGING_ENVIRONMENT", "unit_test")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
os.environ.setdefault("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
os.environ.setdefault("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

from server.config import reset_config
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

project_root = Path(__file__).parent.parent.parent

# Register fixture plugins
pytest_plugins = [
    "server.tests.fixtures.shared",
    "server.tests.fixtures.unit",
    "server.tests.fixtures.integration",
]


@pytest.fixture(autouse=True)
def reset_config_singleton() -> Generator[None, None, None]:
    """
    Reset config singleton before and after each test.

    In test mode, get_config() always returns fresh instances (no caching),
    but we still clear global state for consistency and to handle any edge cases.
    """
    # Reset before test to ensure clean state
    reset_config()
    yield
    # Reset after test to prevent state leakage to next test
    reset_config()


@pytest.fixture(autouse=True)
def deterministic_random_seed() -> Generator[None, None, None]:
    """Set deterministic random seed for reproducible tests."""
    random.seed(42)
    yield
    # Seed is reset automatically per test


@pytest.fixture(scope="session", autouse=True)
def configure_event_loop_policy() -> Generator[None, None, None]:
    """
    Configure event loop policy suitable for Windows/asyncio.

    CRITICAL: On Windows, we MUST use WindowsSelectorEventLoopPolicy for asyncpg compatibility.
    ProactorEventLoop causes "Event loop is closed" errors with asyncpg connections.
    """
    if os.name == "nt":  # Windows
        # WindowsSelectorEventLoopPolicy is required for asyncpg on Windows
        # ProactorEventLoop has known issues with asyncpg's connection handling
        policy = asyncio.WindowsSelectorEventLoopPolicy()
    else:
        try:
            import uvloop

            policy = uvloop.EventLoopPolicy()
        except ImportError:
            policy = asyncio.DefaultEventLoopPolicy()

    # Set the policy before any async operations
    asyncio.set_event_loop_policy(policy)
    yield
    # Policy persists across tests - don't reset it


@pytest.fixture
def test_logger() -> Any:
    """Provide a logger for tests."""
    return get_logger(__name__)


def pytest_collection_modifyitems(config: Any, items: list[Any]) -> None:
    """
    Auto-mark tests based on their file path.

    Tests in unit/ get @pytest.mark.unit
    Tests in integration/ get @pytest.mark.integration (and serial for xdist safety)
    Tests in e2e/ get @pytest.mark.e2e
    """
    for item in items:
        file_path = str(item.fspath)

        if "/unit/" in file_path or "\\unit\\" in file_path:
            item.add_marker(pytest.mark.unit)
        elif "/integration/" in file_path or "\\integration\\" in file_path:
            item.add_marker(pytest.mark.integration)
            # Mark integration tests as serial to avoid event loop conflicts in parallel execution
            item.add_marker(pytest.mark.serial)
        elif "/e2e/" in file_path or "\\e2e\\" in file_path:
            item.add_marker(pytest.mark.e2e)
