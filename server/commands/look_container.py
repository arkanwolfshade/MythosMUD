"""
Container look functionality for MythosMUD.

This module handles looking at containers, including finding containers in rooms
or equipped items, formatting container displays, and handling container look requests.
"""

# pylint: disable=too-many-arguments,too-many-locals,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Container look params; Protocol stubs (PEP 544)

from __future__ import annotations

from collections.abc import Mapping
from typing import NamedTuple, Protocol, TypeVar, cast
from uuid import UUID

from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from .inventory_command_contracts import CommandResponse
from .look_helpers import LookRequest, _get_wearable_container_service

logger = get_logger(__name__)

JsonMap = dict[str, object]
_T = TypeVar("_T")


def _select_match(matching: list[_T], instance_number: int | None) -> _T | None:  # noqa: UP047  # Reason: PEP 695 [T] fails older pylint/Codacy parsers
    """Pick a single match by instance number, or the sole match when unambiguous."""
    if not matching:
        return None
    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching):
            return None
        return matching[instance_number - 1]
    if len(matching) == 1:
        return matching[0]
    return None


class _LookPlayer(Protocol):
    player_id: object

    def get_equipped_items(self) -> dict[str, object]: ...


class _LookRoom(Protocol):
    def get_containers(self) -> list[object]: ...


class _ContainerPersistence(Protocol):
    async def get_container(self, container_id: UUID) -> Mapping[str, object] | None: ...


class _WearableContainer(Protocol):
    container_id: object
    metadata: Mapping[str, object] | None


class _WearableSvc(Protocol):
    async def get_wearable_containers_for_player(self, player_id: UUID) -> list[_WearableContainer]: ...


class _Prototype(Protocol):
    long_description: str | None


class _PrototypeRegistry(Protocol):
    def get(self, prototype_id: object) -> object | None: ...


class ContainerLookArgs(NamedTuple):
    """Arguments for looking at a container."""

    target: str
    target_lower: str
    instance_number: int | None
    room: object
    player: object
    persistence: object
    prototype_registry: object | None
    command_data: Mapping[str, object]
    request: LookRequest | None
    player_name: str


def _as_map(value: object) -> JsonMap:
    if not isinstance(value, dict):
        return {}
    typed = cast(dict[object, object], value)
    return {str(k): v for k, v in typed.items()}


def _as_map_list(value: object) -> list[JsonMap]:
    if not isinstance(value, list):
        return []
    typed = cast(list[object], value)
    return [_as_map(item) for item in typed]


def _as_uuid(value: object) -> UUID | None:
    if isinstance(value, UUID):
        return value
    if isinstance(value, str):
        try:
            return UUID(value)
        except ValueError:
            return None
    return None


def _room_container_maps(room: object) -> list[JsonMap]:
    if not hasattr(room, "get_containers"):
        return []
    return _as_map_list(cast(_LookRoom, room).get_containers())


def _player_equipped(player: object) -> dict[str, object]:
    if not hasattr(player, "get_equipped_items"):
        return {}
    return dict(cast(_LookPlayer, player).get_equipped_items())


def _container_name(container: Mapping[str, object]) -> str:
    meta = _as_map(container.get("metadata"))
    name = meta.get("name")
    if name:
        return str(name)
    cid = str(container.get("container_id", "Unknown"))
    return f"Container {cid[:8]}"


async def _fetch_container(persistence: object, container_id: object) -> JsonMap | None:
    uid = _as_uuid(container_id)
    if uid is None or not hasattr(persistence, "get_container"):
        return None
    raw = await cast(_ContainerPersistence, persistence).get_container(uid)
    if raw is None:
        return None
    return _as_map(raw)


def _find_container_in_room(
    containers: list[JsonMap], target: str, instance_number: int | None = None
) -> JsonMap | None:
    """
    Find a container in room containers by name or container_id.

    Args:
        containers: List of container dictionaries
        target: Container name or container_id to search for
        instance_number: Optional instance number for targeting specific containers

    Returns:
        Matching container dictionary or None if not found
    """
    target_lower = target.lower()
    matching_containers: list[JsonMap] = []

    for container in containers:
        meta = _as_map(container.get("metadata"))
        container_name = str(meta.get("name", container.get("container_id", ""))).lower()
        container_id = str(container.get("container_id", "")).lower()

        if target_lower in container_name or target_lower in container_id:
            matching_containers.append(container)

    return _select_match(matching_containers, instance_number)


def _wearable_matches_target(item: Mapping[str, object], target_lower: str) -> bool:
    item_name = str(item.get("item_name", item.get("name", ""))).lower()
    prototype_id = str(item.get("prototype_id", item.get("item_id", ""))).lower()
    item_id = str(item.get("item_id", "")).lower()
    return target_lower in item_name or target_lower in prototype_id or target_lower in item_id


