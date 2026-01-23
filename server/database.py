"""
Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization for the MythosMUD application.

CRITICAL: Database initialization is LAZY and requires configuration to be loaded first.
         The system will FAIL LOUDLY if configuration is not properly set.
"""

# pylint: disable=too-many-lines  # Reason: Database module requires extensive configuration, connection management, and session handling code

import asyncio
import importlib.util
import threading
from collections.abc import AsyncIterator
from pathlib import Path

from anyio import sleep
from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .database_config_helpers import (
    configure_pool_settings,
    get_test_database_url,
    load_database_url,
    normalize_database_url,
    set_test_database_url,
    validate_database_url,
)
from .exceptions import DatabaseError, ValidationError
from .structured_logging.enhanced_logging_config import get_logger
from .utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)

# Backward-compatibility override for tests expecting module-level URL
# Tests may patch `server.database._database_url` to control path resolution.
# This syncs with database_config_helpers for actual storage
# Using a dict to avoid global statement while maintaining mutable state
_database_url_state: dict[str, str | None] = {"url": None}

# Expose as simple variable for backward compatibility with tests
# Tests can patch this directly: `server.database._database_url = "postgresql://..."`
_database_url: str | None = None  # pylint: disable=invalid-name  # Reason: Private module-level variable for test compatibility, intentionally uses _ prefix


def _get_database_url_state() -> str | None:
    """
    Get database URL state for testing.

    This is a public function to access the internal _database_url_state
    without directly accessing the protected member.
    """
    return _database_url_state["url"]


def _reset_database_url_state() -> None:
    """
    Reset database URL state for testing.

    This is a public function to reset the internal _database_url_state
    without directly accessing the protected member.
    """
    _database_url_state["url"] = None
    # Note: _database_url is for backward compatibility and can be patched directly by tests


