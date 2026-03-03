"""
Room cache loading for async persistence layer.

Extracted from async_persistence.py to satisfy file-nloc limit.
Loads rooms from PostgreSQL via get_rooms_with_exits() and builds in-memory Room cache.
"""

import json
from typing import Any, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from .database import get_async_session
from .exceptions import DatabaseError


class RoomCacheLoader:
    """
    Loads room data from the database and populates a room cache dict.

    Used by AsyncPersistenceLayer for lazy room cache loading.
    """

    def __init__(
        self,
        room_cache: dict[str, Any],
        room_mappings: dict[str, Any],
        logger: Any,
        event_bus: Any,
    ) -> None:
        self._room_cache = room_cache
        self._room_mappings = room_mappings
        self._logger = logger
        self._event_bus = event_bus

    async def load(self) -> None:
        """Load rooms from PostgreSQL and update the room cache."""
        async for session in get_async_session():
            try:
                combined_rows = await self._query_rooms_with_exits_async(session)
                room_data_list, exits_by_room = self._process_combined_rows(combined_rows)
                result_container: dict[str, Any] = {"rooms": {}}
                self._build_room_objects(room_data_list, exits_by_room, result_container)
                self._apply_rooms_to_cache(result_container.get("rooms"))
                self._log_room_cache_after_load()
            except (DatabaseError, OSError, RuntimeError, ConnectionError, TimeoutError, SQLAlchemyError) as e:
                self._handle_room_load_error(e)
            break

    def _apply_rooms_to_cache(self, rooms: Any) -> None:
        if rooms is not None and isinstance(rooms, dict):
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

    async def _query_rooms_with_exits_async(self, session: Any) -> list[dict[str, Any]]:
        try:
            result = await session.execute(text("SELECT * FROM get_rooms_with_exits()"))
            rows = result.fetchall()
            return [dict(row._mapping) for row in rows]  # pylint: disable=protected-access  # SQLAlchemy Row._mapping
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

    def _parse_exits_json(self, exits_json: Any) -> list[dict[str, Any]]:
        if isinstance(exits_json, str):
            try:
                result: list[dict[str, Any]] = cast(list[dict[str, Any]], json.loads(exits_json))
                return result
            except json.JSONDecodeError:
                return []
        if isinstance(exits_json, list):
            return exits_json
        return []

    def _process_exits_for_room(
        self, room_id: str, exits_list: list[dict[str, Any]], exits_by_room: dict[str, dict[str, str]]
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
        self, combined_rows: list[dict[str, Any]]
    ) -> tuple[list[dict[str, Any]], dict[str, dict[str, str]]]:
        room_data_list = []
        exits_by_room: dict[str, dict[str, str]] = {}

        for row in combined_rows:
            stable_id = row.get("stable_id")
            name = row.get("name")
            description = row.get("description")
            attributes = row.get("attributes") if row.get("attributes") else {}
            subzone_stable_id = row.get("subzone_stable_id")
            zone_stable_id = row.get("zone_stable_id")
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

    def _build_room_data_from_row(self, row: dict[str, Any]) -> dict[str, Any] | None:
        stable_id = row.get("stable_id")
        zone_stable_id = row.get("zone_stable_id")
        if zone_stable_id is None:
            self._logger.warning("zone_stable_id is None, skipping room", stable_id=stable_id)
            return None
        if stable_id is None:
            self._logger.warning("stable_id is None, skipping room", zone_stable_id=zone_stable_id)
            return None

        name = row.get("name")
        description = row.get("description")
        attributes = row.get("attributes") if row.get("attributes") else {}
        subzone_stable_id = row.get("subzone_stable_id")
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

    def _process_room_rows(self, rooms_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        room_data_list: list[dict[str, Any]] = []
        for row in rooms_rows:
            room_data = self._build_room_data_from_row(row)
            if room_data is not None:
                room_data_list.append(room_data)
        return room_data_list

    def _extract_exit_fields(
        self, row: dict[str, Any]
    ) -> tuple[str, str, str, str, str, str | None, str | None] | None:
        from_stable_id = row.get("from_room_stable_id")
        to_stable_id = row.get("to_room_stable_id")
        direction = row.get("direction")
        from_subzone = row.get("from_subzone_stable_id")
        from_zone = row.get("from_zone_stable_id")
        to_subzone = row.get("to_subzone_stable_id")
        to_zone = row.get("to_zone_stable_id")

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

    def _process_exit_rows(self, exits_rows: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
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
        room_data_list: list[dict[str, Any]],
        exits_by_room: dict[str, dict[str, str]],
        result_container: dict[str, Any],
    ) -> None:
        from .models.room import Room

        for room_data_item in room_data_list:
            room_id = room_data_item["room_id"]
            name = room_data_item["name"]
            description = room_data_item["description"]
            attributes = room_data_item["attributes"]
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

            room_data = {
                "id": room_id,
                "name": name,
                "description": description,
                "plane": plane_name,
                "zone": zone_name,
                "sub_zone": subzone_stable_id,
                "resolved_environment": attributes.get("environment", "outdoors")
                if isinstance(attributes, dict)
                else "outdoors",
                "exits": exits,
                "attributes": attributes if isinstance(attributes, dict) else {},
            }

            result_container["rooms"][room_id] = Room(room_data, self._event_bus)
