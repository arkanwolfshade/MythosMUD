"""Time service for managing Mythos game time and calendar.

This module provides the MythosChronicle and related classes for managing
in-game time, calendar systems, and time-based calculations.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Time service requires many state tracking and configuration attributes

from __future__ import annotations

import calendar
import json
import os
import tempfile
import threading
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from prometheus_client import Counter

from server.config import get_config
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:  # pragma: no cover - only used for type hints
    from server.config.models import TimeConfig


logger = get_logger(__name__)

MYTHOS_TICK_COUNTER = Counter(
    "mythos_chronicle_ticks_total",
    "Total number of accelerated Mythos hours recorded by the chronicle",
)
MYTHOS_FREEZE_COUNTER = Counter(
    "mythos_chronicle_freeze_events_total",
    "Total number of freeze events captured for deterministic resume operations",
)

_SEASON_BY_MONTH = {
    12: "winter",
    1: "winter",
    2: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn",
}


@dataclass(frozen=True)
class ChronicleState:
    """
    Snapshot of the chronicle's reference timestamps.

    The last frozen real timestamp and its Mythos counterpart anchor all future conversions,
    just as noted in the Pnakotic Manuscripts' treatment of calendrical drift.
    """

    real_timestamp: datetime
    mythos_timestamp: datetime


@dataclass(frozen=True)
class MythosCalendarComponents:  # pylint: disable=too-many-instance-attributes  # Reason: Calendar components dataclass requires many fields to capture complete calendar state
    """Structured view of the accelerated calendar for downstream systems."""

    mythos_datetime: datetime
    year: int
    month: int
    month_name: str
    day_of_month: int
    week_of_month: int
    day_of_week: int
    day_name: str
    season: str
    is_daytime: bool
    is_witching_hour: bool
    daypart: str


def _ensure_utc(value: datetime) -> datetime:
    """Normalize datetimes to UTC for deterministic math."""

    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


class ChronicleLike(Protocol):
    """
    Minimal chronicle contract required by downstream systems.

    The canonical MythosChronicle implements many more behaviors, but most consumers only
    need the accelerated timestamp for scheduling calculations or diagnostics.
    """

    def get_current_mythos_datetime(self) -> datetime:  # pragma: no cover - Protocol definition
        """Get the current Mythos datetime.

        Returns:
            datetime: The current Mythos datetime
        """

    def format_clock(self, mythos_dt: datetime | None = None) -> str:  # pragma: no cover - Protocol definition
        """Format the clock display string.

        Args:
            mythos_dt: Optional Mythos datetime to format (defaults to current time)

        Returns:
            str: The formatted clock string
        """


class MythosChronicle:
    """Authoritative converter between real and Mythos time."""

    _instance: MythosChronicle | None = None
    _instance_lock = threading.Lock()

    def __init__(self, *, config: TimeConfig | None = None, state_path: Path | None = None) -> None:
        self._config = config or get_config().time
        self._compression_ratio = self._config.compression_ratio
        self._state_file = Path(state_path) if state_path else Path(self._config.state_file)
        self._state_lock = threading.RLock()
        self._state = self._load_state()
        self._last_freeze_state: ChronicleState | None = self._state
        logger.debug(
            "Mythos chronicle initialized",
            compression_ratio=self._compression_ratio,
            state_file=str(self._state_file),
            real_reference=self._state.real_timestamp.isoformat(),
            mythos_reference=self._state.mythos_timestamp.isoformat(),
        )

    @classmethod
    def get_instance(cls) -> MythosChronicle:
        """Return the singleton chronicle instance."""

        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the singleton instance (testing support)."""

        with cls._instance_lock:
            cls._instance = None

    @property
    def compression_ratio(self) -> float:
        """Mythos hours per real hour."""

        return self._compression_ratio

    def get_state_snapshot(self) -> ChronicleState:
        """Return the current persisted state snapshot."""

        with self._state_lock:
            return ChronicleState(self._state.real_timestamp, self._state.mythos_timestamp)

    def to_mythos_datetime(self, real_dt: datetime) -> datetime:
        """Convert a real-world timestamp into Mythos time."""

        normalized_real = _ensure_utc(real_dt)
        with self._state_lock:
            delta_hours = self._hours_between(normalized_real, self._state.real_timestamp)
            mythos_delta = timedelta(hours=delta_hours * self._compression_ratio)
            return self._state.mythos_timestamp + mythos_delta

    def to_real_datetime(self, mythos_dt: datetime) -> datetime:
        """Convert a Mythos timestamp back into real-world time."""

        normalized_mythos = _ensure_utc(mythos_dt)
        with self._state_lock:
            delta_hours = self._hours_between(normalized_mythos, self._state.mythos_timestamp)
            real_delta = timedelta(hours=delta_hours / self._compression_ratio)
            return self._state.real_timestamp + real_delta

    def get_current_mythos_datetime(self) -> datetime:
        """Return the Mythos timestamp corresponding to now."""

        return self.to_mythos_datetime(datetime.now(UTC))

    def format_clock(self, mythos_dt: datetime | None = None) -> str:
        """Provide a simple HH:MM clock string for UI surfaces."""

        target = mythos_dt or self.get_current_mythos_datetime()
        return target.strftime("%H:%M Mythos")

    def get_calendar_components(self, mythos_dt: datetime | None = None) -> MythosCalendarComponents:
        """Return normalized calendar metadata for the supplied Mythos timestamp."""

        normalized = _ensure_utc(mythos_dt or self.get_current_mythos_datetime())
        day_of_month = normalized.day
        # Calculate week of month using standard calendar (first week starts on day 1)
        first_day_weekday = calendar.monthrange(normalized.year, normalized.month)[0]
        # Adjust: calendar.monthrange returns 0=Monday, so we need to align with day_of_month
        week_of_month = ((day_of_month - 1 + first_day_weekday) // 7) + 1
        # Use standard Python datetime.weekday() (0=Monday, 6=Sunday)
        day_of_week = normalized.weekday()
        components = MythosCalendarComponents(
            mythos_datetime=normalized,
            year=normalized.year,
            month=normalized.month,
            month_name=calendar.month_name[normalized.month],
            day_of_month=day_of_month,
            week_of_month=week_of_month,
            day_of_week=day_of_week,
            day_name=calendar.day_name[day_of_week],
            season=_season_for_month(normalized.month),
            is_daytime=self.is_daytime(normalized),
            is_witching_hour=self.is_witching_hour(normalized),
            daypart=self.get_daypart(normalized),
        )
        return components

    def is_witching_hour(self, mythos_dt: datetime | None = None) -> bool:
        """Return True when the timestamp falls within the 23:00–01:00 witching window."""

        target = _ensure_utc(mythos_dt or self.get_current_mythos_datetime())
        hour = target.hour
        return hour == 23 or not hour

    def is_daytime(self, mythos_dt: datetime | None = None) -> bool:
        """Return True when the timestamp is between dawn (06:00) and dusk (18:00)."""

        target = _ensure_utc(mythos_dt or self.get_current_mythos_datetime())
        return 6 <= target.hour < 18

    def get_daypart(self, mythos_dt: datetime | None = None) -> str:
        """Return a coarse textual descriptor for the given timestamp."""

        target = _ensure_utc(mythos_dt or self.get_current_mythos_datetime())
        hour = target.hour
        if self.is_witching_hour(target):
            return "witching"
        if 5 <= hour < 7:
            return "dawn"
        if 18 <= hour < 20:
            return "dusk"
        if self.is_daytime(target):
            return "day"
        return "night"

    def advance_mythos(self, delta_hours: float) -> ChronicleState:
        """
        Move the chronicle forward by a number of Mythos hours.

        This helper is primarily used by scheduler integrations and deterministic tests.
        """

        if delta_hours < 0:
            raise ValueError("delta_hours must be positive")

        with self._state_lock:
            delta_mythos = timedelta(hours=delta_hours)
            delta_real = timedelta(hours=delta_hours / self._compression_ratio)
            updated_state = ChronicleState(
                real_timestamp=self._state.real_timestamp + delta_real,
                mythos_timestamp=self._state.mythos_timestamp + delta_mythos,
            )
            self._persist_state(updated_state)
            MYTHOS_TICK_COUNTER.inc(delta_hours)
            logger.debug(
                "Mythos chronicle advanced",
                delta_hours=delta_hours,
                new_real_timestamp=updated_state.real_timestamp.isoformat(),
                new_mythos_timestamp=updated_state.mythos_timestamp.isoformat(),
            )
            return updated_state

    def freeze(self) -> ChronicleState:
        """Capture the current state so the chronicle can resume deterministically after downtime."""

        now_real = datetime.now(UTC)
        mythos_now = self.to_mythos_datetime(now_real)
        new_state = ChronicleState(real_timestamp=now_real, mythos_timestamp=mythos_now)
        with self._state_lock:
            self._persist_state(new_state)
            self._last_freeze_state = new_state
            MYTHOS_FREEZE_COUNTER.inc()
            logger.info(
                "Mythos chronicle frozen",
                real_timestamp=new_state.real_timestamp.isoformat(),
                mythos_timestamp=new_state.mythos_timestamp.isoformat(),
            )
            return new_state

    def get_last_freeze_state(self) -> ChronicleState | None:
        """Return the most recent freeze snapshot, if any."""

        with self._state_lock:
            return self._last_freeze_state

    def _load_state(self) -> ChronicleState:  # pylint: disable=too-many-locals  # Reason: Migration logic requires multiple variables for epoch detection, time calculations, and state conversion
        """Load the chronicle state from disk or initialize from config defaults.

        Includes migration logic to detect and convert old state files from the previous
        system (1930 epoch, 9.6 compression ratio) to the new system (1920 epoch, 4.0 ratio).
        """

        old_epoch = datetime(1930, 1, 1, tzinfo=UTC)
        old_compression_ratio = 9.6
        new_epoch = _ensure_utc(self._config.mythos_epoch)
        new_compression_ratio = self._config.compression_ratio

        if self._state_file.exists():
            try:
                with self._state_file.open("r", encoding="utf-8") as handle:
                    payload = json.load(handle)
                real = _ensure_utc(datetime.fromisoformat(payload["real_timestamp"]))
                mythos = _ensure_utc(datetime.fromisoformat(payload["mythos_timestamp"]))

                # Check if this is an old state file (mythos_timestamp using old epoch)
                # We detect old state by checking if mythos_timestamp is close to old_epoch
                # (within a reasonable threshold of a few years)
                time_from_old_epoch = abs((mythos - old_epoch).total_seconds())
                time_from_new_epoch = abs((mythos - new_epoch).total_seconds())

                # If closer to old epoch than new epoch, this is an old state file
                if time_from_old_epoch < time_from_new_epoch and time_from_old_epoch < (
                    365 * 24 * 3600 * 5
                ):  # Within 5 years of old epoch
                    logger.info(
                        "Detected old chronicle state file, migrating to new system",
                        old_mythos_timestamp=mythos.isoformat(),
                        old_epoch=old_epoch.isoformat(),
                        new_epoch=new_epoch.isoformat(),
                        old_ratio=old_compression_ratio,
                        new_ratio=new_compression_ratio,
                    )

                    # Convert old state to new system
                    # Formula: new_mythos_time = new_epoch + (old_mythos_time - old_epoch) * (new_ratio / old_ratio)
                    time_delta_from_old_epoch = mythos - old_epoch
                    converted_delta = timedelta(
                        seconds=time_delta_from_old_epoch.total_seconds()
                        * (new_compression_ratio / old_compression_ratio)
                    )
                    new_mythos = new_epoch + converted_delta

                    # Create new state with converted timestamp
                    migrated_state = ChronicleState(real_timestamp=real, mythos_timestamp=new_mythos)

                    # Persist the migrated state
                    self._persist_state(migrated_state)

                    logger.info(
                        "Chronicle state migration complete",
                        new_mythos_timestamp=new_mythos.isoformat(),
                    )

                    return migrated_state

                # Not an old state file, return as-is
                return ChronicleState(real_timestamp=real, mythos_timestamp=mythos)
            except (OSError, KeyError, ValueError) as error:
                logger.error(
                    "Failed to load chronicle state, falling back to configured epochs",
                    error=str(error),
                    state_file=str(self._state_file),
                )
        # No state file exists, initialize with new defaults
        return ChronicleState(
            real_timestamp=_ensure_utc(self._config.real_epoch_utc),
            mythos_timestamp=new_epoch,
        )

    def _persist_state(self, state: ChronicleState) -> None:
        """Persist the provided state atomically."""

        payload = {
            "real_timestamp": _ensure_utc(state.real_timestamp).isoformat(),
            "mythos_timestamp": _ensure_utc(state.mythos_timestamp).isoformat(),
        }
        self._state_file.parent.mkdir(parents=True, exist_ok=True)
        tmp_fd, tmp_path = tempfile.mkstemp(prefix="chronicle_", suffix=".json", dir=str(self._state_file.parent))
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as handle:
                json.dump(payload, handle)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp_path, self._state_file)
            self._state = state
        except OSError as error:
            logger.error("Failed to persist chronicle state", error=str(error), state_file=str(self._state_file))
            raise
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    @staticmethod
    def _hours_between(lhs: datetime, rhs: datetime) -> float:
        """Return the difference between two timestamps expressed in hours."""

        delta = lhs - rhs
        return delta.total_seconds() / 3600.0


def get_mythos_chronicle() -> MythosChronicle:
    """Convenience wrapper mirroring other service access patterns."""

    return MythosChronicle.get_instance()


def _season_for_month(month: int) -> str:
    """Return the lore-friendly season label for the provided month number."""

    return _SEASON_BY_MONTH.get(month, "unknown")
