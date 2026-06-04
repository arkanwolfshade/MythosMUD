"""
Test configuration and fixtures for MythosMUD greenfield test suite.

This module provides core fixtures and test isolation for the new test suite.
"""

import asyncio
import importlib
import os
import random
from collections.abc import Callable, Generator, Mapping
from pathlib import Path
from typing import cast
from urllib.parse import urlparse

import pytest
from structlog.stdlib import BoundLogger

# Protected DBs: tests must NEVER run against these (integration tests truncate tables).
# If DATABASE_URL points here, we overwrite with mythos_unit so pytest cannot touch mythos_dev.
_PROTECTED_DB_NAMES = ("mythos_dev", "mythos_stage", "mythos_prod")
_DEFAULT_TEST_DATABASE_URL = "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"


def _get_db_name_from_url(url: str) -> str:
    """Extract database name from a PostgreSQL URL. Returns empty string on parse failure."""
    try:
        parsed = urlparse(url)
        path = (parsed.path or "").strip("/")
        return path.split("/")[0] if path else ""
    except (ValueError, AttributeError, IndexError, TypeError):
        return ""


# Set critical environment variables immediately to prevent module-level config loading failures
# Use explicit assignment if empty, not setdefault (which only sets if key doesn't exist)
if not os.environ.get("MYTHOSMUD_ADMIN_PASSWORD"):
    os.environ["MYTHOSMUD_ADMIN_PASSWORD"] = "test-admin-password-for-development"
# Fix MYTHOSMUD_JWT_SECRET: handle empty strings (setdefault only sets if key doesn't exist)
if not os.environ.get("MYTHOSMUD_JWT_SECRET"):
    os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-key-for-testing-only"
# Set token secrets for UserManager tests (must not start with 'dev-' per validation)
if not os.environ.get("MYTHOSMUD_RESET_TOKEN_SECRET"):
    os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-testing-only-secure-value"
if not os.environ.get("MYTHOSMUD_VERIFICATION_TOKEN_SECRET"):
    os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-testing-only-secure-value"
if "SERVER_PORT" not in os.environ:
    os.environ["SERVER_PORT"] = "54768"
if "SERVER_HOST" not in os.environ:
    os.environ["SERVER_HOST"] = "127.0.0.1"
if "LOGGING_ENVIRONMENT" not in os.environ:
    os.environ["LOGGING_ENVIRONMENT"] = "unit_test"
# CRITICAL: Never run tests against mythos_dev. If DATABASE_URL points at a protected DB, force mythos_unit.
# setdefault alone would leave mythos_dev in place if e.g. .env or shell had it set, allowing truncation.
_current_db_url = os.environ.get("DATABASE_URL", "")
_current_db_name = _get_db_name_from_url(_current_db_url)
if _current_db_name in _PROTECTED_DB_NAMES:
    os.environ["DATABASE_URL"] = _DEFAULT_TEST_DATABASE_URL
else:
    if "DATABASE_URL" not in os.environ:
        os.environ["DATABASE_URL"] = _DEFAULT_TEST_DATABASE_URL
# Use explicit assignment to ensure DATABASE_NPC_URL is always set (not just setdefault)
# This prevents test isolation issues where env vars might be cleared by other tests
if not os.environ.get("DATABASE_NPC_URL"):
    os.environ["DATABASE_NPC_URL"] = "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
if "GAME_ALIASES_DIR" not in os.environ:
    os.environ["GAME_ALIASES_DIR"] = "data/unit_test/players/aliases"
# Unit tests use schema mythos_unit in database mythos_unit (not public)
if "POSTGRES_SEARCH_PATH" not in os.environ:
    os.environ["POSTGRES_SEARCH_PATH"] = "mythos_unit"
# Force NATS TLS off for unit tests so config validation does not require cert files (not present in CI)
os.environ["NATS_TLS_ENABLED"] = "false"

# Imports must come after environment variables to prevent config loading failures
from server.config import (  # pylint: disable=wrong-import-position  # noqa: E402  # Reason: Import must come after environment variables to prevent config loading failures during test setup
    reset_config,
)
from server.structured_logging.enhanced_logging_config import (  # pylint: disable=wrong-import-position  # noqa: E402  # Reason: Import must come after environment variables to prevent config loading failures during test setup
    get_logger,
)

logger = get_logger(__name__)

project_root = Path(__file__).parent.parent.parent

# Register fixture plugins
pytest_plugins = [
    "server.tests.fixtures.shared",
    "server.tests.fixtures.unit",
    "server.tests.fixtures.integration",
]


# autouse: truly global - ensures env vars are set before every test (some tests clear them)
@pytest.fixture(autouse=True)
def ensure_test_environment_variables() -> Generator[None, None, None]:
    """
    Ensure critical environment variables are set before each test.

    Some tests may clear environment variables (e.g., DATABASE_NPC_URL),
    so we ensure they're always set before each test runs.
    """
    # Ensure DATABASE_NPC_URL is always set (some tests clear it)
    if "DATABASE_NPC_URL" not in os.environ:
        os.environ["DATABASE_NPC_URL"] = "postgresql+asyncpg://postgres:Cthulhu1@localhost:5432/mythos_unit"
    yield
    # No cleanup needed - env vars persist for next test