class DatabaseManager:
    """
    Thread-safe singleton for database management.

    Manages database engine, session maker, and URL with proper
    initialization and thread safety.
    """

    _instance: "DatabaseManager | None" = None
    _lock: threading.Lock = threading.Lock()

    def __init__(self) -> None:
        """Initialize the database manager."""
        if DatabaseManager._instance is not None:
            raise RuntimeError("Use DatabaseManager.get_instance()")

        self.engine: AsyncEngine | None = None
        self.session_maker: async_sessionmaker | None = None
        self.database_url: str | None = None
        self._initialized: bool = False
        self._creation_loop_id: int | None = None  # Track which loop created the engine

    @classmethod
    def get_instance(cls) -> "DatabaseManager":
        """Get the singleton instance."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset singleton for testing."""
        with cls._lock:
            cls._instance = None

    def _initialize_database(self) -> None:
        """
        Initialize database engine and session maker from configuration.

        CRITICAL: This function FAILS LOUDLY if configuration is not properly set.

        Raises:
            ValidationError: If configuration is missing or invalid
        """
        # Avoid re-initialization
        if self._initialized:
            return

        context = create_error_context()
        context.metadata["operation"] = "database_initialization"

        # Check if config module is available
        config_spec = importlib.util.find_spec(".config", package=__package__)
        if config_spec is None:
            log_and_raise(
                ValidationError,
                "Failed to import config - configuration system unavailable",
                context=context,
                details={"import_error": "config module not found"},
                user_friendly="Critical system error: configuration system not available",
            )

        # Handle test override for backward compatibility
        # Check both dict-based storage and direct variable (for backward compatibility)
        # Tests can patch either _database_url_state["url"] or _database_url directly
        test_url = _database_url_state["url"] or _database_url
        if test_url is not None:
            set_test_database_url(test_url)
            # Sync dict storage (no global needed)
            _database_url_state["url"] = test_url
        else:
            # Sync from config helpers if module-level is None
            test_url_from_config = get_test_database_url()
            _database_url_state["url"] = test_url_from_config

        database_url = load_database_url(context)
        validate_database_url(database_url, context)
        self.database_url = normalize_database_url(database_url)
        logger.info("Using PostgreSQL database URL from environment", database_url=self.database_url)

        pool_kwargs = configure_pool_settings(self.database_url)

        # Create async engine with PostgreSQL configuration
        # CRITICAL FIX: Add proper exception handling for engine creation
        # Handles connection failures, authentication errors, and configuration issues
        try:
            self.engine = create_async_engine(
                self.database_url,
                echo=False,
                pool_pre_ping=True,
                **pool_kwargs,
            )

            pool_type = "NullPool" if "test" in self.database_url else "AsyncAdaptedQueuePool"
            logger.info("Database engine created", pool_type=pool_type)

        except (ValueError, TypeError) as e:
            # Configuration error (invalid URL format, invalid pool parameters)
            context = create_error_context()
            context.metadata["operation"] = "create_async_engine"
            context.metadata["database_url_prefix"] = self.database_url[:30]  # Truncate for security
            log_and_raise(
                ValidationError,
                f"Invalid database configuration: {e}",
                context=context,
                details={
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "pool_config": {k: v for k, v in pool_kwargs.items() if k not in ["pool_recycle"]},
                },
                user_friendly="Database configuration error. Please check DATABASE_URL environment variable.",
            )
        except (ConnectionError, OSError) as e:
            # Network/connection error (database server unreachable, DNS failure)
            context = create_error_context()
            context.metadata["operation"] = "create_async_engine"
            log_and_raise(
                DatabaseError,
                f"Failed to connect to database: {e}",
                context=context,
                details={
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "database_url_prefix": self.database_url[:30],
                },
                user_friendly="Cannot connect to database. Please check database server is running.",
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: create_async_engine can raise a wide variety of exceptions depending on the driver (asyncpg), network state, and provided credentials, we catch Exception here to provide a unified, context-rich DatabaseError for any failure during this critical infrastructure setup
            context = create_error_context()
            context.metadata["operation"] = "create_async_engine"
            log_and_raise(
                DatabaseError,
                f"Failed to create database engine: {e}",
                context=context,
                details={
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "database_url_prefix": self.database_url[:30],
                },
                user_friendly="Database connection failed. Please check database configuration and credentials.",
            )

        # Create async session maker
        self.session_maker = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )

        logger.info("Database session maker created")
        self._initialized = True
        # Track the event loop that created this engine
        try:
            loop = asyncio.get_running_loop()
            self._creation_loop_id = id(loop)
        except RuntimeError:
            # No running loop - that's okay, we'll track it as None
            self._creation_loop_id = None

    def get_engine(self) -> AsyncEngine:
        """
        Get the database engine, initializing if necessary.

        Returns:
            AsyncEngine: The database engine (never None after initialization)

        Raises:
            ValidationError: If database cannot be initialized
        """
        if not self._initialized:
            self._initialize_database()
        # Double-check: if initialization didn't set engine, try again
        if self.engine is None:
            logger.warning("Engine is None after initialization, attempting re-initialization")
            self._initialized = False  # Force re-initialization
            self._initialize_database()

        # CRITICAL: Check if we're in a different event loop than when engine was created
        # asyncpg connections must be created in the same loop they're used in
        # If the event loop changes, we need to recreate the engine for the new loop
        try:
            current_loop = asyncio.get_running_loop()
            current_loop_id = id(current_loop)
            if self._creation_loop_id is not None and current_loop_id != self._creation_loop_id:
                logger.warning(
                    "Event loop changed, recreating database engine",
                    old_loop_id=self._creation_loop_id,
                    new_loop_id=current_loop_id,
                )
                # CRITICAL: asyncpg connections MUST be closed in the same event loop they were created in.
                # We cannot dispose the old engine here because we're already in a different loop.
                # The old engine will be properly disposed by the test fixture's event_loop cleanup
                # (which runs in the original loop) or by garbage collection.
                # For production, this should never happen as there's only one event loop.
                # Reset and recreate engine for the new loop
                self.engine = None
                self.session_maker = None
                self._initialized = False
                self._initialize_database()
        except RuntimeError:
            # No running loop - that's okay, engine will be created when needed
            logger.debug("No running event loop, engine will be created when needed")

        if self.engine is None:
            raise RuntimeError("Database engine not initialized")
        return self.engine

    def get_session_maker(self) -> async_sessionmaker:
        """
        Get the async session maker, initializing if necessary.

        Returns:
            async_sessionmaker: The session maker (never None after initialization)

        Raises:
            ValidationError: If database cannot be initialized
        """
        if not self._initialized:
            self._initialize_database()
        if self.session_maker is None:
            raise RuntimeError("Session maker not initialized")
        return self.session_maker

    def get_database_url(self) -> str | None:
        """
        Get the database URL, initializing if necessary.

        Returns:
            str: The database URL

        Raises:
            ValidationError: If database cannot be initialized
        """
        if not self._initialized:
            self._initialize_database()
        return self.database_url

    def get_database_path(self) -> Path | None:
        """
        Get the database file path.

        DEPRECATED: PostgreSQL does not use file paths. This method always returns None
        for PostgreSQL databases. Kept for backward compatibility with code that may
        check for database paths.

        Returns:
            Path | None: Always None for PostgreSQL (no file path)
        """
        database_url = self.get_database_url()

        if database_url is None:
            context = create_error_context()
            context.metadata["operation"] = "get_database_path"
            log_and_raise(
                ValidationError,
                "Database URL is None",
                context=context,
                user_friendly="Database not initialized",
            )

        if database_url.startswith("postgresql"):
            # PostgreSQL doesn't have a file path
            return None

        context = create_error_context()
        context.metadata["operation"] = "get_database_path"
        context.metadata["database_url"] = database_url
        log_and_raise(
            ValidationError,
            f"Unsupported database URL: {database_url}. Only PostgreSQL is supported.",
            context=context,
            details={"database_url": database_url},
            user_friendly="Unsupported database configuration - PostgreSQL required",
        )

    async def close(self) -> None:
        """Close database connections."""
        if self.engine is not None:
            # Store engine in local variable for type narrowing
            engine = self.engine
            try:
                # Check if event loop is still running before disposing
                try:
                    loop = asyncio.get_running_loop()
                    if loop.is_closed():
                        logger.warning("Event loop is closed, skipping engine disposal")
                        self.engine = None
                        self._initialized = False
                        self._creation_loop_id = None
                        return
                except RuntimeError:
                    # No running loop - that's okay, we can still try to dispose
                    pass

                # For Windows/asyncpg: Close connections gracefully before disposal
                # CRITICAL: asyncpg connections must be closed in the same event loop they were created in
                # We need to ensure all connections are properly closed before disposal to prevent
                # RuntimeWarning about unawaited Connection._cancel coroutines during GC
                try:
                    # Step 1: Wait for any pending operations to complete
                    # This gives time for any in-flight queries to finish
                    await sleep(0.3)

                    # Step 2: Shield disposal from cancellation to ensure cleanup completes
                    # This prevents Connection._cancel coroutines from being interrupted during cleanup
                    async def _dispose_engine() -> None:
                        await engine.dispose()
                        # Wait a bit more to ensure all asyncpg cleanup coroutines complete
                        # This helps prevent Connection._cancel coroutines from being garbage collected
                        # before they're awaited
                        await sleep(0.2)

                    # Shield the disposal to prevent cancellation from interrupting cleanup
                    await asyncio.wait_for(asyncio.shield(_dispose_engine()), timeout=3.0)

                    logger.info("Database connections closed")
                except TimeoutError:
                    # If disposal times out, try to force close connections
                    logger.warning("Engine disposal timed out, attempting force close")
                    try:
                        # Force close by disposing the pool directly
                        if hasattr(engine, "sync_engine") and hasattr(engine.sync_engine, "pool"):
                            pool = engine.sync_engine.pool
                            if pool:
                                pool.dispose()
                    except (RuntimeError, AttributeError, TypeError):
                        pass  # Ignore errors during force close
                    logger.info("Database connections force closed")
            except (RuntimeError, AttributeError) as e:
                # Event loop is closed or proactor is None - this is expected during cleanup
                # Don't log as error, just as debug since this is normal during test teardown
                logger.debug("Event loop closed during engine disposal (expected during cleanup)", error=str(e))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: This is a best-effort cleanup of database connections during engine disposal, we log any unexpected failures but must not raise them, ensuring the application shutdown process can continue for other components even if database cleanup fails
                # Any other error - log but don't raise
                logger.warning("Error disposing database engine", error=str(e), error_type=type(e).__name__)
            finally:
                # Always reset state, even if disposal failed
                self.engine = None
                self._initialized = False
                self._creation_loop_id = None
        else:
            # Engine already None, but reset flag if it was initialized
            self._initialized = False
            self._creation_loop_id = None


