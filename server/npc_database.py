"""
NPC Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization specifically for the NPC subsystem.

CRITICAL: Database initialization is LAZY and requires configuration to be loaded first.
         The system will FAIL LOUDLY if configuration is not properly set.
"""

import asyncio
import os
from collections.abc import AsyncGenerator
from pathlib import Path
from typing import Any

from anyio import sleep
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

from .exceptions import ValidationError
from .structured_logging.enhanced_logging_config import get_logger
from .utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)

# LAZY INITIALIZATION: These are initialized on first use, not at import time
_npc_engine: AsyncEngine | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix
_npc_async_session_maker: async_sessionmaker | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix
_npc_database_url: str | None = None  # pylint: disable=invalid-name  # Reason: Private module-level variable, intentionally uses _ prefix
_npc_creation_loop_id: int | None = None  # pylint: disable=invalid-name  # Reason: Private module-level variable, intentionally uses _ prefix  # Track which loop created the NPC engine


def _initialize_npc_database() -> None:
    """
    Initialize NPC database engine and session maker from configuration.

    CRITICAL: This function FAILS LOUDLY if configuration is not properly set.

    Raises:
        ValidationError: If configuration is missing or invalid
    """
    global _npc_engine, _npc_async_session_maker, _npc_database_url  # pylint: disable=global-statement  # Reason: Singleton pattern for database engine

    # Avoid re-initialization
    if _npc_engine is not None:
        return

    context = create_error_context()
    context.metadata["operation"] = "npc_database_initialization"

    # Import config here to avoid circular imports
    try:
        from .config import get_config
    except ImportError as e:
        log_and_raise(
            ValidationError,
            "Failed to import config - configuration system unavailable",
            context=context,
            details={"import_error": str(e)},
            user_friendly="Critical system error: configuration system not available",
        )

    # Load configuration. If primary DB URL is missing in tests, optionally fall back to env-based NPC URL.
    try:
        config = get_config()
        npc_database_url = config.database.npc_url
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Configuration errors unpredictable, fallback needed for tests
        # Optional fallback for unit tests that provide only NPC DB URL
        allow_env_fallback = os.getenv("NPC_DB_ENV_FALLBACK", "").lower() in {"1", "true", "yes"}
        env_npc_url = os.getenv("DATABASE_NPC_URL") or os.getenv("NPC_DATABASE_URL") or os.getenv("DATABASE__NPC_URL")
        if allow_env_fallback and env_npc_url:
            npc_database_url = env_npc_url
            logger.warning(
                "Using NPC database URL from environment fallback",
                error=str(e),
                npc_database_url=npc_database_url,
            )
        else:
            log_and_raise(
                ValidationError,
                f"Failed to load configuration: {e}",
                context=context,
                details={"config_error": str(e)},
                user_friendly="NPC database cannot be initialized: configuration not loaded or invalid",
            )

    # Use NPC database URL from configuration
    _npc_database_url = npc_database_url
    logger.info("Using NPC database URL from configuration", npc_database_url=_npc_database_url)

    # PostgreSQL connection args (no SQLite-specific args)
    connect_args: dict[str, Any] = {}
    if not _npc_database_url.startswith("postgresql"):
        log_and_raise(
            ValidationError,
            f"Unsupported database URL: {_npc_database_url}. Only PostgreSQL is supported.",
            context=context,
            details={"database_url": _npc_database_url},
            user_friendly="NPC database configuration error - PostgreSQL required",
        )

    # Configure pool settings based on database URL
    # Use NullPool for tests, default AsyncAdaptedQueuePool for production
    # For async engines, AsyncAdaptedQueuePool is used automatically if poolclass not specified
    pool_kwargs: dict[str, Any] = {}
    if "test" in _npc_database_url:
        pool_kwargs["poolclass"] = NullPool
    else:
        # For production, use default AsyncAdaptedQueuePool with configured pool size
        # AsyncAdaptedQueuePool is automatically used by create_async_engine()
        # Get pool configuration from config (NPC database uses same pool settings as main database)
        config = get_config()
        pool_kwargs.update(
            {
                "pool_size": config.database.pool_size,
                "max_overflow": config.database.max_overflow,  # pylint: disable=no-member  # Pydantic FieldInfo dynamic attribute
                "pool_timeout": config.database.pool_timeout,  # pylint: disable=no-member  # Pydantic FieldInfo dynamic attribute
            }
        )

    _npc_engine = create_async_engine(
        _npc_database_url,
        echo=False,
        pool_pre_ping=True,
        connect_args=connect_args,
        **pool_kwargs,
    )

    pool_type = "NullPool" if "test" in _npc_database_url else "AsyncAdaptedQueuePool"
    logger.info("NPC Database engine created", pool_type=pool_type)

    # Create async session maker for NPC database
    _npc_async_session_maker = async_sessionmaker(
        _npc_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )

    logger.info("NPC Database session maker created")
    # Track the event loop that created this engine
    try:
        loop = asyncio.get_running_loop()
        global _npc_creation_loop_id  # pylint: disable=global-statement  # Reason: Singleton pattern for tracking creation loop
        _npc_creation_loop_id = id(loop)
    except RuntimeError:
        # No running loop - that's okay, we'll track it as None
        _npc_creation_loop_id = None


