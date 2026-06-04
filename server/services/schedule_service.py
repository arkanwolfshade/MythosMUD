"""Schedule service for managing in-game schedules and recurring events.

This module provides the ScheduleService class for loading, caching, and
querying schedule data from calendar JSON files.
"""

from __future__ import annotations

import asyncio
import os
import threading
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict, cast

import asyncpg

from server.database_config_helpers import get_asyncpg_server_settings_for_database_url
from server.schemas.calendar import ScheduleCollection, ScheduleEntry
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.project_paths import get_calendar_paths_for_environment, normalize_environment

# Map legacy Latin weekday names (pre-migration 11) to standard English Western-hemisphere
# names (Sunday, Monday, ...) so DB rows load correctly with or without migration 11.
_LATIN_TO_STANDARD_WEEKDAY = {
    "Primus": "Monday",
    "Secundus": "Tuesday",
    "Tertius": "Wednesday",
    "Quartus": "Thursday",
    "Quintus": "Friday",
    "Sextus": "Saturday",
    "Septimus": "Sunday",
}


def normalize_weekday_names(days: list[str]) -> list[str]:
    """Map Latin weekday names to standard English (Sunday, Monday, ...); pass-through if already standard."""
    return [_LATIN_TO_STANDARD_WEEKDAY.get(d, d) for d in days]


_CALENDAR_NPC_SCHEDULES_QUERY = """
    SELECT
        stable_id,
        name,
        category,
        start_hour,
        end_hour,
        days,
        applies_to,
        effects,
        notes
    FROM calendar_npc_schedules
    ORDER BY category, start_hour, name
"""


def _string_list_from_row(value: object) -> list[str]:
    """Normalize nullable PostgreSQL array columns to string values."""
    if value is None:
        return []
    if not isinstance(value, list):
        return []
    seq = cast(list[object], value)
    return [str(item) for item in seq]


def _lower_string_list_from_row(value: object) -> list[str]:
    """Normalize nullable PostgreSQL array columns to lowercase slug strings."""
    return [item.lower() for item in _string_list_from_row(value)]


def _resolve_asyncpg_database_url() -> str:
    """Return asyncpg-compatible DATABASE_URL from the environment."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set")
    if database_url.startswith("postgresql+asyncpg://"):
        return database_url.replace("postgresql+asyncpg://", "postgresql://", 1)
    return database_url


def _schedule_entry_from_row(row: asyncpg.Record) -> ScheduleEntry:
    """Build a ScheduleEntry from a calendar_npc_schedules row."""
    applies_to = _lower_string_list_from_row(cast(object, row["applies_to"]))
    effects = _lower_string_list_from_row(cast(object, row["effects"]))
    raw_days = _string_list_from_row(cast(object, row["days"]))
    days = normalize_weekday_names(raw_days)
    return ScheduleEntry(
        id=cast(str, row["stable_id"]),
        name=cast(str, row["name"]),
        category=cast(str, row["category"]),
        start_hour=cast(int, row["start_hour"]),
        end_hour=cast(int, row["end_hour"]),
        days=days,
        applies_to=applies_to,
        effects=effects,
        notes=cast(str | None, row["notes"]),
    )


async def _fetch_schedule_entries(conn: asyncpg.Connection) -> list[ScheduleEntry]:
    """Load and normalize schedule rows from PostgreSQL."""
    rows = await conn.fetch(_CALENDAR_NPC_SCHEDULES_QUERY)
    return [_schedule_entry_from_row(row) for row in rows]


if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer


class _DatabaseLoadResult(TypedDict):
    entries: list[ScheduleEntry] | None
    error: Exception | None


logger = get_logger(__name__)


class ScheduleService:
    """Provides schedule lookups for NPCs and environmental consumers."""

    _environment: str
    _async_persistence: AsyncPersistenceLayer | None
    _schedule_dir: Path | None

    def __init__(
        self,
        *,
        schedule_dir: Path | str | None = None,
        collections: Sequence[tuple[Path, ScheduleCollection]] | None = None,
        environment: str | None = None,
        async_persistence: AsyncPersistenceLayer | None = None,
    ) -> None:
        self._environment = normalize_environment(environment)
        self._async_persistence = async_persistence
        resolved_dir: Path | None = Path(schedule_dir) if schedule_dir is not None else None
        if resolved_dir is None and collections is None:
            resolved_dir = get_calendar_paths_for_environment(self._environment)[1]

        self._schedule_dir = resolved_dir

        # Initialize _entries attribute (declared once to avoid redefinition)
        if collections is None:
            # Load from PostgreSQL database (required)
            if self._async_persistence is None:
                raise ValueError("async_persistence is required for ScheduleService")

            entries = self._load_from_database()
            if entries is None:
                raise RuntimeError("Failed to load schedules from database")

            self._entries: list[ScheduleEntry] = entries
            logger.info(
                "Loaded Mythos schedule definitions from PostgreSQL database",
                entry_count=len(self._entries),
                environment=self._environment,
            )
        else:
            # If collections is provided, initialize entries as empty list
            # (collections parameter is currently not used in implementation)
            self._entries = []

    def _load_from_database(self) -> list[ScheduleEntry] | None:
        """Load schedules from PostgreSQL database."""
        result_container: _DatabaseLoadResult = {"entries": None, "error": None}

        def run_async() -> None:
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                new_loop.run_until_complete(self._async_load_from_database(result_container))
            finally:
                new_loop.close()

        thread = threading.Thread(target=run_async)
        thread.start()
        thread.join()

        error = result_container.get("error")
        if error is not None:
            # error is guaranteed to be an Exception from _async_load_from_database
            raise error

        return result_container["entries"]

    async def _async_load_from_database(self, result_container: _DatabaseLoadResult) -> None:
        """Async helper to load schedules from PostgreSQL database."""
        try:
            database_url = _resolve_asyncpg_database_url()
            server_settings = get_asyncpg_server_settings_for_database_url(database_url)
            # Use asyncpg directly to avoid event loop conflicts; match engine search_path
            conn = await asyncpg.connect(database_url, server_settings=server_settings)
            try:
                result_container["entries"] = await _fetch_schedule_entries(conn)
            finally:
                await conn.close()
        except Exception as e:
            result_container["error"] = e
            raise

    def get_active_entries(self, *, mythos_dt: datetime, day_name: str) -> list[ScheduleEntry]:
        """Return schedule entries active at the provided Mythos date/time."""

        hour = mythos_dt.hour
        active = [
            entry for entry in self._entries if day_name in entry.days and entry.start_hour <= hour < entry.end_hour
        ]
        logger.debug(
            "Resolved schedule entries",
            day_name=day_name,
            hour=hour,
            active_count=len(active),
        )
        return active

    @property
    def entries(self) -> list[ScheduleEntry]:
        """Get all schedule entries.

        Returns:
            list[ScheduleEntry]: List of all schedule entries
        """
        return list(self._entries)

    @property
    def entry_count(self) -> int:
        """Get the number of schedule entries.

        Returns:
            int: The count of schedule entries
        """
        return len(self._entries)