def _find_container_wearable(
    equipped: Mapping[str, object], target: str, instance_number: int | None = None
) -> tuple[str, JsonMap] | None:
    """
    Find a wearable container in equipped items by name or prototype_id.

    Args:
        equipped: Dictionary of equipped items (slot -> item dict)
        target: Container name or prototype_id to search for
        instance_number: Optional instance number for targeting specific containers

    Returns:
        Tuple of (slot, item_dict) or None if not found
    """
    target_lower = target.lower()
    matching_containers: list[tuple[str, JsonMap]] = []

    for slot, raw_item in equipped.items():
        item = _as_map(raw_item)
        # Name match is what actually selects; inner_container alone never appended.
        if _wearable_matches_target(item, target_lower):
            matching_containers.append((slot, item))

    return _select_match(matching_containers, instance_number)


async def _find_container_via_inner_container(item: Mapping[str, object], persistence: object) -> JsonMap | None:
    """Find container via inner_container_id from item."""
    inner_container_id = item.get("inner_container")
    if not inner_container_id:
        return None
    try:
        return await _fetch_container(persistence, inner_container_id)
    except (ValueError, TypeError):
        return None


def _matches_item_instance_id(item_instance_id: object, container_item_instance_id: object) -> bool:
    """Check if item instance IDs match."""
    return (
        bool(item_instance_id)
        and bool(container_item_instance_id)
        and str(item_instance_id) == str(container_item_instance_id)
    )


def _matches_name_or_slot(container_slot: str, container_item_name: str, slot_lower: str, target_lower: str) -> bool:
    """Check if container matches by name or slot."""
    return container_slot == slot_lower or target_lower in container_item_name or target_lower in container_slot


async def _get_container_data_from_component(
    container_component: _WearableContainer, persistence: object
) -> JsonMap | None:
    """Get container data from component ID."""
    container_id_from_component = container_component.container_id
    if not container_id_from_component:
        return None
    return await _fetch_container(persistence, container_id_from_component)


def _extract_container_metadata(container_component: _WearableContainer) -> JsonMap:
    """Extract metadata from container component."""
    container_metadata = _as_map(getattr(container_component, "metadata", None))
    return {
        "item_name": str(container_metadata.get("item_name", "")).lower(),
        "slot": str(container_metadata.get("slot", "")).lower(),
        "item_instance_id": container_metadata.get("item_instance_id"),
    }


async def _try_match_container_component(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container look requires many parameters for context and matching logic
    container_component: _WearableContainer,
    item_instance_id: object,
    slot_lower: str,
    target_lower: str,
    persistence: object,
    slot: str,
    player_name: str,
) -> JsonMap | None:
    """Try to match a container component and return container data if found."""
    metadata = _extract_container_metadata(container_component)

    if _matches_item_instance_id(item_instance_id, metadata["item_instance_id"]):
        container_data = await _get_container_data_from_component(container_component, persistence)
        if container_data:
            logger.debug(
                "Found container via wearable container service (item_instance_id match) for look command",
                container_id=str(container_component.container_id),
                slot=slot,
                item_instance_id=item_instance_id,
                player=player_name,
            )
            return container_data

    if _matches_name_or_slot(str(metadata["slot"]), str(metadata["item_name"]), slot_lower, target_lower):
        container_data = await _get_container_data_from_component(container_component, persistence)
        if container_data:
            logger.debug(
                "Found container via wearable container service (name match) for look command",
                container_id=str(container_component.container_id),
                slot=slot,
                player=player_name,
            )
            return container_data

    return None


