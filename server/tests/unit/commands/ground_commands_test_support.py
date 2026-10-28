"""Typed fakes for the /ground tests (#713): recording notifier, persistence, DB session, lucidity service.

Small hand-written fakes with real methods, shared by `test_ground_channel.py` and
`test_rescue_commands.py`, so the tests read real attributes instead of chains of MagicMock.
"""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from types import SimpleNamespace

from server.commands.ground_channel import GroundChannel
from server.models.lucidity import PlayerLucidity


@dataclass
class SentRescueEvent:
    """One rescue_update the code under test tried to send."""

    player_id: uuid.UUID | str
    status: str
    role: str | None
    eta_seconds: float | None
    message: str | None


class RescueEventRecorder:
    """Satisfies `ground_channel.RescueNotifier`: records every event instead of dispatching it."""

    def __init__(self) -> None:
        self.sent: list[SentRescueEvent] = []

    async def __call__(  # noqa: PLR0913  # Reason: mirrors send_rescue_update_event's keyword surface
        self,
        player_id: uuid.UUID | str,
        *,
        status: str,
        role: str | None = None,
        current_lcd: int | None = None,  # noqa: ARG002  # Reason: accepted to match send_rescue_update_event
        rescuer_name: str | None = None,  # noqa: ARG002  # Reason: accepted to match send_rescue_update_event
        target_name: str | None = None,  # noqa: ARG002  # Reason: accepted to match send_rescue_update_event
        message: str | None = None,
        progress: float | None = None,  # noqa: ARG002  # Reason: accepted to match send_rescue_update_event
        eta_seconds: float | None = None,
    ) -> None:
        self.sent.append(SentRescueEvent(player_id, status, role, eta_seconds, message))

    def with_status(self, status: str) -> list[SentRescueEvent]:
        """Events sent with the given status, in send order."""
        return [e for e in self.sent if e.status == status]

    def status_roles(self) -> set[tuple[str, str | None]]:
        """(status, role) pairs sent so far."""
        return {(e.status, e.role) for e in self.sent}


class FakeConnectionManager:
    """The connection-manager attributes the ground channel reads and writes."""

    def __init__(self) -> None:
        self.grounding_channels: dict[uuid.UUID, GroundChannel] = {}
        self.grounding_by_rescuer: dict[uuid.UUID, uuid.UUID] = {}
        self.resting_players: dict[uuid.UUID, object] = {}


@dataclass
class FakePlayer:
    """A player as `ground` reads it."""

    player_id: uuid.UUID
    current_room_id: str | None


class FakePersistence:
    """Persistence stand-in serving players by name."""

    def __init__(self, players: dict[str, FakePlayer]) -> None:
        self.players: dict[str, FakePlayer] = players

    async def get_player_by_name(self, name: str) -> FakePlayer | None:
        """Look a player up by name."""
        return self.players.get(name)


class FakeSession:
    """DB session stand-in: serves one lucidity record and counts rollbacks."""

    def __init__(self, record: PlayerLucidity | None) -> None:
        self.record: PlayerLucidity | None = record
        self.rollbacks: int = 0

    async def get(self, _model: object, _key: str) -> PlayerLucidity | None:
        """Return the configured record."""
        return self.record

    async def commit(self) -> None:
        """Accept the commit."""

    async def rollback(self) -> None:
        """Count the rollback."""
        self.rollbacks += 1

    async def factory(self) -> AsyncIterator[FakeSession]:
        """Stand-in for `get_async_session()`: yields this session once per call."""
        yield self


@dataclass(frozen=True)
class FakeAdjustmentResult:
    """The only field of `LucidityUpdateResult` that `ground` reads."""

    new_lcd: int


@dataclass
class FakeLucidityService:
    """Lucidity service stand-in; raises `error` if configured, else grounds to LCD 1."""

    error: Exception | None = None
    calls: list[tuple[uuid.UUID, str]] = field(default_factory=list)

    async def apply_lucidity_adjustment(  # noqa: PLR0913  # Reason: mirrors LucidityService's signature
        self,
        player_id: uuid.UUID,
        _delta: int,
        *,
        reason_code: str,
        **_extra: object,  # metadata / location_id: accepted to match the real signature, unused here
    ) -> FakeAdjustmentResult:
        """Record the call, then fail or succeed as configured."""
        self.calls.append((player_id, reason_code))
        if self.error is not None:
            raise self.error
        return FakeAdjustmentResult(new_lcd=1)


def catatonic_record(tier: str = "catatonic") -> PlayerLucidity:
    """A lucidity record at LCD 0 in the given tier."""
    return PlayerLucidity(player_id=str(uuid.uuid4()), current_lcd=0, current_tier=tier)


def ground_request(persistence: FakePersistence, manager: FakeConnectionManager) -> SimpleNamespace:
    """A request whose app.state carries the services `handle_ground_command` resolves."""
    state = SimpleNamespace(
        persistence=persistence, catatonia_registry=None, container=None, connection_manager=manager
    )
    return SimpleNamespace(app=SimpleNamespace(state=state))
