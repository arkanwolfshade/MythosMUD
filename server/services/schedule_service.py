"""Schedule service for managing in-game schedules and recurring events.

This module provides the ScheduleService class for loading, caching, and
querying schedule data from calendar JSON files.
"""

from __future__ import annotations

import asyncio
import threading
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path

from server.schemas.calendar import ScheduleCollection, ScheduleEntry
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.project_paths import get_calendar_paths_for_environment, normalize_environment

logger = get_logger(__name__)


class ScheduleService:
    """Provides schedule lookups for NPCs and environmental consumers."""

    def __init__(
        self,
        *,
        schedule_dir: Path | str | None = None,
        collections: Sequence[tuple[Path, ScheduleCollection]] | None = None,
        environment: str | None = None,
        async_persistence=None,
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
        result_container = {"entries": None, "error": None}

        def run_async():
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

    async def _async_load_from_database(self, result_container: dict) -> None:
        """Async helper to load schedules from PostgreSQL database."""
        import os

        import asyncpg

        try:
            # Get database URL from environment
            database_url = os.getenv("DATABASE_URL")
            if not database_url:
                raise ValueError("DATABASE_URL environment variable not set")

            # Convert SQLAlchemy-style URL to asyncpg-compatible format
            if database_url.startswith("postgresql+asyncpg://"):
                database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

            # Use asyncpg directly to avoid event loop conflicts
            conn = await asyncpg.connect(database_url)
            try:
                # Query calendar_npc_schedules table
                query = """
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
                rows = await conn.fetch(query)

                entries = []
                for row in rows:
                    # Normalize applies_to and effects to lowercase to match validation requirements
                    applies_to = [item.lower() for item in (row["applies_to"] or [])]
                    effects = [item.lower() for item in (row["effects"] or [])]

                    schedule_entry = ScheduleEntry(
                        id=row["stable_id"],
                        name=row["name"],
                        category=row["category"],
                        start_hour=row["start_hour"],
                        end_hour=row["end_hour"],
                        days=list(row["days"]) if row["days"] else [],  # Convert array to list
                        applies_to=applies_to,
                        effects=effects,
                        notes=row["notes"],
                    )
                    entries.append(schedule_entry)

                result_container["entries"] = entries
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
