"""
Player Respawn Service for managing player resurrection and limbo state.

This service handles player death transitions, limbo room placement, and respawn mechanics.
As documented in the Pnakotic Manuscripts, resurrection requires careful navigation of
the spaces between worlds.
"""

from __future__ import annotations

# pylint: disable=too-many-locals,too-many-statements,too-many-lines  # Reason: Respawn service requires many intermediate variables and statements for complex respawn logic; single cohesive module preferred over split.
import random
import uuid
from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Protocol, cast

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

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
from ..models.player import Player
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from ..utils.liability_types import LiabilityStackEntry
from .debrief_service import mark_debrief_pending
from .lucidity_helpers import LIABILITY_CATALOG, decode_liabilities, encode_liabilities, resolve_tier
from .lucidity_repository import LucidityRepository
from .lucidity_tier_cache import lucidity_tier_cache
from .player_respawn_state import (
    apply_sanitarium_player_state,
    apply_standard_respawn_state,
    log_delirium_respawn,
    log_sanitarium_respawn,
    log_standard_respawn,
    normalize_current_dp,
    record_death_room_on_player,
)

if TYPE_CHECKING:
    from ..game.player_registry import PlayerRegistry

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
            player_registry: Holds the player's lucidity (ADR-029 step 5b-i), which a delirium or sanitarium
                respawn resets once its session has committed
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

    def _can_move_to_limbo(self, player: Player, death_location: str) -> tuple[bool, int]:
        """Return (allowed, current_dp_int) for limbo movement gate checks."""
        if death_location == "catatonia_failover":
            return True, 0

        stats = player.get_stats() or {}
        current_dp_int = normalize_current_dp(stats)
        player_is_dead = player.is_dead()

        # Require actual DP <= -10; do not rely on is_dead() alone (defense against bad/stale stats)
        allowed = not (current_dp_int > -10 or not player_is_dead)
        return allowed, current_dp_int

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

    async def _set_respawn_lucidity(self, player_id: uuid.UUID, lcd: int, *, sanitarium: bool = False) -> None:
        """After the respawn commits: set the player's lucidity (and, for the sanitarium, raise their liabilities)."""
        if self._player_registry is None:
            return
        async with self._player_registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            liabilities = None
            if sanitarium:
                raised = raise_sanitarium_liabilities(decode_liabilities(player.lucidity.data.liabilities), random)
                liabilities = encode_liabilities(raised)
            _ = player.lucidity.set(lcd=lcd, tier=resolve_tier(lcd), liabilities=liabilities)
        lucidity_tier_cache.set_tier(player_id, resolve_tier(lcd))

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

    async def _prepare_delirium_respawn(
        self, player_id: uuid.UUID, player: Player, session: AsyncSession
    ) -> tuple[str, str, int, int] | None:
        """Apply the delirium location and debrief updates and return the respawn context.

        The lucidity it returns is set by the caller once the session commits (it lives in the player registry).
        """
        old_lucidity = await self.current_lcd(player_id)
        if old_lucidity is None:
            logger.warning("Lucidity not available for delirium respawn", player_id=player_id)
            return None
        new_lucidity = DELIRIUM_RESPAWN_LCD

        await mark_debrief_pending(LucidityRepository(session), player_id)

        respawn_room = RECOVERY_WARD_ROOM_ID
        _ = player.restore_to_full_health()
        old_room = player.current_room_id
        player.current_room_id = respawn_room
        if apply_first_exposure_end_state(player):
            new_lucidity = RESTORED_LCD
        return respawn_room, old_room, old_lucidity, new_lucidity

    async def _prepare_sanitarium_respawn(
        self, player_id: uuid.UUID, player: Player, session: AsyncSession
    ) -> tuple[str, dict[str, object], str, int, int] | None:
        """Apply the sanitarium state and debrief updates and return the respawn context.

        The lucidity reset and the liability rise are applied by the caller once the session commits.
        """
        old_lucidity = await self.current_lcd(player_id)
        if old_lucidity is None:
            logger.warning("Lucidity not available for sanitarium respawn", player_id=player_id)
            return None

        respawn_room = RECOVERY_WARD_ROOM_ID
        stats, old_room = apply_sanitarium_player_state(player, respawn_room)
        await mark_debrief_pending(LucidityRepository(session), player_id)

        return respawn_room, stats, old_room, old_lucidity, SANITARIUM_RESPAWN_LCD

    async def move_player_to_limbo(self, player_id: uuid.UUID, death_location: str, session: AsyncSession) -> bool:
        """
        Move a dead player to the limbo room.

        The limbo room completely isolates the player from the game world
        during the death/respawn sequence.

        Args:
            player_id: ID of the player to move
            death_location: Room ID where the player died (for reference)
            session: Async database session for player data access

        Returns:
            True if player was moved to limbo, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for limbo movement", player_id=player_id)
                return False

            # Player must be at -10 or lower DP before moving to limbo (death transition).
            # Catatonia failover is the only exception (lucidity-based, not DP).
            can_move, current_dp_int = self._can_move_to_limbo(player, death_location)
            if not can_move:
                logger.warning(
                    "Refusing to move player to limbo: DP must be -10 or lower",
                    player_id=player_id,
                    current_dp=current_dp_int,
                )
                return False

            # Move player to limbo room
            old_room = player.current_room_id
            # Record where they died before overwriting current_room_id with limbo.
            record_death_room_on_player(player, death_location if death_location else str(old_room))
            player.current_room_id = LIMBO_ROOM_ID

            # Commit changes using async API
            await session.commit()

            logger.info(
                "Player moved to limbo",
                player_id=player_id,
                player_name=player.name,
                from_room=old_room,
                death_location=death_location,
            )

            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error moving player to limbo", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error("Unexpected error moving player to limbo", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False

    async def get_respawn_room(self, player_id: uuid.UUID, session: AsyncSession) -> str:
        """
        Get the respawn room for a player.

        Returns the player's custom respawn room if set, otherwise returns
        the default respawn room (Arkham Sanitarium foyer).

        Args:
            player_id: ID of the player
            session: Async database session for player data access

        Returns:
            Room ID for respawn location
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for respawn room lookup, using default", player_id=player_id)
                return DEFAULT_RESPAWN_ROOM

            # Prefer a configured custom respawn room when available, falling back to the
            # default Arkham Sanitarium foyer when none is configured.
            respawn_room_id = cast(str | None, getattr(player, "respawn_room_id", None))
            if respawn_room_id:
                logger.debug(
                    "Using custom respawn room for player",
                    player_id=player_id,
                    custom_respawn_room=respawn_room_id,
                )
                return self._redirect_template_respawn(player_id, respawn_room_id)

            logger.debug(
                "Using default respawn room for player",
                player_id=player_id,
                effective_respawn_room=DEFAULT_RESPAWN_ROOM,
            )
            return DEFAULT_RESPAWN_ROOM

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error getting respawn room, using default", player_id=player_id, error=str(e))
            return DEFAULT_RESPAWN_ROOM
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error("Unexpected error getting respawn room, using default", player_id=player_id, error=str(e))
            return DEFAULT_RESPAWN_ROOM

    async def respawn_player(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Respawn a dead player at their respawn location with full DP.

        This method:
        1. Restores player DP to their max_dp (not hardcoded 100)
        2. Moves player from limbo to respawn room
        3. Publishes respawn event for UI updates

        Args:
            player_id: ID of the player to respawn
            session: Database session for player data access

        Returns:
            True if respawn was successful, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for respawn", player_id=player_id)
                return False

            # Get respawn room using async API
            respawn_room = await self.get_respawn_room(player_id, session)

            old_dp, max_dp, old_room = apply_standard_respawn_state(player, respawn_room)

            # BUGFIX #244: clear combat state on resurrection to prevent stale combat continuity.
            await self._clear_respawn_combat_state(player_id=player_id, respawn_context="standard")

            # Commit changes using async API
            await session.commit()

            log_standard_respawn(player, player_id, respawn_room, old_dp, max_dp, old_room)

            self._publish_standard_respawn_event(
                player_id=player_id,
                player_name=str(player.name),
                respawn_room=respawn_room,
                stats={"current_dp": old_dp, "max_dp": max_dp},
                old_room=old_room,
            )

            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error("Unexpected error respawning player", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False

    async def _finish_first_exposure(self, player_id: uuid.UUID, instance_id: str | None) -> None:
        """After the respawn committed: finish the tutorial the player just left. Never fails the respawn."""
        if not instance_id or self._first_exposure_finish is None:
            return
        try:
            await self._first_exposure_finish(player_id, instance_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: the respawn already committed; a failed finish must not turn it into an error
            logger.error("First Exposure finish failed", player_id=player_id, instance_id=instance_id, error=str(e))

    async def respawn_player_from_delirium(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Respawn a delirious player in the Sanitarium Recovery Ward with restored lucidity.

        This method:
        1. Sets player lucidity to 10
        2. Moves player to the Recovery Ward (RECOVERY_WARD_ROOM_ID) and leaves a pending debrief
        3. Publishes delirium respawn event for UI updates

        Args:
            player_id: ID of the player to respawn
            session: Database session for player data access

        Returns:
            True if respawn was successful, False otherwise
        """
        try:
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for delirium respawn", player_id=player_id)
                return False

            first_exposure_instance = tutorial_instance_of(player)
            prepared = await self._prepare_delirium_respawn(player_id, player, session)
            if not prepared:
                return False
            respawn_room, old_room, old_lucidity, new_lucidity = prepared

            await self._clear_respawn_combat_state(player_id=player_id, respawn_context="delirium")

            # Commit changes using async API
            await session.commit()
            await self._set_respawn_lucidity(player_id, new_lucidity)

            log_delirium_respawn(player, player_id, respawn_room, old_lucidity, new_lucidity, old_room)

            self._publish_delirium_respawn_event(
                player_id=player_id,
                player_name=str(player.name),
                respawn_room=respawn_room,
                old_lucidity=old_lucidity,
                new_lucidity=new_lucidity,
                old_room=old_room,
            )

            await self._finish_first_exposure(player_id, first_exposure_instance)
            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player from delirium", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error(
                "Unexpected error respawning player from delirium", player_id=player_id, error=str(e), exc_info=True
            )
            await session.rollback()
            return False

    async def respawn_player_from_sanitarium(self, player_id: uuid.UUID, session: AsyncSession) -> bool:  # pylint: disable=too-many-locals  # Reason: Respawn processing requires many intermediate variables for complex respawn logic
        """
        Respawn a player from sanitarium failover at LCD -100.

        This method:
        1. Sets player lucidity to 1 (Deranged tier)
        2. Moves player to the Recovery Ward (RECOVERY_WARD_ROOM_ID) and leaves a pending debrief
        3. Increases liability stages (or adds one if none exist)
        4. Publishes sanitarium respawn event for UI updates

        Args:
            player_id: ID of the player to respawn
            session: Database session for player data access

        Returns:
            True if respawn was successful, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for sanitarium respawn", player_id=player_id)
                return False

            prepared = await self._prepare_sanitarium_respawn(player_id, player, session)
            if not prepared:
                return False
            respawn_room, stats, old_room, old_lucidity, new_lucidity = prepared

            await self._clear_respawn_combat_state(player_id=player_id, respawn_context="sanitarium")

            # Commit changes using async API (includes debrief flag)
            await session.commit()
            await self._set_respawn_lucidity(player_id, new_lucidity, sanitarium=True)

            log_sanitarium_respawn(player, player_id, respawn_room, old_lucidity, new_lucidity, old_room)

            self._publish_standard_respawn_event(
                player_id=player_id,
                player_name=str(player.name),
                respawn_room=respawn_room,
                stats=stats,
                old_room=old_room,
            )

            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player from sanitarium", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error(
                "Unexpected error respawning player from sanitarium", player_id=player_id, error=str(e), exc_info=True
            )
            await session.rollback()
            return False
