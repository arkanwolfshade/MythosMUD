"""
Player combat service for managing player combat state and XP rewards.

This service handles player combat state tracking, XP reward calculation,
and integration with the existing player service for XP persistence.
"""

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Any
from uuid import UUID

from server.events.event_types import BaseEvent
from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


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


class PlayerXPAwardEvent(BaseEvent):
    """Event published when a player receives XP."""

    def __init__(self, player_id: UUID, xp_amount: int, new_level: int, timestamp: datetime | None = None) -> None:
        # AI Agent: BaseEvent fields have init=False, so we can't pass them to super().__init__()
        # Instead, we set them directly after calling super().__init__() with no args
        super().__init__()
        object.__setattr__(self, "event_type", "player_xp_awarded")
        object.__setattr__(self, "timestamp", timestamp or datetime.now(UTC))
        self.player_id = player_id
        self.xp_amount = xp_amount
        self.new_level = new_level


class PlayerCombatService:
    """
    Service for managing player combat state and XP rewards.

    This service tracks player combat states, calculates XP rewards,
    and integrates with the persistence layer for XP persistence.
    """

    def __init__(self, persistence: Any, event_bus: Any, npc_combat_integration_service: Any = None) -> None:
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
        self._player_combat_states: dict[UUID, PlayerCombatState] = {}
        self._combat_timeout_minutes = 30  # Configurable timeout

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
        return player_id in self._player_combat_states

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
        players_to_clear = []
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
        try:
            # Get player from persistence
            player = await self._persistence.async_get_player(str(player_id))
            if not player:
                logger.warning("Player not found for XP award", player_id=player_id)
                return

            # Award XP
            player.add_experience(xp_amount)

            # Save player
            await self._persistence.async_save_player(player)

            # Publish XP award event
            event = PlayerXPAwardEvent(
                player_id=player_id,
                xp_amount=xp_amount,
                new_level=player.level,
            )
            if self._event_bus:
                self._event_bus.publish(event)  # EventBus.publish is sync, not async
            else:
                logger.warning("No event bus available for XP award event", player_id=player_id)

            logger.info("Awarded XP to player", xp_amount=xp_amount, player_name=player.name, new_level=player.level)

        except Exception as e:
            logger.error(
                "Error awarding XP to player",
                player_id=str(player_id),
                error=str(e),
            )

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

        # First, try to get XP directly from the UUID-to-XP mapping
        # This is more reliable than looking it up from the lifecycle manager,
        # since NPCs may be removed from the lifecycle manager after death
        if self._npc_combat_integration_service:
            # Access the UUID-to-XP mapping directly from the NPC combat integration service
            uuid_to_xp_mapping = getattr(self._npc_combat_integration_service, "_uuid_to_xp_mapping", {})
            if npc_id in uuid_to_xp_mapping:
                xp_reward = uuid_to_xp_mapping[npc_id]
                logger.debug(
                    "Retrieved XP reward from UUID-to-XP mapping",
                    npc_id=npc_id,
                    xp_amount=xp_reward,
                )
                assert isinstance(xp_reward, int)
                return xp_reward
            else:
                logger.debug("UUID not found in XP mapping", npc_id=npc_id)

        # Fallback to database lookup if UUID-to-XP mapping doesn't have the value
        try:
            # Try to get NPC definition to read xp_value from database
            logger.debug(
                "Checking if persistence has get_npc_lifecycle_manager method",
                has_method=hasattr(self._persistence, "get_npc_lifecycle_manager"),
            )
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = self._persistence.get_npc_lifecycle_manager()
                logger.debug("Got lifecycle manager", has_lifecycle_manager=bool(lifecycle_manager))

                # First try to get the original string ID from the NPC combat integration service
                original_string_id = None
                if self._npc_combat_integration_service:
                    logger.debug("Calling get_original_string_id", npc_id=npc_id)
                    original_string_id = self._npc_combat_integration_service.get_original_string_id(npc_id)
                    logger.debug("Got original string ID", original_string_id=original_string_id)
                else:
                    logger.debug("NPC combat integration service is None")

                # Use the original string ID if available, otherwise fall back to UUID string
                lookup_id = original_string_id or str(npc_id)
                logger.debug("Using lookup ID", lookup_id=lookup_id)

                if lifecycle_manager and lookup_id in lifecycle_manager.lifecycle_records:
                    npc_definition = lifecycle_manager.lifecycle_records[lookup_id].definition
                    logger.debug("Found NPC definition", has_definition=bool(npc_definition))
                    if npc_definition:
                        # Use the get_base_stats() method to parse the JSON string
                        base_stats = npc_definition.get_base_stats()
                        logger.debug("Got base stats", base_stats=base_stats)
                        if isinstance(base_stats, dict) and "xp_value" in base_stats:
                            xp_reward = base_stats["xp_value"]
                            logger.debug(
                                "Calculated XP reward from NPC definition",
                                npc_id=npc_id,
                                original_id=original_string_id,
                                xp_amount=xp_reward,
                            )
                            assert isinstance(xp_reward, int)
                            return xp_reward
                        else:
                            logger.debug("No xp_value in base_stats", base_stats=base_stats)
                else:
                    # Log all available lifecycle record IDs for debugging
                    available_ids = (
                        list(lifecycle_manager.lifecycle_records.keys())
                        if lifecycle_manager and hasattr(lifecycle_manager, "lifecycle_records")
                        else []
                    )
                    logger.debug(
                        "NPC not found in lifecycle records",
                        lookup_id=lookup_id,
                        has_lifecycle_manager=bool(lifecycle_manager),
                        available_ids=available_ids,
                        total_records=len(available_ids),
                    )
            else:
                logger.debug("Persistence does not have get_npc_lifecycle_manager method")
        except Exception as e:
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
        stale_players = []

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
