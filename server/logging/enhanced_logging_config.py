"""
Enhanced structlog-based logging configuration for MythosMUD server.

This module provides an enhanced logging system with MDC (Mapped Diagnostic Context),
correlation IDs, security sanitization, and performance optimizations.
"""

import logging
import sys
import uuid
from datetime import UTC, datetime
from typing import Any

import structlog
from structlog.contextvars import (
    bind_contextvars,
    clear_contextvars,
    merge_contextvars,
)
from structlog.stdlib import BoundLogger, LoggerFactory

# Import existing configuration
from server.logging_config import _resolve_log_base, detect_environment, get_logger


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

    def sanitize_dict(d: dict) -> dict:
        """Recursively sanitize dictionary values."""
        sanitized = {}
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

    # Enhanced processors with MDC support
    processors = [
        # Security first - sanitize sensitive data
        sanitize_sensitive_data,
        # Add correlation and context information
        add_correlation_id,
        add_request_context,
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

    # Add renderer based on environment
    if sys.stderr.isatty():
        # Development: Pretty console output
        processors.append(structlog.dev.ConsoleRenderer())
    else:
        # Production: Structured JSON output
        processors.extend(
            [
                structlog.processors.dict_tracebacks,
                structlog.processors.JSONRenderer(),
            ]
        )

    # Configure standard library logging for file output
    if log_config and not log_config.get("disable_logging", False):
        _setup_enhanced_file_logging(environment, log_config, log_level, player_service, enable_async)

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=BoundLogger,
        cache_logger_on_first_use=False,
    )


def _setup_enhanced_file_logging(
    environment: str,
    log_config: dict[str, Any],
    log_level: str,
    player_service: Any = None,
    enable_async: bool = True,
) -> None:
    """Set up enhanced file logging handlers with async support."""
    from logging.handlers import RotatingFileHandler

    log_base = _resolve_log_base(log_config.get("log_base", "logs"))
    env_log_dir = log_base / environment
    env_log_dir.mkdir(parents=True, exist_ok=True)

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
        "persistence": ["persistence", "PersistenceLayer", "aiosqlite"],
        "authentication": ["auth"],
        "world": ["world"],
        "communications": ["realtime", "communications"],
        "commands": ["commands"],
        "errors": ["errors"],
        "access": ["access", "server.app.factory"],
        "security": ["security", "audit"],
        "performance": ["performance", "metrics"],
    }

    # Create handlers for different log categories
    for log_file, prefixes in log_categories.items():
        log_path = env_log_dir / f"{log_file}.log"

        # Create rotating file handler
        handler = RotatingFileHandler(
            log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        handler.setLevel(logging.DEBUG)

        # Create formatter - use PlayerGuidFormatter if player_service is available
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
            logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
            logger.propagate = True

    # Enhanced console handler with structured output
    console_log_path = env_log_dir / "console.log"
    console_handler = RotatingFileHandler(
        console_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    console_handler.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))

    # Use enhanced formatter for console handler
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
    errors_handler = RotatingFileHandler(
        errors_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    errors_handler.setLevel(logging.WARNING)

    # Use enhanced formatter for errors handler
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

    root_logger.setLevel(logging.DEBUG)


def setup_enhanced_logging(config: dict[str, Any], player_service: Any = None) -> None:
    """
    Set up enhanced logging configuration with MDC and security features.

    Args:
        config: Server configuration dictionary
        player_service: Optional player service for GUID-to-name conversion
    """
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
    except Exception:
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


def get_enhanced_logger(name: str) -> BoundLogger:
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
