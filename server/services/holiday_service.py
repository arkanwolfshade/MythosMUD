"""Holiday service for managing in-game holidays and events.

This module provides the HolidayService class for loading, caching, and
querying holiday data from calendar JSON files.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Holiday service requires many parameters for context and holiday operations

from __future__ import annotations

import asyncio
import threading
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

from server.async_persistence import AsyncPersistenceLayer
from server.schemas.calendar import HolidayCollection, HolidayEntry
from server.structured_logging.enhanced_logging_config import get_logger
from server.time.time_service import ChronicleLike
from server.utils.project_paths import get_calendar_paths_for_environment, normalize_environment

logger = get_logger(__name__)


def _ensure_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


class HolidayService:
    """Tracks active Mythos holidays and upcoming triggers."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Holiday service initialization requires many service dependencies
        self,
        *,
        chronicle: ChronicleLike,
        data_path: Path | str | None = None,
        collection: HolidayCollection | None = None,
        environment: str | None = None,
        async_persistence: AsyncPersistenceLayer | None = None,
    ) -> None:
        self._chronicle = chronicle
        self._environment = normalize_environment(environment)
        self._async_persistence = async_persistence

        resolved_data_path: Path | None = Path(data_path) if data_path is not None else None
        if resolved_data_path is None and collection is None:
            resolved_data_path = get_calendar_paths_for_environment(self._environment)[0]
        self._data_path = resolved_data_path

        # Declare _collection once to avoid mypy redefinition error
        if collection is None:
            # Load from PostgreSQL database (required)
            if self._async_persistence is None:
                raise ValueError("async_persistence is required for HolidayService")

            loaded_collection = self._load_from_database()
            if loaded_collection is None:
                raise RuntimeError("Failed to load holidays from database")
            self._collection: HolidayCollection = loaded_collection
            self._collection.ensure_unique_ids()
            logger.info(
                "Holiday service initialized from PostgreSQL database",
                holiday_count=len(self._collection.holidays),
                environment=self._environment,
            )
        else:
            self._collection = collection

        self._collection.ensure_unique_ids()
        self._active_started: dict[str, datetime] = {}
        self._last_refresh: datetime | None = None
        logger.info(
            "Holiday service initialized",
            holiday_count=len(self._collection.holidays),
            data_path=str(self._data_path) if self._data_path else "<collection-provided>",
            environment=self._environment,
        )

    def _load_from_database(self) -> HolidayCollection | None:
        """Load holidays from PostgreSQL database."""
        result_container: dict[str, Any] = {"collection": None, "error": None}

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
            if isinstance(error, BaseException):
                raise error
            raise RuntimeError(f"Unexpected error type: {type(error)}")

        collection = result_container.get("collection")
        if isinstance(collection, HolidayCollection):
            return collection
        return None

    async def _async_load_from_database(self, result_container: dict[str, Any]) -> None:
        """Async helper to load holidays from PostgreSQL database."""
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
                # Query calendar_holidays table
                query = """
                    SELECT
                        stable_id,
                        name,
                        tradition,
                        month,
                        day,
                        duration_hours,
                        season,
                        bonus_tags
                    FROM calendar_holidays
                    ORDER BY month, day, name
                """
                rows = await conn.fetch(query)

                holidays = []
                for row in rows:
                    holiday_entry = HolidayEntry(
                        id=row["stable_id"],
                        name=row["name"],
                        tradition=row["tradition"],
                        month=row["month"],
                        day=row["day"],
                        duration_hours=row["duration_hours"],
                        season=row["season"],
                        bonus_tags=list(row["bonus_tags"]) if row["bonus_tags"] else [],  # Convert array to list
                    )
                    holidays.append(holiday_entry)

                result_container["collection"] = HolidayCollection(holidays=holidays)
            finally:
                await conn.close()
        except Exception as e:
            result_container["error"] = e
            raise

    def refresh_active(self, mythos_dt: datetime | None = None) -> list[HolidayEntry]:
        """Update the active holiday window for the provided Mythos timestamp."""

        current = _ensure_utc(mythos_dt or self._chronicle.get_current_mythos_datetime())
        self._last_refresh = current

        # Remove expired holidays
        for holiday_id, start in list(self._active_started.items()):
            entry = self._collection.id_map.get(holiday_id)
            if not entry:
                del self._active_started[holiday_id]
                continue
            effective_duration = min(entry.duration_hours, 48)
            if current >= start + timedelta(hours=effective_duration):
                logger.debug("Holiday expired", holiday_id=holiday_id)
                del self._active_started[holiday_id]

        # Activate newly matching holidays
        for entry in self._collection.holidays:
            if entry.month == current.month and entry.day == current.day:
                self._active_started.setdefault(entry.id, current)

        return self.get_active_holidays()

    def get_active_holidays(self) -> list[HolidayEntry]:
        """Return currently active holiday entries."""

        entries = []
        for holiday_id in self._active_started:
            entry = self._collection.id_map.get(holiday_id)
            if entry:
                entries.append(entry)
        return entries

    def get_serialized_active_holidays(self, mythos_dt: datetime) -> list[HolidayEntry]:
        """
        Get active holidays and serialize them for API responses.

        This method encapsulates the logic for refreshing active holidays and
        ensuring they are properly serialized, centralizing business logic
        that was previously in the API endpoint.

        Args:
            mythos_dt: Current Mythos datetime

        Returns:
            list[HolidayEntry]: Serialized active holiday entries
        """
        active_entries = self.refresh_active(mythos_dt)
        # HolidayEntry objects are already Pydantic models, so they serialize directly
        return active_entries

    def get_serialized_upcoming_holidays(self, count: int = 3) -> list[HolidayEntry]:
        """
        Get upcoming holidays and serialize them for API responses.

        This method encapsulates the logic for retrieving upcoming holidays,
        centralizing business logic that was previously in the API endpoint.

        Args:
            count: Number of upcoming holidays to retrieve

        Returns:
            list[HolidayEntry]: Serialized upcoming holiday entries
        """
        upcoming_entries = self.get_upcoming_holidays(count)
        # HolidayEntry objects are already Pydantic models, so they serialize directly
        return upcoming_entries

    def get_active_holiday_names(self) -> list[str]:
        """Convenience helper for formatted admin output."""

        return [entry.name for entry in self.get_active_holidays()]

    def get_upcoming_holidays(self, count: int = 3, *, start_dt: datetime | None = None) -> list[HolidayEntry]:
        """Return the next N holidays, wrapping around the calendar."""

        current = _ensure_utc(start_dt or self._chronicle.get_current_mythos_datetime())
        ordinal_today = self._day_ordinal(current.month, current.day)

        sorted_entries = sorted(
            self._collection.holidays,
            key=lambda e: (self._day_ordinal(e.month, e.day), e.name),
        )

        upcoming: list[HolidayEntry] = []
        for entry in sorted_entries:
            ordinal = self._day_ordinal(entry.month, entry.day)
            if ordinal >= ordinal_today:
                upcoming.append(entry)
        for entry in sorted_entries:
            if len(upcoming) >= count:
                break
            upcoming.append(entry)

        return upcoming[:count]

    def get_upcoming_summary(self, count: int = 3) -> list[str]:
        """Return formatted strings describing upcoming holidays."""

        return [f"{entry.month:02d}/{entry.day:02d} - {entry.name}" for entry in self.get_upcoming_holidays(count)]

    def _day_ordinal(self, month: int, day: int) -> int:
        """Convert month/day into a monotonically increasing ordinal (1-indexed)."""

        return (month - 1) * 30 + day

    @property
    def collection(self) -> HolidayCollection:
        """Get the holiday collection.

        Returns:
            HolidayCollection: The loaded holiday collection
        """
        return self._collection

    @property
    def last_refresh(self) -> datetime | None:
        """Get the last refresh timestamp.

        Returns:
            datetime | None: The timestamp of the last refresh or None if never refreshed
        """
        return self._last_refresh
