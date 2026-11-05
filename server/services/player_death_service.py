"""
Player Death Service for managing player mortality and DP decay.

This service handles the mortally wounded state (0 to -10 DP), automatic DP decay,
and death detection. As documented in the Necronomicon's chapter on mortality,
the threshold between life and death requires careful management.

Decay and death are sync player registry units (ADR-029 step 6a); the per-tick candidate queries still read players
from the database, which the sync writes keep current.
"""

from __future__ import annotations

import uuid
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Protocol, cast

from sqlalchemy import select, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.constants.spawn_defaults import LIMBO_ROOM_ID
from server.events.event_types import PlayerDiedEvent, PlayerDPDecayEvent
from server.exceptions import DatabaseError
from server.game.player_registry import PlayerNotFoundError
from server.models.game import PositionState
from server.models.player import Player
from server.models.player_dp import DEAD_DP, DpChange, decayed, dp_of
from server.services.player_health_service import PlayerHealthService
from server.structured_logging.enhanced_logging_config import get_logger, log_exception_once
from server.utils.room_utils import format_room_location

if TYPE_CHECKING:
    from server.game.player_registry import PlayerAggregate, PlayerRegistry

logger = get_logger(__name__)


class _DecayEventPublisher(Protocol):  # pylint: disable=too-few-public-methods  # Reason: one-method event sink
    """The event bus, as the decay publishes to it."""

    def publish(self, event: PlayerDPDecayEvent) -> None:
        """Deliver a DP decay event."""


# Mirrored in player_respawn_service — room of death for interstitial / login UI.
DEATH_ROOM_ID_STAT = "death_room_id"
DEATH_LOCATION_STAT = "death_location"


# Per-tick prefilter lives in Postgres (db/procedures/players.sql): it returns every player whose
# stats.current_dp is NOT a JSON number > 0 -- normally no rows. It is a deliberate superset of
# "dead or mortally wounded" (odd stored values come back too), so the Python predicates
# (Player.is_dead / is_mortally_wounded, via coerce_int) keep the final say. from_statement() maps the
# rows onto Player entities; the tick reads their ids and rooms, and changes them through the registry.
_DP_CHECK_CANDIDATES = select(Player).from_statement(
    text(  # ADR-015: explicit column list -- the lint guard forbids `SELECT *`.
        """
        SELECT player_id, user_id, name, inventory, current_room_id,
               respawn_room_id, experience_points, level, is_admin, profession_id,
               created_at, last_active, stats, is_deleted, deleted_at, tutorial_instance_id
        FROM get_players_not_clearly_alive()
        """
    )
)


async def _load_dp_check_candidates(session: AsyncSession) -> Sequence[Player]:
    """Run the prefilter; the cast is the typed seam, since from_statement() yields an untyped Result."""
    result = await session.execute(_DP_CHECK_CANDIDATES)
    return cast("Sequence[Player]", result.scalars().all())


