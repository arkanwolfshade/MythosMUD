"""
NPC Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization specifically for the NPC subsystem.

CRITICAL: Database initialization is LAZY and requires configuration to be loaded first.
         The system will FAIL LOUDLY if configuration is not properly set.
"""

from collections.abc import AsyncGenerator
from pathlib import Path

from sqlalchemy import event, text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool, StaticPool

from .exceptions import ValidationError
from .logging_config import get_logger
from .npc_metadata import npc_metadata
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

    # Load configuration - will FAIL LOUDLY with ValidationError if required fields missing
    try:
        config = get_config()
        npc_database_url = config.database.npc_url
    except Exception as e:
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
    # Use NullPool for tests to prevent SQLite file locking issues
    pool_class = NullPool if "test" in _npc_database_url else StaticPool

    # Create async engine for NPC database
    _npc_engine = create_async_engine(
        _npc_database_url,
        echo=False,
        poolclass=pool_class,
        pool_pre_ping=True,
        connect_args={
            "check_same_thread": False,
            "timeout": 30,
        },
    )

    # Enable foreign key constraints for SQLite
    @event.listens_for(_npc_engine.sync_engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        """Enable foreign key constraints for SQLite connections."""
        conn_str = str(dbapi_connection)
        conn_type = str(type(dbapi_connection))
        logger.debug(f"NPC database connect event fired, type: {conn_type}, str: {conn_str[:100]}")

        # Check both the connection string and type for sqlite
        if "sqlite" in conn_str.lower() or "sqlite" in conn_type.lower():
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
            logger.debug("Foreign keys enabled for NPC database connection")
        else:
            logger.warning(f"Skipping PRAGMA for non-SQLite connection: {conn_type}")

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


def get_npc_engine() -> AsyncEngine:
    """
    Get the NPC database engine, initializing if necessary.

    Returns:
        AsyncEngine: The NPC database engine

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
        async_sessionmaker: The NPC session maker

    Raises:
        ValidationError: If NPC database cannot be initialized
    """
    if _npc_async_session_maker is None:
        _initialize_npc_database()
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
    session_maker = get_npc_session_maker()  # Initialize if needed
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
    Initialize NPC database with all tables.

    Creates all tables defined in the NPC metadata.
    """
    context = create_error_context()
    context.metadata["operation"] = "init_npc_db"

    logger.info("Initializing NPC database")

    try:
        # Import all NPC models to ensure they're registered with metadata
        from sqlalchemy.orm import configure_mappers

        from server.models.npc import NPCDefinition  # noqa: F401

        logger.debug("Configuring NPC SQLAlchemy mappers")
        configure_mappers()

        engine = get_npc_engine()  # Initialize if needed
        async with engine.begin() as conn:
            logger.info("Creating NPC database tables")
            await conn.run_sync(npc_metadata.create_all)
            # Enable foreign key constraints for SQLite
            await conn.execute(text("PRAGMA foreign_keys = ON"))
            logger.info("NPC database tables created successfully")
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


def ensure_npc_database_directory():
    """Ensure NPC database directory exists."""
    db_path = get_npc_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
