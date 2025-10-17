"""
Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization for the MythosMUD application.

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
from .metadata import metadata
from .utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)

# LAZY INITIALIZATION: These are initialized on first use, not at import time
_engine: AsyncEngine | None = None
_async_session_maker: async_sessionmaker | None = None
_database_url: str | None = None


def _initialize_database() -> None:
    """
    Initialize database engine and session maker from configuration.

    CRITICAL: This function FAILS LOUDLY if configuration is not properly set.

    Raises:
        ValidationError: If configuration is missing or invalid
    """
    global _engine, _async_session_maker, _database_url

    # Avoid re-initialization
    if _engine is not None:
        return

    context = create_error_context()
    context.metadata["operation"] = "database_initialization"

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

    # Load configuration - this will FAIL LOUDLY with ValidationError if required fields missing
    try:
        config = get_config()
        database_url = config.database.url
    except Exception as e:
        log_and_raise(
            ValidationError,
            f"Failed to load configuration: {e}",
            context=context,
            details={"config_error": str(e)},
            user_friendly="Database cannot be initialized: configuration not loaded or invalid",
        )

    # Handle database_url - could be a path or a full SQLite URL
    if database_url.startswith("sqlite"):
        # Already a full SQLite URL (from environment variable)
        _database_url = database_url
        logger.info("Using database URL from environment", database_url=_database_url)
    else:
        # It's a path from YAML - convert to absolute path and construct SQLite URL
        db_path_obj = Path(database_url).resolve()
        _database_url = f"sqlite+aiosqlite:///{db_path_obj}"
        logger.info("Database URL configured from YAML", database_url=_database_url, db_path=str(db_path_obj))

    # Determine pool class based on database URL
    # Use NullPool for tests to prevent SQLite file locking issues
    pool_class = NullPool if "test" in _database_url else StaticPool

    # Create async engine
    _engine = create_async_engine(
        _database_url,
        echo=False,
        poolclass=pool_class,
        pool_pre_ping=True,
        connect_args={
            "check_same_thread": False,
            "timeout": 30,
        },
    )

    # Enable foreign key constraints for SQLite
    @event.listens_for(_engine.sync_engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        """Enable foreign key constraints for SQLite connections."""
        conn_str = str(dbapi_connection)
        conn_type = str(type(dbapi_connection))

        # Check both the connection string and type for sqlite (case-insensitive)
        if "sqlite" in conn_str.lower() or "sqlite" in conn_type.lower():
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

    logger.info("Database engine created", pool_class=pool_class.__name__)

    # Create async session maker
    _async_session_maker = async_sessionmaker(
        _engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )

    logger.info("Database session maker created")


def get_engine() -> AsyncEngine:
    """
    Get the database engine, initializing if necessary.

    Returns:
        AsyncEngine: The database engine

    Raises:
        ValidationError: If database cannot be initialized
    """
    if _engine is None:
        _initialize_database()
    return _engine


def get_session_maker() -> async_sessionmaker:
    """
    Get the async session maker, initializing if necessary.

    Returns:
        async_sessionmaker: The session maker

    Raises:
        ValidationError: If database cannot be initialized
    """
    if _async_session_maker is None:
        _initialize_database()
    return _async_session_maker


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
        except Exception as e:
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
            except Exception as rollback_error:
                logger.error(
                    "Failed to rollback database session",
                    context=context.to_dict(),
                    rollback_error=str(rollback_error),
                )
            raise
        # Session is automatically closed by the async context manager


async def init_db():
    """
    Initialize database with all tables.

    Creates all tables defined in the metadata.
    """
    context = create_error_context()
    context.metadata["operation"] = "init_db"

    logger.info("Initializing database")

    try:
        # Import all models to ensure they're registered with metadata
        # Configure all mappers before setting up relationships
        from sqlalchemy.orm import configure_mappers

        from server.models.invite import Invite  # noqa: F401
        from server.models.npc import NPCDefinition, NPCSpawnRule  # noqa: F401
        from server.models.player import Player  # noqa: F401
        from server.models.user import User  # noqa: F401

        logger.debug("Configuring SQLAlchemy mappers")
        configure_mappers()

        # Set up relationships after all models are imported and configured
        from server.models.relationships import setup_relationships

        logger.debug("Setting up model relationships")
        setup_relationships()

        engine = get_engine()  # Initialize if needed
        async with engine.begin() as conn:
            logger.info("Creating database tables")
            await conn.run_sync(metadata.create_all)
            # Enable foreign key constraints for SQLite
            await conn.execute(text("PRAGMA foreign_keys = ON"))
            logger.info("Database tables created successfully")
    except Exception as e:
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Database initialization failed",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        raise


async def close_db():
    """Close database connections."""
    context = create_error_context()
    context.metadata["operation"] = "close_db"

    logger.info("Closing database connections")
    try:
        engine = get_engine()  # Initialize if needed
        await engine.dispose()
        logger.info("Database connections closed")
    except Exception as e:
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Error closing database connections",
            context=context.to_dict(),
            error=str(e),
            error_type=type(e).__name__,
        )
        raise


def get_database_path() -> Path:
    """
    Get the database file path.

    Returns:
        Path: Path to the database file
    """
    # Initialize database if needed
    if _database_url is None:
        _initialize_database()

    if _database_url.startswith("sqlite+aiosqlite:///"):
        db_path = _database_url.replace("sqlite+aiosqlite:///", "")
        return Path(db_path)
    else:
        context = create_error_context()
        context.metadata["operation"] = "get_database_path"
        context.metadata["database_url"] = _database_url
        log_and_raise(
            ValidationError,
            f"Unsupported database URL: {_database_url}",
            context=context,
            details={"database_url": _database_url},
            user_friendly="Unsupported database configuration",
        )


def ensure_database_directory():
    """Ensure database directory exists."""
    db_path = get_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
