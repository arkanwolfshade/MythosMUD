"""Player combat state, XP rewards, and NPC integration (UUID / lifecycle lookup helpers in support module)."""

# pylint: disable=too-few-public-methods  # Reason: Combat service class with focused responsibility, minimal public interface

from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import cast
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.events.event_types import BaseEvent
from server.services.player_combat_service_support import (
    EventBusPublish as _EventBusPublish,
)
from server.services.player_combat_service_support import (
    NPCCombatIntegrationReadApi as _NPCCombatIntegrationReadApi,
)
from server.services.player_combat_service_support import (
    PlayerXpLike as _PlayerXpLike,
)
from server.services.player_combat_service_support import (
    async_load_lifecycle_manager as _async_load_lifecycle_manager,
)
from server.services.player_combat_service_support import (
    lifecycle_lookup_id as _lifecycle_lookup_id,
)
from server.services.player_combat_service_support import (
    log_missing_lifecycle_npc as _log_missing_lifecycle_npc,
)
from server.services.player_combat_service_support import (
    original_string_id_for_npc as _original_string_id_for_npc,
)
from server.services.player_combat_service_support import (
    xp_int_from_base_stats_mapping as _xp_int_from_base_stats_mapping,
)
from server.structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)


@dataclass
class PlayerCombatState:
    """Represents a player's combat state."""

    player_id: UUID
    player_name: str
    combat_id: UUID
    room_id: str
    is_in_combat: bool = True
    last_activity: datetime | None = None

    def __post_init__(self) -> None:
        """Initialize last_activity if not provided."""
        if self.last_activity is None:
            self.last_activity = datetime.now(UTC)


@dataclass
class PlayerXPAwardEvent(BaseEvent):  # pylint: disable=too-few-public-methods  # Reason: Event dataclass with focused responsibility, minimal public interface
    """Event published when a player receives XP."""

    player_id: UUID
    xp_amount: int
    new_level: int

    def __post_init__(self) -> None:
        """Set event_type for serialization/deserialization."""
        super().__post_init__()
        object.__setattr__(self, "event_type", "player_xp_awarded")


