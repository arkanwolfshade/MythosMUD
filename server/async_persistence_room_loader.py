"""
Room cache loading for async persistence layer.

Extracted from async_persistence.py to satisfy file-nloc limit.
Loads rooms from PostgreSQL via get_rooms_with_exits() and builds in-memory Room cache.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, TypedDict, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from structlog.stdlib import BoundLogger

from .database import get_async_session
from .events import EventBus
from .exceptions import DatabaseError

if TYPE_CHECKING:
    from .models.room import Room


class ExitJsonEntry(TypedDict, total=False):
    """One exit entry from get_rooms_with_exits exits JSON."""

    direction: str
    to_room_stable_id: str
    to_subzone_stable_id: str
    to_zone_stable_id: str


class ProcessedRoomData(TypedDict):
    """Intermediate room row after zone/id normalization."""

    room_id: str
    stable_id: str | None
    name: str | None
    description: str | None
    attributes: object
    plane: str
    zone: str
    sub_zone: str | None


class RoomLoadResult(TypedDict):
    """Mutable container passed through room object construction."""

    rooms: dict[str, Room]


class RoomInitPayload(TypedDict, total=False):
    """Payload passed to Room.__init__ during cache load."""

    id: str
    name: str | None
    description: str | None
    plane: str
    zone: str
    sub_zone: str | None
    resolved_environment: str
    exits: dict[str, str]
    attributes: dict[str, object]


def _row_optional_str(row: dict[str, object], key: str) -> str | None:
    value = row.get(key)
    return value if isinstance(value, str) else None


def _attributes_from_row(row: dict[str, object]) -> dict[str, object]:
    raw = row.get("attributes")
    if isinstance(raw, dict):
        return cast(dict[str, object], raw)
    return {}


def _coerce_exit_entries(raw: object) -> list[ExitJsonEntry]:
    if not isinstance(raw, list):
        return []
    entries: list[ExitJsonEntry] = []
    for item in cast(list[object], raw):
        if not isinstance(item, dict):
            continue
        item_dict = cast(dict[str, object], item)
        entry: ExitJsonEntry = {}
        direction = item_dict.get("direction")
        if isinstance(direction, str):
            entry["direction"] = direction
        to_room_stable_id = item_dict.get("to_room_stable_id")
        if isinstance(to_room_stable_id, str):
            entry["to_room_stable_id"] = to_room_stable_id
        to_subzone_stable_id = item_dict.get("to_subzone_stable_id")
        if isinstance(to_subzone_stable_id, str):
            entry["to_subzone_stable_id"] = to_subzone_stable_id
        to_zone_stable_id = item_dict.get("to_zone_stable_id")
        if isinstance(to_zone_stable_id, str):
            entry["to_zone_stable_id"] = to_zone_stable_id
        entries.append(entry)
    return entries


class RoomCacheLoader:
    """
    Loads room data from the database and populates a room cache dict.

    Used by AsyncPersistenceLayer for lazy room cache loading.
    """

    def __init__(
        self,
        room_cache: dict[str, Room],
        room_mappings: dict[str, object],
        logger: BoundLogger,
        event_bus: EventBus | None,
    ) -> None:
        self._room_cache: dict[str, Room] = room_cache
        self._room_mappings: dict[str, object] = room_mappings
        self._logger: BoundLogger = logger
        self._event_bus: EventBus | None = event_bus

    async def load(self) -> None:
        """Load rooms from PostgreSQL and update the room cache."""
        async for session in get_async_session():
            try:
                combined_rows = await self._query_rooms_with_exits_async(session)
                room_data_list, exits_by_room = self._process_combined_rows(combined_rows)
                result_container: RoomLoadResult = {"rooms": {}}
                self._build_room_objects(room_data_list, exits_by_room, result_container)
                self._apply_rooms_to_cache(result_container["rooms"])
                self._log_room_cache_after_load()
            except (DatabaseError, OSError, RuntimeError, ConnectionError, TimeoutError, SQLAlchemyError) as e:
                self._handle_room_load_error(e)
            break

    def _apply_rooms_to_cache(self, rooms: dict[str, Room] | None) -> None:
        if rooms is not None:
            self._room_cache.clear()
            self._room_cache.update(rooms)
        else:
            self._room_cache.clear()

    def _log_room_cache_after_load(self) -> None:
        self._logger.info(
            "Loaded rooms into cache from PostgreSQL database",
            room_count=len(self._room_cache),
            mapping_count=len(self._room_mappings),
        )
        if not self._room_cache:
            self._logger.warning(
                "Room cache is empty after load - player room validation will treat all rooms as invalid",
                room_count=0,
            )
        else:
            sample_room_ids = list(self._room_cache.keys())[:5]
            self._logger.debug("Sample room IDs loaded", sample_room_ids=sample_room_ids)

    def _handle_room_load_error(self, e: BaseException) -> None:
        error_msg = str(e).lower()
        if "does not exist" in error_msg or "relation" in error_msg:
            self._room_cache.clear()
            self._logger.warning(
                "Room tables not found or empty, initializing with empty cache",
                error=str(e),
            )
        else:
            raise e

    async def _query_rooms_with_exits_async(self, session: AsyncSession) -> list[dict[str, object]]:
        try:
            result = await session.execute(
                text(
                    """
                    SELECT
                        room_uuid,
                        stable_id,
                        name,
                        description,
                        attributes,
                        subzone_stable_id,
                        zone_stable_id,
                        plane,
                        zone,
                        exits
                    FROM get_rooms_with_exits()
                    """
                )
            )
            rows = result.fetchall()
            combined_rows: list[dict[str, object]] = []
            for row in rows:
                # Reason: Result rows are SQLAlchemy Row objects; we need column-name keys for the
                # cache builder. Row exposes that only via _mapping (no public dict() helper in our
                # SQLAlchemy typings), so pyright/pylint flag the access despite it being the ORM idiom.
                combined_rows.append(
                    dict(row._mapping)  # pyright: ignore[reportPrivateUsage]  # pylint: disable=protected-access
                )
            return combined_rows
        except Exception as e:
            error_msg = str(e).lower()
            if "does not exist" in error_msg or "relation" in error_msg or "function get_rooms_with_exits" in error_msg:
                self._logger.warning("Room tables or procedures not found, returning empty room list", error=str(e))
                return []
            raise

    def _parse_zone_parts(self, zone_stable_id: str | None) -> tuple[str, str]:
        zone_parts = (zone_stable_id or "").split("/")
        plane_name = zone_parts[0] if zone_parts else ""
        zone_name = zone_parts[1] if len(zone_parts) > 1 else (zone_stable_id or "")
        return plane_name, zone_name

    def _generate_room_id_from_zone_data(
        self, zone_stable_id: str | None, subzone_stable_id: str | None, stable_id: str | None
    ) -> str:
        from .world_loader import generate_room_id

        plane_name, zone_name = self._parse_zone_parts(zone_stable_id)
        subzone_str = subzone_stable_id or ""
        stable_str = stable_id or ""
        expected_prefix = f"{plane_name}_{zone_name}_{subzone_str}_"
        if stable_str.startswith(expected_prefix):
            return stable_str
        return generate_room_id(plane_name, zone_name, subzone_str, stable_str)

    def _parse_exits_json(self, exits_json: object) -> list[ExitJsonEntry]:
        if isinstance(exits_json, str):
            try:
                parsed = cast(object, json.loads(exits_json))
            except json.JSONDecodeError:
                return []
            return _coerce_exit_entries(parsed)
        if isinstance(exits_json, list):
            return _coerce_exit_entries(cast(object, exits_json))
        return []

    def _process_exits_for_room(
        self, room_id: str, exits_list: list[ExitJsonEntry], exits_by_room: dict[str, dict[str, str]]
    ) -> None:
        for exit_data in exits_list:
            direction = exit_data.get("direction")
            if not direction:
                continue
            to_stable_id = exit_data.get("to_room_stable_id")
            to_subzone = exit_data.get("to_subzone_stable_id")
            to_zone = exit_data.get("to_zone_stable_id")
            to_room_id = self._generate_room_id_from_zone_data(to_zone, to_subzone, to_stable_id)
            if room_id not in exits_by_room:
                exits_by_room[room_id] = {}
            exits_by_room[room_id][direction] = to_room_id

    def _process_combined_rows(
        self, combined_rows: list[dict[str, object]]
    ) -> tuple[list[ProcessedRoomData], dict[str, dict[str, str]]]:
        room_data_list: list[ProcessedRoomData] = []
        exits_by_room: dict[str, dict[str, str]] = {}

        for row in combined_rows:
            stable_id = _row_optional_str(row, "stable_id")
            name = _row_optional_str(row, "name")
            description = _row_optional_str(row, "description")
            attributes = _attributes_from_row(row)
            subzone_stable_id = _row_optional_str(row, "subzone_stable_id")
            zone_stable_id = _row_optional_str(row, "zone_stable_id")
            exits_json = row.get("exits")

            room_id = self._generate_room_id_from_zone_data(zone_stable_id, subzone_stable_id, stable_id)
            zone_parts = (zone_stable_id or "").split("/")
            plane_name = zone_parts[0] if len(zone_parts) > 0 else ""
            zone_name = zone_parts[1] if len(zone_parts) > 1 else (zone_stable_id or "")

            room_data_list.append(
                {
                    "room_id": room_id,
                    "stable_id": stable_id,
                    "name": name,
                    "description": description,
                    "attributes": attributes,
                    "plane": plane_name,
                    "zone": zone_name,
                    "sub_zone": subzone_stable_id,
                }
            )

            if exits_json:
                exits_list = self._parse_exits_json(exits_json)
                self._process_exits_for_room(room_id, exits_list, exits_by_room)

        return room_data_list, exits_by_room

    def _build_room_data_from_row(self, row: dict[str, object]) -> ProcessedRoomData | None:
        stable_id = _row_optional_str(row, "stable_id")
        zone_stable_id = _row_optional_str(row, "zone_stable_id")
        if zone_stable_id is None:
            self._logger.warning("zone_stable_id is None, skipping room", stable_id=stable_id)
            return None
        if stable_id is None:
            self._logger.warning("stable_id is None, skipping room", zone_stable_id=zone_stable_id)
            return None

        name = _row_optional_str(row, "name")
        description = _row_optional_str(row, "description")
        attributes = _attributes_from_row(row)
        subzone_stable_id = _row_optional_str(row, "subzone_stable_id")
        room_id = self._generate_room_id_from_zone_data(zone_stable_id, subzone_stable_id, stable_id)
        plane_name, zone_name = self._parse_zone_parts(zone_stable_id)

        return {
            "room_id": room_id,
            "stable_id": stable_id,
            "name": name,
            "description": description,
            "attributes": attributes,
            "plane": plane_name,
            "zone": zone_name,
            "sub_zone": subzone_stable_id,
        }

    def _process_room_rows(self, rooms_rows: list[dict[str, object]]) -> list[ProcessedRoomData]:
        room_data_list: list[ProcessedRoomData] = []
        for row in rooms_rows:
            room_data = self._build_room_data_from_row(row)
            if room_data is not None:
                room_data_list.append(room_data)
        return room_data_list

    def _extract_exit_fields(
        self, row: dict[str, object]
    ) -> tuple[str, str, str, str, str, str | None, str | None] | None:
        from_stable_id = _row_optional_str(row, "from_room_stable_id")
        to_stable_id = _row_optional_str(row, "to_room_stable_id")
        direction = _row_optional_str(row, "direction")
        from_subzone = _row_optional_str(row, "from_subzone_stable_id")
        from_zone = _row_optional_str(row, "from_zone_stable_id")
        to_subzone = _row_optional_str(row, "to_subzone_stable_id")
        to_zone = _row_optional_str(row, "to_zone_stable_id")

        if direction is None:
            self._logger.warning(
                "Missing direction for exit, skipping", from_stable_id=from_stable_id, to_stable_id=to_stable_id
            )
            return None
        if from_zone is None or to_zone is None:
            self._logger.warning(
                "Missing zone data for exit, skipping",
                from_zone=from_zone,
                to_zone=to_zone,
                direction=direction,
            )
            return None
        if from_stable_id is None or to_stable_id is None:
            self._logger.warning(
                "Missing stable_id for exit, skipping",
                from_stable_id=from_stable_id,
                to_stable_id=to_stable_id,
                direction=direction,
            )
            return None

        return from_stable_id, to_stable_id, direction, from_zone, to_zone, from_subzone, to_subzone

    def _resolve_exit_room_ids(
        self,
        from_zone: str,
        from_subzone: str | None,
        from_stable_id: str,
        to_zone: str,
        to_subzone: str | None,
        to_stable_id: str,
    ) -> tuple[str, str]:
        from_room_id = self._generate_room_id_from_zone_data(from_zone, from_subzone, from_stable_id)
        to_room_id = self._generate_room_id_from_zone_data(to_zone, to_subzone, to_stable_id)
        return from_room_id, to_room_id

    def _log_exit_debug(
        self,
        from_stable_id: str,
        from_room_id: str,
        direction: str,
        to_room_id: str,
        from_zone: str,
        from_subzone: str | None,
    ) -> None:
        if from_stable_id == "earth_arkhamcity_sanitarium_room_foyer_001":
            plane_name, zone_name = self._parse_zone_parts(from_zone)
            from_expected_prefix = f"{plane_name}_{zone_name}_{from_subzone or ''}_"
            self._logger.info(
                "Debugging exit processing",
                from_stable_id=from_stable_id,
                from_room_id=from_room_id,
                from_expected_prefix=from_expected_prefix,
                direction=direction,
                to_room_id=to_room_id,
            )

    def _process_exit_rows(self, exits_rows: list[dict[str, object]]) -> dict[str, dict[str, str]]:
        exits_by_room: dict[str, dict[str, str]] = {}
        for row in exits_rows:
            extracted = self._extract_exit_fields(row)
            if extracted is None:
                continue
            (
                from_stable_id,
                to_stable_id,
                direction,
                from_zone,
                to_zone,
                from_subzone,
                to_subzone,
            ) = extracted

            from_room_id, to_room_id = self._resolve_exit_room_ids(
                from_zone, from_subzone, from_stable_id, to_zone, to_subzone, to_stable_id
            )

            room_exits = exits_by_room.setdefault(from_room_id, {})
            room_exits[direction] = to_room_id

            self._log_exit_debug(
                from_stable_id=from_stable_id,
                from_room_id=from_room_id,
                direction=direction,
                to_room_id=to_room_id,
                from_zone=from_zone,
                from_subzone=from_subzone,
            )

        return exits_by_room

    def _build_room_objects(
        self,
        room_data_list: list[ProcessedRoomData],
        exits_by_room: dict[str, dict[str, str]],
        result_container: RoomLoadResult,
    ) -> None:
        from .models.room import Room

        for room_data_item in room_data_list:
            room_id = room_data_item["room_id"]
            name = room_data_item["name"]
            description = room_data_item["description"]
            attributes_raw = room_data_item["attributes"]
            plane_name = room_data_item["plane"]
            zone_name = room_data_item["zone"]
            subzone_stable_id = room_data_item["sub_zone"]
            exits = exits_by_room.get(room_id, {})

            if room_id == "earth_arkhamcity_sanitarium_room_foyer_001":
                self._logger.info(
                    "Debugging exit matching",
                    room_id=room_id,
                    exits_found=exits,
                    exits_by_room_keys=list(exits_by_room.keys())[:10],
                    exits_by_room_size=len(exits_by_room),
                )

            if isinstance(attributes_raw, dict):
                attributes = cast(dict[str, object], attributes_raw)
                environment = attributes.get("environment", "outdoors")
                resolved_environment = environment if isinstance(environment, str) else "outdoors"
                attributes_payload = attributes
            else:
                resolved_environment = "outdoors"
                attributes_payload = {}

            room_payload: RoomInitPayload = {
                "id": room_id,
                "name": name,
                "description": description,
                "plane": plane_name,
                "zone": zone_name,
                "sub_zone": subzone_stable_id,
                "resolved_environment": resolved_environment,
                "exits": exits,
                "attributes": attributes_payload,
            }

            result_container["rooms"][room_id] = Room(dict(room_payload), self._event_bus)
