"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.
"""

import os

# Set critical environment variables immediately to prevent module-level config loading failures
if not os.environ.get("MYTHOSMUD_ADMIN_PASSWORD") or len(os.environ.get("MYTHOSMUD_ADMIN_PASSWORD", "")) < 8:
    os.environ["MYTHOSMUD_ADMIN_PASSWORD"] = "test-admin-password-for-development"
os.environ.setdefault("SERVER_PORT", "54731")
os.environ.setdefault("SERVER_HOST", "127.0.0.1")
os.environ.setdefault("LOGGING_ENVIRONMENT", "unit_test")

import asyncio
import atexit
import weakref
from collections.abc import AsyncGenerator, Callable, Generator
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, Mock

import pytest
from dotenv import load_dotenv
from httpx import ASGITransport, AsyncClient
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import AsyncSession

from server.events.event_bus import EventBus
from server.logging.enhanced_logging_config import get_logger

pytest_plugins = [
    "server.tests.fixtures.inventory_fixtures",
    "server.tests.fixtures.container_fixtures",
]

logger = get_logger(__name__)

# Import Windows-specific logging fixes
try:
    from .windows_logging_fix import (  # pyright: ignore
        configure_windows_logging,
        disable_problematic_log_handlers,
    )

    configure_windows_logging()
    disable_problematic_log_handlers()
except ImportError:
    pass

# Import Windows-specific event loop fixes
try:
    from .windows_event_loop_fix import configure_windows_event_loops  # pyright: ignore

    configure_windows_event_loops()
except ImportError:
    pass

project_root = Path(__file__).parent.parent.parent


def _is_postgres_url(url: str) -> bool:
    return url.startswith("postgresql")


def _configure_database_urls() -> tuple[Path | None, Path | None]:
    database_url = os.getenv("DATABASE_URL")
    if not database_url or not _is_postgres_url(database_url):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL.")

    npc_database_url = os.getenv("DATABASE_NPC_URL")
    if not npc_database_url:
        os.environ["DATABASE_NPC_URL"] = database_url

    return None, None


TEST_ENV_PATH = project_root / "server" / "tests" / ".env.unit_test"
EXAMPLE_ENV_PATH = project_root / "env.unit_test.example"


def validate_test_environment() -> None:
    if not TEST_ENV_PATH.exists():
        raise FileNotFoundError(f"Required test environment file missing: {TEST_ENV_PATH}")


@pytest.hookimpl(optionalhook=True)
def pytest_configure_node(node: Any) -> None:
    npc_url = os.environ.get("DATABASE_NPC_URL")
    if not npc_url:
        raise ValueError("DATABASE_NPC_URL environment variable is required.")
    node.workerinput["MYTHOSMUD_WORKER_NPC_DB_PATH"] = npc_url


try:
    validate_test_environment()
    load_dotenv(TEST_ENV_PATH, override=False)
except Exception:  # pylint: disable=broad-exception-caught
    print("Test environment validation failed")

os.environ["MYTHOSMUD_ENV"] = "test"


def _cleanup_on_exit() -> None:
    pass


atexit.register(_cleanup_on_exit)


@pytest.fixture(scope="session")
def engine() -> Engine:
    database_url = os.getenv("DATABASE_URL", "")
    sync_url = database_url.replace("+asyncpg", "")
    return create_engine(sync_url, echo=False)


@pytest.fixture(scope="session")
def db_engine() -> Engine:
    database_url = os.getenv("DATABASE_URL", "")
    sync_url = database_url.replace("+asyncpg", "")
    return create_engine(sync_url, echo=False)


def sync_test_environment() -> None:
    npc_url = os.environ.get("DATABASE_NPC_URL")
    if npc_url:
        os.environ["MYTHOSMUD_WORKER_NPC_DB_PATH"] = npc_url


@pytest.fixture(autouse=True)
def _auto_sync_test_env() -> None:
    sync_test_environment()


def pytest_configure(config: Any) -> None:
    """Configure pytest for the session."""
    # pylint: disable=unused-argument
    sync_test_environment()


@pytest.fixture(scope="session")
def test_env_vars() -> dict[str, str]:
    return {
        "SERVER_PORT": os.getenv("SERVER_PORT", "54731"),
        "SERVER_HOST": os.getenv("SERVER_HOST", "127.0.0.1"),
    }


@pytest.fixture(scope="session", name="test_database")
def _test_database_fixture() -> str:
    return os.getenv("DATABASE_URL", "")


@pytest.fixture(scope="session", name="test_npc_database")
def _test_npc_database_fixture() -> str:
    return os.getenv("DATABASE_NPC_URL", "")


@pytest.fixture(scope="function")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    # CRITICAL: On Windows with ProactorEventLoop, ensure all pending operations
    # complete before closing the loop to prevent "Event loop is closed" errors
    try:
        # Cancel all pending tasks
        pending = asyncio.all_tasks(loop)
        for task in pending:
            task.cancel()
        # Run until all tasks are cancelled
        if pending:
            loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
    except Exception:  # pylint: disable=broad-except
        # JUSTIFICATION: Silently handle any errors during cleanup to prevent
        # test failures from cleanup issues. Some tasks might already be cancelled.
        pass
    finally:
        loop.close()


@pytest.fixture(scope="session", autouse=True)
def cleanup_session_resources() -> Generator[None, None, None]:
    yield


@pytest.fixture(autouse=True)
def cleanup_all_asyncio_tasks() -> Generator[None, None, None]:
    eventbus_instances: weakref.WeakSet[EventBus] = weakref.WeakSet()
    original_init = EventBus.__init__

    def tracking_init(self: Any, *args: Any, **kwargs: Any) -> None:
        original_init(self, *args, **kwargs)
        eventbus_instances.add(self)

    EventBus.__init__ = tracking_init  # type: ignore
    yield
    EventBus.__init__ = original_init  # type: ignore


@pytest.fixture(name="mock_application_container")
def _mock_application_container_fixture() -> Any:
    return Mock()


@pytest.fixture
def test_client(mock_application_container: Any) -> Any:  # pylint: disable=unused-argument
    from fastapi.testclient import TestClient

    from ..main import app

    return TestClient(app)


@pytest.fixture
async def async_test_client(mock_application_container: Any) -> AsyncGenerator[AsyncClient, None]:  # pylint: disable=unused-argument
    from ..main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        client.app = app  # type: ignore
        yield client


@pytest.fixture
async def async_database_session() -> AsyncGenerator[AsyncSession, None]:
    from ..database import get_async_session

    async for session in get_async_session():
        yield session
        break


@pytest.fixture
async def async_npc_database_session() -> AsyncGenerator[AsyncSession, None]:
    from ..npc_database import get_npc_session

    async for session in get_npc_session():
        yield session
        break


@pytest.fixture(name="async_event_bus")
async def _async_event_bus_fixture() -> AsyncGenerator[EventBus, None]:
    event_bus = EventBus()
    yield event_bus
    await event_bus.shutdown()


@pytest.fixture(name="async_connection_manager")
async def _async_connection_manager_fixture() -> AsyncGenerator[Any, None]:
    from ..realtime.connection_manager import ConnectionManager

    cm = ConnectionManager()
    cm.async_persistence = Mock()
    yield cm


@pytest.fixture
async def async_event_handler(async_event_bus: EventBus, async_connection_manager: Any) -> AsyncGenerator[Any, None]:
    from ..realtime.event_handler import RealTimeEventHandler

    handler = RealTimeEventHandler(async_event_bus)
    handler.connection_manager = async_connection_manager
    yield handler


@pytest.fixture(name="event_bus")
def _event_bus_fixture() -> EventBus:
    return EventBus()


@pytest.fixture(name="connection_manager")
def _connection_manager_fixture() -> Any:
    from ..realtime.connection_manager import ConnectionManager

    cm = ConnectionManager()
    cm.async_persistence = Mock()
    return cm


@pytest.fixture
def event_handler(event_bus: EventBus, connection_manager: Any) -> Any:
    from ..realtime.event_handler import RealTimeEventHandler

    handler = RealTimeEventHandler(event_bus)
    handler.connection_manager = connection_manager
    return handler


@pytest.fixture
def mock_string() -> Callable[[str], Any]:
    def _create(value: str) -> Any:
        m = MagicMock()
        m.return_value = value
        return m

    return _create


@pytest.fixture
def mock_command_string() -> Callable[[str], Any]:
    def _create(command: str) -> Any:
        m = MagicMock()
        m.return_value = command
        return m

    return _create


def pytest_runtest_makereport(item: Any, call: Any) -> Any:
    # pylint: disable=unused-argument
    return None