class PlayerCombatService:
    """
    Service for managing player combat state and XP rewards.

    This service tracks player combat states, calculates XP rewards,
    and integrates with the persistence layer for XP persistence.
    """

    _persistence: object
    _event_bus: object | None
    _npc_combat_integration_service: object | None
    _player_combat_states: dict[UUID, PlayerCombatState]
    _combat_timeout_minutes: int

    def __init__(
        self,
        persistence: object,
        event_bus: object | None,
        npc_combat_integration_service: object | None = None,
    ) -> None:
        """
        Initialize the player combat service.

        Args:
            persistence: Persistence layer for player data
            event_bus: Event bus for publishing events
            npc_combat_integration_service: NPC combat integration service for
                UUID mapping
        """
        logger.debug(
            "PlayerCombatService constructor called",
            persistence_type=type(persistence).__name__,
            has_event_bus=bool(event_bus),
            has_npc_service=bool(npc_combat_integration_service),
        )
        self._persistence = persistence
        self._event_bus = event_bus
        self._npc_combat_integration_service = npc_combat_integration_service
        self._player_combat_states = {}
        self._combat_timeout_minutes = 30  # Configurable timeout

    def set_npc_combat_integration_service(self, service: object | None) -> None:
        """Attach NPC combat integration for UUID/XP mapping (post-construction wiring)."""
        self._npc_combat_integration_service = service

    async def track_player_combat_state(
        self,
        player_id: UUID,
        player_name: str,
        combat_id: UUID,
        room_id: str,
    ) -> None:
        """
        Track a player's combat state.

        Args:
            player_id: ID of the player
            player_name: Name of the player
            combat_id: ID of the combat instance
            room_id: ID of the room where combat is taking place
        """
        logger.info("Tracking combat state for player", player_name=player_name, combat_id=combat_id)

        state = PlayerCombatState(
            player_id=player_id,
            player_name=player_name,
            combat_id=combat_id,
            room_id=room_id,
        )

        self._player_combat_states[player_id] = state

    async def get_player_combat_state(self, player_id: UUID) -> PlayerCombatState | None:
        """
        Get a player's combat state.

        Args:
            player_id: ID of the player

        Returns:
            PlayerCombatState if found, None otherwise
        """
        return self._player_combat_states.get(player_id)

    async def clear_player_combat_state(self, player_id: UUID) -> None:
        """
        Clear a player's combat state.

        Args:
            player_id: ID of the player
        """
        if player_id in self._player_combat_states:
            logger.info("Clearing combat state for player", player_id=player_id)
            del self._player_combat_states[player_id]

    def is_player_in_combat_sync(self, player_id: UUID) -> bool:
        """
        Synchronously check if a player is currently in combat.

        This is the preferred method for non-async contexts like movement validation.
        As noted in "Temporal Mechanics of Eldritch Combat" - Dr. Armitage, 1928,
        combat state checks must be instantaneous to prevent dimensional breaches.

        Args:
            player_id: ID of the player

        Returns:
            True if player is in combat, False otherwise
        """
        result = player_id in self._player_combat_states
        if result:
            logger.critical(
                "Combat movement violation detected",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                total_players_in_combat=len(self._player_combat_states),
                combat_states=str(list(self._player_combat_states.keys())),
            )
        else:
            logger.debug(
                "Combat sync check cleared",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id,
                total_players_in_combat=len(self._player_combat_states),
            )
        return result

    async def is_player_in_combat(self, player_id: UUID) -> bool:
        """
        Check if a player is currently in combat.

        Args:
            player_id: ID of the player

        Returns:
            True if player is in combat, False otherwise
        """
        return player_id in self._player_combat_states

    async def get_players_in_combat(self) -> list[UUID]:
        """
        Get all players currently in combat.

        Returns:
            List of player IDs currently in combat
        """
        return list(self._player_combat_states.keys())

    async def handle_combat_start(
        self,
        player_id: UUID,
        player_name: str,
        combat_id: UUID,
        room_id: str,
    ) -> None:
        """
        Handle combat start for a player.

        Args:
            player_id: ID of the player
            player_name: Name of the player
            combat_id: ID of the combat instance
            room_id: ID of the room where combat is taking place
        """
        await self.track_player_combat_state(
            player_id=player_id,
            player_name=player_name,
            combat_id=combat_id,
            room_id=room_id,
        )

    async def handle_combat_end(self, combat_id: UUID) -> None:
        """
        Handle combat end by clearing all players in the combat.

        Args:
            combat_id: ID of the combat that ended
        """
        logger.info("Handling combat end", combat_id=combat_id)

        # Find all players in this combat and clear their states
        players_to_clear: list[UUID] = []
        for player_id, state in self._player_combat_states.items():
            if state.combat_id == combat_id:
                players_to_clear.append(player_id)

        for player_id in players_to_clear:
            await self.clear_player_combat_state(player_id)

    async def handle_npc_death(
        self,
        player_id: UUID,
        npc_id: UUID,
        xp_amount: int,
    ) -> None:
        """
        Handle NPC death and award XP to the player.

        Args:
            player_id: ID of the player who defeated the NPC
            npc_id: ID of the defeated NPC (for logging purposes)
            xp_amount: Amount of XP to award
        """
        logger.info("Awarding XP to player for defeating NPC", xp_amount=xp_amount, player_id=player_id, npc_id=npc_id)

        await self.award_xp_on_npc_death(
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
        )

    async def _award_xp_via_npc_rewards(self, player_id: UUID, npc_id: UUID, xp_amount: int) -> bool:
        """
        Return True if the NPC rewards path handled the award (success or logged failure).

        When True, callers must not run persistence fallback.
        """
        integration = self._npc_combat_integration_service
        if integration is None or xp_amount <= 0:
            return False
        rewards_obj = cast(_NPCCombatIntegrationReadApi, integration).get_rewards_service()
        if rewards_obj is None:
            return False
        try:
            await rewards_obj.award_xp_to_killer(str(player_id), str(npc_id), int(xp_amount))
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.error(
                "Error awarding XP via NPCCombatRewards",
                player_id=player_id,
                npc_id=npc_id,
                error=str(e),
            )
        return True

    async def _award_xp_via_persistence_fallback(self, player_id: UUID, xp_amount: int) -> None:
        """Fallback: load player, add XP, save, publish (used without integration in tests)."""
        get_player_raw = getattr(self._persistence, "get_player_by_id", None)
        save_player_raw = getattr(self._persistence, "save_player", None)
        if not callable(get_player_raw) or not callable(save_player_raw):
            return
        get_player = cast(Callable[[UUID], Awaitable[_PlayerXpLike | None]], get_player_raw)
        save_player = cast(Callable[[_PlayerXpLike], Awaitable[object]], save_player_raw)
        player = await get_player(player_id)
        if not player:
            logger.warning("Player not found for XP award", player_id=player_id)
            return

        player.add_experience(xp_amount)
        _ = await save_player(player)

        event = PlayerXPAwardEvent(
            player_id=player_id,
            xp_amount=xp_amount,
            new_level=int(player.level),
        )
        bus = self._event_bus
        if bus is not None:
            cast(_EventBusPublish, bus).publish(event)
        else:
            logger.warning("No event bus available for XP award event", player_id=player_id)

        logger.info(
            "Awarded XP to player",
            xp_amount=xp_amount,
            player_name=str(player.name),
            new_level=int(player.level),
        )

    async def award_xp_on_npc_death(
        self,
        player_id: UUID,
        npc_id: UUID,
        xp_amount: int,
    ) -> None:
        """
        Award XP to a player for defeating an NPC.

        Args:
            player_id: ID of the player
            npc_id: ID of the defeated NPC
            xp_amount: Amount of XP to award
        """
        logger.debug(
            "award_xp_on_npc_death called",
            player_id=player_id,
            npc_id=npc_id,
            xp_amount=xp_amount,
            persistence_type=type(self._persistence).__name__,
        )
        delegated = await self._award_xp_via_npc_rewards(player_id, npc_id, xp_amount)
        if delegated:
            return
        try:
            await self._award_xp_via_persistence_fallback(player_id, xp_amount)
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: XP award errors unpredictable, must not crash service
            logger.error(
                "Error awarding XP to player",
                player_id=player_id,
                error=str(e),
            )

    async def _get_xp_from_lifecycle_manager(self, npc_id: UUID) -> int | None:
        """
        Try to get XP reward from persistence lifecycle manager.

        Returns XP amount if found, None otherwise. Caller must catch exceptions.
        """
        if not hasattr(self._persistence, "get_npc_lifecycle_manager"):
            logger.debug("Persistence does not have get_npc_lifecycle_manager method")
            return None

        logger.debug(
            "Checking if persistence has get_npc_lifecycle_manager method",
            has_method=True,
        )
        lifecycle_manager = await _async_load_lifecycle_manager(self._persistence)
        logger.debug("Got lifecycle manager", has_lifecycle_manager=bool(lifecycle_manager))

        integration = self._npc_combat_integration_service
        original_string_id = _original_string_id_for_npc(integration, npc_id)
        if integration is not None:
            logger.debug("Calling get_original_string_id", npc_id=npc_id)
            logger.debug("Got original string ID", original_string_id=original_string_id)
        else:
            logger.debug("NPC combat integration service is None")

        lookup_id = _lifecycle_lookup_id(integration, npc_id)
        logger.debug("Using lookup ID", lookup_id=lookup_id)

        if lifecycle_manager is None or lookup_id not in lifecycle_manager.lifecycle_records:
            _log_missing_lifecycle_npc(lookup_id, lifecycle_manager)
            return None

        npc_definition = lifecycle_manager.lifecycle_records[lookup_id].definition
        logger.debug("Found NPC definition", has_definition=bool(npc_definition))
        if not npc_definition:
            _log_missing_lifecycle_npc(lookup_id, lifecycle_manager)
            return None

        get_bs = getattr(npc_definition, "get_base_stats", None)
        if not callable(get_bs):
            return None
        base_stats = get_bs()
        logger.debug("Got base stats", base_stats=base_stats)
        xp_reward = _xp_int_from_base_stats_mapping(base_stats)
        if xp_reward is None:
            logger.debug("No xp_value in base_stats", base_stats=base_stats)
            return None

        logger.debug(
            "Calculated XP reward from NPC definition",
            npc_id=npc_id,
            original_id=original_string_id,
            xp_amount=xp_reward,
        )
        return xp_reward

    async def calculate_xp_reward(self, npc_id: UUID) -> int:
        """
        Calculate XP reward for defeating an NPC.

        Args:
            npc_id: ID of the NPC (UUID from combat system)

        Returns:
            XP reward amount
        """
        logger.debug("Starting XP reward calculation", npc_id=npc_id)
        logger.debug(
            "NPC combat integration service reference", has_npc_service=bool(self._npc_combat_integration_service)
        )
        logger.debug("Persistence object", persistence_type=type(self._persistence).__name__)

        # First, try to get XP from the UUID mapping on the NPC combat integration service.
        # XP is stored on _uuid_mapping (NPCCombatUUIDMapping) when combat starts; use it so
        # we have a value even after the NPC is removed from the lifecycle manager.
        integration = self._npc_combat_integration_service
        if integration is not None:
            uuid_mapping = cast(_NPCCombatIntegrationReadApi, integration).get_uuid_mapping()
            xp_reward = uuid_mapping.get_xp_value(npc_id)
            if xp_reward is not None:
                logger.debug(
                    "Retrieved XP reward from UUID mapping",
                    npc_id=npc_id,
                    xp_amount=xp_reward,
                )
                return xp_reward

        # Fallback to database lookup if UUID-to-XP mapping doesn't have the value
        try:
            xp_reward = await self._get_xp_from_lifecycle_manager(npc_id)
            if xp_reward is not None:
                return xp_reward
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError) as e:
            logger.warning(
                "Error reading NPC XP value from database",
                npc_id=npc_id,
                error=str(e),
                exc_info=True,
            )

        # Fallback to default XP reward if we can't read from database
        default_xp = 0
        logger.debug("Using default XP reward for NPC", npc_id=npc_id, xp_amount=default_xp)
        return default_xp

    async def cleanup_stale_combat_states(self) -> int:
        """
        Clean up stale combat states.

        Returns:
            Number of stale states cleaned up
        """
        cutoff_time = datetime.now(UTC) - timedelta(minutes=self._combat_timeout_minutes)
        stale_players: list[UUID] = []

        for player_id, state in self._player_combat_states.items():
            if state.last_activity is not None and state.last_activity < cutoff_time:
                stale_players.append(player_id)

        for player_id in stale_players:
            await self.clear_player_combat_state(player_id)
            logger.info("Cleaned up stale combat state for player", player_id=player_id)

        return len(stale_players)

    async def get_combat_stats(self) -> dict[str, int]:
        """
        Get statistics about player combat states.

        Returns:
            Dictionary with combat statistics
        """
        return {
            "players_in_combat": len(self._player_combat_states),
            "active_combats": len({state.combat_id for state in self._player_combat_states.values()}),
        }
