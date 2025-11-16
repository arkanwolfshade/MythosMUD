"""
Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization for the MythosMUD application.

CRITICAL: Database initialization is LAZY and requires configuration to be loaded first.
         The system will FAIL LOUDLY if configuration is not properly set.
"""

import threading
from collections.abc import AsyncGenerator
from pathlib import Path

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


# Backward-compatibility override for tests expecting module-level URL
# Tests may patch `server.database._database_url` to control path resolution.
_database_url: str | None = None


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

        # Allow test override via module-level _database_url
        global _database_url
        if _database_url is not None:
            database_url = _database_url
        else:
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

        # PostgreSQL-only: Verify we have a PostgreSQL URL
        if not database_url.startswith("postgresql"):
            log_and_raise(
                ValidationError,
                f"Unsupported database URL: {database_url}. Only PostgreSQL is supported.",
                context=context,
                user_friendly="Database configuration error - PostgreSQL required",
            )

        # PostgreSQL URL (postgresql+asyncpg:// or postgresql://)
        if not database_url.startswith("postgresql+asyncpg"):
            # Convert postgresql:// to postgresql+asyncpg:// for async support
            self.database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
        else:
            self.database_url = database_url
        logger.info("Using PostgreSQL database URL from environment", database_url=self.database_url)

        # Determine pool class based on database URL
        # Use NullPool for tests, StaticPool for production
        pool_class = NullPool if "test" in self.database_url else StaticPool

        # Create async engine with PostgreSQL configuration
        self.engine = create_async_engine(
            self.database_url,
            echo=False,
            poolclass=pool_class,
            pool_pre_ping=True,
        )

        logger.info("Database engine created", pool_class=pool_class.__name__)

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
        assert self.engine is not None, "Database engine not initialized"
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
        assert self.session_maker is not None, "Session maker not initialized"
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
        Get the database file path (SQLite only).

        For PostgreSQL, returns None as there is no file path.

        Returns:
            Path | None: Path to the database file (SQLite) or None (PostgreSQL)
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
            # This should never be reached due to log_and_raise above
            raise RuntimeError("Unreachable code")

        if database_url.startswith("postgresql"):
            # PostgreSQL doesn't have a file path
            return None
        else:
            context = create_error_context()
            context.metadata["operation"] = "get_database_path"
            context.metadata["database_url"] = database_url
            log_and_raise(
                ValidationError,
                f"Unsupported database URL: {database_url}",
                context=context,
                details={"database_url": database_url},
                user_friendly="Unsupported database configuration",
            )
            # This should never be reached due to log_and_raise above
            raise RuntimeError("Unreachable code")

    async def close(self) -> None:
        """Close database connections."""
        if self.engine is not None:
            await self.engine.dispose()
            logger.info("Database connections closed")


# DEPRECATED: Module-level global removed - use ApplicationContainer instead
# For backward compatibility during migration, delegate to DatabaseManager.get_instance()
# TODO: Remove this function once all code uses container
def get_database_manager() -> DatabaseManager:
    """
    Get the database manager singleton.

    DEPRECATED: Use ApplicationContainer.database_manager instead.
    This function exists only for backward compatibility during migration.

    Returns:
        DatabaseManager: The database manager instance
    """
    return DatabaseManager.get_instance()


def get_engine() -> AsyncEngine:
    """
    Get the database engine, initializing if necessary.

    Returns:
        AsyncEngine: The database engine (never None)

    Raises:
        ValidationError: If database cannot be initialized
    """
    return get_database_manager().get_engine()


def get_session_maker() -> async_sessionmaker:
    """
    Get the async session maker, initializing if necessary.

    Returns:
        async_sessionmaker: The session maker (never None)

    Raises:
        ValidationError: If database cannot be initialized
    """
    return get_database_manager().get_session_maker()


def get_database_url() -> str | None:
    """
    Get the database URL, initializing if necessary.

    Returns:
        str | None: The database URL, or None if not configured

    Raises:
        ValidationError: If database cannot be initialized
    """
    return get_database_manager().get_database_url()


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


async def init_db() -> None:
    """
    Initialize database connection and verify configuration.

    NOTE: DDL (table creation) is NOT managed by this function.
    All database schema must be created via SQL scripts in db/schema/
    and applied using database management scripts (e.g., psql).

    This function only:
    - Initializes the database engine and session maker
    - Configures SQLAlchemy mappers for ORM relationships
    - Verifies database connectivity

    To create tables, use the SQL scripts in db/schema/ directory.
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
        from server.models.invite import Invite  # noqa: F401
        from server.models.player import Player  # noqa: F401
        from server.models.sanity import (  # noqa: F401
            PlayerSanity,
            SanityAdjustmentLog,
            SanityCooldown,
            SanityExposureState,
        )
        from server.models.user import User  # noqa: F401

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


async def close_db() -> None:
    """Close database connections."""
    context = create_error_context()
    context.metadata["operation"] = "close_db"

    logger.info("Closing database connections")
    try:
        db_manager = get_database_manager()
        # Ensure engine is initialized so dispose is meaningful
        _ = db_manager.get_engine()
        await db_manager.close()
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
        # Tests expect a RuntimeError on failure here
        raise RuntimeError("Failed to close database connections") from e


def get_database_path() -> Path | None:
    """
    Get the database file path (SQLite only).

    For PostgreSQL, returns None as there is no file path.

    Returns:
        Path | None: Path to the database file (SQLite) or None (PostgreSQL)
    """
    # Test override path handling without requiring initialization
    if _database_url is not None:
        url = _database_url
        if not url:
            raise ValidationError("Database URL is None")
        if url.startswith("postgresql"):
            # PostgreSQL doesn't have a file path
            return None
        # Unsupported URL schemes should raise
        raise ValidationError(f"Unsupported database URL: {url}. Only PostgreSQL is supported.")

    return get_database_manager().get_database_path()


def ensure_database_directory() -> None:
    """Ensure database directory exists (SQLite only)."""
    db_path = get_database_path()
    if db_path is not None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
