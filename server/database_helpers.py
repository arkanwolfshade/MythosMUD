"""
Database utility functions.

This module provides module-level utility functions for database operations,
including session management and initialization helpers.
"""

# pylint: disable=unused-import  # Reason: Model imports required for SQLAlchemy side effects (model registration), not directly used

from collections.abc import AsyncGenerator
from pathlib import Path

from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from .database import DatabaseManager
from .database_config_helpers import get_test_database_url
from .exceptions import ValidationError
from .structured_logging.enhanced_logging_config import get_logger
from .utils.error_logging import create_error_context

logger = get_logger(__name__)


def reset_database() -> None:
    """
    Reset database state for testing.

    This function resets the DatabaseManager singleton and module-level
    _database_url. Use this in test fixtures to ensure clean state.
    """
    from .database import _reset_database_url_state
    from .database_config_helpers import set_test_database_url

    # Reset test URL in config helpers
    set_test_database_url(None)
    # Reset module-level variable using public function
    _reset_database_url_state()
    DatabaseManager.reset_instance()
    logger.debug("Database state reset")


def get_engine() -> AsyncEngine:
    """
    Get the database engine, initializing if necessary.

    Returns:
        AsyncEngine: The database engine (never None)

    Raises:
        ValidationError: If database cannot be initialized
    """
    return DatabaseManager.get_instance().get_engine()


def get_session_maker() -> async_sessionmaker[AsyncSession]:
    """
    Get the async session maker, initializing if necessary.

    Returns:
        async_sessionmaker: The session maker (never None)

    Raises:
        ValidationError: If database cannot be initialized
    """
    return DatabaseManager.get_instance().get_session_maker()


