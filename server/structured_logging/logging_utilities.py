"""
Logging utilities for directory management, path resolution, and environment detection.

This module provides thread-safe directory creation, log path resolution,
log file rotation, and environment detection utilities.
"""

import os
import sys
import threading
import time
from datetime import UTC, datetime
from pathlib import Path

import structlog

logger = structlog.get_logger(__name__)

# Thread-safe directory creation locks (one lock per directory path)
_dir_locks: dict[str, threading.Lock] = {}
_dir_locks_lock = threading.Lock()

# Cache of directories we've successfully created (avoids repeated mkdir calls)
# This prevents blocking on os.stat() inside mkdir() under heavy filesystem load
_created_dirs: set[str] = set()
_created_dirs_lock = threading.Lock()


def ensure_log_directory(log_path: Path) -> None:
    """
    Thread-safe directory creation for log files.

    This function ensures that the parent directory of a log file exists,
    using per-directory locks to prevent deadlocks when multiple threads
    try to create the same directory simultaneously.

    Uses a cache to avoid repeated mkdir() calls, which prevents blocking
    on os.stat() inside mkdir() under heavy filesystem load.

    Args:
        log_path: Path to the log file (directory will be created for parent)
    """
    if not log_path or not log_path.parent:
        return

    dir_path = log_path.parent
    dir_str = str(dir_path)

    # Fast path: check cache first (no filesystem access needed)
    with _created_dirs_lock:
        if dir_str in _created_dirs:
            return  # Directory already created in this process

    # Get or create lock for this specific directory path
    with _dir_locks_lock:
        if dir_str not in _dir_locks:
            _dir_locks[dir_str] = threading.Lock()
        lock = _dir_locks[dir_str]

    # Use per-directory lock to prevent concurrent creation attempts
    with lock:
        # Double-check cache after acquiring lock (another thread may have created it)
        with _created_dirs_lock:
            if dir_str in _created_dirs:
                return

        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            # Successfully created - add to cache
            with _created_dirs_lock:
                _created_dirs.add(dir_str)
        except (OSError, PermissionError) as e:
            # Log but don't raise - logging should not fail due to directory issues
            # This prevents deadlocks if directory creation fails
            # Note: We don't add to cache on failure, so we'll retry next time
            logger.warning(
                "Failed to create log directory",
                directory=str(dir_path),
                error=str(e),
                error_type=type(e).__name__,
            )


def resolve_log_base(log_base: str) -> Path:
    """
    Resolve log_base path to absolute path relative to project root.

    Args:
        log_base: Relative or absolute path to log directory

    Returns:
        Absolute path to log directory
    """
    log_path = Path(log_base)

    # If already absolute, return as is
    if log_path.is_absolute():
        return log_path

    # Find the project root (where pyproject.toml is located)
    current_dir = Path.cwd()
    project_root = None

    # Look for pyproject.toml in current directory or parents
    for parent in [current_dir] + list(current_dir.parents):
        if (parent / "pyproject.toml").exists():
            project_root = parent
            break

    if project_root:
        return project_root / log_path
    else:
        # Fallback to current directory if project root not found
        return current_dir / log_path


