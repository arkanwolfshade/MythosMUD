"""
Enhanced structlog-based logging configuration for MythosMUD server.

This module provides an enhanced logging system with MDC (Mapped Diagnostic
Context), correlation IDs, security sanitization, and performance optimizations.

This is the main entry point for the logging system. Implementation details
are split across multiple modules for better maintainability.
"""

# pylint: disable=too-few-public-methods  # Reason: Logging configuration classes with focused responsibility, minimal public interface

import json
import logging
import re
from typing import Any, cast

import structlog
from structlog.contextvars import merge_contextvars
from structlog.stdlib import BoundLogger, LoggerFactory

# Import from refactored modules
from server.structured_logging.logging_context import (
    bind_request_context as _bind_request_context,
)
from server.structured_logging.logging_context import (
    clear_request_context as _clear_request_context,
)
from server.structured_logging.logging_context import (
    get_current_context as _get_current_context,
)
from server.structured_logging.logging_context import (
    log_with_context as _log_with_context,
)
from server.structured_logging.logging_file_setup import setup_enhanced_file_logging
from server.structured_logging.logging_handlers import create_aggregator_handler
from server.structured_logging.logging_processors import (
    add_correlation_id,
    add_request_context,
    enhance_player_ids,
    sanitize_sensitive_data,
    set_global_player_service,
)
from server.structured_logging.logging_utilities import (
    detect_environment,
    ensure_log_directory,
    resolve_log_base,
    rotate_log_files,
)

# Re-export public functions for backward compatibility
bind_request_context = _bind_request_context
clear_request_context = _clear_request_context
get_current_context = _get_current_context
log_with_context = _log_with_context

# Re-export private functions for backward compatibility (used by other modules)
_resolve_log_base = resolve_log_base
_ensure_log_directory = ensure_log_directory
_rotate_log_files = rotate_log_files
_create_aggregator_handler = create_aggregator_handler
_setup_enhanced_file_logging = setup_enhanced_file_logging

# Module-level logger for internal use
# NOTE: Infrastructure files may use structlog.get_logger() directly to avoid
# circular imports during logging system initialization. This is acceptable for
# internal logging infrastructure code only. All other modules must use
# get_logger() from this module.
logger = structlog.get_logger(__name__)


class _LoggingState:  # pylint: disable=too-few-public-methods  # Reason: State container class with focused responsibility, minimal public interface
    """State container for logging initialization to avoid global statements."""

    initialized: bool = False
    signature: str | None = None


