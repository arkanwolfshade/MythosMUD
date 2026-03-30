"""Lookups for wearable containers, room containers, and inventory items."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import cast
from uuid import UUID

from ..models.player import Player
from .container_helpers_inventory_logging import logger
from .inventory_service_helpers import get_shared_services


def find_item_in_inventory(
    inventory: Sequence[Mapping[str, object]], item_name: str
) -> tuple[dict[str, object] | None, int | None]:
    """Find an item in inventory by name or index."""
    try:
        index = int(item_name)
        if 1 <= index <= len(inventory):
            item_index = index - 1
            return cast(dict[str, object], inventory[item_index]), item_index
    except ValueError:
        pass

    target_lower = item_name.lower()
    for idx, item in enumerate(inventory):
        item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
        if target_lower in item_name_check:
            return cast(dict[str, object], item), idx

    return None, None


def check_item_matches_target(item: Mapping[str, object], slot: str, target_lower: str) -> tuple[bool, bool]:
    """Check if item matches target. Returns (name_matches, slot_matches)."""
    item_name_check = str(item.get("item_name", item.get("name", ""))).lower()
    slot_lower = slot.lower()
    name_matches = target_lower in item_name_check
    slot_matches = target_lower == slot_lower or target_lower in slot_lower
    return name_matches, slot_matches


def _component_metadata(component: object) -> dict[str, object]:
    meta = getattr(component, "metadata", None)
    return cast(dict[str, object], meta) if isinstance(meta, dict) else {}


def _container_uuid(raw_id: object) -> UUID:
    """Normalize persistence / component ids to UUID."""
    return raw_id if isinstance(raw_id, UUID) else UUID(str(raw_id))


def _wearable_put_metadata_matches(metadata: dict[str, object], slot_lower: str, target_lower: str) -> bool:
    name_l = str(metadata.get("name", "")).lower()
    slot_l = str(metadata.get("slot", "")).lower()
    return slot_l == slot_lower or target_lower in name_l


def _wearable_get_name_slot_matches(metadata: dict[str, object], slot_lower: str, target_lower: str) -> bool:
    item_l = str(metadata.get("item_name", "")).lower()
    slot_l = str(metadata.get("slot", "")).lower()
    return slot_l == slot_lower or target_lower in item_l or target_lower in slot_l


def _instance_id_matches_metadata(metadata: dict[str, object], item_instance_id: object) -> bool:
    cii = metadata.get("item_instance_id")
    return bool(cii) and str(item_instance_id) == str(cii)


def _resolve_inner_uuid(inner: object) -> UUID | None:
    try:
        cid = UUID(inner) if isinstance(inner, str) else inner
        return cid if isinstance(cid, UUID) else UUID(str(inner))
    except (ValueError, TypeError):
        return None


def _get_container_pair(persistence: object, raw_id: object) -> tuple[dict[str, object], UUID] | None:
    get_container = getattr(persistence, "get_container", None)
    if not raw_id or not callable(get_container):
        return None
    uid = _container_uuid(raw_id)
    data = get_container(uid)
    if not data:
        return None
    return cast(dict[str, object], data), uid


async def try_inner_container(
    persistence: object, item: Mapping[str, object]
) -> tuple[dict[str, object] | None, UUID | None]:
    """Try to get container from inner_container. Returns (container_data, container_id)."""
    inner_container_id = item.get("inner_container")
    if not inner_container_id:
        return None, None
    uid = _resolve_inner_uuid(inner_container_id)
    if uid is None:
        return None, None
    pair = _get_container_pair(persistence, uid)
    return (pair[0], pair[1]) if pair else (None, None)


async def try_wearable_container_service(
    persistence: object, request: object, player: Player, slot: str, target_lower: str
) -> tuple[dict[str, object] | None, UUID | None]:
    """Try to find container via wearable container service. Returns (container_data, container_id)."""
    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)
        slot_lower = slot.lower()
        for container_component in wearable_containers:
            meta = _component_metadata(container_component)
            if not _wearable_put_metadata_matches(meta, slot_lower, target_lower):
                continue
            raw_id: object | None = cast(object | None, getattr(container_component, "container_id", None))
            if not raw_id:
                continue
            pair = _get_container_pair(persistence, raw_id)
            if pair:
                return pair
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container lookup errors unpredictable
        logger.debug("Error finding container via wearable container service", error=str(e), player=player.name)

    return None, None


def _container_from_equip_dict(
    persistence: object, container_result: dict[str, object]
) -> tuple[dict[str, object], UUID] | None:
    raw = container_result.get("container_id")
    return _get_container_pair(persistence, raw) if raw else None


def _fallback_create_equipment_container(
    persistence: object, player_id_uuid: UUID, slot: str, item: Mapping[str, object]
) -> tuple[dict[str, object], UUID] | None:
    item_name = item.get("item_name", item.get("name", "Unknown"))
    create_container = getattr(persistence, "create_container", None)
    if not callable(create_container):
        return None
    created = create_container(
        source_type="equipment",
        entity_id=player_id_uuid,
        capacity_slots=20,
        metadata_json={"name": item_name, "slot": slot, "item_id": item.get("item_id")},
    )
    if not created or not isinstance(created, dict):
        return None
    created_dict = cast(dict[str, object], created)
    cid_raw: object | None = created_dict.get("container_id")
    if not cid_raw:
        return None
    return created_dict, _container_uuid(cid_raw)


async def create_wearable_container(
    persistence: object, request: object, player: Player, slot: str, item: Mapping[str, object]
) -> tuple[dict[str, object] | None, UUID | None]:
    """Create a wearable container for an equipped item."""
    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        equip_out = await wearable_container_service.handle_equip_wearable_container(
            player_id=player_id_uuid,
            item_stack=dict(item),
        )
        if isinstance(equip_out, dict):
            from_equip = _container_from_equip_dict(persistence, equip_out)
            if from_equip:
                return from_equip
        return _fallback_create_equipment_container(persistence, player_id_uuid, slot, item) or (None, None)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container creation errors unpredictable
        logger.debug("Failed to create container for equipped item", error=str(e), player=player.name)

    return None, None


async def _try_put_container_for_equipped_item(
    persistence: object,
    request: object,
    player: Player,
    slot: str,
    item_map: dict[str, object],
    target_lower: str,
) -> tuple[dict[str, object], UUID | None] | None:
    """Resolve container for put for one equipped slot; returns None if this slot is not a match."""
    name_matches, slot_matches = check_item_matches_target(item_map, slot, target_lower)
    if not (name_matches or slot_matches):
        return None

    container_data, container_id = await try_inner_container(persistence, item_map)
    if container_data:
        return container_data, container_id

    container_data, container_id = await try_wearable_container_service(
        persistence, request, player, slot, target_lower
    )
    if container_data:
        return container_data, container_id

    if slot_matches:
        container_found, container_id = await create_wearable_container(persistence, request, player, slot, item_map)
        if container_found:
            return container_found, container_id
    return None


async def find_wearable_container_for_put(
    persistence: object,
    request: object,
    player: Player,
    container_name: str,
) -> tuple[dict[str, object] | None, UUID | None]:
    """Find a wearable container for put command, creating if necessary."""
    equipped = player.get_equipped_items()
    target_lower = container_name.lower()
    equipped_map = cast(Mapping[str, object], equipped)

    for slot, item_raw in equipped_map.items():
        if not isinstance(item_raw, dict):
            continue
        item_map = cast(dict[str, object], item_raw)
        found = await _try_put_container_for_equipped_item(persistence, request, player, slot, item_map, target_lower)
        if found:
            return found

    return None, None


def find_container_in_room(
    room_manager: object, room_id: str, container_name: str
) -> tuple[dict[str, object] | None, UUID | None]:
    """Find a container in the room by name."""
    get_containers = getattr(room_manager, "get_containers", None)
    if callable(get_containers):
        room_containers_raw: object = get_containers(room_id)
    else:
        room_containers_raw = []
    room_containers: list[object]
    if isinstance(room_containers_raw, list):
        room_containers = list(cast(list[object], room_containers_raw))
    else:
        room_containers = []
    target_lower = container_name.lower()

    for container in room_containers:
        if not isinstance(container, dict):
            continue
        c = cast(dict[str, object], container)
        meta = c.get("metadata")
        meta_map = cast(dict[str, object], meta) if isinstance(meta, dict) else {}
        name_part = str(meta_map.get("name", c.get("container_id", ""))).lower()
        if target_lower in name_part:
            raw_id = c.get("container_id")
            return c, UUID(str(raw_id))

    return None, None


def find_matching_equipped_containers(
    equipped: Mapping[str, object], container_name: str
) -> list[tuple[str, dict[str, object]]]:
    """Find equipped items that match container name."""
    target_lower = container_name.lower()
    matching_containers: list[tuple[str, dict[str, object]]] = []

    for slot, item in equipped.items():
        if not isinstance(item, dict):
            continue
        item_map = cast(dict[str, object], item)
        equipped_item_name = str(item_map.get("item_name", item_map.get("name", ""))).lower()
        prototype_id = str(item_map.get("prototype_id", item_map.get("item_id", ""))).lower()
        item_id = str(item_map.get("item_id", "")).lower()
        name_matches = target_lower in equipped_item_name or target_lower in prototype_id or target_lower in item_id

        if item_map.get("inner_container") or name_matches:
            if name_matches:
                matching_containers.append((slot, item_map))

    return matching_containers


def try_inner_container_by_id(
    persistence: object, inner_container_id: object, slot: str, player_name: str
) -> tuple[dict[str, object] | None, UUID | None]:
    """Try to get container via inner_container_id."""
    if not inner_container_id:
        return None, None
    uid = _resolve_inner_uuid(inner_container_id)
    if uid is None:
        return None, None
    pair = _get_container_pair(persistence, uid)
    if not pair:
        return None, None
    logger.debug(
        "Found container via inner_container for get command",
        container_id=str(uid),
        slot=slot,
        player=player_name,
    )
    return pair


async def try_wearable_container_service_by_instance_id(
    persistence: object,
    wearable_containers: Sequence[object],
    item_instance_id: object,
    player_name: str,
) -> tuple[dict[str, object] | None, UUID | None]:
    """Try to find container via wearable container service using item_instance_id match."""
    if not item_instance_id:
        return None, None

    for container_component in wearable_containers:
        meta = _component_metadata(container_component)
        if not _instance_id_matches_metadata(meta, item_instance_id):
            continue
        raw_id: object | None = cast(object | None, getattr(container_component, "container_id", None))
        if not raw_id:
            continue
        pair = _get_container_pair(persistence, raw_id)
        if pair:
            logger.debug(
                "Found container via wearable container service (item_instance_id match) for get command",
                container_id=str(pair[1]),
                item_instance_id=item_instance_id,
                player=player_name,
            )
            return pair
    return None, None


async def try_wearable_container_service_by_name(
    persistence: object,
    wearable_containers: Sequence[object],
    slot: str,
    target_lower: str,
    player_name: str,
) -> tuple[dict[str, object] | None, UUID | None]:
    """Try to find container via wearable container service using name/slot match."""
    slot_lower = slot.lower() if slot else ""
    for container_component in wearable_containers:
        meta = _component_metadata(container_component)
        if not _wearable_get_name_slot_matches(meta, slot_lower, target_lower):
            continue
        raw_id: object | None = cast(object | None, getattr(container_component, "container_id", None))
        if not raw_id:
            continue
        pair = _get_container_pair(persistence, raw_id)
        if pair:
            logger.debug(
                "Found container via wearable container service (name/slot match) for get command",
                container_id=str(pair[1]),
                container_name=str(meta.get("item_name", "")).lower(),
                slot=slot,
                player=player_name,
            )
            return pair
    return None, None


async def find_wearable_container(
    persistence: object,
    request: object,
    player: Player,
    container_name: str,
) -> tuple[dict[str, object] | None, UUID | None]:
    """Find a wearable container by name."""
    equipped = player.get_equipped_items()
    matching_containers = find_matching_equipped_containers(cast(Mapping[str, object], equipped), container_name)

    if not matching_containers:
        return None, None

    slot, item = matching_containers[0]
    item_instance_id = item.get("item_instance_id")
    inner_container_id = item.get("inner_container")
    target_lower = container_name.lower()

    container_data, container_id = try_inner_container_by_id(persistence, inner_container_id, slot, player.name)
    if container_data:
        return container_data, container_id

    try:
        _, wearable_container_service, _ = get_shared_services(request)
        player_id_uuid = UUID(str(player.player_id))
        wearable_containers = await wearable_container_service.get_wearable_containers_for_player(player_id_uuid)

        container_data, container_id = await try_wearable_container_service_by_instance_id(
            persistence, wearable_containers, item_instance_id, player.name
        )
        if container_data:
            return container_data, container_id

        container_data, container_id = await try_wearable_container_service_by_name(
            persistence, wearable_containers, slot, target_lower, player.name
        )
        if container_data:
            return container_data, container_id
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container lookup errors unpredictable, fallback available
        logger.debug(
            "Error finding container via wearable container service for get command",
            error=str(e),
            player=player.name,
        )

    return None, None
