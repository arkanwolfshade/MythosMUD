"""
Integration-tier fixtures with real database connections.
"""

import inspect
import os
from collections.abc import AsyncGenerator, Callable, Generator
from typing import Any, cast
from urllib.parse import urlparse

import pytest
from sqlalchemy.exc import InterfaceError, OperationalError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

# Ensure all table metadata is registered so create_all creates every table
# (e.g. quest_definitions, quest_offers) regardless of which test runs first.
import server.models  # noqa: F401  # Reason: Import for side effect so create_all registers all table metadata (e.g. quest_*)
from server.database import close_db, reset_database
from server.database_config_helpers import get_postgres_connect_args
from server.models.base import Base

# The only database errors the setup/cleanup fixtures may tolerate: the server going away.
_CONNECTION_ERRORS = (OperationalError, InterfaceError, OSError)

# Databases that integration tests MAY truncate (reset at will).
# ONLY these names are allowed when db_cleanup runs.
_ALLOWED_INTEGRATION_DB_NAMES = ("mythos_unit", "mythos_e2e")

# mythos_dev must NEVER be truncated or deleted by tests. Do not add it to allowed names.
_PROTECTED_DB_NAMES = ("mythos_dev", "mythos_stage", "mythos_prod")

# Every ORM table data/db/seed.sql populates (world topology plus content catalogs).
# db_cleanup must not wipe these between integration tests; flow tests create their own rows.
# make test-playwright runs integration tests against mythos_e2e, so wiping the content tables broke
# later Playwright runs on the same E2E stack (#963). A unit test fails if seed.sql gains a table
# this set misses.
_REFERENCE_SEED_TABLES = frozenset(
    {
        "zones",
        "subzones",
        "rooms",
        "room_links",
        "zone_configurations",
        "professions",
        "item_prototypes",
        "skills",
        "spells",
        "emotes",
        "emote_aliases",
        "quest_definitions",
        "quest_offers",
        "dialogue_definitions",
        "calendar_holidays",
        "calendar_npc_schedules",
    }
)


def _get_db_name_from_url(url: str) -> str:
    """Extract database name from a PostgreSQL URL. Returns empty string on parse failure."""
    try:
        parsed = urlparse(url)
        path = (parsed.path or "").strip("/")
        return path.split("/")[0] if path else ""
    except (ValueError, AttributeError, IndexError, TypeError):
        return ""


def _is_allowed_integration_test_db(url: str) -> bool:
    """Return True only if the URL points to an allowed test-only database (mythos_unit or mythos_e2e)."""
    db_name = _get_db_name_from_url(url)
    return db_name in _ALLOWED_INTEGRATION_DB_NAMES


def _assert_allowed_integration_test_db(database_url: str) -> None:
    """Raise ValueError if URL is not an allowed test DB. Never truncate mythos_dev."""
    db_name = _get_db_name_from_url(database_url)
    if db_name in _PROTECTED_DB_NAMES:
        raise ValueError(
            f"Database {db_name!r} is protected. Integration tests must NEVER truncate or delete from "
            "mythos_dev. Use mythos_unit or mythos_e2e for tests. Refusing to run."
        )
    if not _is_allowed_integration_test_db(database_url):
        raise ValueError(
            "Integration tests TRUNCATE all tables. DATABASE_URL must point to a test database: "
            f"database name must be one of {_ALLOWED_INTEGRATION_DB_NAMES!r}. "
            f"Current database name: {db_name!r}. Refusing to run to prevent data loss."
        )


@pytest.fixture(scope="session")
def integration_db_url() -> Generator[str, None, None]:
    """
    Provide an isolated PostgreSQL database URL for integration tests.

    Reads from DATABASE_URL environment variable.
    Raises if missing, not PostgreSQL, or not an allowed test-only database name
    (integration tests truncate tables; we never run against dev/prod).
    """
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        raise ValueError("DATABASE_URL is required for integration tests.")

    if not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be a PostgreSQL URL. SQLite is no longer supported.")

    _assert_allowed_integration_test_db(database_url)
    yield database_url


@pytest.fixture(scope="session")
def integration_engine(request: pytest.FixtureRequest) -> Generator[AsyncEngine, None, None]:
    """
    Provide a SQLAlchemy async engine bound to the integration DB URL.

    CRITICAL: This fixture is session-scoped and creates the engine once.
    We use NullPool on all platforms to avoid connection reuse across event loops.
    This prevents "Event loop is closed" and "Future attached to different loop"
    errors when connections from one test's event loop are reused in another test's
    event loop, especially with pytest-xdist parallel execution.
    """
    # Use NullPool on all platforms to avoid connection reuse across event loops
    # This ensures each test gets a fresh connection tied to its own event loop
    # This is critical for pytest-xdist parallel execution where each worker
    # has its own event loop but may share the engine
    from sqlalchemy.pool import NullPool

    pool_class = NullPool
    db_url = request.getfixturevalue("integration_db_url")
    connect_args = get_postgres_connect_args()

    # Create engine with connection pool settings optimized for tests
    engine = create_async_engine(
        db_url,
        future=True,
        echo=False,
        poolclass=pool_class,  # NullPool prevents cross-loop connection reuse on all platforms
        pool_pre_ping=True,  # Verify connections before using (if using a pool)
        connect_args=connect_args,
    )
    yield engine
    # Cleanup: properly dispose engine and close all connections
    # Use sync dispose to avoid event loop issues during teardown
    engine.sync_engine.dispose()


# Track if tables have been created to avoid concurrent creation (namespace avoids global statement)
class _IntegrationState:
    tables_created = False