_logging_state = _LoggingState()


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
        setup_enhanced_file_logging(environment, log_config, log_level, player_service, enable_async)

    # Configure structlog with a custom renderer that strips ANSI codes
    def strip_ansi_renderer(bound_logger: Any, name: str, event_dict: dict[str, Any]) -> str | bytes:
        """Custom renderer that strips ANSI escape sequences."""
        try:
            # Use KeyValueRenderer to get the formatted message
            formatted = structlog.processors.KeyValueRenderer()(bound_logger, name, event_dict)

            # Strip ANSI escape sequences
            ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
            return ansi_escape.sub("", formatted)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Logging renderer can fail in various ways (regex errors, encoding issues, etc.), and we must return a safe error message to prevent logging failures from crashing the application
            # Graceful fallback: if rendering fails, return a safe error message
            # This prevents logging failures from crashing the application
            return f"Logging renderer error: {type(e).__name__}: {str(e)}"

    try:
        structlog.configure(
            processors=base_processors + [strip_ansi_renderer],
            context_class=dict,
            logger_factory=LoggerFactory(),
            wrapper_class=BoundLogger,
            cache_logger_on_first_use=False,
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: structlog.configure can fail for various reasons (import errors, configuration errors, etc.), and we must fall back to basic configuration to ensure logging still works
        # Fallback to basic structlog configuration if enhanced setup fails
        # This ensures logging still works even if enhanced features fail
        logger.warning(
            "Enhanced structlog configuration failed, using basic configuration",
            error=str(e),
            error_type=type(e).__name__,
        )
        structlog.configure(
            processors=[
                structlog.stdlib.add_log_level,
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.format_exc_info,
                structlog.dev.ConsoleRenderer(),  # type: ignore[attr-defined]  # Reason: structlog.dev module exists at runtime but type stubs may not include it, this is fallback configuration for error recovery
            ],
            wrapper_class=BoundLogger,
            logger_factory=LoggerFactory(),
        )

    # AI Agent: Now that structlog is configured, log the enhanced error handling setup
    # This confirms that the global error handler is capturing all errors from all modules
    if log_config and not log_config.get("disable_logging", False):
        env_log_dir = resolve_log_base(log_config.get("log_base", "logs")) / environment
        errors_log_path = env_log_dir / "errors.log"
        # NOTE: Using structlog.get_logger() directly is acceptable here since structlog
        # is already configured at this point, and this is infrastructure code.
        configured_logger = structlog.get_logger(__name__)
        configured_logger.info(
            "Enhanced error logging configured",
            errors_log_path=str(errors_log_path),
            captures_all_errors=True,
            global_error_handler_enabled=True,
        )


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
    config_signature = json.dumps(config, sort_keys=True, default=str)

    if _logging_state.initialized and not force_reconfigure:
        setup_logger = get_logger("server.structured_logging.setup")
        setup_logger.debug(
            "setup_enhanced_logging skipped; logging system already initialized",
            config_signature=_logging_state.signature,
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
    setup_logger = get_logger("server.structured_logging.enhanced")
    setup_logger.info(
        "Enhanced logging system initialized",
        environment=environment,
        log_level=log_level,
        log_base=logging_config.get("log_base", "logs"),
        mdc_enabled=True,
        security_sanitization=True,
        correlation_ids=True,
    )

    _logging_state.initialized = True
    _logging_state.signature = config_signature


def _configure_enhanced_uvicorn_logging() -> None:
    """Configure uvicorn to use our enhanced StructLog system."""
    config_logger = get_logger("uvicorn.enhanced")

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

    config_logger.info("Enhanced uvicorn logging configured")


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

    This is the public API for obtaining loggers. All application code
    should use this function rather than calling structlog.get_logger()
    directly.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Configured Structlog logger instance
    """
    # NOTE: This function is the public API wrapper around structlog.get_logger().
    # Using structlog.get_logger() here is correct as this IS the enhanced logging API.
    return structlog.get_logger(name)


def update_logging_with_player_service(player_service: Any) -> None:
    """
    Update existing logging handlers to use PlayerGuidFormatter.

    This function should be called after the player service becomes available
    to enhance existing log handlers with GUID-to-name conversion.

    Args:
        player_service: The player service for GUID-to-name conversion
    """
    from server.structured_logging.player_guid_formatter import PlayerGuidFormatter

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
        "inventory",
        "npc",
        "game",
        "api",
        "middleware",
        "monitoring",
        "time",
        "caching",
        "communications",
        "commands",
        "events",
        "infrastructure",
        "validators",
        "combat",
        "magic",
        "access",
        "security",
    ]

    for category in log_categories:
        category_logger = logging.getLogger(category)
        for handler in category_logger.handlers:
            if hasattr(handler, "setFormatter"):
                handler.setFormatter(enhanced_formatter)

    # Log that the enhancement has been applied
    structured_logger = cast(Any, get_logger("server.structured_logging"))
    structured_logger.info("Logging system enhanced with PlayerGuidFormatter", player_service_available=True)


def log_exception_once(
    bound_logger: BoundLogger,
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
        bound_logger: Structlog bound logger instance.
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

    log_method = getattr(bound_logger, level.lower(), bound_logger.error)
    log_method(message, **kwargs)

    if exc is not None and mark_logged:
        marker = getattr(exc, "mark_logged", None)
        if callable(marker):
            marker()  # pylint: disable=not-callable  # Reason: callable() check confirms marker is callable at runtime, pylint cannot detect this through getattr
        else:
            cast(Any, exc)._already_logged = True  # pylint: disable=protected-access  # Reason: Accessing protected member _already_logged is necessary for exception logging state tracking, this is part of the exception protocol
