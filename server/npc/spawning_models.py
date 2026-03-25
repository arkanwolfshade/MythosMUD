"""Data models for NPC spawn requests and results (Cultes des Goules, appendix: logistics)."""

# pylint: disable=too-few-public-methods  # Reason: Data classes and request objects with focused responsibility

import time
from dataclasses import dataclass
from typing import override

from server.models.npc import NPCDefinition, NPCSpawnRule
from server.npc.behaviors import NPCBase


@dataclass
class SimpleNPCDefinition:  # pylint: disable=too-many-instance-attributes  # Reason: flat copy of NPC fields
    """Holds NPC definition data without SQLAlchemy relationships (avoids lazy-load in spawn path)."""

    id: int
    name: str
    npc_type: str
    room_id: str | None
    description: str | None
    base_stats: str
    behavior_config: str
    ai_integration_stub: str


class NPCSpawnRequest:
    """Represents a request to spawn an NPC."""

    definition: NPCDefinition
    room_id: str
    spawn_rule: NPCSpawnRule | None
    priority: int
    reason: str
    created_at: float

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: full spawn context
        self,
        definition: NPCDefinition,
        room_id: str,
        spawn_rule: NPCSpawnRule | None = None,
        priority: int = 0,
        reason: str = "automatic",
    ) -> None:
        """
        Initialize spawn request.

        Args:
            definition: NPC definition to spawn
            room_id: Room where NPC should be spawned
            spawn_rule: Spawn rule that triggered this request
            priority: Spawn priority (higher = more important)
            reason: Reason for spawning (automatic, manual, required, etc.)
        """
        self.definition = definition
        self.room_id = room_id
        self.spawn_rule = spawn_rule
        self.priority = priority
        self.reason = reason
        self.created_at = time.time()

    @override
    def __repr__(self) -> str:
        """String representation of spawn request."""
        return (
            f"<NPCSpawnRequest(definition={self.definition.name}, room={self.room_id}, "
            f"priority={self.priority}, reason={self.reason})>"
        )


class NPCSpawnResult:
    """Represents the result of an NPC spawn attempt."""

    success: bool
    npc_id: str | None
    npc_instance: NPCBase | None
    error_message: str | None
    spawn_request: NPCSpawnRequest | None
    spawned_at: float | None

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: full result context
        self,
        success: bool,
        npc_id: str | None = None,
        npc_instance: NPCBase | None = None,
        error_message: str | None = None,
        spawn_request: NPCSpawnRequest | None = None,
    ) -> None:
        """
        Initialize spawn result.

        Args:
            success: Whether the spawn was successful
            npc_id: ID of the spawned NPC (if successful)
            npc_instance: NPC instance object (if successful)
            error_message: Error message (if failed)
            spawn_request: Original spawn request
        """
        self.success = success
        self.npc_id = npc_id
        self.npc_instance = npc_instance
        self.error_message = error_message
        self.spawn_request = spawn_request
        self.spawned_at = time.time() if success else None

    @override
    def __repr__(self) -> str:
        """String representation of spawn result."""
        if self.success:
            return f"<NPCSpawnResult(success=True, npc_id={self.npc_id})>"
        return f"<NPCSpawnResult(success=False, error={self.error_message})>"
