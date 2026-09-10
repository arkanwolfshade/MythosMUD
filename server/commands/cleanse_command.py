"""Cleansing rite that pares back corruption's grip on the mind."""

# pylint: disable=missing-function-docstring  # Reason: Protocol method stubs; contracts live in class docstrings
# pylint: disable=too-few-public-methods  # Reason: Protocol stubs, no behavior needed

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import Protocol, cast

from ..alias_storage import AliasStorage
from ..services.corruption_service import (
    CorruptionActionOnCooldownError,
    CorruptionPersistencePlayer,
    CorruptionService,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.command_parser import get_username_from_user

logger = get_logger(__name__)

_ACTION_CODE = "cleanse"


class CleanseTargetPlayer(CorruptionPersistencePlayer, Protocol):
    """Player surface needed by the cleanse command, beyond corruption stat access."""

    player_id: uuid.UUID | str
    current_room_id: str | None


class CleansePersistence(Protocol):
    """Persistence surface the cleanse command and `CorruptionService` both need.

    `get_player_by_id`/`save_player` are typed against `CorruptionPersistencePlayer` (not the
    richer `CleanseTargetPlayer`) so this Protocol matches `CorruptionPersistenceProtocol`
    exactly on the members they share -- narrowing those parameter types here would make this
    Protocol structurally incompatible with the one `CorruptionService.__init__` expects.
    """

    async def get_player_by_name(self, name: str) -> CleanseTargetPlayer | None: ...
    async def get_player_by_id(self, player_id: uuid.UUID) -> CorruptionPersistencePlayer | None: ...
    async def save_player(self, player: CorruptionPersistencePlayer) -> None: ...


class CleanseContainer(Protocol):
    """DI container surface exposing the async persistence layer."""

    @property
    def async_persistence(self) -> CleansePersistence: ...


class CleanseAppState(Protocol):
    """FastAPI app.state fields required by the cleanse command."""

    container: CleanseContainer | None
    persistence: CleansePersistence | None


class CleanseApp(Protocol):
    """FastAPI app surface with typed state for the cleanse command."""

    state: CleanseAppState


class CleanseRequest(Protocol):
    """Request surface exposing the app instance."""

    @property
    def app(self) -> CleanseApp | None: ...


def _format_cooldown_message(cooldown_expires_at: datetime) -> dict[str, str]:
    """Format cooldown error message with remaining time."""
    expiry = cooldown_expires_at if cooldown_expires_at.tzinfo is not None else cooldown_expires_at.replace(tzinfo=UTC)
    remaining_seconds = max(0.0, (expiry - datetime.now(UTC)).total_seconds())
    remaining_hours = remaining_seconds / 3600
    return {
        "result": (
            "The cleansing rite still lingers in your blood; another so soon would do more harm than "
            f"good. Return in {remaining_hours:.1f} hours to try again."
        )
    }


def _resolve_persistence(request: object) -> CleansePersistence | None:
    """Extract the async persistence layer from the request's app state, container-first."""
    req = cast(CleanseRequest, request)
    app = req.app
    if app is None:
        return None
    if app.state.container is not None:
        return app.state.container.async_persistence
    return app.state.persistence


async def handle_cleanse_command(
    _command_data: dict[str, object],
    current_user: dict[str, object],
    request: object,
    _alias_storage: AliasStorage | None,
    player_name: str,
) -> dict[str, str]:
    """Undertake a cleansing rite to pare back accrued corruption."""
    persistence = _resolve_persistence(request)
    if not persistence:
        logger.error("Cleanse command invoked without persistence", player=player_name)
        return {"result": "The rite falters; the ley lines are inaccessible."}

    username = get_username_from_user(current_user)
    player = await persistence.get_player_by_name(username)
    if not player:
        logger.error("Cleanse command failed to locate player", username=username)
        return {"result": "Your identity wavers in the void. Try again after stabilizing your presence."}

    room_id = player.current_room_id
    service = CorruptionService(persistence)
    try:
        result = await service.perform_recovery_action(
            uuid.UUID(str(player.player_id)),
            action_code=_ACTION_CODE,
            location_id=str(room_id) if room_id else None,
        )
    except CorruptionActionOnCooldownError:
        expiry = await service.get_cooldown_expiry(uuid.UUID(str(player.player_id)), _ACTION_CODE)
        if expiry:
            return _format_cooldown_message(expiry)
        return {"result": "The rite's residue has not yet faded; patience is required."}

    return {
        "result": (
            f"You complete the cleansing rite. Corruption recedes by {abs(result.delta)}, "
            f"settling at {result.new_value}/100."
        )
    }


__all__ = ["handle_cleanse_command"]
