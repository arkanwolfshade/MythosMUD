"""
Chat logging service for MythosMUD.

This module provides structured logging for chat messages, moderation events,
and system events, optimized for AI processing and log shipping.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from ..logging_config import get_logger

logger = get_logger("communications.chat_logger")


class ChatLogger:
    """
    Structured logging service for chat system events.

    This logger creates JSON-structured log files optimized for AI processing
    and log shipping to external moderation systems.
    """

    def __init__(self, log_dir: str = "logs"):
        """
        Initialize chat logger.

        Args:
            log_dir: Directory for log files
        """
        self.log_dir = Path(log_dir)
        self._ensure_log_directories()

        # Create subdirectories for different log types
        self.chat_dir = self.log_dir / "chat"
        self.moderation_dir = self.log_dir / "moderation"
        self.system_dir = self.log_dir / "system"

        logger.info("ChatLogger initialized", log_dir=str(self.log_dir))

    def _ensure_log_directories(self):
        """Ensure log directories exist."""
        for subdir in ["chat", "moderation", "system"]:
            (self.log_dir / subdir).mkdir(parents=True, exist_ok=True)

    def _get_current_log_file(self, log_type: str) -> Path:
        """
        Get the current log file path for the specified type.

        Args:
            log_type: Type of log ('chat', 'moderation', 'system')

        Returns:
            Path to current log file
        """
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"{log_type}_{today}.log"

        if log_type == "chat":
            return self.chat_dir / filename
        elif log_type == "moderation":
            return self.moderation_dir / filename
        elif log_type == "system":
            return self.system_dir / filename
        else:
            raise ValueError(f"Unknown log type: {log_type}")

    def _write_log_entry(self, log_type: str, entry: dict[str, Any]):
        """
        Write a log entry to the appropriate log file.

        Args:
            log_type: Type of log ('chat', 'moderation', 'system')
            entry: Log entry data
        """
        try:
            log_file = self._get_current_log_file(log_type)

            # Add timestamp if not present
            if "timestamp" not in entry:
                entry["timestamp"] = datetime.utcnow().isoformat() + "Z"

            # Write JSON line to file
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        except Exception as e:
            logger.error("Failed to write log entry", error=str(e), log_type=log_type, entry=entry)

    def log_chat_message(self, message_data: dict[str, Any]):
        """
        Log a chat message for AI processing.

        Args:
            message_data: Chat message data including:
                - message_id: Unique message identifier
                - channel: Channel type (say, local, global, party, whisper)
                - sender_id: Player ID of sender
                - sender_name: Player name of sender
                - content: Message content
                - room_id: Room ID where message was sent
                - filtered: Whether message was filtered
                - moderation_notes: Any moderation notes
        """
        entry = {
            "event_type": "chat_message",
            "message_id": message_data.get("message_id"),
            "channel": message_data.get("channel"),
            "sender_id": message_data.get("sender_id"),
            "sender_name": message_data.get("sender_name"),
            "content": message_data.get("content"),
            "room_id": message_data.get("room_id"),
            "party_id": message_data.get("party_id"),
            "target_player_id": message_data.get("target_player_id"),
            "filtered": message_data.get("filtered", False),
            "moderation_notes": message_data.get("moderation_notes"),
        }

        self._write_log_entry("chat", entry)
        logger.debug("Chat message logged", message_id=message_data.get("message_id"))

    def log_moderation_event(self, event_type: str, event_data: dict[str, Any]):
        """
        Log a moderation event for AI training and processing.

        Args:
            event_type: Type of moderation event
            event_data: Event-specific data
        """
        entry = {"event_type": event_type, **event_data}

        self._write_log_entry("moderation", entry)
        logger.debug("Moderation event logged", event_type=event_type)

    def log_message_flagged(
        self,
        message_id: str,
        flag_reason: str,
        confidence: float = 0.0,
        ai_model: str = "content_filter_v1",
        action_taken: str = "none",
    ):
        """
        Log a flagged message for AI moderation.

        Args:
            message_id: ID of the flagged message
            flag_reason: Reason for flagging
            confidence: AI confidence score (0.0 to 1.0)
            ai_model: AI model that flagged the message
            action_taken: Action taken (none, muted, deleted, etc.)
        """
        entry = {
            "event_type": "message_flagged",
            "message_id": message_id,
            "flag_reason": flag_reason,
            "confidence": confidence,
            "ai_model": ai_model,
            "action_taken": action_taken,
            "moderator_id": "ai_system",
        }

        self._write_log_entry("moderation", entry)
        logger.info("Message flagged for moderation", message_id=message_id, flag_reason=flag_reason)

    def log_player_muted(
        self,
        muter_id: str,
        target_id: str,
        target_name: str,
        mute_type: str,
        duration_minutes: int | None = None,
        reason: str = "",
    ):
        """
        Log a player mute action.

        Args:
            muter_id: ID of player who applied mute
            target_id: ID of muted player
            target_name: Name of muted player
            mute_type: Type of mute (channel, player, global)
            duration_minutes: Duration in minutes (None for permanent)
            reason: Reason for mute
        """
        entry = {
            "event_type": "player_muted",
            "muter_id": muter_id,
            "target_id": target_id,
            "target_name": target_name,
            "mute_type": mute_type,
            "duration_minutes": duration_minutes,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

        self._write_log_entry("moderation", entry)
        logger.info("Player mute logged", target_id=target_id, mute_type=mute_type)

    def log_player_unmuted(self, unmuter_id: str, target_id: str, target_name: str, mute_type: str):
        """
        Log a player unmute action.

        Args:
            unmuter_id: ID of player who removed mute
            target_id: ID of unmuted player
            target_name: Name of unmuted player
            mute_type: Type of mute that was removed
        """
        entry = {
            "event_type": "player_unmuted",
            "unmuter_id": unmuter_id,
            "target_id": target_id,
            "target_name": target_name,
            "mute_type": mute_type,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

        self._write_log_entry("moderation", entry)
        logger.info("Player unmute logged", target_id=target_id, mute_type=mute_type)

    def log_system_event(self, event_type: str, event_data: dict[str, Any]):
        """
        Log a system event for AI context.

        Args:
            event_type: Type of system event
            event_data: Event-specific data
        """
        entry = {"event_type": event_type, **event_data}

        self._write_log_entry("system", entry)
        logger.debug("System event logged", event_type=event_type)

    def log_player_joined_room(self, player_id: str, player_name: str, room_id: str, room_name: str):
        """
        Log when a player joins a room.

        Args:
            player_id: Player ID
            player_name: Player name
            room_id: Room ID
            room_name: Room name
        """
        entry = {
            "event_type": "player_joined_room",
            "player_id": player_id,
            "player_name": player_name,
            "room_id": room_id,
            "room_name": room_name,
        }

        self._write_log_entry("system", entry)

    def log_player_left_room(self, player_id: str, player_name: str, room_id: str, room_name: str):
        """
        Log when a player leaves a room.

        Args:
            player_id: Player ID
            player_name: Player name
            room_id: Room ID
            room_name: Room name
        """
        entry = {
            "event_type": "player_left_room",
            "player_id": player_id,
            "player_name": player_name,
            "room_id": room_id,
            "room_name": room_name,
        }

        self._write_log_entry("system", entry)

    def log_rate_limit_violation(self, player_id: str, player_name: str, channel: str, message_count: int, limit: int):
        """
        Log a rate limit violation.

        Args:
            player_id: Player ID
            player_name: Player name
            channel: Channel where violation occurred
            message_count: Number of messages sent
            limit: Rate limit that was exceeded
        """
        entry = {
            "event_type": "rate_limit_violation",
            "player_id": player_id,
            "player_name": player_name,
            "channel": channel,
            "message_count": message_count,
            "limit": limit,
        }

        self._write_log_entry("moderation", entry)
        logger.warning("Rate limit violation logged", player_id=player_id, channel=channel)

    def get_log_file_paths(self) -> dict[str, Path]:
        """
        Get paths to current log files.

        Returns:
            Dictionary mapping log types to file paths
        """
        return {
            "chat": self._get_current_log_file("chat"),
            "moderation": self._get_current_log_file("moderation"),
            "system": self._get_current_log_file("system"),
        }

    def get_log_stats(self) -> dict[str, Any]:
        """
        Get statistics about log files.

        Returns:
            Dictionary with log file statistics
        """
        stats = {}

        for log_type in ["chat", "moderation", "system"]:
            log_file = self._get_current_log_file(log_type)
            if log_file.exists():
                stats[log_type] = {
                    "file_path": str(log_file),
                    "file_size_bytes": log_file.stat().st_size,
                    "last_modified": datetime.fromtimestamp(log_file.stat().st_mtime).isoformat(),
                }
            else:
                stats[log_type] = {"file_path": str(log_file), "file_size_bytes": 0, "last_modified": None}

        return stats


# Global chat logger instance
chat_logger = ChatLogger()
