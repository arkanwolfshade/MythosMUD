"""
Dead Letter Queue for failed NATS messages.

Stores messages that fail after all retry attempts for later
analysis, manual processing, or replay.

AI: DLQ is critical for preventing message loss and enabling forensic analysis.
"""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..logging_config import get_logger

logger = get_logger(__name__)


class DeadLetterQueue:
    """
    Store messages that fail after all retries.

    Implements file-based storage for failed messages with metadata.
    Each failed message is stored as a separate JSON file for easy
    inspection and potential replay.

    AI: File-based DLQ is simple, durable, and doesn't require additional infrastructure.
    """

    def __init__(self, storage_path: str = "logs/dlq"):
        """
        Initialize dead letter queue.

        Args:
            storage_path: Directory to store DLQ files

        AI: Creates directory structure if it doesn't exist.
        """
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)

        logger.info("DeadLetterQueue initialized", storage_path=str(self.storage_path))

    async def enqueue(
        self, message_data: dict[str, Any], error: Exception, retry_count: int, metadata: dict[str, Any] | None = None
    ) -> str:
        """
        Add failed message to dead letter queue.

        Stores message with full context including error details,
        retry count, and timestamp for later analysis.

        Args:
            message_data: The message that failed
            error: The exception that caused failure
            retry_count: Number of retry attempts made
            metadata: Additional context about the failure

        Returns:
            Filepath of the stored DLQ entry

        AI: Include all context needed for debugging and potential replay.
        """
        dlq_entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "message": message_data,
            "error": str(error),
            "error_type": type(error).__name__,
            "retry_count": retry_count,
            "metadata": metadata or {},
        }

        # Create unique filename with timestamp and microseconds
        filename = f"dlq_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S_%f')}.json"
        filepath = self.storage_path / filename

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(dlq_entry, f, indent=2, ensure_ascii=False)

            logger.error(
                "Message added to dead letter queue",
                filepath=str(filepath),
                message_id=message_data.get("message_id"),
                error=str(error),
                retry_count=retry_count,
            )

            return str(filepath)

        except Exception as write_error:
            logger.critical(
                "Failed to write to DLQ - message may be lost!",
                error=str(write_error),
                original_error=str(error),
                message_id=message_data.get("message_id"),
            )
            raise

    async def get_pending_count(self) -> int:
        """
        Get count of messages in DLQ.

        Returns:
            Number of messages currently in DLQ

        AI: Useful for monitoring and alerting on DLQ backlog.
        """
        try:
            count = len(list(self.storage_path.glob("dlq_*.json")))
            return count
        except Exception as e:
            logger.error("Error counting DLQ entries", error=str(e))
            return 0

    async def get_messages(self, limit: int | None = None) -> list[dict[str, Any]]:
        """
        Retrieve messages from DLQ.

        Args:
            limit: Maximum number of messages to retrieve (None for all)

        Returns:
            List of DLQ entries with message data and metadata

        AI: For admin dashboards and manual message replay.
        """
        messages = []
        dlq_files = sorted(self.storage_path.glob("dlq_*.json"))

        if limit:
            dlq_files = dlq_files[:limit]

        for filepath in dlq_files:
            try:
                with open(filepath, encoding="utf-8") as f:
                    entry = json.load(f)
                    entry["dlq_file"] = str(filepath)
                    messages.append(entry)
            except Exception as e:
                logger.error("Error reading DLQ file", filepath=str(filepath), error=str(e))
                continue

        return messages

    async def remove_message(self, filepath: str) -> bool:
        """
        Remove a message from DLQ (after manual processing/replay).

        Args:
            filepath: Path to DLQ file to remove

        Returns:
            True if removed successfully, False otherwise

        AI: Use after successfully replaying or manually resolving a message.
        """
        try:
            Path(filepath).unlink()
            logger.info("Message removed from DLQ", filepath=filepath)
            return True
        except Exception as e:
            logger.error("Failed to remove DLQ message", filepath=filepath, error=str(e))
            return False

    async def get_statistics(self) -> dict[str, Any]:
        """
        Get DLQ statistics for monitoring.

        Returns:
            Dictionary with DLQ metrics

        AI: For monitoring dashboards and alerting systems.
        """
        try:
            dlq_files = list(self.storage_path.glob("dlq_*.json"))
            total_count = len(dlq_files)

            # Get error type distribution
            error_types: dict[str, int] = {}
            for filepath in dlq_files:
                try:
                    with open(filepath, encoding="utf-8") as f:
                        entry = json.load(f)
                        error_type = entry.get("error_type", "unknown")
                        error_types[error_type] = error_types.get(error_type, 0) + 1
                except Exception:
                    continue

            return {
                "total_messages": total_count,
                "error_types": error_types,
                "storage_path": str(self.storage_path),
            }

        except Exception as e:
            logger.error("Error getting DLQ statistics", error=str(e))
            return {"total_messages": 0, "error_types": {}, "storage_path": str(self.storage_path)}

    async def cleanup_old_messages(self, days_to_keep: int = 7) -> int:
        """
        Clean up old DLQ messages.

        Removes DLQ entries older than specified days to prevent
        unbounded storage growth.

        Args:
            days_to_keep: Number of days to retain DLQ entries

        Returns:
            Number of messages cleaned up

        AI: Call periodically (e.g., daily) to prevent disk space issues.
        """
        from datetime import timedelta

        try:
            cutoff_time = datetime.now(UTC) - timedelta(days=days_to_keep)
            removed_count = 0

            for filepath in self.storage_path.glob("dlq_*.json"):
                try:
                    # Extract timestamp from filename
                    file_stat = filepath.stat()
                    file_time = datetime.fromtimestamp(file_stat.st_mtime, UTC)

                    if file_time < cutoff_time:
                        filepath.unlink()
                        removed_count += 1

                except Exception as e:
                    logger.warning("Error removing old DLQ file", filepath=str(filepath), error=str(e))
                    continue

            if removed_count > 0:
                logger.info("Cleaned up old DLQ messages", removed_count=removed_count, days_to_keep=days_to_keep)

            return removed_count

        except Exception as e:
            logger.error("Error during DLQ cleanup", error=str(e))
            return 0
