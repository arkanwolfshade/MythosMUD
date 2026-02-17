"""
Admin actions logger for MythosMUD.

This module provides comprehensive logging for admin actions including
teleport commands, with structured logging for audit purposes.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Admin logging requires many parameters for complete audit context

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class AdminActionsLogger:
    """
    Logger for admin actions with structured logging and file persistence.

    Provides comprehensive audit logging for admin teleport and other
    administrative actions with JSON-structured log entries.
    """

    def __init__(self, log_directory: str | None = None) -> None:
        """
        Initialize the admin actions logger.

        Args:
            log_directory: Directory to store admin action logs (if None, uses environment-based path)
        """
        if log_directory is None:
            # Use environment-based configuration like the rest of the system
            from server.config import get_config
            from server.structured_logging.enhanced_logging_config import _resolve_log_base

            config = get_config()
            # pylint: disable=no-member  # Pydantic FieldInfo dynamic attributes
            log_base = config.logging.log_base
            environment = config.logging.environment

            resolved_log_base = _resolve_log_base(log_base)
            self.log_directory = resolved_log_base / environment
        else:
            self.log_directory = Path(log_directory)

        self.log_directory.mkdir(parents=True, exist_ok=True)

        # Create today's log file
        self.current_log_file = self._get_log_file_path()
        logger.info("Admin actions logger initialized", log_file=str(self.current_log_file))

    def _get_log_file_path(self) -> Path:
        """Get the log file path for the current date."""
        today = datetime.now().strftime("%Y-%m-%d")
        return self.log_directory / f"admin_actions_{today}.log"

    def _ensure_log_file_exists(self) -> None:
        """Ensure the current log file exists and create if necessary."""
        if not self.current_log_file.exists():
            # Create the file with a header
            with open(self.current_log_file, "w", encoding="utf-8") as f:
                f.write("# MythosMUD Admin Actions Log\n")
                f.write(f"# Created: {datetime.now().isoformat()}\n")
                f.write("# Format: JSON lines\n\n")

    def log_teleport_action(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Teleport logging requires many parameters for complete audit context
        self,
        admin_name: str,
        target_player: str,
        action_type: str,
        from_room: str,
        to_room: str,
        success: bool,
        error_message: str | None = None,
        additional_data: dict[str, Any] | None = None,
    ) -> None:
        """
        Log a teleport action with comprehensive details.

        Args:
            admin_name: Name of the admin performing the action
            target_player: Name of the target player
            action_type: Type of teleport ('teleport' or 'goto')
            from_room: Room ID the player is leaving
            to_room: Room ID the player is arriving at
            success: Whether the action was successful
            error_message: Error message if the action failed
            additional_data: Additional data to include in the log
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": "teleport",
            "teleport_type": action_type,
            "admin_name": admin_name,
            "target_player": target_player,
            "from_room": from_room,
            "to_room": to_room,
            "success": success,
            "error_message": error_message,
            "additional_data": additional_data or {},
        }

        self._log_entry(log_entry)

        # Also log to the main logger for immediate visibility
        if success:
            logger.info(
                "Admin teleport action logged",
                admin_name=admin_name,
                action_type=action_type,
                target_player=target_player,
                from_room=from_room,
                to_room=to_room,
            )
        else:
            logger.warning(
                "Admin teleport action failed",
                admin_name=admin_name,
                action_type=action_type,
                target_player=target_player,
                error_message=error_message,
            )

    def log_admin_command(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Admin command logging requires many parameters for complete audit context
        self,
        admin_name: str,
        command: str,
        target_player: str | None = None,
        success: bool = True,
        error_message: str | None = None,
        additional_data: dict[str, Any] | None = None,
    ) -> None:
        """
        Log a general admin command action.

        Args:
            admin_name: Name of the admin performing the action
            command: Command that was executed
            target_player: Target player if applicable
            success: Whether the action was successful
            error_message: Error message if the action failed
            additional_data: Additional data to include in the log
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": "admin_command",
            "admin_name": admin_name,
            "command": command,
            "target_player": target_player,
            "success": success,
            "error_message": error_message,
            "additional_data": additional_data or {},
        }

        self._log_entry(log_entry)

        # Also log to the main logger for immediate visibility
        if success:
            logger.info("Admin command logged", admin_name=admin_name, command=command)
        else:
            logger.warning("Admin command failed", admin_name=admin_name, command=command, error=error_message)

    def log_permission_check(
        self,
        player_name: str,
        action: str,
        has_permission: bool,
        additional_data: dict[str, Any] | None = None,
    ) -> None:
        """
        Log permission check attempts.

        Args:
            player_name: Name of the player attempting the action
            action: Action being attempted
            has_permission: Whether the player has permission
            additional_data: Additional data to include in the log
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action_type": "permission_check",
            "player_name": player_name,
            "action": action,
            "has_permission": has_permission,
            "additional_data": additional_data or {},
        }

        self._log_entry(log_entry)

        if not has_permission:
            logger.warning(
                "Permission denied", player_name=player_name, action=action, reason="insufficient_admin_privileges"
            )

    def _log_entry(self, log_entry: dict[str, Any]) -> None:
        """
        Write a log entry to the current log file.

        Args:
            log_entry: Dictionary containing the log entry data
        """
        try:
            self._ensure_log_file_exists()

            # Check if we need to rotate to a new day's log file
            if self.current_log_file != self._get_log_file_path():
                self.current_log_file = self._get_log_file_path()
                logger.info("Rotated to new admin actions log file", log_file=str(self.current_log_file))

            # Write the log entry as a JSON line
            with open(self.current_log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry) + "\n")

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: File write errors unpredictable, must log but not fail
            logger.error("Failed to write admin action log entry", error=str(e), operation="log_entry_write")

    def get_recent_actions(
        self, hours: int = 24, action_type: str | None = None, admin_name: str | None = None
    ) -> list[dict[str, Any]]:
        """
        Retrieve recent admin actions from the log files.

        Args:
            hours: Number of hours to look back
            action_type: Filter by action type
            admin_name: Filter by admin name

        Returns:
            List of log entries matching the criteria
        """
        try:
            from datetime import timedelta

            cutoff_time = datetime.now() - timedelta(hours=hours)
            actions = []

            # Get all log files in the directory
            log_files = sorted(self.log_directory.glob("admin_actions_*.log"), reverse=True)

            for log_file in log_files:
                if not log_file.exists():
                    continue

                with open(log_file, encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"):
                            continue

                        try:
                            entry = json.loads(line)
                            entry_time = datetime.fromisoformat(entry["timestamp"])

                            # Check if entry is within time range
                            if entry_time < cutoff_time:
                                continue

                            # Apply filters
                            if action_type and entry.get("action_type") != action_type:
                                continue

                            if admin_name and entry.get("admin_name") != admin_name:
                                continue

                            actions.append(entry)

                        except (json.JSONDecodeError, KeyError, ValueError) as e:
                            logger.warning(
                                "Failed to parse log entry",
                                line_preview=line[:100],
                                error=str(e),
                                operation="log_parsing",
                            )
                            continue

            return actions

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: File read errors unpredictable, must return empty list
            logger.error("Failed to retrieve recent admin actions", error=str(e), operation="admin_actions_retrieval")
            return []

    def get_teleport_statistics(self, hours: int = 24) -> dict[str, Any]:
        """
        Get statistics about teleport actions.

        Args:
            hours: Number of hours to analyze

        Returns:
            Dictionary containing teleport statistics
        """
        actions = self.get_recent_actions(hours=hours, action_type="teleport")

        teleport_types: dict[str, int] = {}
        admin_activity: dict[str, int] = {}
        target_players: dict[str, int] = {}

        stats = {
            "total_teleports": len(actions),
            "successful_teleports": len([a for a in actions if a.get("success", False)]),
            "failed_teleports": len([a for a in actions if not a.get("success", False)]),
            "teleport_types": teleport_types,
            "admin_activity": admin_activity,
            "target_players": target_players,
        }

        for action in actions:
            # Count teleport types
            teleport_type = action.get("teleport_type", "unknown")
            teleport_types[teleport_type] = teleport_types.get(teleport_type, 0) + 1

            # Count admin activity
            admin_name = action.get("admin_name", "unknown")
            admin_activity[admin_name] = admin_activity.get(admin_name, 0) + 1

            # Count target players
            target_player = action.get("target_player", "unknown")
            target_players[target_player] = target_players.get(target_player, 0) + 1

        return stats


# Global instance for easy access
_admin_actions_logger: AdminActionsLogger | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_admin_actions_logger() -> AdminActionsLogger:
    """
    Get the global admin actions logger instance.

    Returns:
        AdminActionsLogger instance
    """
    global _admin_actions_logger  # pylint: disable=global-statement  # Reason: Required for singleton pattern
    if _admin_actions_logger is None:
        _admin_actions_logger = AdminActionsLogger()
    return _admin_actions_logger