def get_npc_engine() -> AsyncEngine | None:
    """
    Get the NPC database engine, initializing if necessary.

    Returns:
        AsyncEngine | None: The NPC database engine

    Raises:
        ValidationError: If NPC database cannot be initialized
    """
    global _npc_engine, _npc_async_session_maker, _npc_creation_loop_id  # pylint: disable=global-statement  # Reason: Singleton pattern for database engine

    if _npc_engine is None:
        _initialize_npc_database()

    # CRITICAL: Check if we're in a different event loop than when engine was created
    # asyncpg connections must be created in the same loop they're used in
    try:
        current_loop = asyncio.get_running_loop()
        current_loop_id = id(current_loop)
        if _npc_creation_loop_id is not None and current_loop_id != _npc_creation_loop_id:
            logger.warning(
                "Event loop changed, recreating NPC database engine",
                old_loop_id=_npc_creation_loop_id,
                new_loop_id=current_loop_id,
            )
            # CRITICAL: asyncpg connections MUST be closed in the same event loop they were created in.
            # We cannot dispose the old engine here because we're already in a different loop.
            # The old engine will be properly disposed by the test fixture's event_loop cleanup
            # (which runs in the original loop) or by garbage collection.
            # For production, this should never happen as there's only one event loop.
            # Reset and recreate engine for the new loop
            _npc_engine = None
            _npc_async_session_maker = None
            _npc_creation_loop_id = None
            _initialize_npc_database()
    except RuntimeError:
        # No running loop - that's okay, engine will be created when needed
        pass

    return _npc_engine


def get_npc_session_maker() -> async_sessionmaker:
    """
    Get the NPC async session maker, initializing if necessary.

    Returns:
        async_sessionmaker: The NPC session maker (never None)

    Raises:
        ValidationError: If NPC database cannot be initialized
    """
    if _npc_async_session_maker is None:
        _initialize_npc_database()
    if _npc_async_session_maker is None:
        raise RuntimeError("NPC session maker not initialized")
    return _npc_async_session_maker


