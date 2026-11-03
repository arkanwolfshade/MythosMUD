"""
Player Respawn Service for managing player resurrection and limbo state.

This service handles player death transitions, limbo room placement, and respawn mechanics.
As documented in the Pnakotic Manuscripts, resurrection requires careful navigation of
the spaces between worlds.

Each transition is one player registry unit, and a sync one (ADR-029 step 6a): the room, DP, posture, death room and
(for a delirium or sanitarium respawn) the lucidity and pending debrief commit together.
"""

from __future__ import annotations

# pylint: disable=too-many-locals,too-many-statements,too-many-lines  # Reason: Respawn service requires many intermediate variables and statements for complex respawn logic; single cohesive module preferred over split.
import random
import uuid
from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Protocol

from sqlalchemy.exc import SQLAlchemyError

from ..constants.spawn_defaults import DEFAULT_RESPAWN_ROOM, LIMBO_ROOM_ID, RECOVERY_WARD_ROOM_ID
from ..events.event_types import BaseEvent, PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from ..exceptions import DatabaseError
from ..game.first_exposure import (
    RESTORED_LCD,
    FinishFirstExposure,
    apply_first_exposure_end_state,
    tutorial_instance_of,
)
from ..game.instance_manager import is_template_room, template_exit_room_id
from ..game.player_registry import PlayerNotFoundError
from ..models.player_dp import DEAD_DP, dp_of, restored
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from ..utils.liability_types import LiabilityStackEntry
from .debrief_service import mark_debrief_pending
from .lucidity_helpers import LIABILITY_CATALOG, decode_liabilities, encode_liabilities, resolve_tier
from .lucidity_tier_cache import lucidity_tier_cache
from .player_health_service import PlayerHealthService
from .player_respawn_state import (
    apply_sanitarium_player_state,
    apply_standard_respawn_state,
    log_lucidity_respawn,
    log_standard_respawn,
    record_death_room,
)

if TYPE_CHECKING:
    from ..game.player_registry import PlayerAggregate, PlayerRegistry, PlayerView

logger = get_logger(__name__)

# Lucidity a delirium respawn restores, and a sanitarium respawn (LCD -100) resets to (Deranged tier).
DELIRIUM_RESPAWN_LCD = 10
SANITARIUM_RESPAWN_LCD = 1
MAX_LIABILITY_STACKS = 5

# Protocol stub bodies use Ellipsis per PEP 544; Pylint W2301 conflicts with pyright if replaced with pass.
# pylint: disable=unnecessary-ellipsis


class _RespawnEventPublisher(Protocol):
    """Minimal surface used by this service to publish respawn-related events."""

    def publish(self, event: BaseEvent) -> None:
        """Deliver a respawn-related domain event to the game's event bus."""
        ...


class _PlayerCombatClearing(Protocol):
    """Minimal surface used to clear combat state when a player respawns."""

    async def clear_player_combat_state(self, player_id: uuid.UUID) -> None:
        """Drop combat involvement for this player after respawn."""
        ...


class _RandomChoiceSource(Protocol):
    """Subset of random.Random / random module API used for liability picks."""

    def choice(self, seq: Sequence[str]) -> str:
        """Return one element from a non-empty sequence of liability codes."""
        ...


def raise_sanitarium_liabilities(
    liabilities: list[LiabilityStackEntry], random_module: _RandomChoiceSource
) -> list[LiabilityStackEntry]:
    """A sanitarium stay: one more stack of every liability (at most 5), or one new liability if there are none."""
    if liabilities:
        return [
            {"code": entry["code"], "stacks": min(entry["stacks"] + 1, MAX_LIABILITY_STACKS)} for entry in liabilities
        ]
    return [{"code": random_module.choice(LIABILITY_CATALOG), "stacks": 1}]  # nosec B311 - Game mechanics, not security-critical


