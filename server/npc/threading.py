# pyright: reportAny=false, reportUnknownVariableType=false, reportUnknownArgumentType=false, reportUnknownMemberType=false
# Reason: json.loads returns Any; NPC message payloads normalize dict keys to str at parse boundary.

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
import time
from collections import defaultdict

from anyio import Lock, sleep

from ..models.npc import NPCDefinition
from ..structured_logging.enhanced_logging_config import get_logger
from .threading_messages import NPCActionMessage, NPCActionType, NPCMessageQueue

logger = get_logger(__name__)

__all__ = [
    "NPCActionMessage",
    "NPCActionType",
    "NPCCommunicationBridge",
    "NPCMessageQueue",
    "NPCThreadManager",
]


class NPCThreadManager:
    """
    Manages NPC threads and their lifecycle.

    This class handles the creation, management, and cleanup of individual
    NPC threads, ensuring proper resource management and thread safety.
    """

    def __init__(self) -> None:
        """Initialize the NPC thread manager."""
        self.active_threads: dict[str, asyncio.Task[object]] = {}
        self.npc_definitions: dict[str, NPCDefinition] = {}
        self.message_queue: NPCMessageQueue = NPCMessageQueue()
        self.is_running: bool = False
        self._lock: Lock = Lock()

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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Thread manager startup errors unpredictable, must return False
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
                    _ = await asyncio.gather(*stop_tasks, return_exceptions=True)

                self.active_threads.clear()
                self.npc_definitions.clear()
                self.message_queue.clear_all_messages()

            logger.info("NPC thread manager stopped")
            return True
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Thread manager shutdown errors unpredictable, must return False
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC thread startup errors unpredictable, must return False
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC thread shutdown errors unpredictable, must return False
            logger.error("Failed to stop NPC thread", npc_id=npc_id, error=str(e))
            return False

    async def _stop_npc_thread_internal(self, npc_id: str) -> bool:
        """Internal method to stop an NPC thread."""
        if npc_id not in self.active_threads:
            logger.warning("NPC thread not found", npc_id=npc_id)
            return True

        task = self.active_threads[npc_id]
        if not task.done():
            _ = task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        del self.active_threads[npc_id]
        if npc_id in self.npc_definitions:
            del self.npc_definitions[npc_id]

        # Clear any pending messages for this NPC
        _ = self.message_queue.clear_messages(npc_id)

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
            _ = await self.stop_npc_thread(npc_id)

            # Start a new thread
            return await self.start_npc_thread(npc_id, npc_definition)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC thread restart errors unpredictable, must return False
            logger.error("Failed to restart NPC thread", npc_id=npc_id, error=str(e))
            return False

    def get_active_npc_threads(self) -> list[str]:
        """Get list of active NPC thread IDs."""
        return list(self.active_threads.keys())

    def get_npc_definition(self, npc_id: str) -> NPCDefinition | None:
        """Get NPC definition for a specific NPC."""
        return self.npc_definitions.get(npc_id)

    async def _npc_thread_worker(self, npc_id: str, npc_definition: NPCDefinition) -> None:
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
                    _ = self.message_queue.clear_messages(npc_id)

                # Execute NPC behavior (placeholder for now)
                await self._execute_npc_behavior(npc_id, npc_definition)

                # Sleep to prevent busy waiting
                await sleep(0.1)

        except asyncio.CancelledError:
            logger.info("NPC thread worker cancelled", npc_id=npc_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Thread worker errors unpredictable, must handle gracefully
            logger.error("Error in NPC thread worker", npc_id=npc_id, error=str(e))
        finally:
            logger.info("NPC thread worker ended", npc_id=npc_id)

    async def _process_npc_message(self, npc_id: str, message: dict[str, object]) -> None:
        """Process a message for an NPC."""
        try:
            message_type = message.get("type")
            action_type = message.get("action_type")
            logger.debug("Processing NPC message", npc_id=npc_id, message_type=message_type, action_type=action_type)

            # Process WANDER actions for idle movement
            if action_type == NPCActionType.WANDER.value or message_type == "wander":
                await self._process_wander_action(npc_id, message)
            # Add other action type handlers here as needed

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message processing errors unpredictable, must handle gracefully
            logger.error("Error processing NPC message", npc_id=npc_id, error=str(e))

    def _resolve_wander_npc(self, npc_id: str) -> tuple[object, object] | None:
        """Resolve active NPC instance and definition for a WANDER action."""
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
            logger.warning("NPC instance service not available for WANDER action", npc_id=npc_id)
            return None

        lifecycle_manager = npc_instance_service.lifecycle_manager
        if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
            logger.warning("NPC instance not found for WANDER action", npc_id=npc_id)
            return None

        npc_definition = self.npc_definitions.get(npc_id)
        if not npc_definition:
            logger.warning("NPC definition not found for WANDER action", npc_id=npc_id)
            return None

        return lifecycle_manager.active_npcs[npc_id], npc_definition

    @staticmethod
    def _parse_behavior_config(npc_instance: object) -> dict[str, object]:
        """Parse NPC behavior config from instance attribute (dict or JSON string)."""
        behavior_config = getattr(npc_instance, "_behavior_config", {})
        if not isinstance(behavior_config, str):
            return behavior_config if isinstance(behavior_config, dict) else {}
        try:
            parsed_obj: object = json.loads(behavior_config)
        except json.JSONDecodeError:
            return {}
        if isinstance(parsed_obj, dict):
            return {str(key): value for key, value in parsed_obj.items()}
        return {}

    def _execute_wander_movement(self, npc_id: str, npc_instance: object, npc_definition: object) -> None:
        """Run idle movement for a resolved wander NPC."""
        from ..container import ApplicationContainer
        from .idle_movement import IdleMovementHandler

        container = ApplicationContainer.get_instance()
        async_persistence = getattr(container, "async_persistence", None) if container else None
        if async_persistence is None:
            logger.error("async_persistence not available for idle movement", npc_id=npc_id)
            return

        behavior_config = self._parse_behavior_config(npc_instance)
        movement_handler = IdleMovementHandler(
            event_bus=getattr(npc_instance, "event_bus", None),
            persistence=async_persistence,
        )
        success = movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
        if success:
            if hasattr(npc_instance, "_last_idle_movement_time"):
                object.__setattr__(npc_instance, "_last_idle_movement_time", time.time())
            logger.debug("WANDER action executed successfully", npc_id=npc_id)
        else:
            logger.debug("WANDER action did not result in movement", npc_id=npc_id)

    async def _process_wander_action(self, npc_id: str, _message: dict[str, object]) -> None:  # pylint: disable=unused-argument  # Reason: Parameter required for action signature, message content not used
        """
        Process a WANDER action for idle movement.

        Args:
            npc_id: ID of the NPC to move
            message: Message containing action data
        """
        try:
            resolved = self._resolve_wander_npc(npc_id)
            if resolved is None:
                return
            npc_instance, npc_definition = resolved
            self._execute_wander_movement(npc_id, npc_instance, npc_definition)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: WANDER action processing errors unpredictable, must handle gracefully
            logger.error("Error processing WANDER action", npc_id=npc_id, error=str(e))

    async def _execute_npc_behavior(self, npc_id: str, _npc_definition: NPCDefinition) -> None:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future definition-based behavior execution
        """Execute NPC behavior based on its type and configuration."""
        try:
            # Get NPC instance from lifecycle manager
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                logger.debug("NPC instance service not available for behavior execution", npc_id=npc_id)
                return

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
                logger.debug("NPC instance not found for behavior execution", npc_id=npc_id)
                return

            npc_instance = lifecycle_manager.active_npcs[npc_id]

            # Execute NPC behavior with empty context (NPC will add its own context)
            context: dict[str, object] = {}
            try:
                _ = await npc_instance.execute_behavior(context)
                logger.debug(
                    "Executed NPC behavior", npc_id=npc_id, npc_type=getattr(npc_instance, "npc_type", "unknown")
                )
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Behavior execution errors unpredictable, must handle gracefully
                logger.error("Error executing NPC behavior", npc_id=npc_id, error=str(e), exc_info=True)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Behavior execution errors unpredictable, must handle gracefully
            logger.error("Error executing NPC behavior", npc_id=npc_id, error=str(e))


class NPCCommunicationBridge:
    """
    Bridge for communication between NPC threads and main game thread.

    This class provides thread-safe communication channels for sending
    messages between NPCs and the main game systems.
    """

    def __init__(self) -> None:
        """Initialize the communication bridge."""
        self.outgoing_messages: list[dict[str, object]] = []
        self.incoming_messages: dict[str, list[dict[str, object]]] = defaultdict(list)
        self._outgoing_lock: Lock = Lock()
        self._incoming_lock: Lock = Lock()

        logger.info("NPC communication bridge initialized")

    async def send_message_to_npc(self, npc_id: str, message: dict[str, object]) -> bool:
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message sending errors unpredictable, must return False
            logger.error("Error sending message to NPC", npc_id=npc_id, error=str(e))
            return False

    async def receive_message_from_npc(self, npc_id: str, message: dict[str, object]) -> bool:
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

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message receiving errors unpredictable, must return False
            logger.error("Error receiving message from NPC", npc_id=npc_id, error=str(e))
            return False

    async def broadcast_to_all_npcs(self, message: dict[str, object]) -> bool:
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
                for _npc_id, messages in self.incoming_messages.items():
                    messages.append(message.copy())

            logger.debug("Broadcast message to all NPCs", message_type=message.get("type"))
            return True

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Message broadcasting errors unpredictable, must return False
            logger.error("Error broadcasting message to NPCs", error=str(e))
            return False

    async def get_pending_messages(self) -> list[dict[str, object]]:
        """Get all pending outgoing messages from NPCs."""
        async with self._outgoing_lock:
            messages = self.outgoing_messages.copy()
            self.outgoing_messages.clear()
            return messages

    async def get_messages_for_npc(self, npc_id: str) -> list[dict[str, object]]:
        """Get pending messages for a specific NPC."""
        async with self._incoming_lock:
            messages = self.incoming_messages[npc_id].copy()
            self.incoming_messages[npc_id].clear()
            return messages


# REMOVED: Duplicate NPCLifecycleManager class (lines 608-773)
# The authoritative NPCLifecycleManager is in server/npc/lifecycle_manager.py
# This duplicate class was only used in tests and has been removed to prevent confusion
