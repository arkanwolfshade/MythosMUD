"""
Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization for the MythosMUD application.
"""

import os
from collections.abc import AsyncGenerator
from pathlib import Path

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import StaticPool

from .exceptions import ValidationError
from .logging_config import get_logger
from .metadata import metadata
from .utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)

# Database URL configuration - read from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    context = create_error_context()
    context.metadata["operation"] = "database_config"
    log_and_raise(
        ValidationError,
        "DATABASE_URL environment variable not set",
        context=context,
        details={"config_file": "server/env.example"},
        user_friendly="Database configuration is missing",
    )

logger.info("Database URL configured", database_url=DATABASE_URL)

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    poolclass=StaticPool,
    pool_pre_ping=True,
    pool_recycle=3600,
    connect_args={
        "check_same_thread": False,
        "timeout": 30,
    },
)

logger.info("Database engine created", pool_class="StaticPool", pool_recycle=3600)

# Create async session maker
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

logger.info("Database session maker created")


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get database session.

    Yields:
        AsyncSession: Database session for async operations
    """
    context = create_error_context()
    context.metadata["operation"] = "database_session"

    logger.debug("Creating database session")
    async with async_session_maker() as session:
        try:
            logger.debug("Database session created successfully")
            yield session
        except Exception as e:
            context.metadata["error_type"] = type(e).__name__
            context.metadata["error_message"] = str(e)
            logger.error(
                "Database session error",
                **context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            try:
                await session.rollback()
            except Exception as rollback_error:
                logger.error(
                    "Failed to rollback database session",
                    **context.to_dict(),
                    rollback_error=str(rollback_error),
                )
            raise
        finally:
            logger.debug("Closing database session")
            try:
                await session.close()
            except Exception as close_error:
                logger.warning(
                    "Error closing database session",
                    **context.to_dict(),
                    close_error=str(close_error),
                )


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
        from server.models.player import Player  # noqa: F401
        from server.models.user import User  # noqa: F401

        logger.debug("Configuring SQLAlchemy mappers")
        configure_mappers()

        # Set up relationships after all models are imported and configured
        from server.models.relationships import setup_relationships

        logger.debug("Setting up model relationships")
        setup_relationships()

        async with engine.begin() as conn:
            logger.info("Creating database tables")
            await conn.run_sync(metadata.create_all)
            logger.info("Database tables created successfully")
    except Exception as e:
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Database initialization failed",
            **context.to_dict(),
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
        await engine.dispose()
        logger.info("Database connections closed")
    except Exception as e:
        context.metadata["error_type"] = type(e).__name__
        context.metadata["error_message"] = str(e)
        logger.error(
            "Error closing database connections",
            **context.to_dict(),
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
    if DATABASE_URL.startswith("sqlite+aiosqlite:///"):
        db_path = DATABASE_URL.replace("sqlite+aiosqlite:///", "")
        return Path(db_path)
    else:
        context = create_error_context()
        context.metadata["operation"] = "get_database_path"
        context.metadata["database_url"] = DATABASE_URL
        log_and_raise(
            ValidationError,
            f"Unsupported database URL: {DATABASE_URL}",
            context=context,
            details={"database_url": DATABASE_URL},
            user_friendly="Unsupported database configuration",
        )


def ensure_database_directory():
    """Ensure database directory exists."""
    db_path = get_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