def get_database_url() -> str | None:
    """
    Get the database URL, initializing if necessary.

    Returns:
        str | None: The database URL, or None if not configured

    Raises:
        ValidationError: If database cannot be initialized
    """
    return DatabaseManager.get_instance().get_database_url()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get database session.

    Yields:
        AsyncSession: Database session for async operations
    """

    context = create_error_context()
    context.metadata["operation"] = "database_session"

    logger.debug("Creating database session")
    session_maker = get_session_maker()  # Initialize if needed
    async with session_maker() as session:
        try:
            logger.debug("Database session created successfully")
            yield session
        except HTTPException:
            # HTTP exceptions (including LoggedHTTPException) are business logic errors,
            # not database errors. They're already logged by LoggedHTTPException,
            # so we should not log them as database errors. Just re-raise.
            raise
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Top-level dependency handler for database sessions must catch any exception during session usage to perform safety rollback before session is automatically closed, ensuring data integrity for any partial operations
            # Only log actual database-related exceptions
            context.metadata["error_type"] = type(e).__name__
            context.metadata["error_message"] = str(e)
            logger.error(
                "Database session error",
                context=context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            try:
                await session.rollback()
                logger.debug("Database session rolled back after error")
            except Exception as rollback_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Safety catch during error handling, if session rollback itself fails we log the failure but must re-raise the original exception to avoid masking the initial root cause
                logger.error(
                    "Failed to rollback database session",
                    context=context.to_dict(),
                    rollback_error=str(rollback_error),
                )
            raise
        finally:
            # Session is automatically closed by the async context manager
            # Log session closure for monitoring (debug level to avoid noise)
            logger.debug("Database session closed")


async def init_db() -> None:
    """
    Initialize database connection and verify configuration.

    NOTE: DDL (table creation) is NOT managed by this function.
    All database schema must be created via SQL scripts in db/authoritative_schema.sql
    and applied using database management scripts (e.g., psql).

    This function only:
    - Initializes the database engine and session maker
    - Configures SQLAlchemy mappers for ORM relationships
    - Verifies database connectivity

    To create tables, use the SQL script db/authoritative_schema.sql.
    """
    context = create_error_context()
    context.metadata["operation"] = "init_db"

    logger.info("Initializing database connection")

    try:
        # Import all models to ensure they're registered with metadata
        # NOTE: NPC models are NOT imported here - they belong to the NPC database
        # Configure all mappers before setting up relationships
        from sqlalchemy.orm import configure_mappers

        # CRITICAL: Import ALL models that use metadata before configure_mappers()
        # This allows SQLAlchemy to resolve string references in relationships
        # Do NOT import NPC models here - they use npc_metadata, not metadata
        # These imports are required for side effects (model registration) but appear unused
        from server.models.invite import (
            Invite,  # noqa: F401  # pylint: disable=unused-import  # Reason: Import required for SQLAlchemy model registration side effects, not directly used
        )
        from server.models.lucidity import (  # noqa: F401  # pylint: disable=unused-import  # Reason: Imports required for SQLAlchemy model registration side effects, not directly used
            LucidityAdjustmentLog,
            LucidityCooldown,
            LucidityExposureState,
            PlayerLucidity,
        )
        from server.models.player import (
            Player,  # noqa: F401  # pylint: disable=unused-import  # Reason: Import required for SQLAlchemy model registration side effects, not directly used
        )
        from server.models.user import (
            User,  # noqa: F401  # pylint: disable=unused-import  # Reason: Import required for SQLAlchemy model registration side effects, not directly used
        )

        logger.debug("Configuring SQLAlchemy mappers")
        # ARCHITECTURE FIX Phase 3.1: Relationships now defined directly in models
        # String references resolved via SQLAlchemy registry after all models imported
        configure_mappers()

        # Initialize engine to verify connectivity
        engine = get_engine()  # Initialize if needed

        # Verify database connectivity with a simple query
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
            logger.info("Database connection verified successfully")

        logger.info("Database initialization complete - DDL must be applied separately via SQL scripts")
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Top-level database initialization must catch any exception to ensure failures during mapper configuration or connectivity checks are logged with structured context before application fails to start
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Database initialization failed",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        raise


async def close_db() -> None:
    """Close database connections."""
    context = create_error_context()
    context.metadata["operation"] = "close_db"

    logger.info("Closing database connections")
    try:
        db_manager = DatabaseManager.get_instance()
        # Ensure engine is initialized so dispose is meaningful
        _ = db_manager.get_engine()
        await db_manager.close()
        logger.info("Database connections closed")
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Global database closure function must catch any error during resource cleanup to ensure failures are logged with structured context, then re-raises
        # RuntimeError as expected by the application's lifecycle management.
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Error closing database connections",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        # Tests expect a RuntimeError on failure here
        raise RuntimeError("Failed to close database connections") from e


def get_database_path() -> Path | None:
    """
    Get the database file path.

    DEPRECATED: PostgreSQL does not use file paths. This function always returns None
    for PostgreSQL databases. Kept for backward compatibility with code that may
    check for database paths.

    Returns:
        Path | None: Always None for PostgreSQL (no file path)
    """
    # Test override path handling without requiring initialization
    # Check module-level _database_url_state first for backward compatibility
    import server.database as db_module

    from .database import _get_database_url_state

    # Check dict-based storage first, then fall back to direct attribute for backward compatibility
    # Handle empty string explicitly (empty string is falsy but we want to treat it as None)
    url_state = _get_database_url_state()
    # Empty string should be treated as None for validation.
    # Must use == "" (not "not url_state"): None means "not set" and we fall back to other sources.
    if url_state == "":  # pylint: disable=use-implicit-booleaness-not-comparison-to-string
        raise ValidationError("Database URL is None")
    test_url = url_state or getattr(db_module, "_database_url", None) or get_test_database_url()
    if test_url is not None:
        url = test_url
        if not url:
            raise ValidationError("Database URL is None")
        if url.startswith("postgresql"):
            # PostgreSQL doesn't have a file path
            return None
        # Unsupported URL schemes should raise
        raise ValidationError(f"Unsupported database URL: {url}. Only PostgreSQL is supported.")

    return DatabaseManager.get_instance().get_database_path()


def ensure_database_directory() -> None:
    """
    Ensure database directory exists.

    DEPRECATED: PostgreSQL does not use file paths or directories. This function
    is a no-op for PostgreSQL databases. Kept for backward compatibility.

    For PostgreSQL, database directories are managed by the PostgreSQL server,
    not by the application.
    """
    db_path = get_database_path()
    # PostgreSQL always returns None, so this is effectively a no-op
    if db_path is not None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