def rotate_log_files(env_log_dir: Path) -> None:
    """
    Rotate existing log files by renaming them with timestamps.

    This function implements the startup-time log rotation as described in the
    restricted archives. When the server starts, existing log files are renamed
    with timestamps before new log files are created, ensuring clean separation
    between server sessions.

    Enhanced with Windows-specific file locking handling to prevent
    PermissionError: [WinError 32] exceptions during concurrent access.
    Now recursively processes subdirectories to ensure all log files are
    rotated.

    Args:
        env_log_dir: Path to the environment-specific log directory
    """
    if not env_log_dir.exists():
        return

    # Generate timestamp for rotation
    timestamp = datetime.now(UTC).strftime("%Y_%m_%d_%H%M%S")

    # Get all log files in the directory and subdirectories
    # Include .log, .jsonl, and other common log file extensions
    log_files = []
    log_files.extend(env_log_dir.glob("*.log"))
    log_files.extend(env_log_dir.glob("*.jsonl"))
    log_files.extend(env_log_dir.rglob("*.log"))  # Recursive search
    log_files.extend(env_log_dir.rglob("*.jsonl"))  # Recursive search

    # Remove duplicates and filter out already rotated files
    log_files = list(set(log_files))
    log_files = [f for f in log_files if not f.name.endswith(f".{timestamp}")]

    if not log_files:
        return

    # Rotate each log file by renaming with timestamp
    for log_file in log_files:
        # Only rotate non-empty files
        if log_file.exists() and log_file.stat().st_size > 0:
            rotated_name = f"{log_file.stem}.log.{timestamp}"
            rotated_path = log_file.parent / rotated_name

            # Windows-specific retry logic for file locking issues
            max_retries = 3
            retry_delay = 0.1  # 100ms delay between retries

            for attempt in range(max_retries):
                try:
                    # On Windows use copy-then-truncate to avoid rename-while-open issues
                    if sys.platform == "win32":
                        try:
                            # Local import to avoid circulars
                            from server.structured_logging.windows_safe_rotation import _copy_then_truncate

                            _copy_then_truncate(str(log_file), str(rotated_path))
                        except OSError:
                            # If helper not available, fall back to rename with retry
                            log_file.rename(rotated_path)
                    else:
                        # Attempt the rename operation on non-Windows systems
                        log_file.rename(rotated_path)

                    # Log the rotation (this will go to the new log file)
                    # Use structlog directly to avoid circular import
                    rotation_logger = structlog.get_logger("server.structured_logging")
                    rotation_logger.info(
                        "Rotated log file",
                        old_name=log_file.name,
                        new_name=rotated_name,
                    )
                    break  # Success, exit retry loop

                except (OSError, PermissionError) as e:
                    if attempt < max_retries - 1:
                        # Wait before retrying
                        time.sleep(retry_delay)
                        retry_delay *= 2  # Exponential backoff
                    else:
                        # Final attempt failed, log the error
                        # Use structlog directly to avoid circular import
                        rotation_logger = structlog.get_logger("server.structured_logging")
                        rotation_logger.warning(
                            "Could not rotate log file after retries",
                            name=log_file.name,
                            error=str(e),
                            attempts=max_retries,
                        )


def detect_environment() -> str:
    """
    Detect the current environment based on various indicators.

    Returns:
        Environment name: "e2e_test", "unit_test", "local", or "production"

    Note: Valid environments are defined in .env files via LOGGING_ENVIRONMENT:
        - e2e_test: End-to-end testing with Playwright
        - unit_test: Unit and integration testing with pytest
        - local: Local development
        - production: Production deployment
    """
    # Define valid environments to prevent invalid directory creation
    VALID_ENVIRONMENTS = ["e2e_test", "unit_test", "production", "local"]

    # Check if running under pytest (unit tests)
    if "pytest" in sys.modules or "pytest" in sys.argv[0]:
        return "unit_test"

    # Check explicit environment variable (with validation)
    env = os.getenv("MYTHOSMUD_ENV")
    if env and env in VALID_ENVIRONMENTS:
        return env

    # Check if test configuration is being used
    if os.getenv("MYTHOSMUD_TEST_MODE"):
        return "unit_test"

    # Try to determine from LOGGING_ENVIRONMENT (Pydantic config)
    logging_env = os.getenv("LOGGING_ENVIRONMENT", "")
    if logging_env in VALID_ENVIRONMENTS:
        return logging_env

    # Fallback: check legacy config path for backward compatibility
    config_path = os.getenv("MYTHOSMUD_CONFIG_PATH", "")
    if "e2e_test" in config_path:
        return "e2e_test"
    elif "unit_test" in config_path:
        return "unit_test"
    elif "production" in config_path:
        return "production"
    elif "local" in config_path:
        return "local"

    # Default to local (not "development" - that's not a valid environment)
    return "local"
