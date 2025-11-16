"""
NPC Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization specifically for the NPC subsystem.

CRITICAL: Database initialization is LAZY and requires configuration to be loaded first.
         The system will FAIL LOUDLY if configuration is not properly set.
"""

import os
from collections.abc import AsyncGenerator
from pathlib import Path
from typing import Any

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool, StaticPool

from .exceptions import ValidationError
from .logging.enhanced_logging_config import get_logger
from .utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)

# LAZY INITIALIZATION: These are initialized on first use, not at import time
_npc_engine: AsyncEngine | None = None
_npc_async_session_maker: async_sessionmaker | None = None
_npc_database_url: str | None = None


def _initialize_npc_database() -> None:
    """
    Initialize NPC database engine and session maker from configuration.

    CRITICAL: This function FAILS LOUDLY if configuration is not properly set.

    Raises:
        ValidationError: If configuration is missing or invalid
    """
    global _npc_engine, _npc_async_session_maker, _npc_database_url

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
    except Exception as e:
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

    # Determine pool class based on database URL
    # Use NullPool for tests
    pool_class = NullPool if "test" in _npc_database_url else StaticPool

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

    # Create async engine for NPC database
    _npc_engine = create_async_engine(
        _npc_database_url,
        echo=False,
        poolclass=pool_class,
        pool_pre_ping=True,
        connect_args=connect_args,
    )

    logger.info("NPC Database engine created", pool_class=pool_class.__name__)

    # Create async session maker for NPC database
    _npc_async_session_maker = async_sessionmaker(
        _npc_engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )

    logger.info("NPC Database session maker created")


def get_npc_engine() -> AsyncEngine | None:
    """
    Get the NPC database engine, initializing if necessary.

    Returns:
        AsyncEngine | None: The NPC database engine

    Raises:
        ValidationError: If NPC database cannot be initialized
    """
    if _npc_engine is None:
        _initialize_npc_database()
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
    assert _npc_async_session_maker is not None, "NPC session maker not initialized"
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
    global _npc_async_session_maker
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
        except Exception as e:
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
            except Exception as rollback_error:
                logger.error(
                    "Failed to rollback NPC database session",
                    context=context.to_dict(),
                    rollback_error=str(rollback_error),
                )
            raise


async def init_npc_db():
    """
    Initialize NPC database connection and verify configuration.

    NOTE: DDL (table creation) is NOT managed by this function.
    All database schema must be created via SQL scripts in db/schema/
    and applied using database management scripts (e.g., psql).

    This function only:
    - Initializes the NPC database engine and session maker
    - Configures SQLAlchemy mappers for ORM relationships
    - Verifies database connectivity

    To create tables, use the SQL scripts in db/schema/ directory.
    """
    context = create_error_context()
    context.metadata["operation"] = "init_npc_db"

    logger.info("Initializing NPC database connection")

    try:
        # Import all NPC models to ensure they're registered with metadata
        from sqlalchemy.orm import configure_mappers

        from server.models.npc import NPCDefinition  # noqa: F401

        logger.debug("Configuring NPC SQLAlchemy mappers")
        configure_mappers()

        # Initialize engine to verify connectivity
        engine = get_npc_engine()  # Initialize if needed

        # Verify database connectivity with a simple query
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
            logger.info("NPC database connection verified successfully")

        logger.info("NPC database initialization complete - DDL must be applied separately via SQL scripts")
    except Exception as e:
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
    context = create_error_context()
    context.metadata["operation"] = "close_npc_db"

    logger.info("Closing NPC database connections")
    try:
        engine = get_npc_engine()  # Initialize if needed
        await engine.dispose()
        logger.info("NPC database connections closed")
    except Exception as e:
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Error closing NPC database connections",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        raise


def get_npc_database_path() -> Path:
    """
    Get the NPC database file path.

    Returns:
        Path: Path to the NPC database file
    """
    # Initialize database if needed
    if _npc_database_url is None:
        _initialize_npc_database()

    # After initialization, database URL should be set
    assert _npc_database_url is not None, "NPC database URL should be initialized"

    if _npc_database_url.startswith("sqlite+aiosqlite:///"):
        db_path = _npc_database_url.replace("sqlite+aiosqlite:///", "")
        return Path(db_path)
    else:
        context = create_error_context()
        context.metadata["operation"] = "get_npc_database_path"
        context.metadata["database_url"] = _npc_database_url
        log_and_raise(
            ValidationError,
            f"Unsupported NPC database URL: {_npc_database_url}",
            context=context,
            details={"database_url": _npc_database_url},
            user_friendly="Unsupported NPC database configuration",
        )
        # Satisfy type checker: log_and_raise raises
        raise AssertionError("unreachable")


def ensure_npc_database_directory():
    """Ensure NPC database directory exists."""
    db_path = get_npc_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
