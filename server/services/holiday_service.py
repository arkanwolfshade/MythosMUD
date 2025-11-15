from __future__ import annotations

from datetime import UTC, datetime, timedelta
from pathlib import Path

from server.logging.enhanced_logging_config import get_logger
from server.schemas.calendar import HolidayCollection, HolidayEntry
from server.time.time_service import ChronicleLike

logger = get_logger(__name__)


def _ensure_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


class HolidayService:
    """Tracks active Mythos holidays and upcoming triggers."""

    def __init__(
        self,
        *,
        chronicle: ChronicleLike,
        data_path: Path | str = Path("data/calendar/holidays.json"),
        collection: HolidayCollection | None = None,
    ) -> None:
        self._chronicle = chronicle
        self._data_path = Path(data_path)
        self._collection = collection or HolidayCollection.load_file(self._data_path)
        self._collection.ensure_unique_ids()
        self._active_started: dict[str, datetime] = {}
        self._last_refresh: datetime | None = None
        logger.info(
            "Holiday service initialized",
            holiday_count=len(self._collection.holidays),
            data_path=str(self._data_path),
        )

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
        return self._collection

    @property
    def last_refresh(self) -> datetime | None:
        return self._last_refresh
