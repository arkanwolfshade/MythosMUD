"""Logger-name categories and per-category file handlers for enhanced logging.

The category map is the routing table: which logger prefixes write to which
subsystem log file. Filters and handler construction live here so the setup
orchestrator stays a coordinator, not a second copy of the Necronomicon.
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import cast, override

from server.structured_logging.logging_utilities import (
    ensure_log_directory,
    load_player_guid_formatter_class,
)

DEFAULT_LOG_CATEGORIES: dict[str, list[str]] = {
    "server": ["server", "uvicorn", "server.app.factory"],
    "persistence": ["persistence", "server.persistence", "PersistenceLayer", "asyncpg", "database"],
    "authentication": ["auth"],
    "inventory": [
        "inventory",
        "server.services.inventory",
        "server.services.inventory_mutation_guard",
        "server.services.container",
        "server.services.container_service",
        "server.services.wearable_container_service",
        "server.services.equipment_service",
        "services.inventory",
        "services.inventory_mutation_guard",
        "services.container",
        "services.container_service",
        "services.wearable_container_service",
        "services.equipment_service",
    ],
    "npc": [
        "npc",
        "server.npc",
        "services.npc",
        "services.npc_service",
        "services.npc_instance_service",
        "services.npc_startup_service",
    ],
    "game": [
        "game",
        "server.game",
        "server.services.player",
        "server.services.room_sync",
        "server.world_loader",
        "server.game.movement_service",
        "server.game.room_service",
        "server.game.player_service",
        "server.game.mechanics",
        "services.player",
        "services.room_sync",
        "world_loader",
        "game.movement_service",
        "game.room_service",
        "game.player_service",
        "game.mechanics",
    ],
    "api": ["api", "server.api"],
    "middleware": ["middleware", "server.middleware"],
    "monitoring": ["monitoring", "server.monitoring", "server.api.monitoring", "performance", "metrics"],
    "time": [
        "time",
        "server.time",
        "services.game_tick",
        "services.game_tick_service",
        "services.schedule",
        "server.services.schedule_service",
    ],
    "caching": ["caching", "server.caching"],
    # WebSocket connect/disconnect/close-code and ADR-018 session-replacement events land here
    # (server.realtime.connection_establishment, .connection_disconnection,
    # .connection_session_management, .websocket_handler_message_loop) -- not in server.log, which
    # is a catch-all that doesn't include this prefix. Grepping server.log for "WebSocket
    # connected"/"disconnected" finds nothing; check communications.log (#297/#610 investigation).
    "communications": ["realtime", "server.realtime", "communications"],
    "commands": [
        "commands",
        "server.commands",
        "server.utils.command_parser",
        "server.utils.command_processor",
    ],
    "events": ["events", "EventBus"],
    "validators": ["validators", "server.validators"],
    "combat": [
        "services.combat_service",
        "services.combat_turn_processor",
        "services.combat_event_publisher",
        "services.npc_combat_integration_service",
        "services.player_combat_service",
        "validators.combat_validator",
        "logging.combat_audit",
    ],
    "magic": ["server.game.magic", "game.magic", "magic"],
    "party": [
        "server.game.party_service",
        "server.commands.party_commands",
        "server.realtime.channel_broadcasting_strategies",
    ],
    "quests": [
        "server.game.quest",
        "server.persistence.repositories.quest_definition_repository",
        "server.persistence.repositories.quest_instance_repository",
        "server.commands.quest_commands",
    ],
    "access": ["access", "uvicorn.access"],
    "security": [
        "security",
        "server.security_utils",
        "server.utils.audit_logger",
        "server.structured_logging.admin_actions_logger",
        "server.middleware.security_headers",
        "server.validators.optimized_security_validator",
        "audit",
    ],
}


def create_formatter(player_service: object | None) -> logging.Formatter:
    """Create formatter (with or without PlayerGuidFormatter)."""
    # Note: Using %(message)s only since structlog already includes all metadata (timestamp, logger name, level)
    # in the rendered message. Adding %(asctime)s - %(name)s - %(levelname)s would cause duplication.
    if player_service is not None:
        PlayerGuidFormatter = load_player_guid_formatter_class()
        return cast(
            logging.Formatter,
            PlayerGuidFormatter(
                player_service=player_service,
                fmt="%(message)s",
                datefmt=None,
            ),
        )
    return logging.Formatter(
        "%(message)s",
        datefmt=None,
    )


class LoggerNameFilter(logging.Filter):
    """
    Filter that only allows logs from loggers matching specified prefixes.

    This prevents cross-contamination where logs from one subsystem
    (e.g., server.npc.behavior_engine) end up in the wrong log file
    (e.g., communications.log instead of npc.log).
    """

    allowed_prefixes: list[str]

    def __init__(self, allowed_prefixes: list[str]) -> None:
        """
        Initialize filter with allowed logger name prefixes.

        Args:
            allowed_prefixes: List of logger name prefixes to allow
        """
        super().__init__()
        self.allowed_prefixes = allowed_prefixes

    @override
    def filter(self, record: logging.LogRecord) -> bool:
        """
        Check if the log record's logger name matches any allowed prefix.

        Args:
            record: Log record to check

        Returns:
            True if logger name matches an allowed prefix, False otherwise
        """
        logger_name = record.name
        # Check if logger name starts with any allowed prefix
        for prefix in self.allowed_prefixes:
            if logger_name == prefix or logger_name.startswith(f"{prefix}."):
                return True
        return False


def add_handler_to_loggers(
    handler: logging.Handler, prefixes: list[str], log_file: str, environment: str, log_level: str
) -> None:
    """
    Add handler to loggers that match the prefixes.

    Adds a filter to the handler to ensure it only processes logs from
    loggers matching the specified prefixes, preventing cross-contamination.
    """
    # Add filter to handler to ensure it only processes logs from intended loggers
    # This prevents logs from other subsystems (e.g., server.npc.behavior_engine)
    # from being written to the wrong log file (e.g., communications.log)
    # NOTE: When async logging is enabled, this filter is added to the QueueHandler,
    # but we also need to add it to the actual file handler (see _setup_category_handlers)
    handler.addFilter(LoggerNameFilter(prefixes))

    for prefix in prefixes:
        # Try both the prefix as-is and with "server." prefix for module-based loggers
        logger_names = [prefix]
        if not prefix.startswith("server."):
            logger_names.append(f"server.{prefix}")

        for logger_name in logger_names:
            target_logger = logging.getLogger(logger_name)
            target_logger.addHandler(handler)
            # Set DEBUG level for combat modules in local/debug environments
            if log_file == "combat" and (environment == "local" or log_level == "DEBUG"):
                target_logger.setLevel(logging.DEBUG)
            elif log_file == "npc" and environment == "e2e_test":
                # NPC behavior-engine/threading debug lines fire continuously (idle movement,
                # condition evaluation, per-tick "Executed NPC behavior") -- at DEBUG level in a
                # long-running e2e session this rotates connect/disconnect and other genuine
                # events out of npc.log's small e2e rotation window (10MB x 3) within minutes,
                # making connection-lifecycle bugs nearly undiagnosable from the logs (#297/#610
                # investigation cost most of a session to this). Opt back into full NPC debug
                # detail locally via LOGGING_LEVEL=DEBUG with LOGGING_ENVIRONMENT=local.
                target_logger.setLevel(logging.INFO)
            else:
                target_logger.setLevel(getattr(logging, str(log_level).upper(), logging.INFO))
            target_logger.propagate = True


def create_handler_for_category(
    log_path: Path,
    handler_class: type[RotatingFileHandler],
    max_bytes: int,
    backup_count: int,
    player_service: object | None,
) -> logging.Handler:
    """
    Create handler for a log category with graceful error handling.

    If handler creation fails, returns a NullHandler to prevent logging
    failures from crashing the application.
    """
    try:
        ensure_log_directory(log_path)
        try:
            handler: logging.Handler = handler_class(
                log_path,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
        except (FileNotFoundError, OSError):
            # If directory doesn't exist or was deleted, recreate it and try again
            ensure_log_directory(log_path)
            handler = handler_class(
                log_path,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding="utf-8",
            )
        handler.setLevel(logging.DEBUG)
        formatter = create_formatter(player_service)
        handler.setFormatter(formatter)
        return handler
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Defensive fallback for handler creation failures, must catch all exceptions to prevent logging setup from crashing the application
        # Graceful fallback: if handler creation fails, use NullHandler
        # This prevents logging setup failures from crashing the application
        # Log the error to stderr as a last resort
        print(
            f"Warning: Failed to create log handler for {log_path}: {type(e).__name__}: {e}",
            file=sys.stderr,
        )
        return logging.NullHandler()
