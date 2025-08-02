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

from .metadata import metadata

# Database URL configuration - read from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL environment variable must be set. See server/env.example for configuration template."
    )

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
if not TEST_DATABASE_URL:
    raise ValueError(
        "TEST_DATABASE_URL environment variable must be set. See server/env.example for configuration template."
    )

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

# Create async session maker
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get database session.

    Yields:
        AsyncSession: Database session for async operations
    """
    async with async_session_maker() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    """
    Initialize database with all tables.

    Creates all tables defined in the metadata.
    """
    # Import all models to ensure they're registered with metadata
    from server.models.invite import Invite  # noqa: F401
    from server.models.player import Player  # noqa: F401
    from server.models.user import User  # noqa: F401

    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


async def close_db():
    """Close database connections."""
    await engine.dispose()


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