# Module-level utility functions for backward compatibility


def get_session_maker() -> async_sessionmaker:
    """
    Get the async session maker from DatabaseManager.

    Returns:
        async_sessionmaker: The session maker

    Raises:
        ValidationError: If database cannot be initialized
    """
    return DatabaseManager.get_instance().get_session_maker()


async def get_async_session() -> AsyncIterator[AsyncSession]:
    """
    Get an async database session as an async context manager.

    Usage:
        async for session in get_async_session():
            # Use session here
            result = await session.execute(query)
            await session.commit()

    Yields:
        AsyncSession: An async database session
    """
    session_maker = get_session_maker()
    async with session_maker() as session:
        try:
            yield session
        except Exception:
            # Rollback on exception before re-raising
            await session.rollback()
            raise


async def init_db() -> None:
    """
    Initialize the database (deprecated - kept for backward compatibility).

    This function initializes the DatabaseManager singleton and configures mappers.
    The database is now initialized lazily when needed, but this function ensures
    proper initialization for compatibility.
    """
    from sqlalchemy.orm import (
        configure_mappers,  # noqa: PLC0415  # Reason: Lazy import inside function to avoid circular import chain during module initialization
    )

    # Configure mappers before initializing database
    configure_mappers()

    # Initialize database manager
    manager = DatabaseManager.get_instance()
    manager._initialize_database()  # noqa: SLF001  # pylint: disable=protected-access  # Reason: Accessing protected method _initialize_database is necessary for database manager initialization, this is part of the DatabaseManager internal API

    # Verify connectivity by getting engine (initializes if needed)
    engine = get_engine()
    async with engine.begin() as conn:
        # Execute a simple query to verify connectivity
        await conn.execute(select(1))  # noqa: S101  # Reason: Query result not needed, just connectivity check to verify database is accessible


