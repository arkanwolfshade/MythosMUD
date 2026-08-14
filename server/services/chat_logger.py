"""
Chat logging service for MythosMUD.

This module provides structured logging for chat messages, moderation events,
and system events, optimized for AI processing and log shipping.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-public-methods  # Reason: Chat logging requires many parameters for context and logging operations. Chat logger legitimately requires many public methods for comprehensive logging operations.

import json
import queue
import threading
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from ..structured_logging.log_time_formats import LOG_DATE
from .chat_channel_logger import ChatChannelLoggerMixin

logger = get_logger("communications.chat_logger")


class ChatLogger(ChatChannelLoggerMixin):
    """
    Structured logging service for chat system events.

    This logger creates JSON-structured log files optimized for AI processing
    and log shipping to external moderation systems.
    """

    def __init__(self, log_dir: str | None = None) -> None:
        """
        Initialize chat logger.

        Args:
            log_dir: Directory for log files (if None, uses environment-based path)
        """
        if log_dir is None:
            # Use environment-based configuration like the rest of the system
            from ..config import get_config
            from ..structured_logging.enhanced_logging_config import _resolve_log_base

            config = get_config()
            # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible after validation, pylint cannot detect them statically
            log_base = config.logging.log_base
            environment = config.logging.environment

            resolved_log_base = _resolve_log_base(log_base)
            self.log_dir = resolved_log_base / environment
        else:
            self.log_dir = Path(log_dir)

        # No longer create subdirectories - write all files to environment directory
        # with prefixed names to distinguish log types

        # Thread-safe logging queue and writer thread
        self._log_queue: queue.Queue[dict[str, Any]] = queue.Queue()
        self._writer_thread: threading.Thread | None = None
        self._shutdown_event = threading.Event()
        self._start_writer_thread()

        logger.info("ChatLogger initialized", log_dir=str(self.log_dir))

    def _ensure_log_directories(self) -> None:
        """Ensure log directory exists."""
        # Only ensure the main environment directory exists
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def _start_writer_thread(self) -> None:
        """Start the background writer thread for thread-safe file writing."""
        self._writer_thread = threading.Thread(target=self._writer_worker, daemon=True)
        self._writer_thread.start()
        logger.debug("ChatLogger writer thread started")

    def _writer_worker(self) -> None:
        """Background worker thread that handles all file writing operations."""
        while not self._shutdown_event.is_set():
            try:
                # Wait for log entries with a timeout to allow checking shutdown
                try:
                    log_entry = self._log_queue.get(timeout=1.0)
                except queue.Empty:
                    continue

                # Process the log entry
                self._process_log_entry(log_entry)
                self._log_queue.task_done()

            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Writer thread errors unpredictable, must continue loop
                logger.error("Error in writer thread", error=str(e))

        logger.debug("ChatLogger writer thread stopped")

    def _process_log_entry(self, log_entry: dict[str, Any]) -> None:
        """
        Process a log entry from the queue and write it to the appropriate file.

        Args:
            log_entry: Dictionary containing 'type', 'file_path', and 'content'
        """
        try:
            log_type = log_entry.get("type")
            file_path = log_entry.get("file_path")
            content = log_entry.get("content")

            if not all([log_type, file_path, content]):
                logger.error("Invalid log entry", log_entry=log_entry)
                return

            # Type narrowing for mypy
            # AI Agent: After validation, we validate types for mypy type safety
            if not isinstance(file_path, str):
                raise TypeError("file_path must be str after validation")
            if not isinstance(content, str):
                raise TypeError("content must be str after validation")

            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)

            # Write to file
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(content + "\n")

            logger.debug("Log entry written", type=log_type, file=str(file_path))

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Log processing errors unpredictable, must handle gracefully
            logger.error("Failed to process log entry", error=str(e), log_entry=log_entry)

    def shutdown(self) -> None:
        """Shutdown the logger and wait for writer thread to finish."""
        logger.info("Shutting down ChatLogger")
        self._shutdown_event.set()

        if self._writer_thread and self._writer_thread.is_alive():
            # Wait for queue to be processed
            self._log_queue.join()
            self._writer_thread.join(timeout=5.0)

        logger.info("ChatLogger shutdown complete")

    def wait_for_queue_processing(self, _timeout: float = 5.0) -> bool:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future timeout-based queue processing
        """
        Wait for all queued log entries to be processed.

        Args:
            timeout: Maximum time to wait in seconds

        Returns:
            True if queue was processed, False if timeout occurred
        """
        try:
            self._log_queue.join()
            return True
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Queue processing wait errors unpredictable, must return False
            logger.error("Error waiting for queue processing", error=str(e))
            return False

    def _queue_log_entry(self, log_type: str, file_path: Path, content: str) -> None:
        """
        Queue a log entry for writing by the background thread.

        Args:
            log_type: Type of log entry for debugging
            file_path: Path to the log file
            content: JSON content to write
        """
        try:
            self._log_queue.put({"type": log_type, "file_path": str(file_path), "content": content})
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Log queue put errors unpredictable, must handle gracefully
            logger.error("Failed to queue log entry", error=str(e), log_type=log_type)

    def _get_current_log_file(self, log_type: str) -> Path:
        """
        Get the current log file path for the specified type.

        Args:
            log_type: Type of log ('chat', 'moderation', 'system')

        Returns:
            Path to current log file
        """
        today = datetime.now(UTC).strftime(LOG_DATE)
        filename = f"chat_{log_type}_{today}.log"
        return self.log_dir / filename

    def _write_log_entry(self, log_type: str, entry: dict[str, Any]) -> None:
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
                entry["timestamp"] = datetime.now(UTC).isoformat()

            # Queue the log entry for thread-safe writing
            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry(log_type, log_file, content)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Log entry queueing errors unpredictable, must handle gracefully
            logger.error("Failed to queue log entry", error=str(e), log_type=log_type, entry=entry)

    def log_chat_message(self, message_data: dict[str, Any]) -> None:
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

    def log_moderation_event(self, event_type: str, event_data: dict[str, Any]) -> None:
        """
        Log a moderation event for AI training and processing.

        Args:
            event_type: Type of moderation event
            event_data: Event-specific data
        """
        entry = {"event_type": event_type, **event_data}

        self._write_log_entry("moderation", entry)
        logger.debug("Moderation event logged", event_type=event_type)

    def log_message_flagged(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Chat logging requires many parameters for complete logging context  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Chat logging requires many parameters for complete logging context
        self,
        message_id: str,
        flag_reason: str,
        confidence: float = 0.0,
        ai_model: str = "content_filter_v1",
        action_taken: str = "none",
    ) -> None:
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
    ) -> None:
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
        muter_id_str = str(muter_id)
        target_id_str = str(target_id)

        entry = {
            "event_type": "player_muted",
            "muter_id": muter_id_str,
            "target_id": target_id_str,
            "target_name": target_name,
            "mute_type": mute_type,
            "duration_minutes": duration_minutes,
            "reason": reason,
            "timestamp": datetime.now(UTC).isoformat(),
        }

        self._write_log_entry("moderation", entry)
        logger.info("Player mute logged", target_id=target_id_str, mute_type=mute_type)

    def log_player_unmuted(self, unmuter_id: str, target_id: str, target_name: str, mute_type: str) -> None:
        """
        Log a player unmute action.

        Args:
            unmuter_id: ID of player who removed mute
            target_id: ID of unmuted player
            target_name: Name of unmuted player
            mute_type: Type of mute that was removed
        """
        unmuter_id_str = str(unmuter_id)
        target_id_str = str(target_id)

        entry = {
            "event_type": "player_unmuted",
            "unmuter_id": unmuter_id_str,
            "target_id": target_id_str,
            "target_name": target_name,
            "mute_type": mute_type,
            "timestamp": datetime.now(UTC).isoformat(),
        }

        self._write_log_entry("moderation", entry)
        logger.info("Player unmute logged", target_id=target_id_str, mute_type=mute_type)

    def log_system_event(self, event_type: str, event_data: dict[str, Any]) -> None:
        """
        Log a system event for AI context.

        Args:
            event_type: Type of system event
            event_data: Event-specific data
        """
        entry = {"event_type": event_type, **event_data}

        self._write_log_entry("system", entry)
        logger.debug("System event logged", event_type=event_type)

    def log_player_joined_room(self, player_id: str, player_name: str, room_id: str, room_name: str) -> None:
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

    def log_player_left_room(self, player_id: str, player_name: str, room_id: str, room_name: str) -> None:
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

    def log_rate_limit_violation(
        self, player_id: str, player_name: str, channel: str, message_count: int, limit: int
    ) -> None:  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Chat logging requires many parameters for complete logging context
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
        stats: dict[str, dict[str, Any]] = {}

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
