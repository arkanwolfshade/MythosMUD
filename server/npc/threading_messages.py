# pyright: reportAny=false, reportUnknownVariableType=false, reportUnknownArgumentType=false, reportUnknownMemberType=false
# Reason: json.loads returns Any; NPC message payloads normalize dict keys to str at parse boundary.

"""NPC action messages and the per-NPC pending-message queue.

As noted in the Pnakotic Manuscripts, a well-bound missive is safer than a
loose scrap; the queue keeps those missives in order until a thread can act.
"""

import json
import threading
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from enum import Enum

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _optional_str_field(mapping: dict[str, object], key: str) -> str | None:
    value = mapping.get(key)
    return value if isinstance(value, str) else None


def _optional_int_field(mapping: dict[str, object], key: str) -> int | None:
    value = mapping.get(key)
    return value if isinstance(value, int) else None


def _float_field(value: object) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value))


class NPCActionType(Enum):
    """Enumeration of NPC action types."""

    MOVE = "move"
    ATTACK = "attack"
    SPEAK = "speak"
    INTERACT = "interact"
    WANDER = "wander"
    HUNT = "hunt"
    FLEE = "flee"
    IDLE = "idle"
    CUSTOM = "custom"


@dataclass
class NPCActionMessage:  # pylint: disable=too-many-instance-attributes  # Reason: NPC action message requires many fields to capture complete action context
    """
    Message structure for NPC actions.

    This class represents a single action that an NPC can perform,
    with all necessary metadata for execution and tracking.
    """

    action_type: NPCActionType
    npc_id: str
    timestamp: float

    # Optional fields for different action types
    target_room: str | None = None
    target_player: str | None = None
    target_npc: str | None = None
    message: str | None = None
    channel: str | None = None
    damage: int | None = None
    item_id: str | None = None
    custom_data: dict[str, object] | None = None

    def to_dict(self) -> dict[str, object]:
        """Convert message to dictionary for serialization."""
        data = asdict(self)
        data["action_type"] = self.action_type.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "NPCActionMessage":
        """Create message from dictionary."""
        action_raw = data["action_type"]
        action_type = action_raw if isinstance(action_raw, NPCActionType) else NPCActionType(str(action_raw))
        custom_raw = data.get("custom_data")
        custom_data: dict[str, object] | None = None
        if isinstance(custom_raw, dict):
            custom_data = {str(key): value for key, value in custom_raw.items()}
        return cls(
            action_type=action_type,
            npc_id=str(data["npc_id"]),
            timestamp=_float_field(data["timestamp"]),
            target_room=_optional_str_field(data, "target_room"),
            target_player=_optional_str_field(data, "target_player"),
            target_npc=_optional_str_field(data, "target_npc"),
            message=_optional_str_field(data, "message"),
            channel=_optional_str_field(data, "channel"),
            damage=_optional_int_field(data, "damage"),
            item_id=_optional_str_field(data, "item_id"),
            custom_data=custom_data,
        )

    def to_json(self) -> str:
        """Convert message to JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "NPCActionMessage":
        """Create message from JSON string."""
        parsed_raw: object = json.loads(json_str)
        if not isinstance(parsed_raw, dict):
            raise ValueError("NPC action message JSON must be an object")
        payload: dict[str, object] = {str(key): value for key, value in parsed_raw.items()}
        return cls.from_dict(payload)


class NPCMessageQueue:
    """
    Thread-safe message queue for NPC actions.

    This queue handles pending actions for NPCs, ensuring reliable
    delivery and proper ordering of actions.
    """

    def __init__(self, max_messages_per_npc: int = 1000) -> None:
        """
        Initialize the NPC message queue.

        Args:
            max_messages_per_npc: Maximum number of pending messages per NPC
        """
        self.pending_messages: dict[str, list[dict[str, object]]] = defaultdict(list)
        self.max_messages_per_npc: int = max_messages_per_npc
        self._lock: threading.RLock = threading.RLock()

        logger.info("NPC message queue initialized", max_messages_per_npc=max_messages_per_npc)

    def add_message(self, npc_id: str, message: dict[str, object]) -> bool:
        """
        Add a message to an NPC's pending message queue.

        Args:
            npc_id: The NPC's ID
            message: The message to queue

        Returns:
            bool: True if message was added successfully, False otherwise
        """
        try:
            with self._lock:
                # Add timestamp if not present
                if "timestamp" not in message:
                    message["timestamp"] = time.time()

                self.pending_messages[npc_id].append(message)

                # Limit queue size
                if len(self.pending_messages[npc_id]) > self.max_messages_per_npc:
                    self.pending_messages[npc_id] = self.pending_messages[npc_id][-self.max_messages_per_npc :]
                    logger.warning(
                        "NPC message queue limit reached, dropping oldest messages",
                        npc_id=npc_id,
                        max_messages=self.max_messages_per_npc,
                    )

                logger.debug("Added message to NPC queue", npc_id=npc_id, message_type=message.get("type"))
                return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message queue errors unpredictable, must return False
            logger.error("Error adding message to NPC queue", npc_id=npc_id, error=str(e))
            return False

    def get_messages(self, npc_id: str) -> list[dict[str, object]]:
        """
        Get all pending messages for an NPC.

        Args:
            npc_id: The NPC's ID

        Returns:
            List of pending messages
        """
        with self._lock:
            return list(self.pending_messages.get(npc_id, []))

    def clear_messages(self, npc_id: str) -> bool:
        """
        Clear all pending messages for an NPC.

        Args:
            npc_id: The NPC's ID

        Returns:
            bool: True if messages were cleared successfully
        """
        try:
            with self._lock:
                removed = self.pending_messages.pop(npc_id, None)
                if removed is not None:
                    logger.debug("Cleared NPC messages", npc_id=npc_id, message_count=len(removed))
                return True
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message clearing errors unpredictable, must return False
            logger.error("Error clearing NPC messages", npc_id=npc_id, error=str(e))
            return False

    def get_queue_size(self, npc_id: str) -> int:
        """Get the number of pending messages for an NPC."""
        with self._lock:
            return len(self.pending_messages.get(npc_id, []))

    def get_total_queue_size(self) -> int:
        """Get the total number of pending messages across all NPCs."""
        with self._lock:
            return sum(len(messages) for messages in self.pending_messages.values())

    def clear_all_messages(self) -> None:
        """Remove every per-NPC pending-message entry."""
        with self._lock:
            self.pending_messages.clear()
