"""
Channel-specific chat log methods for MythosMUD.

Mixin used by ChatLogger: local/global/system/whisper channel logs and cleanup.
"""

# pylint: disable=too-many-public-methods  # Reason: Channel logger groups all channel log/stats/cleanup APIs together.

from __future__ import annotations

import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from ..structured_logging.log_time_formats import LOG_DATE
from ..utils.room_utils import extract_subzone_from_room_id

logger = get_logger("communications.chat_logger")


class ChatChannelLoggerMixin:
    """Channel log paths, writers, stats, and cleanup. Requires ChatLogger attrs."""

    # Provided by ChatLogger when mixed in
    log_dir: Path

    def _queue_log_entry(self, log_type: str, file_path: Path, content: str) -> None:
        """Queue a log entry; implemented by ChatLogger."""
        raise NotImplementedError

    def _get_local_channel_log_file(self, subzone: str) -> Path:
        """
        Get the local channel log file path for a specific sub-zone.

        Args:
            subzone: Sub-zone identifier (e.g., "docks", "northside")

        Returns:
            Path to the local channel log file for the sub-zone
        """
        today = datetime.now(UTC).strftime(LOG_DATE)
        filename = f"chat_local_{subzone}_{today}.log"
        return self.log_dir / filename

    def log_local_channel_message(self, message_data: dict[str, Any]) -> None:
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
                room_id = message_data.get("room_id")
                if room_id:
                    subzone = extract_subzone_from_room_id(room_id) or "unknown"
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

            if "timestamp" not in entry:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("local_channel", log_file, content)

            logger.debug(
                "Local channel message queued",
                message_id=message_data.get("message_id"),
                subzone=subzone,
            )

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Local channel logging errors unpredictable, must handle gracefully
            logger.error("Failed to log local channel message", error=str(e), message_data=message_data)

    def log_global_channel_message(self, message_data: dict[str, Any]) -> None:
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

            if "timestamp" in message_data:
                entry["timestamp"] = message_data["timestamp"]
            else:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("global_channel", log_file, content)

            logger.debug("Global channel message queued", message_id=message_data.get("message_id"))

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Global channel logging errors unpredictable, must handle gracefully
            logger.error("Failed to log global channel message", error=str(e), message_data=message_data)

    def _get_global_channel_log_file(self) -> Path:
        """
        Get the global channel log file path.

        Returns:
            Path to the global channel log file
        """
        today = datetime.now(UTC).strftime(LOG_DATE)
        return self.log_dir / f"chat_global_{today}.log"

    def log_system_channel_message(self, message_data: dict[str, Any]) -> None:
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

            if "timestamp" in message_data:
                entry["timestamp"] = message_data["timestamp"]
            else:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("system_channel", log_file, content)

            logger.debug("System channel message queued", message_id=message_data.get("message_id"))

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: System channel logging errors unpredictable, must handle gracefully
            logger.error("Failed to log system channel message", error=str(e), message_data=message_data)

    def log_whisper_channel_message(self, message_data: dict[str, Any]) -> None:
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

            if "timestamp" in message_data:
                entry["timestamp"] = message_data["timestamp"]
            else:
                entry["timestamp"] = datetime.now(UTC).isoformat()

            content = json.dumps(entry, ensure_ascii=False)
            self._queue_log_entry("whisper_channel", log_file, content)

            logger.debug("Whisper channel message queued", message_id=message_data.get("message_id"))

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Whisper channel logging errors unpredictable, must handle gracefully
            logger.error("Failed to log whisper channel message", error=str(e), message_data=message_data)

    def _get_whisper_channel_log_file(self) -> Path:
        """
        Get the whisper channel log file path.

        Returns:
            Path to the whisper channel log file
        """
        today = datetime.now(UTC).strftime(LOG_DATE)
        return self.log_dir / f"chat_whisper_{today}.log"

    def _get_system_channel_log_file(self) -> Path:
        """
        Get the system channel log file path.

        Returns:
            Path to the system channel log file
        """
        today = datetime.now(UTC).strftime(LOG_DATE)
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
                    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Log file deletion errors unpredictable, must continue processing
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
        deleted_files = []
        current_time = datetime.now(UTC)
        cutoff_date = current_time - timedelta(days=days_to_keep)

        for log_file in self.log_dir.glob("chat_local_*.log"):
            try:
                file_mtime = datetime.fromtimestamp(log_file.stat().st_mtime, UTC)
                if file_mtime < cutoff_date:
                    log_file.unlink()
                    deleted_files.append(str(log_file))
                    logger.info("Deleted old local channel log file", file_path=str(log_file))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Log file deletion errors unpredictable, must handle gracefully
                logger.error("Failed to delete old local channel log file", file_path=str(log_file), error=str(e))

        return deleted_files
