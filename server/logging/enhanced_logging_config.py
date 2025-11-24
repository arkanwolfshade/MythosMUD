"""
Enhanced structlog-based logging configuration for MythosMUD server.

This module provides an enhanced logging system with MDC (Mapped Diagnostic
Context), correlation IDs, security sanitization, and performance optimizations.
"""

import json
import logging
import os
import sys
import threading
import time
import uuid
from datetime import UTC, datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any, cast

import structlog
from structlog.contextvars import (
    bind_contextvars,
    clear_contextvars,
    merge_contextvars,
)
from structlog.stdlib import BoundLogger, LoggerFactory

# Module-level logger for internal use
logger = structlog.get_logger(__name__)

_LOGGING_INITIALIZED = False
_LOGGING_SIGNATURE: str | None = None


def _resolve_log_base(log_base: str) -> Path:
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


def _rotate_log_files(env_log_dir: Path) -> None:
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
                            from server.logging.windows_safe_rotation import _copy_then_truncate

                            _copy_then_truncate(str(log_file), str(rotated_path))
                        except Exception:
                            # If helper not available, fall back to rename with retry
                            log_file.rename(rotated_path)
                    else:
                        # Attempt the rename operation on non-Windows systems
                        log_file.rename(rotated_path)

                    # Log the rotation (this will go to the new log file)
                    logger = get_enhanced_logger("server.logging")
                    logger.info(
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
                        logger = get_enhanced_logger("server.logging")
                        logger.warning(
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


def sanitize_sensitive_data(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Remove sensitive data from log entries.

    This processor automatically redacts sensitive information like passwords,
    tokens, and credentials from log entries to prevent information leakage.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to sanitize

    Returns:
        Sanitized event dictionary
    """
    sensitive_keys = [
        "password",
        "token",
        "secret",
        "key",
        "credential",
        "auth",
        "jwt",
        "api_key",
        "private_key",
        "session_token",
        "access_token",
        "refresh_token",
        "bearer",
        "authorization",
    ]

    def sanitize_dict(d: dict[str, Any]) -> dict[str, Any]:
        """Recursively sanitize dictionary values."""
        sanitized: dict[str, Any] = {}
        for key, value in d.items():
            if isinstance(value, dict):
                sanitized[key] = sanitize_dict(value)
            elif isinstance(key, str) and any(sensitive in key.lower() for sensitive in sensitive_keys):
                sanitized[key] = "[REDACTED]"
            else:
                sanitized[key] = value
        return sanitized

    return sanitize_dict(event_dict)


def add_correlation_id(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Add correlation ID to log entries if not already present.

    This processor ensures that all log entries have a correlation ID for
    request tracing and debugging.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to enhance

    Returns:
        Enhanced event dictionary with correlation ID
    """
    if "correlation_id" not in event_dict:
        event_dict["correlation_id"] = str(uuid.uuid4())

    return event_dict


def add_request_context(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Add request context information to log entries.

    This processor adds contextual information like request ID, user ID,
    and session information to log entries.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to enhance

    Returns:
        Enhanced event dictionary with request context
    """
    # Add timestamp if not present
    if "timestamp" not in event_dict:
        event_dict["timestamp"] = datetime.now(UTC).isoformat()

    # Add logger name for better traceability
    if "logger_name" not in event_dict:
        event_dict["logger_name"] = _name

    # Add request ID if not present
    if "request_id" not in event_dict:
        event_dict["request_id"] = str(uuid.uuid4())

    return event_dict


# Global player service registry for logging enhancement
_global_player_service = None
# Thread-local flag to prevent recursion in enhance_player_ids
_enhancing_player_ids = threading.local()


def set_global_player_service(player_service: Any) -> None:
    """
    Set the global player service for logging enhancement.

    This allows the logging system to access player information for
    enhancing log entries with player names.

    Args:
        player_service: The player service instance
    """
    global _global_player_service
    _global_player_service = player_service


def enhance_player_ids(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Enhance player_id fields with player names for better log readability.

    This processor automatically converts player_id fields to include both
    player name and ID in the format "<name>: <ID>" for better debugging.

    Args:
        _logger: Logger instance (unused)
        _name: Logger name (unused)
        event_dict: Event dictionary to enhance

    Returns:
        Enhanced event dictionary with player names
    """
    global _global_player_service

    # Prevent recursion: if we're already enhancing player IDs, skip immediately
    # Check this FIRST before any other operations
    if hasattr(_enhancing_player_ids, "active") and _enhancing_player_ids.active:
        return event_dict

    # Set recursion guard IMMEDIATELY before any operations that might trigger logging
    _enhancing_player_ids.active = True
    try:
        if _global_player_service and hasattr(_global_player_service, "persistence"):
            # Process any player_id fields in the event dictionary
            for key, value in event_dict.items():
                if key == "player_id" and isinstance(value, str):
                    # Check if this looks like a UUID
                    if len(value) == 36 and value.count("-") == 4:
                        # Import here to avoid circular import with server.exceptions -> enhanced_logging_config
                        # Define a local exception type alias for optional dependency
                        try:
                            from server.exceptions import DatabaseError as _ImportedDatabaseError  # noqa: F401

                            _DatabaseErrorType: type[BaseException] = _ImportedDatabaseError
                        except Exception:  # noqa: BLE001 - fallback if exceptions not yet available
                            _DatabaseErrorType = Exception

                        try:
                            # Try to get the player name
                            # Convert string to UUID if needed
                            import uuid

                            player_id_uuid = uuid.UUID(value) if isinstance(value, str) else value
                            player = _global_player_service.persistence.get_player(player_id_uuid)
                            if player and hasattr(player, "name"):
                                # Enhance the player_id field with the player name
                                event_dict[key] = f"<{player.name}>: {value}"
                        except (AttributeError, KeyError, TypeError, ValueError, _DatabaseErrorType, RecursionError):
                            # Silently skip on recursion or other errors - don't log to avoid infinite loop
                            # If lookup fails, leave the original value
                            pass
    finally:
        # Clear recursion guard - ALWAYS clear it, even if an exception occurs
        _enhancing_player_ids.active = False

    return event_dict


def configure_enhanced_structlog(
    environment: str | None = None,
    log_level: str = "INFO",
    log_config: dict[str, Any] | None = None,
    player_service: Any = None,
    enable_async: bool = True,
) -> None:
    """
    Configure enhanced Structlog with MDC, security, and performance features.

    Args:
        environment: Environment name (auto-detected if None)
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_config: Logging configuration dictionary
        player_service: Optional player service for GUID-to-name conversion
        enable_async: Enable async logging for better performance
    """
    if environment is None:
        environment = detect_environment()

    # Base processors with MDC support (no renderer)
    base_processors = [
        # Security first - sanitize sensitive data
        sanitize_sensitive_data,
        # Add correlation and context information
        add_correlation_id,
        add_request_context,
        # Enhance player IDs with names for better debugging
        enhance_player_ids,
        # Merge context variables (MDC)
        merge_contextvars,
        # Standard structlog processors
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    # Configure standard library logging for file output FIRST
    # This ensures file handlers are set up before structlog configuration
    if log_config and not log_config.get("disable_logging", False):
        _setup_enhanced_file_logging(environment, log_config, log_level, player_service, enable_async)

    # Configure structlog with a custom renderer that strips ANSI codes
    def strip_ansi_renderer(logger: Any, name: str, event_dict: dict[str, Any]) -> str | bytes:
        """Custom renderer that strips ANSI escape sequences."""
        import re

        # Use KeyValueRenderer to get the formatted message
        formatted = structlog.processors.KeyValueRenderer()(logger, name, event_dict)

        # Strip ANSI escape sequences
        ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
        return ansi_escape.sub("", formatted)

    structlog.configure(
        processors=base_processors + [strip_ansi_renderer],
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=BoundLogger,
        cache_logger_on_first_use=False,
    )

    # AI Agent: Now that structlog is configured, log the enhanced error handling setup
    # This confirms that the global error handler is capturing all errors from all modules
    if log_config and not log_config.get("disable_logging", False):
        env_log_dir = _resolve_log_base(log_config.get("log_base", "logs")) / environment
        errors_log_path = env_log_dir / "errors.log"
        configured_logger = structlog.get_logger(__name__)
        configured_logger.info(
            "Enhanced error logging configured",
            errors_log_path=str(errors_log_path),
            captures_all_errors=True,
            global_error_handler_enabled=True,
        )


class SafeRotatingFileHandler(RotatingFileHandler):
    """
    RotatingFileHandler that ensures directory exists before file operations.

    This handler wraps RotatingFileHandler to prevent FileNotFoundError
    when shouldRollover() is called from different threads in CI environments.
    """

    def shouldRollover(self, record):  # noqa: N802
        """
        Determine if rollover should occur, ensuring directory exists first.

        This overrides the parent method to ensure the log directory exists
        before attempting to open the log file, preventing race conditions
        in CI environments where directories might be cleaned up.
        """
        # Ensure directory exists before checking rollover
        if self.baseFilename:
            log_path = Path(self.baseFilename)
            log_path.parent.mkdir(parents=True, exist_ok=True)

        # Call parent method to perform actual rollover check
        return super().shouldRollover(record)


def _setup_enhanced_file_logging(
    environment: str,
    log_config: dict[str, Any],
    log_level: str,
    player_service: Any = None,
    enable_async: bool = True,  # noqa: ARG001
) -> None:
    """Set up enhanced file logging handlers with async support."""
    # Use Windows-safe rotation handlers when available
    _WinSafeHandler: type[RotatingFileHandler] = RotatingFileHandler
    try:
        from server.logging.windows_safe_rotation import WindowsSafeRotatingFileHandler as _ImportedWinSafeHandler

        _WinSafeHandler = _ImportedWinSafeHandler
    except Exception:  # noqa: BLE001 - optional enhancement
        _WinSafeHandler = RotatingFileHandler

    # Use SafeRotatingFileHandler as base for all handlers to prevent CI race conditions
    _BaseHandler = SafeRotatingFileHandler

    log_base = _resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    env_log_dir.mkdir(parents=True, exist_ok=True)

    # Rotate existing log files before setting up new handlers
    _rotate_log_files(env_log_dir)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Get rotation settings from config
    rotation_config = log_config.get("rotation", {})
    max_size_str = rotation_config.get("max_size", "10MB")
    backup_count = rotation_config.get("backup_count", 5)

    # Convert max_size string to bytes
    if isinstance(max_size_str, str):
        if max_size_str.endswith("MB"):
            max_bytes = int(max_size_str[:-2]) * 1024 * 1024
        elif max_size_str.endswith("KB"):
            max_bytes = int(max_size_str[:-2]) * 1024
        elif max_size_str.endswith("B"):
            max_bytes = int(max_size_str[:-1])
        else:
            max_bytes = int(max_size_str)
    else:
        max_bytes = max_size_str

    # Enhanced log categories with security and performance considerations
    log_categories = {
        "server": ["server", "uvicorn"],
        "persistence": ["persistence", "PersistenceLayer", "asyncpg"],
        "authentication": ["auth"],
        "world": ["world"],
        "communications": ["realtime", "communications"],
        "commands": ["commands"],
        "combat": [
            "services.combat_service",
            "services.combat_event_publisher",
            "services.npc_combat_integration_service",
            "services.player_combat_service",
            "validators.combat_validator",
            "logging.combat_audit",
        ],
        "errors": ["errors"],
        "access": ["access", "server.app.factory"],
        "security": ["security", "audit"],
        "performance": ["performance", "metrics"],
    }

    # Create handlers for different log categories
    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"

        # Create rotating file handler (Windows-safe on win32, with directory safety)
        handler_class = _BaseHandler
        try:
            if sys.platform == "win32":
                # Windows-safe handler also needs directory safety
                # Create a hybrid class that combines both features
                class SafeWinHandlerCategory(_WinSafeHandler):  # type: ignore[misc, valid-type]
                    def shouldRollover(self, record):  # noqa: N802
                        if self.baseFilename:
                            log_path = Path(self.baseFilename)
                            log_path.parent.mkdir(parents=True, exist_ok=True)
                        return super().shouldRollover(record)

                handler_class = SafeWinHandlerCategory
        except Exception:
            # Fallback to safe handler on any detection error
            handler_class = _BaseHandler

        # Ensure directory exists right before creating handler to prevent race conditions
        log_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            handler = handler_class(
                log_path,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
        except (FileNotFoundError, OSError):
            # If directory doesn't exist or was deleted, recreate it and try again
            log_path.parent.mkdir(parents=True, exist_ok=True)
            handler = handler_class(
                log_path,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
        handler.setLevel(logging.DEBUG)

        # Create formatter - use PlayerGuidFormatter if player_service is available
        formatter: logging.Formatter
        if player_service is not None:
            from server.logging.player_guid_formatter import PlayerGuidFormatter

            formatter = PlayerGuidFormatter(
                player_service=player_service,
                fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        else:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        handler.setFormatter(formatter)

        # Add handler to loggers that match the prefixes
        for prefix in prefixes:
            logger = logging.getLogger(prefix)
            logger.addHandler(handler)
            # Set DEBUG level for combat modules in local/debug environments
            if log_file == "combat" and (environment == "local" or log_level == "DEBUG"):
                logger.setLevel(logging.DEBUG)
            else:
                logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
            logger.propagate = True

    # Enhanced console handler with structured output
    console_log_path = env_log_dir / "console.log"
    handler_class = _BaseHandler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            class SafeWinHandlerConsole(_WinSafeHandler):  # type: ignore[misc, valid-type]
                def shouldRollover(self, record):  # noqa: N802
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        log_path.parent.mkdir(parents=True, exist_ok=True)
                    return super().shouldRollover(record)

            handler_class = SafeWinHandlerConsole
    except Exception:
        handler_class = _BaseHandler

    # Ensure directory exists right before creating handler to prevent race conditions
    console_log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        console_handler = handler_class(
            console_log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    except (FileNotFoundError, OSError):
        # If directory doesn't exist or was deleted, recreate it and try again
        console_log_path.parent.mkdir(parents=True, exist_ok=True)
        console_handler = handler_class(
            console_log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    console_handler.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Use enhanced formatter for console handler
    console_formatter: logging.Formatter
    if player_service is not None:
        from server.logging.player_guid_formatter import PlayerGuidFormatter

        console_formatter = PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        console_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)

    # Enhanced errors handler with security focus
    errors_log_path = env_log_dir / "errors.log"
    handler_class = _BaseHandler
    try:
        if sys.platform == "win32":
            # Windows-safe handler also needs directory safety
            class SafeWinHandlerErrors(_WinSafeHandler):  # type: ignore[misc, valid-type]
                def shouldRollover(self, record):  # noqa: N802
                    if self.baseFilename:
                        log_path = Path(self.baseFilename)
                        log_path.parent.mkdir(parents=True, exist_ok=True)
                    return super().shouldRollover(record)

            handler_class = SafeWinHandlerErrors
    except Exception:
        handler_class = _BaseHandler

    # Ensure directory exists right before creating handler to prevent race conditions
    errors_log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        errors_handler = handler_class(
            errors_log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    except (FileNotFoundError, OSError):
        # If directory doesn't exist or was deleted, recreate it and try again
        errors_log_path.parent.mkdir(parents=True, exist_ok=True)
        errors_handler = handler_class(
            errors_log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    errors_handler.setLevel(logging.WARNING)

    # Use enhanced formatter for errors handler
    errors_formatter: logging.Formatter
    if player_service is not None:
        from server.logging.player_guid_formatter import PlayerGuidFormatter

        errors_formatter = PlayerGuidFormatter(
            player_service=player_service,
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        errors_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    errors_handler.setFormatter(errors_formatter)
    root_logger.addHandler(errors_handler)

    # CRITICAL FIX: Route ALL ERROR and CRITICAL logs to errors.log
    # The above handler only captures "errors.*" prefix modules
    # This ensures ALL error-level logs from ANY module are captured
    # AI Agent: This fixes the observability gap where critical errors in combat,
    # persistence, and game mechanics were being silently suppressed
    # Ensure directory exists right before creating handler to prevent race conditions
    errors_log_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        global_errors_handler = handler_class(
            errors_log_path,  # Same file as errors_handler
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    except (FileNotFoundError, OSError):
        # If directory doesn't exist or was deleted, recreate it and try again
        errors_log_path.parent.mkdir(parents=True, exist_ok=True)
        global_errors_handler = handler_class(
            errors_log_path,  # Same file as errors_handler
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
    global_errors_handler.setLevel(logging.ERROR)  # ERROR and CRITICAL only
    global_errors_handler.setFormatter(errors_formatter)

    # Add to root logger to capture ALL errors from all modules
    root_logger.addHandler(global_errors_handler)

    root_logger.setLevel(logging.DEBUG)

    # AI Agent: Log after structlog is configured using structlog logger
    # This will be called after configure_enhanced_structlog() completes


def setup_enhanced_logging(
    config: dict[str, Any],
    player_service: Any = None,
    *,
    force_reconfigure: bool = False,
) -> None:
    """
    Set up enhanced logging configuration with MDC and security features.

    Args:
        config: Server configuration dictionary
        player_service: Optional player service for GUID-to-name conversion
        force_reconfigure: When True, tear down existing handlers before reconfiguring
    """
    global _LOGGING_INITIALIZED
    global _LOGGING_SIGNATURE

    config_signature = json.dumps(config, sort_keys=True, default=str)

    if _LOGGING_INITIALIZED and not force_reconfigure:
        setup_logger = get_logger("server.logging.setup")
        setup_logger.debug(
            "setup_enhanced_logging skipped; logging system already initialized",
            config_signature=_LOGGING_SIGNATURE,
        )
        return

    logging_config = config.get("logging", {})
    environment = logging_config.get("environment", detect_environment())
    log_level = logging_config.get("level", "INFO")
    enable_async = logging_config.get("enable_async", True)

    # Check if logging should be disabled
    disable_logging = logging_config.get("disable_logging", False)

    if disable_logging:
        # Configure minimal logging without file handlers
        configure_enhanced_structlog(environment, log_level, {"disable_logging": True}, player_service)
        return

    # Configure enhanced Structlog
    configure_enhanced_structlog(environment, log_level, logging_config, player_service, enable_async)

    # Configure uvicorn to use our enhanced StructLog system
    _configure_enhanced_uvicorn_logging()

    # Log the setup
    logger = get_logger("server.logging.enhanced")
    logger.info(
        "Enhanced logging system initialized",
        environment=environment,
        log_level=log_level,
        log_base=logging_config.get("log_base", "logs"),
        mdc_enabled=True,
        security_sanitization=True,
        correlation_ids=True,
    )

    _LOGGING_INITIALIZED = True
    _LOGGING_SIGNATURE = config_signature


def _configure_enhanced_uvicorn_logging() -> None:
    """Configure uvicorn to use our enhanced StructLog system."""
    logger = get_logger("uvicorn.enhanced")

    # Configure uvicorn's access logger to use our enhanced system
    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    uvicorn_access_logger.handlers = []
    uvicorn_access_logger.propagate = True
    uvicorn_access_logger.setLevel(logging.DEBUG)

    # Configure uvicorn's error logger
    uvicorn_error_logger = logging.getLogger("uvicorn.error")
    uvicorn_error_logger.handlers = []
    uvicorn_error_logger.propagate = True
    uvicorn_error_logger.setLevel(logging.DEBUG)

    # Configure uvicorn's main logger
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.handlers = []
    uvicorn_logger.propagate = True
    uvicorn_logger.setLevel(logging.DEBUG)

    logger.info("Enhanced uvicorn logging configured")


# Context management utilities
def bind_request_context(
    correlation_id: str | None = None,
    user_id: str | None = None,
    session_id: str | None = None,
    request_id: str | None = None,
    **kwargs,
) -> None:
    """
    Bind request context to the current logging context.

    This function sets up the logging context for a request, ensuring all
    subsequent log entries include the request context.

    Args:
        correlation_id: Unique correlation ID for the request
        user_id: User ID if available
        session_id: Session ID if available
        request_id: Request ID if available
        **kwargs: Additional context variables
    """
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())

    context_vars = {
        "correlation_id": correlation_id,
        "user_id": user_id,
        "session_id": session_id,
        "request_id": request_id,
        **kwargs,
    }

    # Remove None values
    context_vars = {k: v for k, v in context_vars.items() if v is not None}

    bind_contextvars(**context_vars)


def clear_request_context() -> None:
    """Clear the current request context from logging."""
    clear_contextvars()


def get_current_context() -> dict[str, Any]:
    """Get the current logging context."""
    try:
        # Use get_contextvars() to get the current context-local context
        return structlog.contextvars.get_contextvars()
    except (AttributeError, KeyError):
        # If there's no bound context, return empty dict
        return {}


def log_with_context(logger: BoundLogger, level: str, message: str, **kwargs) -> None:
    """
    Log a message with the current context automatically included.

    Args:
        logger: Structlog logger instance
        level: Log level (debug, info, warning, error, critical)
        message: Log message
        **kwargs: Additional log data
    """
    # Get current context and merge with additional kwargs
    current_context = get_current_context()
    log_data = {**current_context, **kwargs}

    # Log at the specified level
    log_method = getattr(logger, level.lower(), logger.info)
    log_method(message, **log_data)


def get_enhanced_logger(name: str) -> Any:  # Returns BoundLogger but typed as Any for flexibility
    """
    Get an enhanced logger instance with structured logging capabilities.

    This function provides a logger instance configured with enhanced
    structured logging processors and context management.

    Args:
        name: Logger name (typically module name)

    Returns:
        Enhanced bound logger instance
    """
    # Get the base logger and wrap it with enhanced capabilities
    base_logger = get_logger(name)

    # Return a bound logger with enhanced processors
    return structlog.wrap_logger(base_logger)


def get_logger(name: str) -> Any:  # Returns BoundLogger but typed as Any for flexibility
    """
    Get a Structlog logger with the specified name.

    This ensures all loggers are properly configured and write to the
    appropriate log files based on their category. As noted in the
    Pnakotic Manuscripts, proper categorization of knowledge is essential
    for its preservation.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured Structlog logger instance
    """
    return structlog.get_logger(name)


def update_logging_with_player_service(player_service: Any) -> None:
    """
    Update existing logging handlers to use PlayerGuidFormatter.

    This function should be called after the player service becomes available
    to enhance existing log handlers with GUID-to-name conversion.

    Args:
        player_service: The player service for GUID-to-name conversion
    """
    from server.logging.player_guid_formatter import PlayerGuidFormatter

    # Set the global player service for structlog processor enhancement
    set_global_player_service(player_service)

    # Create the enhanced formatter
    enhanced_formatter = PlayerGuidFormatter(
        player_service=player_service,
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Update all existing handlers with the enhanced formatter
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        if hasattr(handler, "setFormatter"):
            handler.setFormatter(enhanced_formatter)

    # Update handlers for specific log categories
    log_categories = [
        "server",
        "persistence",
        "authentication",
        "world",
        "communications",
        "commands",
        "errors",
        "access",
    ]

    for category in log_categories:
        logger = logging.getLogger(category)
        for handler in logger.handlers:
            if hasattr(handler, "setFormatter"):
                handler.setFormatter(enhanced_formatter)

    # Log that the enhancement has been applied
    structured_logger = cast(Any, get_logger("server.logging"))
    structured_logger.info("Logging system enhanced with PlayerGuidFormatter", player_service_available=True)


def log_exception_once(
    logger: BoundLogger,
    level: str,
    message: str,
    *,
    exc: Exception | None = None,
    mark_logged: bool = True,
    **kwargs: Any,
) -> None:
    """
    Log an exception once, respecting exceptions that have already been logged.

    Args:
        logger: Structlog bound logger instance.
        level: Logging level to use (for example, "error" or "warning").
        message: Log message to emit.
        exc: Optional exception to include in the log entry.
        mark_logged: When True, mark the exception as logged to prevent duplicates.
        **kwargs: Additional key-value pairs for structured logging.
    """
    if exc is not None:
        already_logged = getattr(exc, "already_logged", False)
        if already_logged:
            return
        kwargs.setdefault("error_type", type(exc).__name__)
        kwargs.setdefault("error", str(exc))

    log_method = getattr(logger, level.lower(), logger.error)
    log_method(message, **kwargs)

    if exc is not None and mark_logged:
        marker = getattr(exc, "mark_logged", None)
        if callable(marker):
            marker()
        else:
            cast(Any, exc)._already_logged = True