# autouse: truly global - prevents config singleton state from leaking between tests
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


# autouse: truly global - reproducible tests; non-interfering
@pytest.fixture(autouse=True)
def deterministic_random_seed() -> Generator[None, None, None]:
    """Set deterministic random seed for reproducible tests."""
    random.seed(42)
    yield
    # Seed is reset automatically per test


def _create_test_event_loop() -> asyncio.AbstractEventLoop:
    """
    Create an event loop suitable for MythosMUD tests.

    CRITICAL: On Windows, SelectorEventLoop is required for asyncpg compatibility.
    ProactorEventLoop causes "Event loop is closed" errors with asyncpg connections.
    """
    if os.name == "nt":
        return asyncio.SelectorEventLoop()
    # uvloop is optional (Linux/macOS only; excluded on Windows) - load dynamically to avoid import errors.
    try:
        uvloop_module = importlib.import_module("uvloop")
        new_event_loop_fn = cast(
            Callable[[], asyncio.AbstractEventLoop] | None,
            getattr(uvloop_module, "new_event_loop", None),
        )
        if new_event_loop_fn is not None:
            return new_event_loop_fn()
        policy_factory_cls = cast(
            Callable[[], object] | None,
            getattr(uvloop_module, "EventLoopPolicy", None),
        )
        if policy_factory_cls is not None:
            policy = policy_factory_cls()
            new_loop_fn = cast(
                Callable[[], asyncio.AbstractEventLoop] | None,
                getattr(policy, "new_event_loop", None),
            )
            if new_loop_fn is not None:
                return new_loop_fn()
    except ImportError:
        pass
    return asyncio.new_event_loop()


def pytest_asyncio_loop_factories(
    config: pytest.Config,
    item: pytest.Item,
) -> Mapping[str, Callable[[], asyncio.AbstractEventLoop]]:
    """
    Register platform-appropriate loop factories for pytest-asyncio (Python 3.14+ safe).

    Replaces the deprecated asyncio.set_event_loop_policy session fixture.
    """
    del config, item  # hook signature; factories are global for the test suite
    return {"default": _create_test_event_loop}


@pytest.fixture
def test_logger() -> BoundLogger:
    """Provide a logger for tests."""
    return get_logger(__name__)


def _test_file_in_category(file_path: str, category: str) -> bool:
    """True when the collected test file lives under a unit/integration/e2e directory."""
    return f"/{category}/" in file_path or f"\\{category}\\" in file_path


def _set_xdist_loadgroup_nodeid(item: pytest.Item, group: str) -> None:
    """Append @group to pytest Item nodeid for xdist --dist loadgroup scheduling.

    pytest.Item.nodeid is read-only; xdist loadgroup keys off _nodeid on the
    controller before workers fork. No public API exists for this assignment.
    """
    grouped_nodeid = f"{item.nodeid}@{group}"
    item._nodeid = grouped_nodeid  # pylint: disable=protected-access  # pyright: ignore[reportPrivateUsage]  # Reason: pytest Item has no public API for nodeid; required for xdist loadgroup


def _apply_path_based_markers(item: pytest.Item, use_loadgroup: bool) -> None:
    """Apply unit/integration/e2e markers (and xdist grouping) from the test file path."""
    file_path = str(item.fspath)
    if _test_file_in_category(file_path, "unit"):
        item.add_marker(pytest.mark.unit)
        return
    if _test_file_in_category(file_path, "integration"):
        item.add_marker(pytest.mark.integration)
        # Mark integration tests as serial to avoid event loop conflicts in parallel execution
        item.add_marker(pytest.mark.serial)
        # Run all integration tests in the same xdist worker to avoid shared DB truncation races
        item.add_marker(pytest.mark.xdist_group(name="integration"))
        # Controller-side nodeid suffix so loadgroup scheduler groups these tests (worker-side
        # modifyitems runs too late for the scheduler).
        if use_loadgroup:
            _set_xdist_loadgroup_nodeid(item, "integration")
        return
    if _test_file_in_category(file_path, "e2e"):
        item.add_marker(pytest.mark.e2e)


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:  # noqa: ARG001  # Reason: Pytest hook signature requires config parameter even if unused  # pylint: disable=unused-argument  # Reason: Pytest hook signature requires config parameter even if unused
    """
    Auto-mark tests based on their file path.

    Tests in unit/ get @pytest.mark.unit
    Tests in integration/ get @pytest.mark.integration (and serial for xdist safety)
    Tests in e2e/ get @pytest.mark.e2e

    When using pytest-xdist with --dist loadgroup, the scheduler (controller) uses nodeids
    to group tests. We must append @group to nodeid in the controller so the scheduler
    sees the group; otherwise integration tests would be distributed across workers and
    shared DB truncation would cause FK violations.
    Suppressed lint warnings: ARG001 (ruff unused argument), unused-argument (pylint).
    """
    dist: str = cast(str, getattr(config.option, "dist", "no"))
    use_loadgroup = dist == "loadgroup"
    for item in items:
        _apply_path_based_markers(item, use_loadgroup)