class PlayerRespawnService:
    """
    Service for managing player respawn and limbo state.

    This service handles:
    - Moving dead players to limbo (isolated from game world)
    - Determining respawn location (custom or default)
    - Restoring player DP and moving to respawn room
    - Publishing respawn events for UI updates
    - Clearing combat state when player respawns
    """

    def __init__(
        self,
        event_bus: _RespawnEventPublisher | None = None,
        player_combat_service: _PlayerCombatClearing | None = None,
        room_lookup: Callable[[str], Room | None] | None = None,
        first_exposure_finish: FinishFirstExposure | None = None,
        player_registry: PlayerRegistry | None = None,
    ) -> None:
        """
        Initialize the player respawn service.

        Args:
            event_bus: Optional event bus for publishing events
            player_combat_service: Optional player combat service for clearing combat state
            room_lookup: Optional room-by-id lookup; lets a respawn room that is an instance
                template be redirected to that template's exit room
            first_exposure_finish: Optional post-commit hook that finishes the First Exposure tutorial
                (corruption floor, epilogue quest, instance flush) for a player who was inside it
            player_registry: Holds the player (ADR-029): every transition here is one unit on it
        """
        self._event_bus: _RespawnEventPublisher | None = event_bus
        self._player_combat_service: _PlayerCombatClearing | None = player_combat_service
        self._room_lookup: Callable[[str], Room | None] | None = room_lookup
        self._first_exposure_finish: FinishFirstExposure | None = first_exposure_finish
        self._player_registry: PlayerRegistry | None = player_registry
        logger.info(
            "PlayerRespawnService initialized",
            event_bus_available=bool(event_bus),
            player_combat_service_available=bool(player_combat_service),
        )

    def _redirect_template_respawn(self, player_id: uuid.UUID, respawn_room_id: str) -> str:
        """A template room is never entered directly: respawn at its exit room instead.

        ponytail: always the exit room, never the player's live instance -- the only template
        today (tutorial bedroom) is no_death, so a respawn into a live instance cannot happen.
        Route to the instance once an instance template allows death.
        """
        room = self._room_lookup(respawn_room_id) if self._room_lookup else None
        if room is None or not is_template_room(room):
            return respawn_room_id
        exit_room_id = template_exit_room_id(room)
        logger.warning(
            "Respawn room is an instance template; using its exit room",
            player_id=player_id,
            template_room_id=respawn_room_id,
            exit_room_id=exit_room_id,
        )
        return exit_room_id

    @staticmethod
    def _can_move_to_limbo(player: PlayerAggregate, death_location: str) -> tuple[bool, int]:
        """Return (allowed, current_dp) for the limbo move: only the dead (DP -10 or lower) or a catatonia failover."""
        if death_location == "catatonia_failover":
            return True, 0
        current_dp = dp_of(player.row.stats)
        return current_dp <= DEAD_DP, current_dp

    def _publish_delirium_respawn_event(
        self,
        player_id: uuid.UUID,
        player_name: str,
        respawn_room: str,
        old_lucidity: int,
        new_lucidity: int,
        old_room: str,
    ) -> None:
        """Publish delirium respawn event when event bus is available."""
        if not self._event_bus:
            return
        event = PlayerDeliriumRespawnedEvent(
            player_id=player_id,
            player_name=player_name,
            respawn_room_id=respawn_room,
            old_lucidity=old_lucidity,
            new_lucidity=new_lucidity,
            delirium_location=old_room if old_room != LIMBO_ROOM_ID else None,
        )
        self._event_bus.publish(event)

    async def current_lcd(self, player_id: uuid.UUID) -> int | None:
        """The player's lucidity from the registry, or None without one (or with no such player)."""
        if self._player_registry is None:
            logger.error("Respawn lucidity unavailable: no player registry", player_id=player_id)
            return None
        player = await self._player_registry.get(player_id)
        return player.lucidity.lcd if player is not None else None

    async def player_view(self, player_id: uuid.UUID) -> PlayerView | None:
        """The player as the registry holds them (where a respawn left them), or None without one or such a player."""
        if self._player_registry is None:
            return None
        return await self._player_registry.get(player_id)

    @staticmethod
    def _apply_respawn_lucidity(player: PlayerAggregate, lcd: int, *, sanitarium: bool = False) -> None:
        """Inside the respawn's unit: set the player's lucidity (and, for the sanitarium, raise their liabilities),
        and leave the pending debrief. The caller sets the tier cache once the unit has committed."""
        liabilities = None
        if sanitarium:
            raised = raise_sanitarium_liabilities(decode_liabilities(player.lucidity.data.liabilities), random)
            liabilities = encode_liabilities(raised)
        _ = player.lucidity.set(lcd=lcd, tier=resolve_tier(lcd), liabilities=liabilities)
        mark_debrief_pending(player)

    def _registry(self, player_id: uuid.UUID, operation: str) -> PlayerRegistry | None:
        if self._player_registry is None:
            logger.error("No player registry; cannot respawn", player_id=player_id, operation=operation)
        return self._player_registry

    async def _clear_respawn_combat_state(self, player_id: uuid.UUID, respawn_context: str) -> None:
        """Clear combat state for a respawning player, logging and swallowing DB errors."""
        if not self._player_combat_service:
            return
        try:
            await self._player_combat_service.clear_player_combat_state(player_id)
            logger.info(
                "Cleared combat state for respawned player", player_id=player_id, respawn_context=respawn_context
            )
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error(
                "Error clearing combat state for respawned player",
                player_id=player_id,
                respawn_context=respawn_context,
                error=str(e),
                exc_info=True,
            )

    def _publish_standard_respawn_event(
        self,
        player_id: uuid.UUID,
        player_name: str,
        respawn_room: str,
        stats: Mapping[str, object],
        old_room: str,
    ) -> None:
        """Publish standard respawn event when event bus is available."""
        if not self._event_bus:
            return
        event = PlayerRespawnedEvent(
            player_id=player_id,
            player_name=player_name,
            respawn_room_id=respawn_room,
            old_dp=coerce_int(stats.get("current_dp"), default=0),
            new_dp=coerce_int(stats.get("max_dp"), default=100),
            death_room_id=old_room if old_room != LIMBO_ROOM_ID else None,
        )
        self._event_bus.publish(event)

    @staticmethod
    def _prepare_delirium_respawn(player: PlayerAggregate) -> tuple[str, str, int, int]:
        """Inside the unit: full health in the Recovery Ward (or a finished tutorial's end state), and the lucidity it
        restores; returns (respawn_room, old_room, old_lucidity, new_lucidity)."""
        old_lucidity, new_lucidity = player.lucidity.lcd, DELIRIUM_RESPAWN_LCD
        respawn_room = RECOVERY_WARD_ROOM_ID
        old_room = player.row.current_room_id
        if apply_first_exposure_end_state(player):
            new_lucidity = RESTORED_LCD
        else:  # unlike a death, the death room is kept
            _ = PlayerHealthService.apply_in(player, restored(player.row.stats))
            player.row.set_current_room_id(respawn_room, sync=True)
        return respawn_room, old_room, old_lucidity, new_lucidity

    async def move_player_to_limbo(self, player_id: uuid.UUID, death_location: str) -> bool:
        """
        Move a dead player to the limbo room, as one sync registry unit.

        The limbo room completely isolates the player from the game world
        during the death/respawn sequence.

        Args:
            player_id: ID of the player to move
            death_location: Room ID where the player died (for reference)

        Returns:
            True if player was moved to limbo, False otherwise
        """
        registry = self._registry(player_id, "move_player_to_limbo")
        if registry is None:
            return False
        try:
            async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                # Player must be at -10 or lower DP before moving to limbo (death transition).
                # Catatonia failover is the only exception (lucidity-based, not DP).
                can_move, current_dp = self._can_move_to_limbo(player, death_location)
                if not can_move:
                    logger.warning(
                        "Refusing to move player to limbo: DP must be -10 or lower",
                        player_id=player_id,
                        current_dp=current_dp,
                    )
                    return False
                old_room = player.row.current_room_id
                # Record where they died before overwriting the room with limbo.
                record_death_room(player, death_location or old_room)
                player.row.set_current_room_id(LIMBO_ROOM_ID, sync=True)
                player_name = player.row.name
        except PlayerNotFoundError:
            logger.warning("Player not found for limbo movement", player_id=player_id)
            return False
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error moving player to limbo", player_id=player_id, error=str(e), exc_info=True)
            return False
        logger.info(
            "Player moved to limbo",
            player_id=player_id,
            player_name=player_name,
            from_room=old_room,
            death_location=death_location,
        )
        return True

    def _respawn_room_of(self, player: PlayerView) -> str:
        """The player's custom respawn room if set (redirected out of a template), else the default foyer."""
        respawn_room_id = player.row.respawn_room_id
        if respawn_room_id:
            return self._redirect_template_respawn(player.row.player_id, respawn_room_id)
        return DEFAULT_RESPAWN_ROOM

    async def get_respawn_room(self, player_id: uuid.UUID) -> str:
        """
        Get the respawn room for a player.

        Returns the player's custom respawn room if set, otherwise returns
        the default respawn room (Arkham Sanitarium foyer).

        Args:
            player_id: ID of the player

        Returns:
            Room ID for respawn location
        """
        registry = self._registry(player_id, "get_respawn_room")
        player = await registry.get(player_id) if registry is not None else None
        if player is None:
            logger.warning("Player not found for respawn room lookup, using default", player_id=player_id)
            return DEFAULT_RESPAWN_ROOM
        return self._respawn_room_of(player)

    async def respawn_player(self, player_id: uuid.UUID) -> bool:
        """
        Respawn a dead player at their respawn location with full DP, as one sync registry unit.

        This method:
        1. Restores player DP to their max_dp (not hardcoded 100)
        2. Moves player from limbo to respawn room
        3. Publishes respawn event for UI updates

        Args:
            player_id: ID of the player to respawn

        Returns:
            True if respawn was successful, False otherwise
        """
        registry = self._registry(player_id, "respawn_player")
        if registry is None:
            return False
        try:
            async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                respawn_room = self._respawn_room_of(player)
                change, old_room = apply_standard_respawn_state(player, respawn_room)
                player_name = player.row.name
        except PlayerNotFoundError:
            logger.warning("Player not found for respawn", player_id=player_id)
            return False
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player", player_id=player_id, error=str(e), exc_info=True)
            return False

        # BUGFIX #244: clear combat state on resurrection to prevent stale combat continuity.
        await self._clear_respawn_combat_state(player_id=player_id, respawn_context="standard")
        log_standard_respawn(player_name, player_id, respawn_room, change, old_room)
        self._publish_standard_respawn_event(
            player_id=player_id,
            player_name=player_name,
            respawn_room=respawn_room,
            stats={"current_dp": change.old_dp, "max_dp": change.max_dp},
            old_room=old_room,
        )
        return True

    async def _finish_first_exposure(self, player_id: uuid.UUID, instance_id: str | None) -> None:
        """After the respawn committed: finish the tutorial the player just left. Never fails the respawn."""
        if not instance_id or self._first_exposure_finish is None:
            return
        try:
            await self._first_exposure_finish(player_id, instance_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: the respawn already committed; a failed finish must not turn it into an error
            logger.error("First Exposure finish failed", player_id=player_id, instance_id=instance_id, error=str(e))

    async def respawn_player_from_delirium(self, player_id: uuid.UUID) -> bool:
        """
        Respawn a delirious player in the Sanitarium Recovery Ward with restored lucidity, as one sync registry unit.

        This method:
        1. Restores full DP and sets player lucidity to 10 (70 at the end of the tutorial)
        2. Moves player to the Recovery Ward (RECOVERY_WARD_ROOM_ID) and leaves a pending debrief
        3. Publishes delirium respawn event for UI updates

        Args:
            player_id: ID of the player to respawn

        Returns:
            True if respawn was successful, False otherwise
        """
        registry = self._registry(player_id, "respawn_player_from_delirium")
        if registry is None:
            return False
        try:
            async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                first_exposure_instance = tutorial_instance_of(player)
                respawn_room, old_room, old_lucidity, new_lucidity = self._prepare_delirium_respawn(player)
                self._apply_respawn_lucidity(player, new_lucidity)
                player_name = player.row.name
        except PlayerNotFoundError:
            logger.warning("Player not found for delirium respawn", player_id=player_id)
            return False
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player from delirium", player_id=player_id, error=str(e), exc_info=True)
            return False
        lucidity_tier_cache.set_tier(player_id, resolve_tier(new_lucidity))

        await self._clear_respawn_combat_state(player_id=player_id, respawn_context="delirium")
        log_lucidity_respawn("delirium", player_name, player_id, respawn_room, (old_lucidity, new_lucidity), old_room)
        self._publish_delirium_respawn_event(
            player_id=player_id,
            player_name=player_name,
            respawn_room=respawn_room,
            old_lucidity=old_lucidity,
            new_lucidity=new_lucidity,
            old_room=old_room,
        )
        await self._finish_first_exposure(player_id, first_exposure_instance)
        return True

    async def respawn_player_from_sanitarium(self, player_id: uuid.UUID) -> bool:
        """
        Respawn a player from sanitarium failover at LCD -100, as one sync registry unit.

        This method:
        1. Sets player lucidity to 1 (Deranged tier)
        2. Moves player to the Recovery Ward (RECOVERY_WARD_ROOM_ID) and leaves a pending debrief
        3. Increases liability stages (or adds one if none exist)
        4. Publishes sanitarium respawn event for UI updates

        Args:
            player_id: ID of the player to respawn

        Returns:
            True if respawn was successful, False otherwise
        """
        registry = self._registry(player_id, "respawn_player_from_sanitarium")
        if registry is None:
            return False
        respawn_room, new_lucidity = RECOVERY_WARD_ROOM_ID, SANITARIUM_RESPAWN_LCD
        try:
            async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                old_lucidity = player.lucidity.lcd
                old_room = apply_sanitarium_player_state(player, respawn_room)
                self._apply_respawn_lucidity(player, new_lucidity, sanitarium=True)
                stats = dict(player.row.stats)
                player_name = player.row.name
        except PlayerNotFoundError:
            logger.warning("Player not found for sanitarium respawn", player_id=player_id)
            return False
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player from sanitarium", player_id=player_id, error=str(e), exc_info=True)
            return False
        lucidity_tier_cache.set_tier(player_id, resolve_tier(new_lucidity))

        await self._clear_respawn_combat_state(player_id=player_id, respawn_context="sanitarium")
        log_lucidity_respawn("sanitarium", player_name, player_id, respawn_room, (old_lucidity, new_lucidity), old_room)
        self._publish_standard_respawn_event(
            player_id=player_id,
            player_name=player_name,
            respawn_room=respawn_room,
            stats=stats,
            old_room=old_room,
        )
        return True
