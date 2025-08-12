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

from .logging_config import get_logger
from .metadata import metadata

logger = get_logger(__name__)

# Database URL configuration - read from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    logger.error("DATABASE_URL environment variable not set")
    raise ValueError(
        "DATABASE_URL environment variable must be set. See server/env.example for configuration template."
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
    logger.debug("Creating database session")
    async with async_session_maker() as session:
        try:
            logger.debug("Database session created successfully")
            yield session
        except Exception as e:
            logger.error(f"Database session error: {type(e).__name__}: {str(e)}")
            logger.debug(f"Database session error details: {type(e).__name__}: {str(e)}")
            await session.rollback()
            raise
        finally:
            logger.debug("Closing database session")
            await session.close()


async def init_db():
    """
    Initialize database with all tables.

    Creates all tables defined in the metadata.
    """
    logger.info("Initializing database")

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


async def close_db():
    """Close database connections."""
    logger.info("Closing database connections")
    await engine.dispose()
    logger.info("Database connections closed")


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
        raise ValueError(f"Unsupported database URL: {DATABASE_URL}")


def ensure_database_directory():
    """Ensure database directory exists."""
    db_path = get_database_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
