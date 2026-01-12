"""
Calendar ingestion schemas for MythosMUD.

These models provide a typed wrapper around the designer-authored JSON files
so other services can safely reason about holidays, schedules, and the
accelerated Mythos calendar.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, field_validator

_TRADITIONS = {"catholic", "islamic", "jewish", "neo_pagan", "mythos"}
_SEASONS = {"winter", "spring", "summer", "autumn"}
_MYTHOS_WEEKDAYS = ["Primus", "Secundus", "Tertius", "Quartus", "Quintus", "Sextus"]


class HolidayEntry(BaseModel):
    """Single holiday definition loaded from data/<env>/calendar/holidays.json."""

    id: str = Field(pattern=r"^[a-z0-9_]+$", min_length=3)
    name: str
    tradition: str
    month: int = Field(ge=1, le=12)
    day: int = Field(ge=1, le=30)
    duration_hours: int = Field(default=24, ge=1, le=48)
    season: str
    bonus_tags: list[str] = Field(default_factory=list)
    notes: str | None = None

    @field_validator("tradition")
    @classmethod
    def validate_tradition(cls, value: str) -> str:
        """Validate tradition value.

        Args:
            value: The tradition string to validate

        Returns:
            str: The validated tradition

        Raises:
            ValueError: If tradition is not in the allowed list
        """
        if value not in _TRADITIONS:
            raise ValueError(f"tradition must be one of: {sorted(_TRADITIONS)}")
        return value

    @field_validator("season")
    @classmethod
    def validate_season(cls, value: str) -> str:
        """Validate season value.

        Args:
            value: The season string to validate

        Returns:
            str: The validated season

        Raises:
            ValueError: If season is not in the allowed list
        """
        if value not in _SEASONS:
            raise ValueError(f"season must be one of: {sorted(_SEASONS)}")
        return value

    @field_validator("bonus_tags")
    @classmethod
    def validate_bonus_tags(cls, value: Sequence[str]) -> list[str]:
        """Validate bonus tags format."""
        for tag in value:
            if not re.fullmatch(r"[a-z0-9_\-]+", tag):
                raise ValueError(f"bonus tag '{tag}' must be lowercase snake/kebab case")
        return list(value)


class HolidayCollection(BaseModel):
    """Wrapper for the complete holiday JSON payload."""

    holidays: list[HolidayEntry]

    @property
    def id_map(self) -> dict[str, HolidayEntry]:
        """Create a mapping of holiday IDs to holiday entries.

        Returns:
            dict[str, HolidayEntry]: Dictionary mapping holiday IDs to entries
        """
        return {entry.id: entry for entry in self.holidays}

    @classmethod
    def load_file(cls, path: Path | str) -> HolidayCollection:
        """Load holiday collection from JSON file."""
        with Path(path).open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return cls.model_validate(payload)

    def ensure_unique_ids(self) -> None:
        """Ensure all holiday IDs are unique.

        Raises:
            ValueError: If duplicate holiday IDs are detected
        """
        seen: set[str] = set()
        duplicates: list[str] = []
        for holiday in self.holidays:
            if holiday.id in seen:
                duplicates.append(holiday.id)
            seen.add(holiday.id)
        if duplicates:
            raise ValueError(f"Duplicate holiday ids detected: {', '.join(sorted(duplicates))}")


class ScheduleEntry(BaseModel):
    """Single schedule block describing routine availability (`data/<env>/calendar/schedules/*.json`)."""

    id: str = Field(pattern=r"^[a-z0-9_]+$", min_length=3)
    name: str
    category: str
    start_hour: int = Field(ge=0, le=23)
    end_hour: int = Field(ge=1, le=24)
    days: list[str] = Field(default_factory=list)
    applies_to: list[str] = Field(default_factory=list)
    effects: list[str] = Field(default_factory=list)
    notes: str | None = None

    @field_validator("days")
    @classmethod
    def validate_days(cls, value: Sequence[str]) -> list[str]:
        """Validate schedule entry days."""
        if not value:
            raise ValueError("days must contain at least one Mythos weekday")
        invalid = [day for day in value if day not in _MYTHOS_WEEKDAYS]
        if invalid:
            raise ValueError(f"invalid Mythos weekdays: {', '.join(invalid)}")
        return list(value)

    @field_validator("applies_to", "effects")
    @classmethod
    def validate_slug_list(cls, value: Sequence[str]) -> list[str]:
        """Validate slug-formatted list entries.

        Args:
            value: Sequence of strings to validate

        Returns:
            list[str]: The validated list of slug-formatted strings

        Raises:
            ValueError: If any entry does not match slug format
        """
        for item in value:
            if not re.fullmatch(r"[a-z0-9_\-]+", item):
                raise ValueError(f"list entry '{item}' must use lowercase slug formatting")
        return list(value)

    @field_validator("end_hour")
    @classmethod
    def validate_duration(cls, end_hour: int, info: Any) -> int:
        """Ensure the schedule window moves time forward like the Chronology Tablets prescribe."""
        start_hour = info.data.get("start_hour") if info and info.data else None
        if isinstance(start_hour, int) and end_hour <= start_hour:
            raise ValueError("end_hour must be greater than start_hour")
        return end_hour


class ScheduleCollection(BaseModel):
    """Wrapper around an array of schedule entries."""

    schedules: list[ScheduleEntry]

    @classmethod
    def load_file(cls, path: Path | str) -> ScheduleCollection:
        """Load schedule collection from a JSON file.

        Args:
            path: Path to the JSON file containing schedule data

        Returns:
            ScheduleCollection: The loaded schedule collection
        """
        with Path(path).open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        return cls.model_validate(payload)


def load_schedule_directory(directory: Path | str) -> list[tuple[Path, ScheduleCollection]]:
    """Utility for loading every schedule file within a directory."""

    dir_path = Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"Schedule directory {dir_path} does not exist")

    collections: list[tuple[Path, ScheduleCollection]] = []
    for json_file in sorted(dir_path.glob("*.json")):
        collections.append((json_file, ScheduleCollection.load_file(json_file)))
    return collections


def slugify_observance(name: str) -> str:
    """Normalize document observance names into snake_case ids."""

    slug = re.sub(r"[^a-z0-9]+", "_", name.strip().lower())
    return slug.strip("_")


def extract_observance_ids(lines: Iterable[str]) -> set[str]:
    """Parse table rows from MYTHOS_HOLIDAY_CANDIDATES.md into slug ids."""

    ids: set[str] = set()
    for line in lines:
        if not line.startswith("|"):
            continue
        if "Observance" in line or line.count("|") < 3:
            continue
        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        if not cells:
            continue
        name = cells[0]
        if not name or set(name) <= {"-", ":"}:
            continue
        ids.add(slugify_observance(name))
    return ids
