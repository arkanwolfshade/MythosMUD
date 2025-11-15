from __future__ import annotations

import json
import os
import tempfile
import threading
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

from prometheus_client import Counter

from server.config import get_config
from server.logging.enhanced_logging_config import get_logger

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


@dataclass(frozen=True)
class ChronicleState:
    """
    Snapshot of the chronicle's reference timestamps.

    The last frozen real timestamp and its Mythos counterpart anchor all future conversions,
    just as noted in the Pnakotic Manuscripts' treatment of calendrical drift.
    """

    real_timestamp: datetime
    mythos_timestamp: datetime


def _ensure_utc(value: datetime) -> datetime:
    """Normalize datetimes to UTC for deterministic math."""

    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


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
            MYTHOS_FREEZE_COUNTER.inc()
            logger.info(
                "Mythos chronicle frozen",
                real_timestamp=new_state.real_timestamp.isoformat(),
                mythos_timestamp=new_state.mythos_timestamp.isoformat(),
            )
            return new_state

    def _load_state(self) -> ChronicleState:
        """Load the chronicle state from disk or initialize from config defaults."""

        if self._state_file.exists():
            try:
                with self._state_file.open("r", encoding="utf-8") as handle:
                    payload = json.load(handle)
                real = _ensure_utc(datetime.fromisoformat(payload["real_timestamp"]))
                mythos = _ensure_utc(datetime.fromisoformat(payload["mythos_timestamp"]))
                return ChronicleState(real_timestamp=real, mythos_timestamp=mythos)
            except (OSError, KeyError, ValueError) as error:
                logger.error(
                    "Failed to load chronicle state, falling back to configured epochs",
                    error=str(error),
                    state_file=str(self._state_file),
                )
        return ChronicleState(
            real_timestamp=_ensure_utc(self._config.real_epoch_utc),
            mythos_timestamp=_ensure_utc(self._config.mythos_epoch),
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
