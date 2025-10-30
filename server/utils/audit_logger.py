"""
Audit logging for security-sensitive commands.

Provides comprehensive audit trails for security-critical operations
like admin commands, permission changes, and player management.

AI: Audit logs are critical for incident response and compliance.
"""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..config import get_config
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class AuditLogger:
    """
    Audit logging for security-sensitive command execution.

    Creates structured JSON logs of security-critical operations for:
    - Forensic analysis after security incidents
    - Compliance requirements
    - Player behavior monitoring
    - Admin activity tracking

    AI: Audit logs should be immutable and stored separately from regular logs.
    """

    def __init__(self, log_directory: str | None = None):
        """
        Initialize audit logger.

        Args:
            log_directory: Optional directory to store audit logs.
                          If None, uses logs/{environment}/audit based on config.

        AI: Creates directory structure if it doesn't exist. Respects environment separation.
        """
        if log_directory is None:
            # Get environment from config
            config = get_config()
            environment = config.logging.environment
            log_base = config.logging.log_base

            # CRITICAL: Use absolute path from project root to prevent creating
            # logs in server/logs/ when code is imported from server/ directory
            # Find project root by looking for pyproject.toml
            current_file = Path(__file__).resolve()
            project_root = current_file.parent
            while project_root.parent != project_root:
                if (project_root / "pyproject.toml").exists():
                    break
                project_root = project_root.parent

            log_directory = str(project_root / log_base / environment)

        self.log_directory = Path(log_directory)
        self.log_directory.mkdir(parents=True, exist_ok=True)

        logger.info("AuditLogger initialized", log_directory=str(self.log_directory))

    def _get_log_file_path(self) -> Path:
        """
        Get the current audit log file path.

        Creates daily log files for easier management and rotation.

        Returns:
            Path to current audit log file

        AI: Daily rotation prevents individual files from growing too large.
        """
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        return self.log_directory / f"audit_{today}.jsonl"

    def log_command(
        self,
        player_name: str,
        command: str,
        success: bool,
        result: str | None = None,
        ip_address: str | None = None,
        session_id: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Log security-sensitive command execution.

        Creates a structured audit log entry with full context about the command execution.

        Args:
            player_name: Player who executed the command
            command: Command that was executed
            success: Whether command executed successfully
            result: Result/output of the command
            ip_address: IP address of the player (if available)
            session_id: Session identifier
            metadata: Additional context-specific data

        AI: Include as much context as possible for forensic analysis.
        """
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event_type": "command_execution",
            "player": player_name,
            "command": command,
            "success": success,
            "result": result[:500] if result and len(result) > 500 else result,  # Truncate long results
            "ip_address": ip_address,
            "session_id": session_id,
            "metadata": metadata or {},
        }

        self._write_entry(entry)

        logger.info(
            "Audit log entry created",
            player=player_name,
            command=command[:50],  # Truncate for regular log
            success=success,
        )

    def log_permission_change(
        self,
        admin_name: str,
        target_player: str,
        permission: str,
        action: str,  # 'grant' or 'revoke'
        success: bool,
        reason: str | None = None,
    ) -> None:
        """
        Log permission/role changes.

        Args:
            admin_name: Admin who made the change
            target_player: Player whose permissions changed
            permission: Permission that was granted/revoked
            action: 'grant' or 'revoke'
            success: Whether action succeeded
            reason: Optional reason for the change

        AI: Critical for tracking privilege escalation.
        """
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event_type": "permission_change",
            "admin": admin_name,
            "target_player": target_player,
            "permission": permission,
            "action": action,
            "success": success,
            "reason": reason,
        }

        self._write_entry(entry)

        logger.warning(
            "Permission change logged", admin=admin_name, target=target_player, permission=permission, action=action
        )

    def log_player_action(
        self,
        admin_name: str,
        target_player: str,
        action: str,  # 'ban', 'unban', 'kick', 'mute', 'unmute'
        duration: int | None = None,  # Duration in minutes if temporary
        reason: str | None = None,
        success: bool = True,
    ) -> None:
        """
        Log administrative actions against players.

        Args:
            admin_name: Admin who performed the action
            target_player: Player who was affected
            action: Type of action (ban, kick, etc.)
            duration: Duration in minutes if temporary action
            reason: Reason for the action
            success: Whether action succeeded

        AI: Essential for tracking moderation actions.
        """
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event_type": "player_action",
            "admin": admin_name,
            "target_player": target_player,
            "action": action,
            "duration_minutes": duration,
            "reason": reason,
            "success": success,
        }

        self._write_entry(entry)

        logger.warning("Player action logged", admin=admin_name, target=target_player, action=action)

    def log_security_event(
        self,
        event_type: str,
        player_name: str | None,
        description: str,
        severity: str = "medium",  # 'low', 'medium', 'high', 'critical'
        metadata: dict[str, Any] | None = None,
    ) -> None:
        """
        Log general security events.

        Used for rate limit violations, injection attempts, etc.

        Args:
            event_type: Type of security event
            player_name: Player involved (if applicable)
            description: Description of the event
            severity: Severity level
            metadata: Additional event data

        AI: Use for anomaly detection and security monitoring.
        """
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event_type": "security_event",
            "security_event_type": event_type,
            "player": player_name,
            "description": description,
            "severity": severity,
            "metadata": metadata or {},
        }

        self._write_entry(entry)

        # Log with appropriate severity level
        if severity == "critical":
            logger.critical("Security event logged", event_type=event_type, player=player_name, severity=severity)
        else:
            logger.warning("Security event logged", event_type=event_type, player=player_name, severity=severity)

    def log_alias_expansion(
        self,
        player_name: str,
        alias_name: str,
        expanded_command: str,
        cycle_detected: bool = False,
        expansion_depth: int = 1,
    ) -> None:
        """
        Log alias expansions for security monitoring.

        Tracks alias usage to detect abuse or malicious aliases.

        Args:
            player_name: Player using the alias
            alias_name: Name of the alias
            expanded_command: Command after expansion
            cycle_detected: Whether circular dependency was detected
            expansion_depth: Depth of alias expansion chain

        AI: Helps detect alias bombs and suspicious patterns.
        """
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "event_type": "alias_expansion",
            "player": player_name,
            "alias_name": alias_name,
            "expanded_command": expanded_command[:500],  # Truncate
            "cycle_detected": cycle_detected,
            "expansion_depth": expansion_depth,
        }

        self._write_entry(entry)

        if cycle_detected:
            logger.warning("Circular alias detected", player=player_name, alias=alias_name)

    def _write_entry(self, entry: dict[str, Any]) -> None:
        """
        Write audit log entry to file.

        Uses JSON Lines format (one JSON object per line) for easy parsing.

        Args:
            entry: Audit log entry to write

        AI: JSON Lines format allows streaming processing of large audit logs.
        """
        try:
            log_file = self._get_log_file_path()

            # Append to file (create if doesn't exist)
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        except Exception as e:
            logger.error("Failed to write audit log entry", error=str(e), entry_type=entry.get("event_type"))

    def get_recent_entries(
        self, hours: int = 24, event_type: str | None = None, player_name: str | None = None
    ) -> list[dict[str, Any]]:
        """
        Retrieve recent audit log entries.

        Useful for admin dashboards and incident investigation.

        Args:
            hours: Number of hours to look back
            event_type: Filter by event type
            player_name: Filter by player name

        Returns:
            List of matching audit log entries

        AI: For large deployments, consider using dedicated log aggregation tools.
        """
        from datetime import timedelta

        cutoff_time = datetime.now(UTC) - timedelta(hours=hours)
        entries = []

        # Get all log files in directory (sorted newest first)
        log_files = sorted(self.log_directory.glob("audit_*.jsonl"), reverse=True)

        for log_file in log_files:
            try:
                with open(log_file, encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue

                        try:
                            entry = json.loads(line)
                            entry_time = datetime.fromisoformat(entry["timestamp"])

                            # Check if within time range
                            if entry_time < cutoff_time:
                                continue

                            # Apply filters
                            if event_type and entry.get("event_type") != event_type:
                                continue

                            if player_name and entry.get("player") != player_name:
                                continue

                            entries.append(entry)

                        except (json.JSONDecodeError, KeyError, ValueError) as e:
                            logger.warning("Failed to parse audit log entry", file=str(log_file), error=str(e))
                            continue

            except Exception as e:
                logger.error("Failed to read audit log file", file=str(log_file), error=str(e))
                continue

        return entries

    def get_statistics(self, hours: int = 24) -> dict[str, Any]:
        """
        Get audit log statistics.

        Args:
            hours: Time window for statistics

        Returns:
            Dictionary containing audit statistics

        AI: Useful for security dashboards and monitoring.
        """
        entries = self.get_recent_entries(hours=hours)

        # AI Agent: Explicit type annotations help mypy understand nested dict structure
        event_types: dict[str, int] = {}
        security_events_by_severity: dict[str, int] = {}
        top_players: dict[str, int] = {}
        
        stats: dict[str, Any] = {
            "total_entries": len(entries),
            "time_window_hours": hours,
            "event_types": event_types,
            "security_events_by_severity": security_events_by_severity,
            "top_players": top_players,
            "failed_commands": 0,
        }

        for entry in entries:
            # Count event types
            event_type = entry.get("event_type", "unknown")
            event_types[event_type] = event_types.get(event_type, 0) + 1

            # Count security events by severity
            if event_type == "security_event":
                severity = entry.get("severity", "unknown")
                security_events_by_severity[severity] = security_events_by_severity.get(severity, 0) + 1

            # Count player activity
            player = entry.get("player")
            if player:
                top_players[player] = top_players.get(player, 0) + 1

            # Count failures
            if not entry.get("success", True):
                stats["failed_commands"] = stats["failed_commands"] + 1  # type: ignore[assignment,operator]

        # Sort top players
        stats["top_players"] = dict(sorted(top_players.items(), key=lambda x: x[1], reverse=True)[:10])

        return stats


# Global audit logger instance
# AI: Singleton pattern for consistent audit logging across the application
audit_logger = AuditLogger()
