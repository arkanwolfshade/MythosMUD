"""
InstanceManager for MythosMUD.

Manages instanced rooms: creates, stores, and destroys instances cloned from
room templates. Used for the new-character tutorial and future instanced content.

As noted in the Pnakotic Manuscripts, dimensional pockets require careful
management lest they leak into the waking world.
"""

from __future__ import annotations

import threading
import uuid
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, cast

from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..events import EventBus

logger = get_logger(__name__)

# Default fixed exit room when not specified in template
DEFAULT_EXIT_ROOM_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


@dataclass
class Instance:
    """An instanced set of rooms, unique per player or group."""

    instance_id: str
    template_id: str
    owner_player_id: str
    rooms: dict[str, Room] = field(default_factory=dict)


class InstanceManager:
    """
    Manages instanced rooms: create from templates, destroy, and lookup.

    Instance room IDs: instance_{instance_uuid}_{template_stable_id}
    """

    def __init__(self, room_cache: dict[str, Room], event_bus: EventBus | None = None) -> None:
        """
        Initialize the instance manager.

        Args:
            room_cache: Shared room cache (from persistence) for template lookup
            event_bus: Optional EventBus for Room creation
        """
        self._room_cache = room_cache
        self._event_bus = event_bus
        self._instances: dict[str, Instance] = {}
        self._lock = threading.RLock()
        self._logger = get_logger(__name__)

    def create_instance(
        self,
        template_id: str,
        owner_player_id: uuid.UUID | str,
        group_ids: set[str] | None = None,
    ) -> Instance:
        """
        Create an instance from room templates with the given template_id.

        Args:
            template_id: Value of instance_template_id in room attributes (e.g. tutorial_sanitarium)
            owner_player_id: Owner of the instance (for per-player instancing)
            group_ids: Optional set of player IDs for group instancing (reserved for future use)

        Returns:
            Instance: The created instance with cloned rooms and remapped exits

        Raises:
            ValueError: If no template rooms found for template_id
        """
        _ = group_ids  # Reserved for future group instancing
        instance_uuid = uuid.uuid4()
        instance_id = f"instance_{instance_uuid}"

        with self._lock:
            templates = [
                r
                for r in self._room_cache.values()
                if getattr(r, "attributes", {}).get("instance_template_id") == template_id
            ]
            if not templates:
                self._logger.error("No template rooms found", template_id=template_id)
                raise ValueError(f"No template rooms found for template_id={template_id!r}")

            template_stable_ids = {self._stable_id_from_room(r) for r in templates}

            rooms: dict[str, Room] = {}
            owner_str = str(owner_player_id)

            for template_room in templates:
                stable_id = self._stable_id_from_room(template_room)
                instance_room_id = f"{instance_id}_{stable_id}"
                remapped_exits = self._remap_exits(
                    template_room.exits,
                    instance_id,
                    template_stable_ids,
                    template_room.attributes.get("instance_exit_room_id", DEFAULT_EXIT_ROOM_ID),
                )
                room_data = {
                    "id": instance_room_id,
                    "name": template_room.name,
                    "description": template_room.description,
                    "plane": template_room.plane,
                    "zone": template_room.zone,
                    "sub_zone": template_room.sub_zone,
                    "resolved_environment": getattr(template_room, "environment", "outdoors"),
                    "exits": remapped_exits,
                    "attributes": dict(getattr(template_room, "attributes", {}) or {}),
                }
                room = Room(room_data, self._event_bus)
                rooms[instance_room_id] = room

            instance = Instance(
                instance_id=instance_id,
                template_id=template_id,
                owner_player_id=owner_str,
                rooms=rooms,
            )
            self._instances[instance_id] = instance
            self._logger.info(
                "Instance created",
                instance_id=instance_id,
                template_id=template_id,
                room_count=len(rooms),
            )
            return instance

    def _stable_id_from_room(self, room: Room) -> str:
        """Extract stable_id from room - use room.id if it looks like a full path."""
        rid = cast(str, room.id)
        if "_" in rid and len(rid) > 20:
            return rid
        # Fallback: room.id might be stable_id format
        return rid

    def _remap_exits(
        self,
        exits: dict[str, str],
        instance_id: str,
        template_stable_ids: set[str],
        exit_room_id: str,
    ) -> dict[str, str]:
        """
        Remap exit targets: same-instance rooms use instance IDs, outside exits use fixed exit.
        """
        remapped = {}
        for direction, target_room_id in (exits or {}).items():
            if not target_room_id:
                continue
            target_stable = self._stable_id_from_target(target_room_id)
            if target_stable and target_stable in template_stable_ids:
                remapped[direction] = f"{instance_id}_{target_stable}"
            else:
                remapped[direction] = exit_room_id
        return remapped

    def _stable_id_from_target(self, target_room_id: str) -> str | None:
        """Extract stable_id from a room ID (may be full path or short form)."""
        if not target_room_id:
            return None
        return target_room_id

    def get_instance(self, instance_id: str) -> Instance | None:
        """Return the instance if it exists."""
        with self._lock:
            return self._instances.get(instance_id)

    def destroy_instance(self, instance_id: str) -> None:
        """Remove the instance from the store."""
        with self._lock:
            if instance_id in self._instances:
                del self._instances[instance_id]
                self._logger.info("Instance destroyed", instance_id=instance_id)

    def get_first_room_id(self, instance_id: str) -> str | None:
        """
        Return the first room ID of the instance (for spawn placement).

        Order is undefined but stable for a given instance.
        """
        with self._lock:
            instance = self._instances.get(instance_id)
            if not instance or not instance.rooms:
                return None
            return next(iter(instance.rooms), None)

    def get_exit_room_id(self, instance_id: str) -> str:
        """Return the fixed exit room ID for this instance (e.g. Main Foyer)."""
        with self._lock:
            instance = self._instances.get(instance_id)
            if not instance or not instance.rooms:
                return DEFAULT_EXIT_ROOM_ID
            first_room = next(iter(instance.rooms.values()), None)
            if first_room:
                exit_id = getattr(first_room, "attributes", {}).get("instance_exit_room_id")
                if exit_id:
                    return str(exit_id)
            return DEFAULT_EXIT_ROOM_ID

    def get_room_by_id(self, room_id: str) -> Room | None:
        """
        Look up a room by ID, checking instances first.

        Used by persistence layer for instance-first room lookup.
        """
        if not room_id or not room_id.startswith("instance_"):
            return None
        parts = room_id.split("_", 2)
        if len(parts) < 3:
            return None
        instance_id = f"{parts[0]}_{parts[1]}"
        with self._lock:
            instance = self._instances.get(instance_id)
            if instance:
                return instance.rooms.get(room_id)
        return None