def reset_database() -> None:
    """
    Reset the database connection state (for testing).

    This resets the DatabaseManager state without closing connections.
    For actually closing connections, use DatabaseManager.get_instance().close() in async contexts.

    Note: This is a synchronous function for test compatibility.
    """
    # Reset singleton instance
    DatabaseManager.reset_instance()
    # Reset module-level _database_url for backward compatibility with tests
    global _database_url  # pylint: disable=global-statement  # Reason: Required for test cleanup, module-level variable must be reset for test isolation
    _database_url = None
    _reset_database_url_state()
    # Also reset database_config_helpers state to ensure tests can mock get_config()
    set_test_database_url(None)


async def close_db() -> None:
    """
    Close database connections.

    This closes the database manager's engine and connections properly.
    For testing, use reset_database() instead.
    """
    try:
        manager = DatabaseManager.get_instance()
        engine = manager.get_engine()
        if engine:
            await manager.close()
    except RuntimeError as e:
        raise RuntimeError("Failed to close database connections") from e


def ensure_database_directory() -> None:
    """
    Ensure database directory exists (deprecated for PostgreSQL).

    This function is a no-op for PostgreSQL databases as they don't use file paths.
    Kept for backward compatibility with code that may call it.
    """
    # PostgreSQL doesn't use file paths, so this is a no-op


def get_engine() -> AsyncEngine:
    """
    Get the database engine from DatabaseManager.

    Returns:
        AsyncEngine: The database engine

    Raises:
        ValidationError: If database cannot be initialized
    """
    return DatabaseManager.get_instance().get_engine()


def get_database_path() -> Path | None:
    """
    Get the database file path (deprecated for PostgreSQL).

    Returns:
        Path | None: Always None for PostgreSQL (no file path)
    """
    return DatabaseManager.get_instance().get_database_path()


def get_database_url() -> str | None:
    """
    Get the database URL from DatabaseManager.

    Returns:
        str | None: The database URL
    """
    return DatabaseManager.get_instance().get_database_url()


__all__ = [
    "DatabaseManager",
    "ValidationError",
    "get_async_session",
    "get_session_maker",
    "get_engine",
    "reset_database",
    "get_database_path",
    "get_database_url",
]
