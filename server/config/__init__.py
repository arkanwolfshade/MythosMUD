"""
Configuration module for MythosMUD server.

This module provides type-safe, validated configuration using Pydantic BaseSettings.
Replaces the legacy config_loader.py with modern configuration management.

Usage:
    from server.config import get_config

    config = get_config()
    logger.info("Configuration loaded", host=config.server.host, port=config.server.port)
    logger.info("Database configuration", url=config.database.url)
"""

from functools import lru_cache
from os import environ, getenv

from .models import AppConfig

__all__ = ["get_config", "reset_config", "AppConfig"]

# Module-level config cache
_config_instance = None


@lru_cache(maxsize=1)
def get_config() -> AppConfig:
    """
    Get application configuration (singleton).

    This function loads and caches the application configuration.
    Configuration is loaded from environment variables and .env file.

    Returns:
        AppConfig: The application configuration

    Raises:
        ValidationError: If configuration is invalid or required fields are missing

    Example:
        config = get_config()
        logger.info("Server configuration", host=config.server.host, port=config.server.port)
    """
    global _config_instance

    if _config_instance is None:
        try:
            _config_instance = AppConfig()
        except Exception as e:
            # Test resilience: if only the primary database URL is missing, provide a safe default in tests
            env = getenv("MYTHOSMUD_ENV", "").lower()
            if env == "test" and "Field required" in str(e) and "DatabaseConfig" in str(e) and "url" in str(e):
                # Provide an in-memory SQLite URL to satisfy components that don't use the main DB
                environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
                _config_instance = AppConfig()
            else:
                raise

    return _config_instance


def reset_config() -> None:
    """
    Reset the configuration cache.

    This is primarily used for testing to force configuration reload.
    Should not be called in production code.
    """
    global _config_instance

    _config_instance = None
    get_config.cache_clear()
