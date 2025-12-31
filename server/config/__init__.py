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

import threading
from functools import lru_cache
from os import getenv

from .models import AppConfig

__all__ = ["get_config", "reset_config", "AppConfig"]

# Module-level config cache
_config_instance = None
_config_lock = threading.Lock()


def _is_test_mode() -> bool:
    """
    Detect if running in test environment.

    Uses multiple detection methods to reliably identify pytest test execution:
    - Checks if pytest module is loaded
    - Checks for pytest-specific environment variables

    Returns:
        bool: True if running in test mode, False otherwise
    """
    import sys

    # Check for pytest module
    if "pytest" in sys.modules:
        return True

    # Check environment variables set by pytest
    if getenv("PYTEST_CURRENT_TEST") or getenv("_PYTEST_RAISE"):
        return True

    return False


def _create_config_instance() -> AppConfig:
    """
    Create a new AppConfig instance from current environment.

    This is a helper function to centralize config instantiation logic.

    Returns:
        AppConfig: A new AppConfig instance loaded from environment variables
    """
    # #region agent log
    import json
    import os
    import time
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".cursor", "debug.log")
    try:
        admin_pw_env = os.getenv("MYTHOSMUD_ADMIN_PASSWORD", "NOT_SET")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "id": f"log_{int(time.time())}_create_config_instance",
                        "timestamp": int(time.time() * 1000),
                        "location": "__init__.py:52",
                        "message": "Creating AppConfig instance - checking environment",
                        "data": {
                            "env_var_exists": "MYTHOSMUD_ADMIN_PASSWORD" in os.environ,
                            "env_var_value": admin_pw_env[:3] + "..." if len(admin_pw_env) > 3 and admin_pw_env != "NOT_SET" else admin_pw_env,
                            "env_var_length": len(admin_pw_env) if admin_pw_env != "NOT_SET" else 0,
                        },
                        "sessionId": "debug-session",
                        "runId": "ci-debug",
                        "hypothesisId": "E",
                    }
                )
                + "\n"
            )
    except Exception:
        pass  # Ignore logging errors
    # #endregion
    return AppConfig()


@lru_cache(maxsize=1)
def _get_config_cached() -> AppConfig:
    """
    Production config loader with caching.

    Uses both @lru_cache and global _config_instance for thread-safe singleton pattern.
    This is only used in production mode.

    Returns:
        AppConfig: Cached application configuration
    """
    global _config_instance
    with _config_lock:
        if _config_instance is None:
            _config_instance = _create_config_instance()
    return _config_instance


def _get_config_test() -> AppConfig:
    """
    Test config loader without caching - always returns fresh instances.

    This ensures test isolation by always creating a new config instance
    from the current environment state, without any caching.

    Returns:
        AppConfig: Fresh application configuration instance
    """
    return _create_config_instance()


def get_config() -> AppConfig:
    """
    Get application configuration (singleton in production, fresh in tests).

    In production mode, this function uses caching (@lru_cache + global instance)
    for performance. In test mode, it always returns a fresh instance to ensure
    test isolation and prevent race conditions.

    Configuration is loaded from environment variables and .env file.

    Returns:
        AppConfig: The application configuration

    Raises:
        ValidationError: If configuration is invalid or required fields are missing

    Example:
        config = get_config()
        logger.info("Server configuration", host=config.server.host, port=config.server.port)
    """
    if _is_test_mode():
        return _get_config_test()
    return _get_config_cached()


def reset_config() -> None:
    """
    Reset the configuration cache.

    In test mode, this is a no-op since get_config() always returns fresh instances.
    In production mode, this clears both the @lru_cache and global _config_instance.

    This is primarily used for testing to force configuration reload.
    Should not be called in production code.
    """
    global _config_instance  # pylint: disable=global-statement
    # JUSTIFICATION: Global statement required for thread-safe singleton pattern.
    # The _config_instance must be reset across function calls for test isolation.

    if _is_test_mode():
        # In test mode, get_config() always returns fresh instances
        # No cache to clear, but clear global state for consistency
        with _config_lock:
            _config_instance = None
            # Clear production cache if it exists (defensive)
            _get_config_cached.cache_clear()
        return

    # Production mode: clear both caches
    with _config_lock:
        _get_config_cached.cache_clear()
        _config_instance = None
        # Force cache clear again after reset to ensure consistency
        _get_config_cached.cache_clear()