async def get_npc_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get NPC database session.

    Yields:
        AsyncSession: Database session for async operations
    """
    context = create_error_context()
    context.metadata["operation"] = "npc_database_session"

    logger.debug("Creating NPC database session")
    # Prefer existing session maker if already set (e.g., tests mocking it)
    global _npc_async_session_maker  # pylint: disable=global-statement,global-variable-not-assigned  # Reason: Singleton pattern, checking if None before assignment
    if _npc_async_session_maker is None:
        # For unit tests, ensure a clean DB schema before providing a session
        if _npc_database_url is None:
            _initialize_npc_database()
        if _npc_database_url and "unit_test" in _npc_database_url:
            await init_npc_db()
        session_maker = get_npc_session_maker()  # Initialize if needed
    else:
        session_maker = _npc_async_session_maker
    async with session_maker() as session:
        try:
            logger.debug("NPC database session created successfully")
            yield session
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Database session errors unpredictable, must log and rollback
            context.metadata["error_type"] = type(e).__name__
            context.metadata["error_message"] = str(e)
            logger.error(
                "NPC database session error",
                context=context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            try:
                await session.rollback()
                logger.debug("NPC database session rolled back after error")
            except Exception as rollback_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Rollback errors unpredictable, must log but not fail
                logger.error(
                    "Failed to rollback NPC database session",
                    context=context.to_dict(),
                    rollback_error=str(rollback_error),
                )
            raise
        finally:
            # Session is automatically closed by the async context manager
            # Log session closure for monitoring (debug level to avoid noise)
            logger.debug("NPC database session closed")


async def init_npc_db():
    """
    Initialize NPC database connection and verify configuration.

    NOTE: DDL (table creation) is NOT managed by this function.
    All database schema must be created via SQL script db/authoritative_schema.sql
    and applied using database management scripts (e.g., psql).

    This function only:
    - Initializes the NPC database engine and session maker
    - Configures SQLAlchemy mappers for ORM relationships
    - Verifies database connectivity

    To create tables, use the SQL script db/authoritative_schema.sql.
    """
    context = create_error_context()
    context.metadata["operation"] = "init_npc_db"

    logger.info("Initializing NPC database connection")

    try:
        # Import all NPC models to ensure they're registered with metadata
        from sqlalchemy.orm import configure_mappers

        # pylint: disable=unused-import  # noqa: F401  # Reason: Imported for side effects (SQLAlchemy mapper registration)
        from server.models.npc import (
            NPCDefinition,  # noqa: F401  # pylint: disable=unused-import  # Reason: Imported for side effects (SQLAlchemy mapper registration), unused but required for ORM setup
        )

        logger.debug("Configuring NPC SQLAlchemy mappers")
        configure_mappers()

        # Initialize engine to verify connectivity
        engine = get_npc_engine()  # Initialize if needed

        # Verify database connectivity with a simple query
        if engine is None:
            log_and_raise(
                ValidationError,
                "NPC database engine is None - initialization failed",
                context=context,
                user_friendly="Critical system error: NPC database not available",
            )
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
            logger.info("NPC database connection verified successfully")

        logger.info("NPC database initialization complete - DDL must be applied separately via SQL scripts")
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Database initialization errors unpredictable, must log with context
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "NPC database initialization failed",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        raise


async def close_npc_db():
    """Close NPC database connections."""
    global _npc_engine, _npc_async_session_maker, _npc_creation_loop_id  # pylint: disable=global-statement  # Reason: Singleton pattern for database engine cleanup

    context = create_error_context()
    context.metadata["operation"] = "close_npc_db"

    logger.info("Closing NPC database connections")
    try:
        engine = get_npc_engine()  # Initialize if needed
        if engine is not None:
            try:
                # Check if event loop is still running before disposing
                try:
                    loop = asyncio.get_running_loop()
                    if loop.is_closed():
                        logger.warning("Event loop is closed, skipping NPC engine disposal")
                        # Reset global state before returning
                        _npc_engine = None
                        _npc_async_session_maker = None
                        _npc_creation_loop_id = None
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
                    async def _dispose_engine():
                        await engine.dispose()
                        # Wait a bit more to ensure all asyncpg cleanup coroutines complete
                        # This helps prevent Connection._cancel coroutines from being garbage collected
                        # before they're awaited
                        await sleep(0.2)

                    # Shield the disposal to prevent cancellation from interrupting cleanup
                    await asyncio.wait_for(asyncio.shield(_dispose_engine()), timeout=3.0)

                    logger.info("NPC database connections closed")
                except TimeoutError:
                    # If disposal times out, log but continue
                    logger.warning("NPC engine disposal timed out")
                    logger.info("NPC database connections force closed")
            except (RuntimeError, AttributeError) as e:
                # Event loop is closed or proactor is None - this is expected during cleanup
                # Don't log as error, just as debug since this is normal during test teardown
                logger.debug("Event loop closed during NPC engine disposal (expected during cleanup)", error=str(e))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Engine disposal errors unpredictable, must log but not fail
                # Any other error - log but don't raise
                logger.warning("Error disposing NPC database engine", error=str(e), error_type=type(e).__name__)
            finally:
                # Always reset global state, even if disposal failed
                _npc_engine = None
                _npc_async_session_maker = None
                _npc_creation_loop_id = None
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cleanup errors unpredictable, best effort only
        # Only log, don't raise - best effort cleanup
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.warning(
            "Error closing NPC database connections",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        # Don't raise - allow cleanup to continue
        # Reset global state anyway
        _npc_engine = None
        _npc_async_session_maker = None
        _npc_creation_loop_id = None


def reset_npc_database() -> None:
    """
    Reset NPC database state for testing.

    This function resets all global NPC database state, including engine,
    session maker, database URL, and creation loop ID. Use this in test
    fixtures to ensure clean state between tests.

    Note: This does NOT close existing connections. Use close_npc_db() first
    if you need to dispose of active connections.
    """
    global _npc_engine, _npc_async_session_maker, _npc_database_url, _npc_creation_loop_id  # pylint: disable=global-statement  # Reason: Singleton pattern for database engine reset
    _npc_engine = None
    _npc_async_session_maker = None
    _npc_database_url = None
    _npc_creation_loop_id = None
    logger.debug("NPC database state reset")


def get_npc_database_path() -> Path | None:
    """
    Get the NPC database file path.

    DEPRECATED: PostgreSQL does not use file paths. This function always returns None
    for PostgreSQL databases. Kept for backward compatibility with code that may
    check for database paths.

    Returns:
        Path | None: Always None for PostgreSQL (no file path)
    """
    # Initialize database if needed
    if _npc_database_url is None:
        _initialize_npc_database()

    # After initialization, database URL should be set
    if _npc_database_url is None:
        raise RuntimeError("NPC database URL should be initialized")

    if _npc_database_url.startswith("postgresql"):
        # PostgreSQL doesn't have a file path
        return None

    context = create_error_context()
    context.metadata["operation"] = "get_npc_database_path"
    context.metadata["database_url"] = _npc_database_url
    log_and_raise(
        ValidationError,
        f"Unsupported NPC database URL: {_npc_database_url}. Only PostgreSQL is supported.",
        context=context,
        details={"database_url": _npc_database_url},
        user_friendly="Unsupported NPC database configuration - PostgreSQL required",
    )
    # log_and_raise returns NoReturn, so this code is unreachable
    # Type checker understands this, but we keep the else branch for clarity


def ensure_npc_database_directory():
    """
    Ensure NPC database directory exists.

    DEPRECATED: PostgreSQL does not use file paths or directories. This function
    is a no-op for PostgreSQL databases. Kept for backward compatibility.

    For PostgreSQL, database directories are managed by the PostgreSQL server,
    not by the application.
    """
    db_path = get_npc_database_path()  # pylint: disable=assignment-from-none  # Reason: Function returns Path | None, but with PostgreSQL it always returns None, assignment is effectively a no-op but pylint flags it
    # PostgreSQL always returns None, so this is effectively a no-op
    if db_path is not None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
