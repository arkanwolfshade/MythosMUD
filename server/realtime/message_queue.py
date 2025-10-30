"""
Message queue management for MythosMUD.

This module provides message queuing functionality for guaranteed delivery
of messages to players who may be temporarily disconnected.
"""

import time
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MessageQueue:
    """
    Message queue for guaranteed delivery of messages to players.

    This class handles pending messages for players who may be temporarily
    disconnected, with automatic cleanup of old messages.
    """

    def __init__(self, max_messages_per_player: int = 1000) -> None:
        """
        Initialize the message queue.

        Args:
            max_messages_per_player: Maximum number of pending messages per player
        """
        # Pending messages for guaranteed delivery
        self.pending_messages: dict[str, list[dict[str, Any]]] = {}
        self.max_messages_per_player = max_messages_per_player

    def add_message(self, player_id: str, message: dict[str, Any]) -> bool:
        """
        Add a message to a player's pending message queue.

        Args:
            player_id: The player's ID
            message: The message to queue

        Returns:
            bool: True if message was added successfully, False otherwise
        """
        try:
            if player_id not in self.pending_messages:
                self.pending_messages[player_id] = []

            # Add timestamp if not present
            if "timestamp" not in message:
                message["timestamp"] = time.time()

            self.pending_messages[player_id].append(message)

            # Limit queue size
            if len(self.pending_messages[player_id]) > self.max_messages_per_player:
                self.pending_messages[player_id] = self.pending_messages[player_id][-self.max_messages_per_player :]
                logger.warning("Message queue limit reached, dropping oldest messages", player_id=player_id)

            logger.debug("Added message to queue", player_id=player_id)
            return True

        except (ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error adding message to queue", player_id=player_id, error=str(e), error_type=type(e).__name__
            )
            return False

    def get_messages(self, player_id: str) -> list[dict[str, Any]]:
        """
        Get all pending messages for a player and clear the queue.

        Args:
            player_id: The player's ID

        Returns:
            List[Dict[str, Any]]: List of pending messages
        """
        try:
            messages = self.pending_messages.get(player_id, [])
            if player_id in self.pending_messages:
                del self.pending_messages[player_id]
                logger.debug("Retrieved and cleared messages", message_count=len(messages), player_id=player_id)
            return messages

        except (ValueError, TypeError, KeyError) as e:
            logger.error("Error retrieving messages", player_id=player_id, error=str(e), error_type=type(e).__name__)
            return []

    def has_messages(self, player_id: str) -> bool:
        """
        Check if a player has pending messages.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if player has pending messages, False otherwise
        """
        return player_id in self.pending_messages and len(self.pending_messages[player_id]) > 0

    def get_message_count(self, player_id: str) -> int:
        """
        Get the number of pending messages for a player.

        Args:
            player_id: The player's ID

        Returns:
            int: Number of pending messages
        """
        return len(self.pending_messages.get(player_id, []))

    def remove_player_messages(self, player_id: str) -> None:
        """
        Remove all pending messages for a specific player.

        Args:
            player_id: The player's ID to remove messages for
        """
        try:
            if player_id in self.pending_messages:
                del self.pending_messages[player_id]
                logger.debug("Removed all pending messages", player_id=player_id)
        except (ValueError, TypeError, KeyError) as e:
            logger.error("Error removing messages", player_id=player_id, error=str(e), error_type=type(e).__name__)

    def cleanup_old_messages(self, max_age_seconds: int = 3600) -> None:
        """
        Clean up old messages to prevent memory bloat.

        Args:
            max_age_seconds: Maximum age of messages to keep (default: 1 hour)
        """
        try:
            current_time = time.time()
            orphaned_players = []
            total_removed = 0

            for player_id, messages in list(self.pending_messages.items()):
                # Remove messages older than max_age_seconds
                original_count = len(messages)
                self.pending_messages[player_id] = [
                    msg for msg in messages if self._is_message_recent(msg, current_time, max_age_seconds)
                ]

                removed_count = original_count - len(self.pending_messages[player_id])
                total_removed += removed_count

                # Remove empty entries
                if not self.pending_messages[player_id]:
                    orphaned_players.append(player_id)

            for player_id in orphaned_players:
                del self.pending_messages[player_id]

            if total_removed > 0 or orphaned_players:
                logger.info(
                    f"Message cleanup completed: {total_removed} old messages removed, "
                    f"{len(orphaned_players)} empty queues cleaned"
                )

        except (ValueError, TypeError, KeyError) as e:
            logger.error("Error cleaning up old messages", error=str(e), error_type=type(e).__name__)

    def cleanup_large_structures(self, max_entries: int = 1000) -> None:
        """
        Clean up large data structures to prevent memory bloat.

        Args:
            max_entries: Maximum number of entries per player to keep (default: 1000)
        """
        try:
            for player_id, messages in list(self.pending_messages.items()):
                if len(messages) > max_entries:
                    # Keep only the most recent messages
                    self.pending_messages[player_id] = messages[-max_entries:]
                    logger.debug(
                        f"Cleaned up large message queue structure for player {player_id}: kept {max_entries} entries"
                    )

        except (ValueError, TypeError, KeyError) as e:
            logger.error("Error cleaning up large message queue structures", error=str(e), error_type=type(e).__name__)

    def _is_message_recent(self, msg: dict[str, Any], current_time: float, max_age_seconds: int) -> bool:
        """
        Check if a message is recent (within the specified age limit).

        Args:
            msg: Message dictionary
            current_time: Current timestamp
            max_age_seconds: Maximum age in seconds

        Returns:
            bool: True if message is recent, False otherwise
        """
        try:
            timestamp = msg.get("timestamp", 0)
            if isinstance(timestamp, str):
                # Try to parse ISO timestamp string
                try:
                    from datetime import datetime

                    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                    msg_ts = dt.timestamp()
                except (ValueError, AttributeError):
                    # If parsing fails, assume it's old
                    return False
            elif isinstance(timestamp, int | float):
                msg_ts = float(timestamp)
            else:
                # Unknown timestamp format, assume it's old
                return False

            return current_time - msg_ts < max_age_seconds

        except (ValueError, TypeError, KeyError) as e:
            logger.error("Error checking message age", error=str(e), error_type=type(e).__name__)
            # If any error occurs, assume the message is old
            return False

    def get_stats(self) -> dict[str, Any]:
        """
        Get message queue statistics.

        Returns:
            Dict[str, Any]: Statistics about the message queue
        """
        try:
            total_queues = len(self.pending_messages)
            total_messages = sum(len(messages) for messages in self.pending_messages.values())

            # Find players with the most messages
            queue_sizes = [(player_id, len(messages)) for player_id, messages in self.pending_messages.items()]
            queue_sizes.sort(key=lambda x: x[1], reverse=True)

            return {
                "total_queues": total_queues,
                "total_messages": total_messages,
                "max_messages_per_player": self.max_messages_per_player,
                "largest_queues": queue_sizes[:5],  # Top 5 largest queues
                "average_queue_size": total_messages / total_queues if total_queues > 0 else 0,
            }
        except (ValueError, TypeError, KeyError) as e:
            logger.error("Error getting message queue stats", error=str(e), error_type=type(e).__name__)
            return {}
