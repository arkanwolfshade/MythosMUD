"""
Chat logging service for MythosMUD.

This module provides structured logging for chat messages, moderation events,
and system events, optimized for AI processing and log shipping.
"""

import json
import queue
import threading
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger("communications.chat_logger")


class ChatLogger:
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
            from ..logging.enhanced_logging_config import _resolve_log_base

            config = get_config()
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
        self._writer_thread = None
        self._shutdown_event = threading.Event()
        self._start_writer_thread()

        logger.info("ChatLogger initialized", log_dir=str(self.log_dir))

    def _ensure_log_directories(self):
        """Ensure log directory exists."""
        # Only ensure the main environment directory exists
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def _start_writer_thread(self):
        """Start the background writer thread for thread-safe file writing."""
        self._writer_thread = threading.Thread(target=self._writer_worker, daemon=True)
        self._writer_thread.start()
        logger.debug("ChatLogger writer thread started")

    def _writer_worker(self):
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

            except Exception as e:
                logger.error("Error in writer thread", error=str(e))

        logger.debug("ChatLogger writer thread stopped")

    def _process_log_entry(self, log_entry: dict[str, Any]):
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
            # AI Agent: After validation, we assert types for mypy type safety
            assert isinstance(file_path, str), "file_path must be str after validation"
            assert isinstance(content, str), "content must be str after validation"

            # Ensure directory exists
            Path(file_path).parent.mkdir(parents=True, exist_ok=True)

            # Write to file
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(content + "\n")

            logger.debug("Log entry written", type=log_type, file=str(file_path))

        except Exception as e:
            logger.error("Failed to process log entry", error=str(e), log_entry=log_entry)

    def shutdown(self):
        """Shutdown the logger and wait for writer thread to finish."""
        logger.info("Shutting down ChatLogger")
        self._shutdown_event.set()

        if self._writer_thread and self._writer_thread.is_alive():
            # Wait for queue to be processed
            self._log_queue.join()
            self._writer_thread.join(timeout=5.0)

        logger.info("ChatLogger shutdown complete")

    def wait_for_queue_processing(self, timeout: float = 5.0):
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
        except Exception as e:
            logger.error("Error waiting for queue processing", error=str(e))
            return False

    def _queue_log_entry(self, log_type: str, file_path: Path, content: str):
        """
        Queue a log entry for writing by the background thread.

        Args:
            log_type: Type of log entry for debugging
            file_path: Path to the log file
            content: JSON content to write
        """
        try:
            self._log_queue.put({"type": log_type, "file_path": str(file_path), "content": content})
        except Exception as e:
            logger.error("Failed to queue log entry", error=str(e), log_type=log_type)

    def _get_local_channel_log_file(self, subzone: str) -> Path:
        """
        Get the local channel log file path for a specific sub-zone.

        Args:
            subzone: Sub-zone identifier (e.g., "docks", "northside")

        Returns:
            Path to the local channel log file for the sub-zone
        """
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        filename = f"chat_local_{subzone}_{today}.log"
        return self.log_dir / filename

    def _get_current_log_file(self, log_type: str) -> Path:
        """
        Get the current log file path for the specified type.

        Args:
            log_type: Type of log ('chat', 'moderation', 'system')

        Returns:
            Path to current log file
        """
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        filename = f"chat_{log_type}_{today}.log"
        return self.log_dir / filename

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
                entry["timestamp"] = datetime.now(UTC).isoformat()

            # Queue the log entry for thread-safe writing
            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry(log_type, log_file, content)

        except Exception as e:
            logger.error("Failed to queue log entry", error=str(e), log_type=log_type, entry=entry)

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

    def log_player_unmuted(self, unmuter_id: str, target_id: str, target_name: str, mute_type: str):
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

    def log_local_channel_message(self, message_data: dict[str, Any]):
        """
        Log a local channel message to sub-zone specific file.

        Args:
            message_data: Local channel message data including:
                - message_id: Unique message identifier
                - channel: Should be "local"
                - sender_id: Player ID of sender
                - sender_name: Player name of sender
                - content: Message content
                - room_id: Room ID where message was sent
                - subzone: Sub-zone identifier
                - filtered: Whether message was filtered
                - moderation_notes: Any moderation notes
        """
        try:
            subzone = message_data.get("subzone")
            if not subzone:
                # Try to extract subzone from room_id if not provided
                from ..utils.room_utils import extract_subzone_from_room_id

                room_id = message_data.get("room_id")
                if room_id:
                    subzone = extract_subzone_from_room_id(room_id)
                    if not subzone:
                        subzone = "unknown"
                else:
                    subzone = "unknown"

            log_file = self._get_local_channel_log_file(subzone)

            # Ensure directory exists
            log_file.parent.mkdir(parents=True, exist_ok=True)

            entry = {
                "event_type": "local_channel_message",
                "message_id": message_data.get("message_id"),
                "channel": message_data.get("channel", "local"),
                "sender_id": message_data.get("sender_id"),
                "sender_name": message_data.get("sender_name"),
                "content": message_data.get("content"),
                "room_id": message_data.get("room_id"),
                "subzone": subzone,
                "filtered": message_data.get("filtered", False),
                "moderation_notes": message_data.get("moderation_notes"),
            }

            # Add timestamp if not present
            if "timestamp" not in entry:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            # Queue the log entry for thread-safe writing
            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("local_channel", log_file, content)

            logger.debug("Local channel message queued", message_id=message_data.get("message_id"), subzone=subzone)

        except Exception as e:
            logger.error("Failed to log local channel message", error=str(e), message_data=message_data)

    def log_global_channel_message(self, message_data: dict[str, Any]):
        """
        Log a global channel message to global.log file.

        Args:
            message_data: Global channel message data including:
                - message_id: Unique message identifier
                - channel: Should be "global"
                - sender_id: Player ID of sender
                - sender_name: Player name of sender
                - content: Message content
                - filtered: Whether message was filtered
                - moderation_notes: Any moderation notes
        """
        try:
            log_file = self._get_global_channel_log_file()

            # Ensure directory exists
            log_file.parent.mkdir(parents=True, exist_ok=True)

            entry = {
                "event_type": "global_channel_message",
                "message_id": message_data.get("message_id"),
                "channel": message_data.get("channel", "global"),
                "sender_id": message_data.get("sender_id"),
                "sender_name": message_data.get("sender_name"),
                "content": message_data.get("content"),
                "filtered": message_data.get("filtered", False),
                "moderation_notes": message_data.get("moderation_notes"),
            }

            # Use provided timestamp or current time
            if "timestamp" in message_data:
                entry["timestamp"] = message_data["timestamp"]
            else:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            # Queue the log entry for thread-safe writing
            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("global_channel", log_file, content)

            logger.debug("Global channel message queued", message_id=message_data.get("message_id"))

        except Exception as e:
            logger.error("Failed to log global channel message", error=str(e), message_data=message_data)

    def _get_global_channel_log_file(self) -> Path:
        """
        Get the global channel log file path.

        Returns:
            Path to the global channel log file
        """
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        return self.log_dir / f"chat_global_{today}.log"

    def log_system_channel_message(self, message_data: dict[str, Any]):
        """
        Log a system channel message to system.log file.

        Args:
            message_data: System channel message data including:
                - message_id: Unique message identifier
                - channel: Should be "system"
                - sender_id: Player ID of sender
                - sender_name: Player name of sender
                - content: Message content
                - filtered: Whether message was filtered
                - moderation_notes: Any moderation notes
        """
        try:
            log_file = self._get_system_channel_log_file()

            # Ensure directory exists
            log_file.parent.mkdir(parents=True, exist_ok=True)

            entry = {
                "event_type": "system_channel_message",
                "message_id": message_data.get("message_id"),
                "channel": message_data.get("channel", "system"),
                "sender_id": message_data.get("sender_id"),
                "sender_name": message_data.get("sender_name"),
                "content": message_data.get("content"),
                "filtered": message_data.get("filtered", False),
                "moderation_notes": message_data.get("moderation_notes"),
            }

            # Use provided timestamp or current time
            if "timestamp" in message_data:
                entry["timestamp"] = message_data["timestamp"]
            else:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            # Queue the log entry for thread-safe writing
            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("system_channel", log_file, content)

            logger.debug("System channel message queued", message_id=message_data.get("message_id"))

        except Exception as e:
            logger.error("Failed to log system channel message", error=str(e), message_data=message_data)

    def log_whisper_channel_message(self, message_data: dict[str, Any]):
        """
        Log a whisper channel message to whisper.log file.

        Args:
            message_data: Whisper channel message data including:
                - message_id: Unique message identifier
                - channel: Should be "whisper"
                - sender_id: Player ID of sender
                - sender_name: Player name of sender
                - target_id: Player ID of target
                - target_name: Player name of target
                - content: Message content
                - filtered: Whether message was filtered
                - moderation_notes: Any moderation notes
        """
        try:
            log_file = self._get_whisper_channel_log_file()

            # Ensure directory exists
            log_file.parent.mkdir(parents=True, exist_ok=True)

            entry = {
                "event_type": "whisper_channel_message",
                "message_id": message_data.get("message_id"),
                "channel": message_data.get("channel", "whisper"),
                "sender_id": message_data.get("sender_id"),
                "sender_name": message_data.get("sender_name"),
                "target_id": message_data.get("target_id"),
                "target_name": message_data.get("target_name"),
                "content": message_data.get("content"),
                "filtered": message_data.get("filtered", False),
                "moderation_notes": message_data.get("moderation_notes"),
            }

            # Use provided timestamp or current time
            if "timestamp" in message_data:
                entry["timestamp"] = message_data["timestamp"]
            else:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            # Queue the log entry for thread-safe writing
            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("whisper_channel", log_file, content)

            logger.debug("Whisper channel message queued", message_id=message_data.get("message_id"))

        except Exception as e:
            logger.error("Failed to log whisper channel message", error=str(e), message_data=message_data)

    def _get_whisper_channel_log_file(self) -> Path:
        """
        Get the whisper channel log file path.

        Returns:
            Path to the whisper channel log file
        """
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        return self.log_dir / f"chat_whisper_{today}.log"

    def _get_system_channel_log_file(self) -> Path:
        """
        Get the system channel log file path.

        Returns:
            Path to the system channel log file
        """
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        return self.log_dir / f"chat_system_{today}.log"

    def get_global_channel_log_files(self) -> list[str]:
        """
        Get all global channel log files.

        Returns:
            List of string paths to global channel log files
        """
        return [str(f) for f in self.log_dir.glob("chat_global_*.log")]

    def get_global_channel_log_stats(self) -> dict[str, Any]:
        """
        Get statistics for global channel log files.

        Returns:
            Dictionary with global channel log file statistics
        """
        stats: dict[str, dict[str, Any]] = {"global_channels": {}}
        log_files = self.get_global_channel_log_files()

        for log_file_path in log_files:
            log_file = Path(log_file_path)
            # Extract date from filename (chat_global_<date>.log)
            filename = log_file.name
            if filename.startswith("chat_global_") and filename.endswith(".log"):
                date = filename[12:-4]  # Remove "chat_global_" prefix and ".log" suffix

                if log_file.exists():
                    stats["global_channels"][date] = {
                        "file_path": str(log_file),
                        "date": date,
                        "file_size_bytes": log_file.stat().st_size,
                        "last_modified": datetime.fromtimestamp(log_file.stat().st_mtime).isoformat(),
                    }
                else:
                    stats["global_channels"][date] = {
                        "file_path": str(log_file),
                        "date": date,
                        "file_size_bytes": 0,
                        "last_modified": None,
                    }

        return stats

    def cleanup_old_global_channel_logs(self, days_to_keep: int = 30) -> list[str]:
        """
        Clean up old global channel log files.

        Args:
            days_to_keep: Number of days to keep log files

        Returns:
            List of deleted file paths
        """
        deleted_files = []
        cutoff_date = datetime.now(UTC) - timedelta(days=days_to_keep)
        log_files = self.get_global_channel_log_files()

        for log_file_path in log_files:
            log_file = Path(log_file_path)
            if log_file.exists():
                file_date = datetime.fromtimestamp(log_file.stat().st_mtime, UTC)
                if file_date < cutoff_date:
                    try:
                        log_file.unlink()
                        deleted_files.append(str(log_file))
                        logger.info("Deleted old global channel log file", file_path=str(log_file))
                    except Exception as e:
                        logger.error(
                            "Failed to delete old global channel log file", file_path=str(log_file), error=str(e)
                        )

        return deleted_files

    def get_local_channel_log_files(self) -> list[str]:
        """
        Get all local channel log files.

        Returns:
            List of string paths to local channel log files
        """
        return [str(f) for f in self.log_dir.glob("chat_local_*.log")]

    def get_local_channel_log_stats(self) -> dict[str, Any]:
        """
        Get statistics for local channel log files.

        Returns:
            Dictionary with local channel log file statistics
        """
        stats: dict[str, dict[str, Any]] = {"local_channels": {}}
        log_files = self.get_local_channel_log_files()

        for log_file_path in log_files:
            log_file = Path(log_file_path)
            # Extract subzone from filename (chat_local_<subzone>_<date>.log)
            filename = log_file.name
            if filename.startswith("chat_local_") and filename.endswith(".log"):
                parts = filename[11:-4].split("_")  # Remove "chat_local_" prefix and ".log" suffix
                if len(parts) >= 2:
                    subzone = parts[0]
                    date = "_".join(parts[1:])  # Rejoin date parts in case of hyphens

                    if log_file.exists():
                        stats["local_channels"][subzone] = {
                            "file_path": str(log_file),
                            "date": date,
                            "file_size_bytes": log_file.stat().st_size,
                            "last_modified": datetime.fromtimestamp(log_file.stat().st_mtime).isoformat(),
                        }
                    else:
                        stats["local_channels"][subzone] = {
                            "file_path": str(log_file),
                            "date": date,
                            "file_size_bytes": 0,
                            "last_modified": None,
                        }

        return stats

    def cleanup_old_local_channel_logs(self, days_to_keep: int = 30) -> list[str]:
        """
        Clean up old local channel log files.

        Args:
            days_to_keep: Number of days of logs to keep

        Returns:
            List of deleted file paths
        """
        from datetime import timedelta

        deleted_files = []
        current_time = datetime.now(UTC)
        cutoff_date = current_time - timedelta(days=days_to_keep)

        for log_file in self.log_dir.glob("chat_local_*.log"):
            try:
                # Check if file is older than cutoff date
                file_mtime = datetime.fromtimestamp(log_file.stat().st_mtime, UTC)
                if file_mtime < cutoff_date:
                    log_file.unlink()
                    deleted_files.append(str(log_file))
                    logger.info("Deleted old local channel log file", file_path=str(log_file))
            except Exception as e:
                logger.error("Failed to delete old local channel log file", file_path=str(log_file), error=str(e))

        return deleted_files


# Global chat logger instance
chat_logger = ChatLogger()
