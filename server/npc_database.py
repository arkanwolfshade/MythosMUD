"""
NPC Database configuration for MythosMUD.

This module provides database connection, session management,
and initialization specifically for the NPC subsystem.
"""

import os
from collections.abc import AsyncGenerator
from pathlib import Path

from sqlalchemy import event
from sqlalchemy.ext.asyncio import (
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

# NPC Database URL configuration - read from environment variables
NPC_DATABASE_URL = os.getenv("NPC_DATABASE_URL")
if not NPC_DATABASE_URL:
    # Default to npcs.db in the data directory
    data_dir = Path(__file__).parent.parent.parent / "data" / "npcs"
    data_dir.mkdir(parents=True, exist_ok=True)
    NPC_DATABASE_URL = f"sqlite+aiosqlite:///{data_dir}/npcs.db"

logger.info("NPC Database URL configured", npc_database_url=NPC_DATABASE_URL)

# Create async engine for NPC database
# Use NullPool for tests to prevent SQLite file locking issues
# StaticPool keeps connections open, which causes problems with SQLite in test environments
pool_class = NullPool if "test" in NPC_DATABASE_URL else StaticPool

npc_engine = create_async_engine(
    NPC_DATABASE_URL,
    echo=False,
    poolclass=pool_class,
    pool_pre_ping=True,
    connect_args={
        "check_same_thread": False,
        "timeout": 30,
    },
)


# Enable foreign key constraints for SQLite
@event.listens_for(npc_engine.sync_engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Enable foreign key constraints for SQLite connections."""
    if "sqlite" in str(dbapi_connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
        print(f"DEBUG: Enabled foreign keys for connection: {dbapi_connection}")


logger.info("NPC Database engine created", pool_class=pool_class.__name__)

# Create async session maker for NPC database
npc_session_maker = async_sessionmaker(
    npc_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

logger.info("NPC Database session maker created")


async def get_npc_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Get an async database session for NPC operations.

    This function provides an async context manager for database sessions
    specifically for NPC operations.

    Yields:
        AsyncSession: An async SQLAlchemy session for NPC database operations

    Example:
        async for session in get_npc_async_session():
            npc = await session.get(NPCDefinition, npc_id)
            break
    """
    async with npc_session_maker() as session:
        try:
            logger.debug("Creating NPC database session")
            # Enable foreign key constraints for this session
            from sqlalchemy import text

            await session.execute(text("PRAGMA foreign_keys = ON"))
            yield session
            logger.debug("NPC Database session created successfully")
        except Exception as e:
            logger.error("NPC Database session error", error=str(e), exc_info=True)
            await session.rollback()
            raise
        finally:
            await session.close()
            logger.debug("Closing NPC database session")


async def init_npc_database() -> None:
    """
    Initialize the NPC database with proper schema.

    This function creates all necessary tables and indexes for the NPC subsystem.
    It should be called during application startup.

    Raises:
        ValidationError: If database initialization fails
    """
    try:
        async with npc_engine.begin() as conn:
            logger.info("Creating NPC database tables")
            await conn.run_sync(npc_metadata.create_all)
            # Enable foreign key constraints for SQLite
            from sqlalchemy import text

            await conn.execute(text("PRAGMA foreign_keys = ON"))
            logger.info("NPC Database tables created successfully")
    except Exception as e:
        context = create_error_context()
        context.metadata["operation"] = "npc_database_init"
        log_and_raise(
            ValidationError,
            f"Failed to initialize NPC database: {e}",
            context=context,
            details={"database_url": NPC_DATABASE_URL},
            user_friendly="NPC database initialization failed",
        )


async def close_npc_database() -> None:
    """
    Close the NPC database engine and cleanup resources.

    This function should be called during application shutdown.
    """
    try:
        await npc_engine.dispose()
        logger.info("NPC Database engine disposed successfully")
    except Exception as e:
        logger.error("Error disposing NPC database engine", error=str(e), exc_info=True)
