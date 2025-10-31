"""
NPC threading and message queue infrastructure for MythosMUD.

This module provides the core threading infrastructure for NPCs, including
message queues, thread management, and thread-safe communication between
NPC threads and the main game loop.

As noted in the Pnakotic Manuscripts, proper thread management is essential
for maintaining the delicate balance between order and chaos in our eldritch
processing systems.
"""

import asyncio
import json
import threading
import time
from collections import defaultdict
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..models.npc import NPCDefinition

logger = get_logger(__name__)


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
class NPCActionMessage:
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
    custom_data: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert message to dictionary for serialization."""
        data = asdict(self)
        data["action_type"] = self.action_type.value
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "NPCActionMessage":
        """Create message from dictionary."""
        data = data.copy()
        data["action_type"] = NPCActionType(data["action_type"])
        return cls(**data)

    def to_json(self) -> str:
        """Convert message to JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> "NPCActionMessage":
        """Create message from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)


class NPCMessageQueue:
    """
    Thread-safe message queue for NPC actions.

    This queue handles pending actions for NPCs, ensuring reliable
    delivery and proper ordering of actions.
    """

    def __init__(self, max_messages_per_npc: int = 1000):
        """
        Initialize the NPC message queue.

        Args:
            max_messages_per_npc: Maximum number of pending messages per NPC
        """
        self.pending_messages: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.max_messages_per_npc = max_messages_per_npc
        self._lock = threading.RLock()

        logger.info("NPC message queue initialized", max_messages_per_npc=max_messages_per_npc)

    def add_message(self, npc_id: str, message: dict[str, Any]) -> bool:
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

        except Exception as e:
            logger.error("Error adding message to NPC queue", npc_id=npc_id, error=str(e))
            return False

    def get_messages(self, npc_id: str) -> list[dict[str, Any]]:
        """
        Get all pending messages for an NPC.

        Args:
            npc_id: The NPC's ID

        Returns:
            List of pending messages
        """
        with self._lock:
            return self.pending_messages[npc_id].copy()

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
                if npc_id in self.pending_messages:
                    message_count = len(self.pending_messages[npc_id])
                    self.pending_messages[npc_id].clear()
                    logger.debug("Cleared NPC messages", npc_id=npc_id, message_count=message_count)
                return True
        except Exception as e:
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


class NPCThreadManager:
    """
    Manages NPC threads and their lifecycle.

    This class handles the creation, management, and cleanup of individual
    NPC threads, ensuring proper resource management and thread safety.
    """

    def __init__(self):
        """Initialize the NPC thread manager."""
        self.active_threads: dict[str, asyncio.Task] = {}
        self.npc_definitions: dict[str, NPCDefinition] = {}
        self.message_queue = NPCMessageQueue()
        self.is_running = False
        self._lock = asyncio.Lock()

        logger.info("NPC thread manager initialized")

    async def start(self) -> bool:
        """
        Start the NPC thread manager.

        Returns:
            bool: True if started successfully, False otherwise
        """
        if self.is_running:
            logger.warning("NPC thread manager is already running")
            return True

        try:
            self.is_running = True
            logger.info("NPC thread manager started")
            return True
        except Exception as e:
            logger.error("Failed to start NPC thread manager", error=str(e))
            return False

    async def stop(self) -> bool:
        """
        Stop the NPC thread manager and all active threads.

        Returns:
            bool: True if stopped successfully, False otherwise
        """
        if not self.is_running:
            logger.warning("NPC thread manager is not running")
            return True

        try:
            async with self._lock:
                self.is_running = False

                # Stop all active threads
                stop_tasks = []
                for npc_id, task in self.active_threads.items():
                    if not task.done():
                        stop_tasks.append(self._stop_npc_thread_internal(npc_id))

                if stop_tasks:
                    await asyncio.gather(*stop_tasks, return_exceptions=True)

                self.active_threads.clear()
                self.npc_definitions.clear()

            logger.info("NPC thread manager stopped")
            return True
        except Exception as e:
            logger.error("Failed to stop NPC thread manager", error=str(e))
            return False

    async def start_npc_thread(self, npc_id: str, npc_definition: NPCDefinition) -> bool:
        """
        Start a thread for a specific NPC.

        Args:
            npc_id: Unique identifier for the NPC
            npc_definition: NPC definition containing behavior and configuration

        Returns:
            bool: True if thread started successfully, False otherwise
        """
        if not self.is_running:
            logger.error("NPC thread manager is not running")
            return False

        try:
            async with self._lock:
                if npc_id in self.active_threads:
                    logger.warning("NPC thread already exists", npc_id=npc_id)
                    return True

                # Create and start the NPC thread
                task = asyncio.create_task(self._npc_thread_worker(npc_id, npc_definition))
                self.active_threads[npc_id] = task
                self.npc_definitions[npc_id] = npc_definition

                logger.info("Started NPC thread", npc_id=npc_id, npc_name=npc_definition.name)
                return True

        except Exception as e:
            logger.error("Failed to start NPC thread", npc_id=npc_id, error=str(e))
            return False

    async def stop_npc_thread(self, npc_id: str) -> bool:
        """
        Stop a specific NPC thread.

        Args:
            npc_id: Unique identifier for the NPC

        Returns:
            bool: True if thread stopped successfully, False otherwise
        """
        try:
            async with self._lock:
                return await self._stop_npc_thread_internal(npc_id)
        except Exception as e:
            logger.error("Failed to stop NPC thread", npc_id=npc_id, error=str(e))
            return False

    async def _stop_npc_thread_internal(self, npc_id: str) -> bool:
        """Internal method to stop an NPC thread."""
        if npc_id not in self.active_threads:
            logger.warning("NPC thread not found", npc_id=npc_id)
            return True

        task = self.active_threads[npc_id]
        if not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        del self.active_threads[npc_id]
        if npc_id in self.npc_definitions:
            del self.npc_definitions[npc_id]

        # Clear any pending messages for this NPC
        self.message_queue.clear_messages(npc_id)

        logger.info("Stopped NPC thread", npc_id=npc_id)
        return True

    async def restart_npc_thread(self, npc_id: str, npc_definition: NPCDefinition) -> bool:
        """
        Restart a specific NPC thread.

        Args:
            npc_id: Unique identifier for the NPC
            npc_definition: NPC definition containing behavior and configuration

        Returns:
            bool: True if thread restarted successfully, False otherwise
        """
        try:
            # Stop the existing thread
            await self.stop_npc_thread(npc_id)

            # Start a new thread
            return await self.start_npc_thread(npc_id, npc_definition)
        except Exception as e:
            logger.error("Failed to restart NPC thread", npc_id=npc_id, error=str(e))
            return False

    def get_active_npc_threads(self) -> list[str]:
        """Get list of active NPC thread IDs."""
        return list(self.active_threads.keys())

    def get_npc_definition(self, npc_id: str) -> NPCDefinition | None:
        """Get NPC definition for a specific NPC."""
        return self.npc_definitions.get(npc_id)

    async def _npc_thread_worker(self, npc_id: str, npc_definition: NPCDefinition):
        """
        Worker function for individual NPC threads.

        This function runs in a separate thread and handles the NPC's
        behavior loop, processing messages and executing actions.
        """
        logger.info("NPC thread worker started", npc_id=npc_id, npc_name=npc_definition.name)

        try:
            while self.is_running and npc_id in self.active_threads:
                # Process pending messages
                messages = self.message_queue.get_messages(npc_id)
                for message in messages:
                    await self._process_npc_message(npc_id, message)

                # Clear processed messages
                if messages:
                    self.message_queue.clear_messages(npc_id)

                # Execute NPC behavior (placeholder for now)
                await self._execute_npc_behavior(npc_id, npc_definition)

                # Sleep to prevent busy waiting
                await asyncio.sleep(0.1)

        except asyncio.CancelledError:
            logger.info("NPC thread worker cancelled", npc_id=npc_id)
        except Exception as e:
            logger.error("Error in NPC thread worker", npc_id=npc_id, error=str(e))
        finally:
            logger.info("NPC thread worker ended", npc_id=npc_id)

    async def _process_npc_message(self, npc_id: str, message: dict[str, Any]):
        """Process a message for an NPC."""
        try:
            message_type = message.get("type")
            logger.debug("Processing NPC message", npc_id=npc_id, message_type=message_type)

            # Placeholder for message processing logic
            # This will be expanded when we implement specific NPC behaviors

        except Exception as e:
            logger.error("Error processing NPC message", npc_id=npc_id, error=str(e))

    async def _execute_npc_behavior(self, npc_id: str, npc_definition: NPCDefinition):
        """Execute NPC behavior based on its type and configuration."""
        try:
            # Placeholder for behavior execution
            # This will be expanded when we implement specific NPC behaviors
            pass

        except Exception as e:
            logger.error("Error executing NPC behavior", npc_id=npc_id, error=str(e))


class NPCCommunicationBridge:
    """
    Bridge for communication between NPC threads and main game thread.

    This class provides thread-safe communication channels for sending
    messages between NPCs and the main game systems.
    """

    def __init__(self):
        """Initialize the communication bridge."""
        self.outgoing_messages: list[dict[str, Any]] = []
        self.incoming_messages: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self._outgoing_lock = asyncio.Lock()
        self._incoming_lock = asyncio.Lock()

        logger.info("NPC communication bridge initialized")

    async def send_message_to_npc(self, npc_id: str, message: dict[str, Any]) -> bool:
        """
        Send a message to a specific NPC.

        Args:
            npc_id: The NPC's ID
            message: The message to send

        Returns:
            bool: True if message was sent successfully
        """
        try:
            message["timestamp"] = time.time()
            message["target_npc"] = npc_id

            async with self._incoming_lock:
                self.incoming_messages[npc_id].append(message)

            logger.debug("Sent message to NPC", npc_id=npc_id, message_type=message.get("type"))
            return True

        except Exception as e:
            logger.error("Error sending message to NPC", npc_id=npc_id, error=str(e))
            return False

    async def receive_message_from_npc(self, npc_id: str, message: dict[str, Any]) -> bool:
        """
        Receive a message from a specific NPC.

        Args:
            npc_id: The NPC's ID
            message: The message received

        Returns:
            bool: True if message was received successfully
        """
        try:
            message["timestamp"] = time.time()
            message["source_npc"] = npc_id

            async with self._outgoing_lock:
                self.outgoing_messages.append(message)

            logger.debug("Received message from NPC", npc_id=npc_id, message_type=message.get("type"))
            return True

        except Exception as e:
            logger.error("Error receiving message from NPC", npc_id=npc_id, error=str(e))
            return False

    async def broadcast_to_all_npcs(self, message: dict[str, Any]) -> bool:
        """
        Broadcast a message to all NPCs.

        Args:
            message: The message to broadcast

        Returns:
            bool: True if message was broadcast successfully
        """
        try:
            message["timestamp"] = time.time()
            message["broadcast"] = True

            async with self._incoming_lock:
                for npc_id in self.incoming_messages.keys():
                    self.incoming_messages[npc_id].append(message.copy())

            logger.debug("Broadcast message to all NPCs", message_type=message.get("type"))
            return True

        except Exception as e:
            logger.error("Error broadcasting message to NPCs", error=str(e))
            return False

    async def get_pending_messages(self) -> list[dict[str, Any]]:
        """Get all pending outgoing messages from NPCs."""
        async with self._outgoing_lock:
            messages = self.outgoing_messages.copy()
            self.outgoing_messages.clear()
            return messages

    async def get_messages_for_npc(self, npc_id: str) -> list[dict[str, Any]]:
        """Get pending messages for a specific NPC."""
        async with self._incoming_lock:
            messages = self.incoming_messages[npc_id].copy()
            self.incoming_messages[npc_id].clear()
            return messages


class NPCLifecycleManager:
    """
    Manages the lifecycle of NPC instances.

    This class handles spawning, despawning, and respawning of NPCs,
    coordinating with the thread manager and database.
    """

    def __init__(self, thread_manager: NPCThreadManager | None = None):
        """
        Initialize the NPC lifecycle manager.

        Args:
            thread_manager: Optional NPC thread manager instance
        """
        self.thread_manager = thread_manager or NPCThreadManager()
        self.active_npcs: dict[int, dict[str, Any]] = {}
        self._lock = asyncio.Lock()

        logger.info("NPC lifecycle manager initialized")

    async def spawn_npc(self, npc_definition: NPCDefinition) -> bool:
        """
        Spawn an NPC instance.

        Args:
            npc_definition: The NPC definition to spawn

        Returns:
            bool: True if NPC was spawned successfully
        """
        try:
            async with self._lock:
                npc_id = f"npc_{npc_definition.id}_{int(time.time())}"

                # Start the NPC thread
                success = await self.thread_manager.start_npc_thread(npc_id, npc_definition)
                if not success:
                    return False

                # Track the active NPC
                self.active_npcs[npc_definition.id] = {
                    "npc_id": npc_id,
                    "definition": npc_definition,
                    "spawned_at": time.time(),
                    "status": "active",
                }

                logger.info("Spawned NPC", npc_id=npc_id, npc_name=npc_definition.name)
                return True

        except Exception as e:
            logger.error("Failed to spawn NPC", npc_definition_id=npc_definition.id, error=str(e))
            return False

    async def despawn_npc(self, npc_definition_id: int) -> bool:
        """
        Despawn an NPC instance.

        Args:
            npc_definition_id: The NPC definition ID to despawn

        Returns:
            bool: True if NPC was despawned successfully
        """
        try:
            async with self._lock:
                if npc_definition_id not in self.active_npcs:
                    logger.warning("NPC not found for despawning", npc_definition_id=npc_definition_id)
                    return True

                npc_info = self.active_npcs[npc_definition_id]
                npc_id = npc_info["npc_id"]

                # Stop the NPC thread
                success = await self.thread_manager.stop_npc_thread(npc_id)
                if not success:
                    return False

                # Remove from active NPCs
                del self.active_npcs[npc_definition_id]

                logger.info("Despawned NPC", npc_id=npc_id, npc_definition_id=npc_definition_id)
                return True

        except Exception as e:
            logger.error("Failed to despawn NPC", npc_definition_id=npc_definition_id, error=str(e))
            return False

    async def respawn_npc(self, npc_definition_id: int, npc_definition: NPCDefinition) -> bool:
        """
        Respawn an NPC instance.

        Args:
            npc_definition_id: The NPC definition ID to respawn
            npc_definition: The updated NPC definition

        Returns:
            bool: True if NPC was respawned successfully
        """
        try:
            # Despawn first
            await self.despawn_npc(npc_definition_id)

            # Spawn with new definition
            return await self.spawn_npc(npc_definition)

        except Exception as e:
            logger.error("Failed to respawn NPC", npc_definition_id=npc_definition_id, error=str(e))
            return False

    async def get_npc_status(self, npc_definition_id: int) -> dict[str, Any] | None:
        """
        Get the status of an NPC instance.

        Args:
            npc_definition_id: The NPC definition ID

        Returns:
            Dict containing NPC status information, or None if not found
        """
        if npc_definition_id not in self.active_npcs:
            return None

        npc_info = self.active_npcs[npc_definition_id]
        return {
            "npc_id": npc_info["npc_id"],
            "npc_definition_id": npc_definition_id,
            "status": npc_info["status"],
            "spawned_at": npc_info["spawned_at"],
            "uptime": time.time() - npc_info["spawned_at"],
        }

    async def cleanup_all_npcs(self) -> bool:
        """
        Clean up all active NPCs.

        Returns:
            bool: True if all NPCs were cleaned up successfully
        """
        try:
            async with self._lock:
                cleanup_tasks = []
                for npc_definition_id in list(self.active_npcs.keys()):
                    cleanup_tasks.append(self.despawn_npc(npc_definition_id))

                if cleanup_tasks:
                    results = await asyncio.gather(*cleanup_tasks, return_exceptions=True)
                    success = all(result is True for result in results)
                else:
                    success = True

                logger.info("Cleaned up all NPCs", npc_count=len(cleanup_tasks))
                return success

        except Exception as e:
            logger.error("Failed to cleanup all NPCs", error=str(e))
            return False

    def get_active_npc_count(self) -> int:
        """Get the number of active NPCs."""
        return len(self.active_npcs)

    def get_active_npc_ids(self) -> list[int]:
        """Get list of active NPC definition IDs."""
        return list(self.active_npcs.keys())
