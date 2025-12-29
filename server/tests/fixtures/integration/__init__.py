"""
Integration-tier fixtures with real database connections.
"""

import os
from collections.abc import AsyncGenerator, Generator
from typing import Any

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base


@pytest.fixture(scope="session")
def integration_db_url() -> Generator[str, None, None]:
    """
    Provide an isolated PostgreSQL database URL for integration tests.

    Reads from DATABASE_URL environment variable.
    Raises if missing or not PostgreSQL.
    """
    database_url = os.getenv("DATABASE_URL", "")
    if not database_url:
        raise ValueError("DATABASE_URL is required for integration tests.")

    if not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be a PostgreSQL URL. SQLite is no longer supported.")

    yield database_url


@pytest.fixture(scope="session")
def integration_engine(integration_db_url: str) -> Generator[AsyncEngine, None, None]:
    """
    Provide a SQLAlchemy async engine bound to the integration DB URL.

    CRITICAL: This fixture is session-scoped and creates the engine once.
    On Windows, we use NullPool to avoid connection reuse across event loops.
    This prevents "Event loop is closed" errors when connections from one test's
    event loop are reused in another test's event loop.
    """
    # Use NullPool on Windows to avoid connection reuse across event loops
    # This ensures each test gets a fresh connection tied to its own event loop
    # On other platforms, we can use the default pool
    import os

    from sqlalchemy.pool import NullPool
    pool_class = NullPool if os.name == "nt" else None

    # Create engine with connection pool settings optimized for tests
    engine = create_async_engine(
        integration_db_url,
        future=True,
        echo=False,
        poolclass=pool_class,  # NullPool on Windows prevents cross-loop connection reuse
        pool_pre_ping=True,    # Verify connections before using (if using a pool)
    )
    yield engine
    # Cleanup: properly dispose engine and close all connections
    # Use sync dispose to avoid event loop issues during teardown
    engine.sync_engine.dispose()


# Track if tables have been created to avoid concurrent creation
_tables_created = False

@pytest.fixture(scope="function")
async def session_factory(integration_engine: AsyncEngine) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
    """
    Provide an async session factory for integration tests.

    CRITICAL: This fixture is function-scoped to ensure each test gets a fresh session factory.
    Tables are created on first use and persist across tests (cleaned by db_cleanup).

    On Windows with NullPool, each test gets a fresh connection tied to its event loop.
    """
    global _tables_created

    # Create tables on first use (with simple flag to avoid concurrent creation)
    # Since integration tests are marked as serial, this should be safe
    if not _tables_created:
        try:
            async with integration_engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            _tables_created = True
        except Exception:
            # Tables might already exist, which is fine
            _tables_created = True

    factory = async_sessionmaker(
        bind=integration_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    yield factory

    # With NullPool on Windows, connections are automatically closed when sessions close
    # No explicit cleanup needed - the session context manager handles it
    # Tables persist - cleaned by db_cleanup fixture


@pytest.fixture(scope="function", autouse=True)
async def db_cleanup(session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[None, None]:
    """
    Clean up database after each test.

    Truncates all tables (except alembic_version) to ensure test isolation.

    CRITICAL: This fixture is autouse=True to ensure cleanup happens after every test.
    It runs AFTER the test completes to clean up data.

    On Windows, we need to ensure cleanup happens before the event loop closes.

    NOTE: Integration tests are marked as serial, so cleanup should not interfere
    with other tests. However, we still check for a valid event loop to avoid errors.
    """
    yield

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

        # Only perform cleanup if we have a valid event loop
        async with session_factory() as session:
            # Truncate all tables except alembic_version
            # Iterate in reverse order to handle foreign key constraints
            for table in reversed(Base.metadata.sorted_tables):
                if table.name != "alembic_version":
                    await session.execute(table.delete())
            await session.commit()
    except (RuntimeError, AttributeError):
        # Event loop is closed or connection issues - this is expected on Windows
        # when the event loop closes before asyncpg connections are fully cleaned up
        # The data will be cleaned up by the next test's setup or manual cleanup
        pass
    except Exception as e:
        # Other exceptions should be logged but not fail the test
        import logging
        logging.getLogger(__name__).debug(f"Database cleanup warning: {e}")