@pytest.fixture(scope="function")
async def fresh_database_manager() -> AsyncGenerator[None, None]:
    """
    Give a test its own process-wide DatabaseManager (the engine AsyncPersistenceLayer uses).

    Each async test runs on its own event loop; a DatabaseManager left over from an earlier test
    keeps an asyncpg pool bound to that test's closed loop, so the next AsyncPersistenceLayer test
    fails with "attached to a different loop".
    """
    reset_database()
    yield
    await close_db()
    reset_database()


@pytest.fixture(scope="function")
async def session_factory(request: pytest.FixtureRequest) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
    """
    Provide an async session factory for integration tests.

    CRITICAL: This fixture is function-scoped to ensure each test gets a fresh session factory.
    Tables are created on first use and persist across tests (cleaned by db_cleanup).

    With NullPool, each test gets a fresh connection tied to its event loop.
    """
    engine = request.getfixturevalue("integration_engine")

    # Create tables on first use (with simple flag to avoid concurrent creation).
    # The whole suite runs serially (#724), so this is safe.
    if not _IntegrationState.tables_created:
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            _IntegrationState.tables_created = True
        except _CONNECTION_ERRORS:
            # DB unreachable; mark created so we do not retry. Metadata/schema errors are NOT
            # caught: a NoReferencedTableError here once skipped create_all silently (#949).
            _IntegrationState.tables_created = True

    factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    yield factory

    # With NullPool on Windows, connections are automatically closed when sessions close
    # No explicit cleanup needed - the session context manager handles it
    # Tables persist - cleaned by db_cleanup fixture


def _should_preserve_table_on_cleanup(table_name: str) -> bool:
    """Return True for the migration ledger and reference/world seed tables.

    `schema_migrations` (dbmate, #811 -- alembic was never wired up and had no ledger table)
    is never actually reached by this check in practice: `Base.metadata.sorted_tables`, the
    only thing `_delete_mutable_integration_test_rows` iterates, contains SQLAlchemy-mapped
    tables only, and migration-ledger tables are created directly by tooling, never ORM-mapped.
    Named here anyway so the intent survives if that ever changes.
    """
    return table_name == "schema_migrations" or table_name in _REFERENCE_SEED_TABLES


async def _delete_mutable_integration_test_rows(session: AsyncSession) -> None:
    """Remove test-created rows; preserve reference seed (world topology, professions)."""
    for table in reversed(Base.metadata.sorted_tables):
        if _should_preserve_table_on_cleanup(table.name):
            continue
        await session.execute(table.delete())
    await session.commit()


# autouse: required for test isolation - truncates tables after every integration test
def _test_touches_database(request: pytest.FixtureRequest) -> bool:
    """True for integration-tier tests and any test that asks for session_factory itself.

    This plugin is loaded for every test, so without this gate the cleanup ran ~33 DELETEs after each
    of ~11.5k unit tests. That only went unnoticed while #949's metadata error made it fail at once.
    request.fixturenames can't be used: it includes session_factory for every test via this fixture.
    """
    # db_cleanup is function-scoped, so the node is the test item.
    if cast(pytest.Item, request.node).get_closest_marker("integration") is not None:
        return True
    test_function = cast("Callable[..., object] | None", getattr(request, "function", None))
    return test_function is not None and "session_factory" in inspect.signature(test_function).parameters


@pytest.fixture(scope="function", autouse=True)
async def db_cleanup(
    request: pytest.FixtureRequest,
    session_factory: async_sessionmaker[AsyncSession],  # pylint: disable=redefined-outer-name  # Intentional: receive fixture by name
) -> AsyncGenerator[None, None]:
    """
    Clean up database after each test.

    Deletes test-created rows from mutable tables. Skips reference/world seed tables
    (zones, rooms, professions, etc.) so procedure tests and E2E seed data persist.
    Only runs for tests that touch the database (see _test_touches_database).

    CRITICAL: This fixture is autouse=True to ensure cleanup happens after every test.
    It runs AFTER the test completes to clean up data.

    CRITICAL: session_factory is taken as a direct fixture parameter so we do NOT
    call request.getfixturevalue() during teardown. That call can trigger
    pytest-asyncio to use Runner.run() from within an already-running event loop
    (e.g. under pytest-xdist), causing RuntimeError.
    """
    yield

    if not _test_touches_database(request):
        return

    # Cleanup happens after test completion
    # Use try/except to handle event loop closure gracefully on Windows
    try:
        # Check if we have a valid event loop before attempting cleanup
        import asyncio

        try:
            loop = asyncio.get_running_loop()
            if loop.is_closed():
                # Loop is closed - skip cleanup
                return
        except RuntimeError:
            # No running loop - skip cleanup (test already completed)
            return

        # Defense in depth: never truncate unless DATABASE_URL is still an allowed test DB
        db_url = os.getenv("DATABASE_URL", "")
        if db_url:
            _assert_allowed_integration_test_db(db_url)

        # Use session_factory from parameter (do not call getfixturevalue in teardown)
        async with session_factory() as session:
            await _delete_mutable_integration_test_rows(session)
    except (RuntimeError, AttributeError):
        # Event loop is closed or connection issues - this is expected on Windows
        # when the event loop closes before asyncpg connections are fully cleaned up
        # The data will be cleaned up by the next test's setup or manual cleanup
        pass
    except _CONNECTION_ERRORS as e:
        # Connection errors during cleanup - log but do not fail the test. Anything else (a
        # metadata/schema error, a constraint violation) means cleanup is broken and must fail
        # the run: a swallowed NoReferencedTableError left cleanup a silent no-op (#949).
        from server.structured_logging.enhanced_logging_config import get_logger

        logger = get_logger(__name__)
        logger.warning("Database cleanup warning", error=str(e), error_type=type(e).__name__)