class PlayerDeathService:
    """
    Service for managing player death, mortally wounded state, and DP decay.

    This service handles:
    - Identifying mortally wounded players (0 >= DP > -10)
    - Processing DP decay (1 DP per tick, capped at -10)
    - Detecting and handling player death (DP <= -10)
    - Publishing appropriate events for UI updates
    - Clearing combat state when player dies
    """

    _event_bus: Any | None
    _player_combat_service: Any | None
    _async_persistence: Any | None

    def __init__(
        self,
        event_bus: Any | None = None,
        player_combat_service: Any | None = None,
        async_persistence: Any | None = None,
        player_registry: PlayerRegistry | None = None,
    ) -> None:
        """
        Initialize the player death service.

        Args:
            event_bus: Optional event bus for publishing events
            player_combat_service: Optional player combat service for clearing combat state
            async_persistence: Optional async persistence layer for room-name lookups (#679:
                injected by CombatBundle instead of reached via ApplicationContainer.get_instance())
            player_registry: Holds the player: decay and death are units on it (ADR-029 step 6a)
        """
        self._event_bus = event_bus
        self._player_combat_service = player_combat_service
        self._async_persistence = async_persistence
        self._player_registry: PlayerRegistry | None = player_registry
        logger.info(
            "PlayerDeathService initialized",
            event_bus_available=bool(event_bus),
            player_combat_service_available=bool(player_combat_service),
        )

    async def get_mortally_wounded_players(self, session: AsyncSession) -> list[Player]:
        """
        Get all players currently in the mortally wounded state.

        A player is considered mortally wounded if their DP is between 0 and -9 (inclusive).

        Args:
            session: Async database session for querying players

        Returns:
            List of Player objects that are mortally wounded
        """
        try:
            # Runs every game-second: let Postgres drop the (normally all) healthy players.
            all_players = await _load_dp_check_candidates(session)

            # Filter for mortally wounded players using Player domain logic
            mortally_wounded = [p for p in all_players if p.is_mortally_wounded()]
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player stats retrieval errors unpredictable, must return empty list
            logger.error("Error getting mortally wounded players", error=str(e), exc_info=True)
            # This session is shared across the rest of this tick's DP-decay processing
            # (get_dead_players, etc. all receive the same session). Without a rollback here,
            # Postgres leaves the transaction aborted and every subsequent query on it fails
            # with InFailedSQLTransactionError, cascading this one query's failure onto
            # completely unrelated ones for the rest of the tick.
            await session.rollback()
            return []

        # Called every game-second; only log when there is something to report (#912).
        if mortally_wounded:
            logger.debug(
                "Found mortally wounded players",
                count=len(mortally_wounded),
                player_ids=[p.player_id for p in mortally_wounded],
            )

        return mortally_wounded

    async def get_dead_players(self, session: AsyncSession) -> list[Player]:
        """
        Get all players who are dead (DP <= -10).

        Args:
            session: Async database session for querying players

        Returns:
            List of Player objects that are dead
        """
        try:
            # Runs every tick while players are online: let Postgres drop the healthy players.
            all_players = await _load_dp_check_candidates(session)

            # Filter for dead players using Player domain logic
            dead_players = [p for p in all_players if p.is_dead()]

            # Called every tick; only log when there is something to report (#912).
            if dead_players:
                logger.debug(
                    "Found dead players",
                    count=len(dead_players),
                    player_ids=[p.player_id for p in dead_players],
                )

            return dead_players

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            log_exception_once(
                logger,
                "error",
                "Error retrieving dead players",
                exc=e,
                exc_info=True,
            )
            # See get_mortally_wounded_players: this session is shared for the rest of the
            # tick, so a failed query here must be rolled back or every later query on it
            # (this function included, on the next tick) inherits an aborted transaction.
            await session.rollback()
            return []

    async def process_mortally_wounded_tick(self, player_id: uuid.UUID) -> DpChange | None:
        """
        Bleed a mortally wounded player 1 DP (to at most -10), as one sync registry unit.

        Args:
            player_id: ID of the player to process

        Returns:
            The DP change, or None if none was applied (already dead, no such player, or the write failed)
        """
        if self._player_registry is None:
            logger.error("No player registry; cannot apply DP decay", player_id=player_id)
            return None
        try:
            async with self._player_registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                if dp_of(player.row.stats) <= DEAD_DP:
                    logger.debug("Player already dead, skipping DP decay", player_id=player_id)
                    return None
                change = PlayerHealthService.apply_in(player, decayed(player.row.stats, 1))
                player_name, room_id = player.row.name, player.row.current_room_id
        except PlayerNotFoundError:
            logger.warning("Player not found for DP decay", player_id=player_id)
            return None
        except (DatabaseError, SQLAlchemyError) as e:
            log_exception_once(
                logger, "error", "Error processing DP decay for player", exc=e, exc_info=True, player_id=player_id
            )
            return None

        if "position" in change.changes:
            logger.info(
                "Player posture changed to lying (unconscious)",
                player_id=player_id,
                player_name=player_name,
                dp=change.new_dp,
            )
        logger.info(
            "DP decay applied to player",
            player_id=player_id,
            player_name=player_name,
            old_dp=change.old_dp,
            new_dp=change.new_dp,
            delta=-1,
        )
        event_bus = cast(_DecayEventPublisher | None, self._event_bus)
        if event_bus:
            event_bus.publish(
                PlayerDPDecayEvent(
                    player_id=player_id,
                    old_dp=change.old_dp,
                    new_dp=change.new_dp,
                    decay_amount=1,
                    room_id=room_id,
                )
            )
        return change

    async def _clear_player_combat_state(self, player_id: uuid.UUID) -> None:
        """
        Clear player combat state when they die.

        BUGFIX #244: As documented in "Mortality and Combat State Persistence" - Dr. Armitage, 1929
        A player's combat essence must be severed upon death to prevent lingering in combat.

        Args:
            player_id: ID of the player whose combat state should be cleared
        """
        if not self._player_combat_service:
            return

        try:
            await self._player_combat_service.clear_player_combat_state(player_id)
            logger.info("Cleared combat state for deceased player", player_id=player_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            log_exception_once(
                logger,
                "error",
                "Error clearing combat state for deceased player",
                exc=e,
                exc_info=True,
                player_id=player_id,
            )

    def _get_room_name_for_death(self, death_location: str) -> str:
        """
        Get room name for death location display.

        Args:
            death_location: Room ID where the player died

        Returns:
            "Zone › Sub-zone › Room" display string, or "Unknown Location" (never the raw room ID, #910)
        """
        if not death_location or death_location == LIMBO_ROOM_ID:
            return "Unknown Location"

        if self._async_persistence:
            try:
                room = self._async_persistence.get_room_by_id(death_location)
                # Handle case where get_room_by_id might return a coroutine (if mocked as async)
                if hasattr(room, "__await__"):
                    # It's a coroutine, can't await in sync context - just return unknown
                    return "Unknown Location"
                return format_room_location(cast(object, room)) or "Unknown Location"
            except AttributeError, TypeError:
                # If room lookup fails, don't leak the room ID
                return "Unknown Location"

        return "Unknown Location"

    @staticmethod
    def _persist_death_location_stats(player: PlayerAggregate, death_location: str, room_name: str) -> None:
        """Store death room id/name on player stats so login can show the place of death."""
        if not death_location or death_location == LIMBO_ROOM_ID:
            return
        player.row.set_stat(DEATH_ROOM_ID_STAT, death_location, sync=True)
        location = room_name if room_name and room_name != LIMBO_ROOM_ID else death_location
        player.row.set_stat(DEATH_LOCATION_STAT, location, sync=True)

    def _publish_death_event(
        self, player_id: uuid.UUID, player_name: str, death_location: str, killer_info: dict[str, Any] | None
    ) -> None:
        """
        Publish player died event if event bus is available.

        Args:
            player_id: ID of the player who died
            player_name: Name of the player who died
            death_location: Room ID where the player died
            killer_info: Optional dict with killer_id and killer_name
        """
        if not self._event_bus:
            return

        room_name = self._get_room_name_for_death(death_location)

        event = PlayerDiedEvent(
            player_id=player_id,
            player_name=str(player_name),
            room_id=death_location,
            death_location=room_name,
            killer_id=killer_info.get("killer_id") if killer_info else None,
            killer_name=killer_info.get("killer_name") if killer_info else None,
        )
        self._event_bus.publish(event)

    async def handle_player_death(
        self, player_id: uuid.UUID, death_location: str, killer_info: dict[str, Any] | None
    ) -> bool:
        """
        Handle player death when DP reaches -10 or below: lying, with the place of death recorded (one sync unit).

        Args:
            player_id: ID of the player who died
            death_location: Room ID where the player died
            killer_info: Optional dict with killer_id and killer_name

        Returns:
            True if death was handled successfully, False otherwise
        """
        if self._player_registry is None:
            logger.error("No player registry; cannot handle player death", player_id=player_id)
            return False
        room_name = self._get_room_name_for_death(death_location)
        try:
            async with self._player_registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                player.row.set_stat("position", PositionState.LYING, sync=True)
                self._persist_death_location_stats(player, death_location, room_name)
                player_name = player.row.name
        except PlayerNotFoundError:
            logger.warning("Player not found for death handling", player_id=player_id)
            return False
        except (DatabaseError, SQLAlchemyError) as e:
            log_exception_once(
                logger, "error", "Error handling player death", exc=e, exc_info=True, player_id=player_id
            )
            return False

        logger.info(
            "Player died",
            player_id=player_id,
            player_name=player_name,
            death_location=death_location,
            killer_id=killer_info.get("killer_id") if killer_info else None,
            killer_name=killer_info.get("killer_name") if killer_info else None,
        )
        await self._clear_player_combat_state(player_id)
        self._publish_death_event(player_id, player_name, death_location, killer_info)
        return True
