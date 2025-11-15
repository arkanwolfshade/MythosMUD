from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
from pathlib import Path

from server.logging.enhanced_logging_config import get_logger
from server.schemas.calendar import ScheduleCollection, ScheduleEntry, load_schedule_directory
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
    ) -> None:
        self._environment = normalize_environment(environment)
        resolved_dir: Path | None = Path(schedule_dir) if schedule_dir is not None else None
        if resolved_dir is None and collections is None:
            resolved_dir = get_calendar_paths_for_environment(self._environment)[1]

        self._schedule_dir = resolved_dir
        if collections is None:
            if self._schedule_dir is None:
                raise ValueError("schedule_dir is required when collections are not provided")
            collections = load_schedule_directory(self._schedule_dir)

        entries: list[ScheduleEntry] = []
        for _path, collection in collections:
            entries.extend(collection.schedules)

        self._entries = entries
        logger.info(
            "Loaded Mythos schedule definitions",
            schedule_dir=str(self._schedule_dir) if self._schedule_dir else "<collections-provided>",
            entry_count=len(self._entries),
            environment=self._environment,
        )

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
        return list(self._entries)

    @property
    def entry_count(self) -> int:
        return len(self._entries)
