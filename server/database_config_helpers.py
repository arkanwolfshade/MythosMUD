"""
Database configuration helper functions.

This module provides utility functions for loading, validating, and configuring
database URLs and connection pool settings.
"""

from typing import Any

from pydantic import ValidationError as PydanticValidationError
from sqlalchemy.pool import NullPool

from .exceptions import ValidationError
from .utils.error_logging import log_and_raise

# Module-level test override for database URL
# Using a dict to avoid global statement while maintaining mutable state
_database_url_state: dict[str, str | None] = {"url": None}


def get_test_database_url() -> str | None:
    """Get test override database URL."""
    return _database_url_state["url"]


def set_test_database_url(url: str | None) -> None:
    """Set test override database URL."""
    _database_url_state["url"] = url


def load_database_url() -> str:
    """
    Load database URL from config or test override.

    Returns:
        Database URL string

    Raises:
        ValidationError: If URL cannot be loaded
    """
    test_url = _database_url_state["url"]
    if test_url is not None:
        return test_url

    try:
        from .config import get_config

        config = get_config()
        database_url = config.database.url
        return database_url
    except (PydanticValidationError, ImportError, RuntimeError) as e:
        log_and_raise(
            ValidationError,
            f"Failed to load configuration: {e}",
            operation="load_database_url",
            details={"config_error": str(e), "error_type": type(e).__name__},
            user_friendly="Database cannot be initialized: configuration not loaded or invalid",
        )


def validate_database_url(database_url: str | None) -> None:
    """
    Validate database URL is set and is PostgreSQL.

    Args:
        database_url: Database URL to validate

    Raises:
        ValidationError: If URL is invalid
    """
    if not database_url:
        log_and_raise(
            ValidationError,
            "Database URL is not configured",
            operation="validate_database_url",
            user_friendly="Database configuration error - URL not set",
        )
    if not database_url.startswith("postgresql"):
        log_and_raise(
            ValidationError,
            f"Unsupported database URL: {database_url}. Only PostgreSQL is supported.",
            operation="validate_database_url",
            database_url=database_url,
            user_friendly="Database configuration error - PostgreSQL required",
        )


def normalize_database_url(database_url: str) -> str:
    """
    Normalize database URL for asyncpg.

    Args:
        database_url: Original database URL

    Returns:
        Normalized database URL
    """
    if not database_url.startswith("postgresql+asyncpg"):
        return database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    return database_url


def configure_pool_settings(database_url: str) -> dict[str, Any]:
    """
    Configure pool settings based on database URL and config.

    Args:
        database_url: Database URL

    Returns:
        Dictionary of pool configuration kwargs
    """
    pool_kwargs: dict[str, Any] = {}
    if "test" in database_url:
        pool_kwargs["poolclass"] = NullPool
    else:
        from .config import get_config

        config = get_config()
        db_config_dict = config.database.model_dump()
        pool_kwargs.update(
            {
                "pool_size": db_config_dict["pool_size"],
                "max_overflow": db_config_dict["max_overflow"],
                "pool_timeout": db_config_dict["pool_timeout"],
            }
        )
    return pool_kwargs
