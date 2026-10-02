"""
Room furniture: fixtures declared on rooms, instantiated as environment containers at startup.

World data declares furniture per room:

    rooms.attributes.furniture = [{"prototype_id": "furniture.sanitarium.lost_and_found_chest",
                                   "role": "lost_and_found"}]

Each entry becomes one environment container in that room, sized by the prototype's
``metadata.container`` and named after the prototype. Startup matches existing containers by
(room_id, prototype_id): missing ones are created, existing ones get their name and capacity
refreshed from the prototype (the prototype is the source of truth), and their items are never
touched. Template rooms are skipped -- furniture inside instances needs per-instance containers.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol, cast
from uuid import UUID

from pydantic import ValidationError as PydanticValidationError
from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError, ValidationError
from ..game.instance_manager import is_template_room
from ..game.items.item_factory import ItemFactory
from ..game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from ..models.room import Room
from ..persistence.container_create_params import ContainerCreateParams
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

ENVIRONMENT_SOURCE_TYPE = "environment"


class FurniturePersistence(Protocol):
    """The slice of AsyncPersistenceLayer the furniture loader needs."""

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        """All container rows in a room."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    async def create_container(
        self, source_type: str, params: ContainerCreateParams | None = None
    ) -> dict[str, object]:
        """Create a container row."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type

    async def update_container(
        self,
        container_id: UUID,
        items_json: list[dict[str, object]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, object] | None = None,
        capacity_slots: int | None = None,
    ) -> dict[str, object] | None:
        """Update a container; capacity_slots resizes it. None if the container is gone."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


class FurnitureStartupPersistence(FurniturePersistence, Protocol):
    """FurniturePersistence plus the room cache, for the startup hook."""

    async def warmup_room_cache(self) -> None:
        """Load the room cache if it is not loaded yet."""

    def list_rooms(self) -> list[Room]:
        """All cached rooms."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


def _furniture_entries(room_id: str, attributes: dict[str, object]) -> list[tuple[str, str | None]]:
    """(prototype_id, role) pairs from room attributes["furniture"]; malformed entries are skipped."""
    raw = attributes.get("furniture")
    if raw is None:
        return []
    if not isinstance(raw, list):
        logger.warning("Room furniture must be a list; ignored", room_id=room_id)
        return []
    entries: list[tuple[str, str | None]] = []
    for item in cast(list[object], raw):
        entry = _as_entry(item)
        prototype_id = entry.get("prototype_id")
        role = entry.get("role")
        if not isinstance(prototype_id, str) or not prototype_id or not isinstance(role, str | None):
            logger.warning("Malformed room furniture entry ignored", room_id=room_id, entry=repr(item))
            continue
        entries.append((prototype_id, role))
    return entries


def _as_entry(item: object) -> dict[str, object]:
    # Narrowing happens here, not in the caller's loop, so `item` stays `object` there
    # (narrowed in place it became dict[Unknown, Unknown] for basedpyright).
    return cast(dict[str, object], item) if isinstance(item, dict) else {}


def _container_metadata(container: dict[str, object]) -> dict[str, object]:
    raw = container.get("metadata_json")
    return cast(dict[str, object], raw) if isinstance(raw, dict) else {}


def _furniture_containers(containers: list[dict[str, object]]) -> dict[str, dict[str, object]]:
    """Environment containers in a room that came from furniture, keyed by prototype_id."""
    by_prototype: dict[str, dict[str, object]] = {}
    for container in containers:
        prototype_id = _container_metadata(container).get("prototype_id")
        if container.get("source_type") == ENVIRONMENT_SOURCE_TYPE and isinstance(prototype_id, str):
            _ = by_prototype.setdefault(prototype_id, container)
    return by_prototype


def _furniture_spec(prototype_id: str, registry: PrototypeRegistry) -> tuple[str, dict[str, object]] | None:
    """(display name, inner_container spec) for a furniture prototype, or None if unusable."""
    try:
        prototype = registry.get(prototype_id)
    except PrototypeRegistryError:
        logger.warning("Room furniture prototype not found", prototype_id=prototype_id)
        return None
    try:
        spec = ItemFactory.build_inner_container(prototype.metadata)
    except PydanticValidationError as e:
        logger.warning(
            "Room furniture prototype has an invalid metadata.container", prototype_id=prototype_id, error=str(e)
        )
        return None
    if spec is None:
        logger.warning("Room furniture prototype has no metadata.container", prototype_id=prototype_id)
        return None
    return prototype.name, spec


async def _refresh_container(
    persistence: FurniturePersistence, existing: dict[str, object], metadata: dict[str, object], capacity: int
) -> None:
    """Bring an existing furniture container's name/capacity in line with its prototype (items untouched)."""
    old_metadata = _container_metadata(existing)
    new_metadata = {**old_metadata, **metadata}
    capacity_changed = existing.get("capacity_slots") != capacity
    if not capacity_changed and new_metadata == old_metadata:
        return
    _ = await persistence.update_container(
        UUID(str(existing["container_id"])),
        metadata_json=new_metadata,
        capacity_slots=capacity if capacity_changed else None,
    )
    logger.info("Room furniture container refreshed from prototype", metadata=new_metadata, capacity_slots=capacity)


