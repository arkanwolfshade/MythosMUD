"""
Dead Letter Queue for failed NATS messages.

Stores messages that fail after all retry attempts for later
analysis, manual processing, or replay.

AI: DLQ is critical for preventing message loss and enabling forensic analysis.
"""

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..config import get_config
from ..logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class DeadLetterMessage:
    """
    Message stored in dead letter queue.

    Contains message data and failure context for forensic analysis.

    AI: Includes all metadata needed to understand and potentially replay the message.
    """

    subject: str
    data: dict[str, Any]
    error: str
    timestamp: datetime
    retry_count: int
    original_headers: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert message to dictionary for JSON serialization."""
        return {
            "subject": self.subject,
            "data": self.data,
            "error": self.error,
            "timestamp": self.timestamp.isoformat(),
            "retry_count": self.retry_count,
            "original_headers": self.original_headers or {},
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DeadLetterMessage":
        """Reconstruct message from dictionary."""
        timestamp_str = data["timestamp"]
        # Handle both string and datetime inputs
        if isinstance(timestamp_str, str):
            timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        else:
            timestamp = timestamp_str

        return cls(
            subject=data["subject"],
            data=data["data"],
            error=data["error"],
            timestamp=timestamp,
            retry_count=data["retry_count"],
            original_headers=data.get("original_headers"),
        )


class DeadLetterQueue:
    """
    Store messages that fail after all retries.

    Implements file-based storage for failed messages with metadata.
    Each failed message is stored as a separate JSON file for easy
    inspection and potential replay.

    AI: File-based DLQ is simple, durable, and doesn't require additional infrastructure.
    """

    def __init__(self, storage_dir: str | None = None):
        """
        Initialize dead letter queue.

        Args:
            storage_dir: Optional directory to store DLQ files.
                        If None, uses logs/{environment}/dlq based on logging config.

        AI: Creates directory structure if it doesn't exist. Respects environment separation.
        """
        if storage_dir is None:
            # Get environment from config
            config = get_config()
            environment = config.logging.environment
            log_base = config.logging.log_base

            # CRITICAL: Use absolute path from project root to prevent creating
            # dlq in server/logs/ when code is imported from server/ directory
            # Find project root by looking for pyproject.toml
            current_file = Path(__file__).resolve()
            project_root = current_file.parent
            while project_root.parent != project_root:
                if (project_root / "pyproject.toml").exists():
                    break
                project_root = project_root.parent

            storage_dir = str(project_root / log_base / environment / "dlq")

        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

        logger.info("DeadLetterQueue initialized", storage_dir=str(self.storage_dir))

    def enqueue(self, message: DeadLetterMessage) -> Path:
        """
        Add failed message to dead letter queue.

        Args:
            message: Dead letter message to enqueue

        Returns:
            Path to stored DLQ file

        AI: Synchronous version for compatibility with tests.
        """
        # Create unique filename
        filename = f"dlq_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S_%f')}.json"
        filepath = self.storage_dir / filename

        # Write message to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(message.to_dict(), f, indent=2, ensure_ascii=False)

        logger.error(
            "Message added to dead letter queue",
            filepath=str(filepath),
            subject=message.subject,
            error=message.error,
            retry_count=message.retry_count,
        )

        return filepath

    def dequeue(self) -> dict[str, Any] | None:
        """
        Retrieve and remove oldest message from DLQ.

        Returns:
            Message data or None if queue is empty

        AI: FIFO processing of failed messages.
        """
        dlq_files = sorted(self.storage_dir.glob("dlq_*.json"))

        if not dlq_files:
            return None

        oldest_file = dlq_files[0]

        try:
            with open(oldest_file, encoding="utf-8") as f:
                data = json.load(f)

            # Remove file after reading
            oldest_file.unlink()

            return data
        except Exception as e:
            logger.error("Error dequeuing DLQ message", filepath=str(oldest_file), error=str(e))
            return None

    def get_statistics(self) -> dict[str, Any]:
        """
        Get DLQ statistics.

        Returns:
            Dictionary with DLQ metrics

        AI: For monitoring dashboards.
        """
        try:
            dlq_files = list(self.storage_dir.glob("dlq_*.json"))
            total_messages = len(dlq_files)

            oldest_age = None
            if dlq_files:
                oldest_file = sorted(dlq_files)[0]
                file_stat = oldest_file.stat()
                oldest_time = datetime.fromtimestamp(file_stat.st_mtime, UTC)
                oldest_age = (datetime.now(UTC) - oldest_time).total_seconds()

            return {
                "total_messages": total_messages,
                "oldest_message_age": oldest_age,
                "storage_dir": str(self.storage_dir),
            }
        except Exception as e:
            logger.error("Error getting DLQ statistics", error=str(e))
            return {
                "total_messages": 0,
                "oldest_message_age": None,
                "storage_dir": str(self.storage_dir),
            }

    def list_messages(self, limit: int | None = None) -> list[dict[str, Any]]:
        """
        List messages in DLQ without removing them.

        Args:
            limit: Maximum number of messages to return

        Returns:
            List of message dictionaries

        AI: For admin UI to display pending DLQ messages.
        """
        messages = []
        dlq_files = sorted(self.storage_dir.glob("dlq_*.json"))

        if limit:
            dlq_files = dlq_files[:limit]

        for filepath in dlq_files:
            try:
                with open(filepath, encoding="utf-8") as f:
                    data = json.load(f)
                    data["dlq_file"] = str(filepath)
                    messages.append(data)
            except Exception as e:
                logger.error("Error reading DLQ file", filepath=str(filepath), error=str(e))
                continue

        return messages

    def replay_message(self, filepath: str) -> dict[str, Any]:
        """
        Retrieve message for replay and remove from DLQ.

        Args:
            filepath: Path to DLQ file

        Returns:
            Message data

        AI: For manual replay of failed messages.
        """
        path = Path(filepath)

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        path.unlink()

        logger.info("Message replayed from DLQ", filepath=filepath)

        return data

    def delete_message(self, filepath: str) -> None:
        """
        Delete a message from DLQ without processing.

        Args:
            filepath: Path to DLQ file

        AI: For discarding messages that can't be replayed.
        """
        Path(filepath).unlink()
        logger.info("Message deleted from DLQ", filepath=filepath)

    def cleanup_old_messages(self, max_age_days: int = 7) -> int:
        """
        Clean up old DLQ messages.

        Args:
            max_age_days: Maximum age of messages to keep

        Returns:
            Number of messages removed

        AI: Prevents unbounded DLQ growth.
        """
        from datetime import timedelta

        try:
            cutoff_time = datetime.now(UTC) - timedelta(days=max_age_days)
            removed_count = 0

            for filepath in self.storage_dir.glob("dlq_*.json"):
                try:
                    file_stat = filepath.stat()
                    file_time = datetime.fromtimestamp(file_stat.st_mtime, UTC)

                    if file_time < cutoff_time:
                        filepath.unlink()
                        removed_count += 1
                except Exception as e:
                    logger.warning("Error removing old DLQ file", filepath=str(filepath), error=str(e))
                    continue

            if removed_count > 0:
                logger.info("Cleaned up old DLQ messages", removed_count=removed_count, max_age_days=max_age_days)

            return removed_count
        except Exception as e:
            logger.error("Error during DLQ cleanup", error=str(e))
            return 0