async def _find_container_via_wearable_service(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container look requires many parameters for context and service lookup
    slot: str,
    item: Mapping[str, object],
    target_lower: str,
    player: object,
    persistence: object,
    request: LookRequest | None,
    player_name: str,
) -> JsonMap | None:
    """Find container via wearable container service."""
    if request is None:
        return None
    try:
        wearable_container_service = cast(_WearableSvc, cast(object, _get_wearable_container_service(request)))
        player_id_uuid = UUID(str(cast(_LookPlayer, player).player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)

        slot_lower = slot.lower() if slot else ""
        item_instance_id = item.get("item_instance_id")

        for container_component in wearable_containers:
            container_data = await _try_match_container_component(
                container_component, item_instance_id, slot_lower, target_lower, persistence, slot, player_name
            )
            if container_data:
                return container_data
    except (AttributeError, TypeError, ValueError) as e:
        logger.debug(
            "Error finding container via wearable container service for look command",
            error=str(e),
            slot=slot,
            player=player_name,
        )

    return None


async def _find_container_in_room_or_equipped(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container look requires many parameters for context and container lookup
    target_lower: str,
    instance_number: int | None,
    room: object,
    player: object,
    persistence: object,
    request: LookRequest | None,
    player_name: str,
) -> tuple[JsonMap | None, JsonMap | None]:
    """
    Find container in room or equipped items.

    Returns:
        tuple: (container_found, container_item) - container_item is the equipped item if found
    """
    room_containers = _room_container_maps(room)
    container_found = _find_container_in_room(room_containers, target_lower, instance_number)
    container_item: JsonMap | None = None

    if container_found:
        return (container_found, container_item)

    equipped = _player_equipped(player)
    wearable_result = _find_container_wearable(equipped, target_lower, instance_number)
    if not wearable_result:
        return (None, None)

    slot, item = wearable_result
    container_item = item

    container_found = await _find_container_via_inner_container(item, persistence)
    if container_found:
        return (container_found, container_item)

    container_found = await _find_container_via_wearable_service(
        slot, item, target_lower, player, persistence, request, player_name
    )
    return (container_found, container_item)


def _get_container_description(
    container_found: Mapping[str, object],
    container_item: Mapping[str, object] | None,
    prototype_registry: object | None,
) -> str | None:
    """Get container description from prototype registry."""
    if container_item:
        prototype_id = container_item.get("prototype_id") or container_item.get("item_id")
    else:
        meta = _as_map(container_found.get("metadata"))
        prototype_id = meta.get("prototype_id") or container_found.get("prototype_id")

    if prototype_registry is None or not prototype_id:
        return None

    registry = cast(_PrototypeRegistry, prototype_registry)
    try:
        prototype = registry.get(prototype_id)
        if prototype is not None and hasattr(prototype, "long_description"):
            return cast(_Prototype, prototype).long_description
    except (AttributeError, TypeError, KeyError):
        logger.debug("Failed to get prototype for container", prototype_id=prototype_id)

    return None


def _format_container_contents(items: list[JsonMap]) -> list[str]:
    """Format container contents as list of lines."""
    lines: list[str] = []
    if items:
        for idx, item_stack in enumerate(items, start=1):
            item_name = str(item_stack.get("item_name", item_stack.get("name", "Unknown Item")))
            quantity = coerce_int(item_stack.get("quantity", 1), default=1)
            if quantity > 1:
                lines.append(f"  {idx}. {item_name} x{quantity}")
            else:
                lines.append(f"  {idx}. {item_name}")
    else:
        lines.append("  (empty)")
    return lines


def _format_container_display(
    container_found: Mapping[str, object],
    container_description: str | None,
    command_data: Mapping[str, object],
) -> str:
    """Format the complete container display text."""
    container_name = _container_name(container_found)
    items = _as_map_list(container_found.get("items", []))
    capacity_slots = coerce_int(container_found.get("capacity_slots", 0), default=0)
    lock_state = str(container_found.get("lock_state", "unlocked"))

    lines = [container_name]

    if container_description:
        lines.append(container_description)

    if lock_state == "locked":
        lines.append("Locked")
    elif lock_state == "sealed":
        lines.append("Sealed")

    used_slots = len(items)
    lines.append(f"Capacity: {used_slots}/{capacity_slots} slots")

    if command_data.get("look_in", False) or command_data.get("target_type") == "container":
        lines.append("Contents:")
        lines.extend(_format_container_contents(items))

    return "\n".join(lines)


async def _handle_container_look(args: ContainerLookArgs) -> CommandResponse | None:
    """Handle looking at a specific container."""
    logger.debug(
        "Looking at container",
        player=args.player_name,
        target=args.target,
        look_in=args.command_data.get("look_in", False),
    )

    container_found, container_item = await _find_container_in_room_or_equipped(
        args.target_lower,
        args.instance_number,
        args.room,
        args.player,
        args.persistence,
        args.request,
        args.player_name,
    )

    if not container_found:
        logger.debug("Container not found", player=args.player_name, target=args.target)
        return {"result": f"You don't see any '{args.target}' here."}

    container_description = _get_container_description(container_found, container_item, args.prototype_registry)
    result_text = _format_container_display(container_found, container_description, args.command_data)

    container_name = _container_name(container_found)
    logger.debug("Container look completed", player=args.player_name, target=args.target, container_name=container_name)
    return {"result": result_text}


async def _try_lookup_container_implicit(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Container look requires many parameters for context and container lookup
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: object,
    player: object,
    persistence: object,
    player_name: str,
) -> CommandResponse | None:
    """Try to find and display a container in implicit lookup."""
    room_containers = _room_container_maps(room)
    container_found = _find_container_in_room(room_containers, target_lower, instance_number)

    if not container_found:
        equipped = _player_equipped(player)
        wearable_result = _find_container_wearable(equipped, target_lower, instance_number)
        if wearable_result:
            _slot, item = wearable_result
            inner_container_id = item.get("inner_container")
            if inner_container_id:
                container_data = await _fetch_container(persistence, inner_container_id)
                if container_data:
                    container_found = container_data

    if not container_found:
        return None

    container_name = _container_name(container_found)
    items = _as_map_list(container_found.get("items", []))
    capacity_slots = coerce_int(container_found.get("capacity_slots", 0), default=0)
    lock_state = str(container_found.get("lock_state", "unlocked"))

    lines = [container_name]
    if lock_state == "locked":
        lines.append("Locked")
    elif lock_state == "sealed":
        lines.append("Sealed")
    lines.append(f"Capacity: {len(items)}/{capacity_slots} slots")

    result_text = "\n".join(lines)
    logger.debug("Container look completed", player=player_name, target=target, container_name=container_name)
    return {"result": result_text}


__all__ = [
    "_find_container_in_room",
    "_find_container_wearable",
    "_find_container_via_inner_container",
    "_find_container_in_room_or_equipped",
    "_get_container_description",
    "_format_container_contents",
    "_format_container_display",
    "_handle_container_look",
    "_try_lookup_container_implicit",
]
