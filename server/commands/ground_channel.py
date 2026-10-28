"""
Timed grounding ritual (#713): channel registry, channel task, and interruption.

`/ground` used to lift a catatonic target instantly, so the rescue banner had nothing to show.
It now channels for `GameConfig.ground_channel_seconds`. The same things that interrupt `/rest`
(movement, spellcasting, combat, disconnect) interrupt the channel, on either participant, and
an interruption on either side ends it for both.

This module owns only the channel lifecycle. The lucidity adjustment (`finish`) and the event
sender (`notify`) are injected by `rescue_commands`: importing `rescue_commands`, `rest_command` or
the `services` package from here would close an import cycle, because combat code (in `services`)
imports this module to interrupt channels. It reads `resting_players` directly for the same reason.
"""

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Literal, Protocol, cast

from ..config import get_config
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# "done": finish already sent the terminal (success/failed) events. "interrupted": the target no
# longer needs or can receive the ritual; the channel tells both participants.
FinishOutcome = Literal["done", "interrupted"]
Finish = Callable[[], Awaitable[FinishOutcome]]


class RescueNotifier(Protocol):
    """The slice of `send_rescue_update_event` this module calls."""

    def __call__(
        self,
        player_id: uuid.UUID | str,
        *,
        status: str,
        role: Literal["rescuer", "target"] | None = None,
        rescuer_name: str | None = None,
        target_name: str | None = None,
        message: str | None = None,
        eta_seconds: float | None = None,
    ) -> Awaitable[None]: ...


@dataclass(eq=False)
class GroundChannel:
    """One in-flight grounding ritual."""

    rescuer_id: uuid.UUID
    target_id: uuid.UUID
    rescuer_name: str
    target_name: str
    notify: RescueNotifier
    # Set once the sleep elapses: the DB commit is running and must not be cancelled mid-flight.
    committing: bool = False
    task: asyncio.Task[None] | None = None


def ground_channel_seconds() -> float:  # lizard: allow - test seam, mirrors rest_countdown_seconds()
    """Channel duration from `GameConfig` (#713), retunable via `GAME_GROUND_CHANNEL_SECONDS`."""
    return get_config().game.ground_channel_seconds


def _registries(manager: object) -> tuple[dict[uuid.UUID, GroundChannel], dict[uuid.UUID, uuid.UUID]] | None:
    """(channels by target id, target id by rescuer id), or None if the manager has no registries."""
    channels = getattr(manager, "grounding_channels", None)
    by_rescuer = getattr(manager, "grounding_by_rescuer", None)
    if not isinstance(channels, dict) or not isinstance(by_rescuer, dict):
        return None
    return cast(dict[uuid.UUID, GroundChannel], channels), cast(dict[uuid.UUID, uuid.UUID], by_rescuer)


def _find_channel(manager: object, player_id: uuid.UUID) -> GroundChannel | None:
    """The channel `player_id` takes part in, as target or as rescuer."""
    registries = _registries(manager)
    if registries is None:
        return None
    channels, by_rescuer = registries
    channel = channels.get(player_id)
    if channel is None and player_id in by_rescuer:
        channel = channels.get(by_rescuer[player_id])
    return channel


def is_player_grounding(player_id: uuid.UUID, manager: object) -> bool:
    """True if the player is channeling, or being grounded, right now."""
    return _find_channel(manager, player_id) is not None


def _unregister(manager: object, channel: GroundChannel) -> None:
    registries = _registries(manager)
    if registries is None:
        return
    channels, by_rescuer = registries
    if channels.get(channel.target_id) is channel:
        del channels[channel.target_id]
    if by_rescuer.get(channel.rescuer_id) == channel.target_id:
        del by_rescuer[channel.rescuer_id]


async def _send_to_both(
    channel: GroundChannel,
    status: str,
    *,
    target_message: str,
    rescuer_message: str,
    eta_seconds: float | None = None,
) -> None:
    await channel.notify(
        channel.target_id,
        status=status,
        role="target",
        rescuer_name=channel.rescuer_name,
        target_name=channel.target_name,
        message=target_message,
        eta_seconds=eta_seconds,
    )
    await channel.notify(
        channel.rescuer_id,
        status=status,
        role="rescuer",
        rescuer_name=channel.rescuer_name,
        target_name=channel.target_name,
        message=rescuer_message,
        eta_seconds=eta_seconds,
    )


async def _send_interrupted(channel: GroundChannel) -> None:
    await _send_to_both(
        channel,
        "interrupted",
        target_message="The grounding ritual is broken; the static presses in again.",
        rescuer_message="Your concentration breaks; the grounding ritual is interrupted.",
    )


async def _run_channel(manager: object, channel: GroundChannel, eta: float, finish: Finish) -> None:
    try:
        await asyncio.sleep(eta)
        channel.committing = True
        if await finish() == "interrupted":
            await _send_interrupted(channel)
    except asyncio.CancelledError:
        logger.debug("Ground channel task cancelled", target_id=channel.target_id)
    except (AttributeError, RuntimeError, ValueError, TypeError, KeyError, OSError) as e:
        logger.error("Error in ground channel task", target_id=channel.target_id, error=str(e), exc_info=True)
        await _send_interrupted(channel)
    finally:
        _unregister(manager, channel)


async def start_ground_channel(  # noqa: PLR0913  # Reason: one keyword per participant fact, kept explicit
    manager: object,
    *,
    rescuer_id: uuid.UUID,
    target_id: uuid.UUID,
    rescuer_name: str,
    target_name: str,
    finish: Finish,
    notify: RescueNotifier,
) -> str | None:
    """Begin the ritual. Returns a message for the rescuer if it cannot start, else None."""
    registries = _registries(manager)
    if registries is None:
        return "The ritual cannot be anchored right now."
    channels, by_rescuer = registries
    if rescuer_id in by_rescuer:
        return "You are already channeling a grounding ritual."
    if target_id in channels:
        return f"{target_name} is already being grounded."
    resting = getattr(manager, "resting_players", None)
    if isinstance(resting, dict) and rescuer_id in resting:
        return "You cannot channel a grounding ritual while resting."

    channel = GroundChannel(rescuer_id, target_id, rescuer_name, target_name, notify)
    channels[target_id] = channel
    by_rescuer[rescuer_id] = target_id
    eta = ground_channel_seconds()
    # Create the task before the first await so an interrupt during the notification below
    # always finds a task to cancel.
    channel.task = asyncio.create_task(_run_channel(manager, channel, eta, finish))
    await _send_to_both(
        channel,
        "channeling",
        target_message=f"{rescuer_name} kneels beside you and begins the grounding ritual.",
        rescuer_message=f"You steady {target_name} and begin channeling focus.",
        eta_seconds=eta,
    )
    return None


async def cancel_ground_channel(player_id: uuid.UUID, manager: object) -> None:
    """Interrupt the channel `player_id` takes part in, as rescuer or target.

    No-op if there is none, or if the adjustment is already committing.
    """
    channel = _find_channel(manager, player_id)
    if channel is None or channel.committing:
        return
    logger.info("Cancelling ground channel", player_id=player_id, target_id=channel.target_id)
    _unregister(manager, channel)
    task = channel.task
    if task is not None and task is not asyncio.current_task():
        _ = task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
    await _send_interrupted(channel)
