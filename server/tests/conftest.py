"""
Test configuration and fixtures for MythosMUD greenfield test suite.

This module provides core fixtures and test isolation for the new test suite.
"""

import asyncio

# Set critical environment variables immediately to prevent module-level config loading failures
# #region agent log
import json
import os
import random
import time
from collections.abc import Generator
from pathlib import Path
from typing import Any

import pytest

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".cursor", "debug.log")
try:
    admin_pw_before = os.environ.get("MYTHOSMUD_ADMIN_PASSWORD", "NOT_SET")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "id": f"log_{int(time.time())}_conftest_before_setdefault",
                    "timestamp": int(time.time() * 1000),
                    "location": "conftest.py:17",
                    "message": "Before setdefault - checking MYTHOSMUD_ADMIN_PASSWORD",
                    "data": {
                        "env_var_exists": "MYTHOSMUD_ADMIN_PASSWORD" in os.environ,
                        "env_var_value": admin_pw_before[:3] + "..."
                        if len(admin_pw_before) > 3 and admin_pw_before != "NOT_SET"
                        else admin_pw_before,
                        "env_var_length": len(admin_pw_before) if admin_pw_before != "NOT_SET" else 0,
                    },
                    "sessionId": "debug-session",
                    "runId": "ci-debug",
                    "hypothesisId": "C",
                }
            )
            + "\n"
        )
except Exception:
    pass  # Ignore logging errors
# #endregion
# Use explicit assignment if empty, not setdefault (which only sets if key doesn't exist)
if not os.environ.get("MYTHOSMUD_ADMIN_PASSWORD"):
    os.environ["MYTHOSMUD_ADMIN_PASSWORD"] = "test-admin-password-for-development"
os.environ.setdefault("MYTHOSMUD_JWT_SECRET", "test-jwt-secret-key-for-testing-only")
os.environ.setdefault("SERVER_PORT", "54731")
os.environ.setdefault("SERVER_HOST", "127.0.0.1")
os.environ.setdefault("LOGGING_ENVIRONMENT", "unit_test")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
os.environ.setdefault("DATABASE_NPC_URL", "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit")
os.environ.setdefault("GAME_ALIASES_DIR", "data/unit_test/players/aliases")
# #region agent log
try:
    admin_pw_after = os.environ.get("MYTHOSMUD_ADMIN_PASSWORD", "NOT_SET")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "id": f"log_{int(time.time())}_conftest_after_setdefault",
                    "timestamp": int(time.time() * 1000),
                    "location": "conftest.py:25",
                    "message": "After setdefault - checking MYTHOSMUD_ADMIN_PASSWORD",
                    "data": {
                        "env_var_exists": "MYTHOSMUD_ADMIN_PASSWORD" in os.environ,
                        "env_var_value": admin_pw_after[:3] + "..."
                        if len(admin_pw_after) > 3 and admin_pw_after != "NOT_SET"
                        else admin_pw_after,
                        "env_var_length": len(admin_pw_after) if admin_pw_after != "NOT_SET" else 0,
                    },
                    "sessionId": "debug-session",
                    "runId": "ci-debug",
                    "hypothesisId": "D",
                }
            )
            + "\n"
        )
except Exception:
    pass  # Ignore logging errors
# #endregion

# Imports must come after environment variables to prevent config loading failures
from server.config import reset_config  # noqa: E402
from server.structured_logging.enhanced_logging_config import get_logger  # noqa: E402

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
        # WindowsSelectorEventLoopPolicy only exists on Windows - using getattr to avoid mypy error on non-Windows platforms
        windows_policy = getattr(asyncio, "WindowsSelectorEventLoopPolicy", None)
        if windows_policy is None:
            raise RuntimeError("WindowsSelectorEventLoopPolicy not available on this platform")
        policy: asyncio.AbstractEventLoopPolicy = windows_policy()
    else:
        try:
            import uvloop  # type: ignore[import-not-found]  # uvloop is optional and may not have type stubs

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
