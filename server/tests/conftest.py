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
# Use explicit assignment if empty, not setdefault (which only sets if key doesn't exist)
if not os.environ.get("MYTHOSMUD_ADMIN_PASSWORD"):
    os.environ["MYTHOSMUD_ADMIN_PASSWORD"] = "test-admin-password-for-development"
# Fix MYTHOSMUD_JWT_SECRET: handle empty strings (setdefault only sets if key doesn't exist)
if not os.environ.get("MYTHOSMUD_JWT_SECRET"):
    os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-key-for-testing-only"
os.environ.setdefault("SERVER_PORT", "54731")
os.environ.setdefault("SERVER_HOST", "127.0.0.1")
os.environ.setdefault("LOGGING_ENVIRONMENT", "unit_test")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
# Use explicit assignment to ensure DATABASE_NPC_URL is always set (not just setdefault)
# This prevents test isolation issues where env vars might be cleared by other tests
if not os.environ.get("DATABASE_NPC_URL"):
    os.environ["DATABASE_NPC_URL"] = "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
os.environ.setdefault("GAME_ALIASES_DIR", "data/unit_test/players/aliases")

# Imports must come after environment variables to prevent config loading failures
from server.config import (
    reset_config,  # noqa: E402  # Reason: Import must come after environment variables to prevent config loading failures during test setup
)
from server.structured_logging.enhanced_logging_config import (
    get_logger,  # noqa: E402  # Reason: Import must come after environment variables to prevent config loading failures during test setup
)

logger = get_logger(__name__)

project_root = Path(__file__).parent.parent.parent

# Register fixture plugins
pytest_plugins = [
    "server.tests.fixtures.shared",
    "server.tests.fixtures.unit",
    "server.tests.fixtures.integration",
]


@pytest.fixture(autouse=True)
def ensure_test_environment_variables() -> Generator[None, None, None]:
    """
    Ensure critical environment variables are set before each test.

    Some tests may clear environment variables (e.g., DATABASE_NPC_URL),
    so we ensure they're always set before each test runs.
    """
    # Ensure DATABASE_NPC_URL is always set (some tests clear it)
    os.environ.setdefault("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
    yield
    # No cleanup needed - env vars persist for next test


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
        # WindowsSelectorEventLoopPolicy only exists on Windows - using getattr to avoid mypy error on non-Windows platforms
        windows_policy = getattr(asyncio, "WindowsSelectorEventLoopPolicy", None)
        if windows_policy is None:
            raise RuntimeError("WindowsSelectorEventLoopPolicy not available on this platform")
        policy: asyncio.AbstractEventLoopPolicy = windows_policy()
    else:
        try:
            import uvloop  # type: ignore[import-not-found]  # Reason: uvloop is optional dependency and may not have type stubs, import-not-found is expected when uvloop is not installed

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


def pytest_collection_modifyitems(config: Any, items: list[Any]) -> None:  # noqa: ARG001  # Reason: Pytest hook signature requires config parameter even if unused  # pylint: disable=unused-argument  # Reason: Pytest hook signature requires config parameter even if unused
    """
    Auto-mark tests based on their file path.

    Tests in unit/ get @pytest.mark.unit
    Tests in integration/ get @pytest.mark.integration (and serial for xdist safety)
    Tests in e2e/ get @pytest.mark.e2e

    Note: `config` parameter is required by pytest hookspec but not used in this implementation.
    Suppressed lint warnings: ARG001 (ruff unused argument), unused-argument (pylint).
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