async def _sync_entry(  # pylint: disable=too-many-arguments  # Reason: one furniture entry needs its room, declaration, existing row, and both collaborators
    room_id: str,
    prototype_id: str,
    role: str | None,
    existing: dict[str, object] | None,
    registry: PrototypeRegistry,
    persistence: FurniturePersistence,
) -> bool:
    """Create or refresh one furniture container. Returns True if it now exists."""
    found = _furniture_spec(prototype_id, registry)
    if found is None:
        return False
    name, spec = found
    capacity = cast(int, spec["capacity_slots"])
    metadata: dict[str, object] = {"name": name, "prototype_id": prototype_id, "role": role}
    if existing is not None:
        await _refresh_container(persistence, existing, metadata, capacity)
        return True
    _ = await persistence.create_container(
        ENVIRONMENT_SOURCE_TYPE,
        ContainerCreateParams(
            room_id=room_id,
            capacity_slots=capacity,
            lock_state=str(spec["lock_state"]),
            allowed_roles=cast(list[str], spec["allowed_roles"]),
            metadata_json=metadata,
        ),
    )
    logger.info("Room furniture container created", room_id=room_id, prototype_id=prototype_id)
    return True


async def sync_room_furniture(
    rooms: Iterable[Room], registry: PrototypeRegistry, persistence: FurniturePersistence
) -> int:
    """Ensure every room's declared furniture has its environment container. Returns the count."""
    synced = 0
    for room in rooms:
        room_id = cast(str, room.id)
        entries = _furniture_entries(room_id, cast(dict[str, object], room.attributes))
        if not entries:
            continue
        if is_template_room(room):
            logger.warning("Furniture on an instance template room is not supported; ignored", room_id=room_id)
            continue
        existing = _furniture_containers(await persistence.get_containers_by_room_id(room_id))
        declared = {prototype_id for prototype_id, _ in entries}
        for prototype_id, role in entries:
            if await _sync_entry(room_id, prototype_id, role, existing.get(prototype_id), registry, persistence):
                synced += 1
        # Rows are kept (they may hold items); undeclared ones only get a warning.
        # ponytail: only rooms that still declare some furniture are checked for orphans; finding
        # orphans in rooms whose furniture list was removed entirely needs a scan of all
        # environment containers (no procedure for that yet).
        for orphan_id in existing.keys() - declared:
            logger.warning(
                "Furniture container no longer declared by its room", room_id=room_id, prototype_id=orphan_id
            )
    logger.info("Room furniture synced", container_count=synced)
    return synced


async def initialize_room_furniture(persistence: FurnitureStartupPersistence | None, registry: object) -> None:
    """Startup hook: sync furniture for every cached room. Never fails startup over a fixture."""
    if persistence is None or not isinstance(registry, PrototypeRegistry):
        logger.warning("Room furniture skipped: persistence or item prototype registry unavailable")
        return
    try:
        await persistence.warmup_room_cache()
        _ = await sync_room_furniture(persistence.list_rooms(), registry, persistence)
    except (DatabaseError, ValidationError, SQLAlchemyError) as e:
        logger.error("Room furniture sync failed; continuing startup", error=str(e))
