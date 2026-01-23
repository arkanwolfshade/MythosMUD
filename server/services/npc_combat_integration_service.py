"""
NPC Combat Integration Service for MythosMUD.

This service provides integration between NPCs and the combat system,
including combat memory management and basic combat interactions.

As documented in the Cultes des Goules, proper combat integration is essential
for maintaining the balance between mortal investigators and the eldritch
entities they encounter in our world.

ASYNC MIGRATION (Phase 2):
All persistence calls wrapped in asyncio.to_thread() to prevent event loop blocking.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines,wrong-import-position  # Reason: NPC combat integration requires many state attributes, parameters, and intermediate variables for complex combat logic. NPC combat integration requires extensive integration logic for comprehensive NPC-combat system integration. Imports after TYPE_CHECKING block are intentional to avoid circular dependencies.

import uuid
from typing import TYPE_CHECKING, Any
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..realtime.connection_manager import ConnectionManager
    from .combat_service import CombatService

from sqlalchemy.exc import SQLAlchemyError

from ..config import get_config
from ..events.event_bus import EventBus
from ..game.mechanics import GameMechanicsService
from ..realtime.login_grace_period import is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger
from .combat_event_publisher import CombatEventPublisher
from .combat_messaging_integration import CombatMessagingIntegration
from .npc_combat_data_provider import NPCCombatDataProvider
from .npc_combat_handlers import NPCCombatHandlers
from .npc_combat_lifecycle import NPCCombatLifecycle
from .npc_combat_lucidity import NPCCombatLucidity
from .npc_combat_memory import NPCCombatMemory
from .npc_combat_rewards import NPCCombatRewards
from .npc_combat_uuid_mapping import NPCCombatUUIDMapping
from .player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class NPCCombatIntegrationService:  # pylint: disable=too-many-instance-attributes  # Reason: Combat integration service requires many state tracking and service attributes
    """
    Service for integrating NPCs with the combat system.

    This service handles:
    - NPC combat memory management
    - Basic combat interactions
    - Event publishing and messaging
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat integration initialization requires many service dependencies
        self,
        event_bus: EventBus | None = None,
        combat_service: "CombatService | None" = None,
        player_combat_service: PlayerCombatService | None = None,
        connection_manager: "ConnectionManager | None" = None,
        async_persistence: "AsyncPersistenceLayer | None" = None,
    ) -> None:
        """
        Initialize the NPC combat integration service.

        Args:
            event_bus: Optional EventBus instance. If None, will get the
                global instance.
            combat_service: Optional CombatService instance. If None, will
                create a new one (for testing).
            player_combat_service: Optional PlayerCombatService instance to use.
                If None, will create a new one (for testing).
                CRITICAL: Production code should ALWAYS pass the shared instance
                from app.state to prevent instance mismatch bugs.
            connection_manager: Optional ConnectionManager instance to use.
                If None, CombatMessagingIntegration will try to lazy-load from container.
                CRITICAL: Production code should ALWAYS pass the shared instance
                from container to prevent initialization failures.
            async_persistence: Async persistence layer instance (required)
        """
        if async_persistence is None:
            raise ValueError("async_persistence is required for NPCCombatIntegrationService")
        self.event_bus = event_bus or EventBus()
        self._persistence = async_persistence
        logger.debug(
            "NPCCombatIntegrationService constructor",
            persistence_type=type(self._persistence).__name__,
            persistence_is_none=self._persistence is None,
        )
        # Initialize GameMechanicsService for proper XP awards and stat updates
        self._game_mechanics = GameMechanicsService(async_persistence)

        # Use shared PlayerCombatService instance if provided, otherwise create new one (for tests)
        # CRITICAL: Production code must pass shared instance to prevent state desynchronization!
        if player_combat_service is not None:
            self._player_combat_service = player_combat_service
            # CRITICAL FIX: Update the shared PlayerCombatService's NPC combat integration service reference
            # so it can access the UUID-to-XP mapping for XP calculations
            self._player_combat_service._npc_combat_integration_service = self
            logger.info(
                "Using shared PlayerCombatService instance and updated NPC combat integration reference",
                instance_id=id(player_combat_service),
            )
        else:
            # Only create new instance for testing - pass self for UUID mapping access
            self._player_combat_service = PlayerCombatService(self._persistence, self.event_bus, self)
            logger.warning(
                "Created NEW PlayerCombatService instance - this should only happen in tests!",
                instance_id=id(self._player_combat_service),
            )

        # Initialize helper modules
        self._combat_memory = NPCCombatMemory()
        self._uuid_mapping = NPCCombatUUIDMapping()
        self._data_provider = NPCCombatDataProvider(async_persistence)
        self._rewards = NPCCombatRewards(async_persistence, self._game_mechanics)
        self._lucidity = NPCCombatLucidity()
        self._lifecycle = NPCCombatLifecycle(async_persistence)

        if combat_service is not None:
            self._combat_service = combat_service
            # CRITICAL FIX: Update the CombatService to use our PlayerCombatService with UUID mapping
            self._combat_service._player_combat_service = self._player_combat_service
            self._combat_service._npc_combat_integration_service = self
        else:
            # Only create a new CombatService if one was not provided
            # (this is primarily for testing)
            # Lazy import to avoid circular dependency with combat_service
            from .combat_service import (
                CombatService,  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import inside function to avoid circular import chain during module initialization, wrong import position is intentional
            )

            self._combat_service = CombatService(self._player_combat_service, npc_combat_integration_service=self)

        # Enable auto-progression features
        self._combat_service.auto_progression_enabled = True
        # CRITICAL FIX: Use config value instead of hardcoded 6 seconds
        # Get combat_tick_interval from config (default 10 seconds)
        # Note: get_config is imported at module level (line 26)
        combat_config = get_config()  # pylint: disable=used-before-assignment  # Reason: get_config is imported at module level, not redefined
        self._combat_service.turn_interval_seconds = combat_config.game.combat_tick_interval

        # CRITICAL FIX: Pass connection_manager to CombatMessagingIntegration
        # If not provided, it will try to lazy-load from container (for backward compatibility)
        self._messaging_integration = CombatMessagingIntegration(connection_manager=connection_manager)
        # CombatEventPublisher expects NATSService, not EventBus. Pass None to use global NATSService.
        self._event_publisher = CombatEventPublisher(nats_service=None)

        # Initialize combat handlers
        self._handlers = NPCCombatHandlers(
            self._data_provider,
            self._rewards,
            self._combat_memory,
            self._lifecycle,
            self._messaging_integration,
        )

        logger.info("NPC Combat Integration Service initialized with auto-progression enabled")

    async def handle_player_attack_on_npc(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Attack handling requires many parameters and intermediate variables for complex combat logic
        self,
        player_id: str,
        npc_id: str,
        room_id: str,
        action_type: str = "punch",
        damage: int = 10,
        npc_instance: Any | None = None,
    ) -> bool:
        """
        Handle a player attacking an NPC using auto-progression combat system.

        Args:
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            room_id: ID of the room where combat occurs
            action_type: Type of attack action
            damage: Damage amount
            npc_instance: Optional pre-validated NPC instance. If provided, avoids redundant lookup
                         and race conditions. If None, will perform lookup.

        Returns:
            bool: True if attack was handled successfully
        """
        try:
            # Check if player is in login grace period - prevent attacks
            try:
                config = get_config()
                app = getattr(config, "_app_instance", None)
                if app:
                    connection_manager = getattr(app.state, "connection_manager", None)
                    if connection_manager:
                        player_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
                        if is_player_in_login_grace_period(player_uuid, connection_manager):
                            logger.info(
                                "Player attack on NPC blocked - player in login grace period",
                                player_id=player_id,
                                npc_id=npc_id,
                            )
                            return False  # Attack blocked
            except (AttributeError, ImportError, TypeError, ValueError) as e:
                # If we can't check grace period, proceed with attack (fail open)
                logger.debug("Could not check login grace period for player attack", player_id=player_id, error=str(e))

            # Validate and get NPC instance
            npc_instance = await self._validate_and_get_npc_instance(player_id, npc_id, npc_instance)
            if not npc_instance:
                return False

            # Validate combat location
            if not await self._validate_combat_location(player_id, npc_id, room_id, npc_instance):
                return False

            # Store combat memory and set up UUIDs
            first_engagement = self._combat_memory.record_attack(npc_id, player_id)
            attacker_uuid, target_uuid = await self._setup_combat_uuids_and_mappings(
                player_id, npc_id, room_id, first_engagement
            )

            # Process combat attack
            combat_result = await self._process_combat_attack(
                player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance
            )

            # Handle combat result
            return await self._handlers.handle_combat_result(
                combat_result,
                player_id,
                npc_id,
                room_id,
                action_type,
                damage,
                npc_instance,
                self.handle_npc_death,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error(
                "Error handling player attack on NPC",
                error=str(e),
                player_id=player_id,
                npc_id=npc_id,
            )
            return False

    async def _validate_and_get_npc_instance(self, player_id: str, npc_id: str, npc_instance: Any | None) -> Any | None:
        """
        Validate and get NPC instance, handling lookup if needed.

        Args:
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            npc_instance: Optional pre-validated NPC instance

        Returns:
            NPC instance if valid, None otherwise
        """
        # BUGFIX: Use provided NPC instance if available to avoid redundant lookup
        # This prevents race conditions where NPC state changes between lookups
        # As documented in investigation: 2025-11-30_session-001_npc-combat-start-failure.md
        npc_instance_provided = npc_instance is not None
        if npc_instance is None:
            logger.debug(
                "Performing NPC instance lookup",
                player_id=player_id,
                npc_id=npc_id,
            )
            npc_instance = self._data_provider.get_npc_instance(npc_id)
        else:
            logger.debug(
                "Using provided NPC instance - avoiding redundant lookup",
                player_id=player_id,
                npc_id=npc_id,
                npc_name=getattr(npc_instance, "name", "unknown"),
            )

        # Enhanced validation and logging for debugging
        if not npc_instance:
            logger.warning(
                "Player attacked non-existent NPC - NPC not found in lifecycle manager",
                player_id=player_id,
                npc_id=npc_id,
                npc_instance_provided=npc_instance_provided,
            )
            return None

        npc_is_alive = getattr(npc_instance, "is_alive", True)
        if not npc_is_alive:
            logger.warning(
                "Player attacked dead NPC - NPC exists but is_alive is False",
                player_id=player_id,
                npc_id=npc_id,
                npc_name=getattr(npc_instance, "name", "unknown"),
                is_alive=npc_is_alive,
                npc_instance_provided=npc_instance_provided,
            )
            return None

        return npc_instance

    async def _validate_combat_location(self, player_id: str, npc_id: str, room_id: str, npc_instance: Any) -> bool:
        """
        Validate that player and NPC are in the same room.

        Args:
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            room_id: ID of the room where combat occurs
            npc_instance: NPC instance

        Returns:
            True if location is valid, False otherwise
        """
        player_room_id = await self._data_provider.get_player_room_id(player_id)
        npc_room_id = getattr(npc_instance, "current_room", None)

        logger.debug(
            "Room validation check",
            player_id=player_id,
            npc_id=npc_id,
            player_room_id=player_room_id,
            npc_room_id=npc_room_id,
            combat_room_id=room_id,
        )

        if player_room_id != npc_room_id:
            logger.warning(
                "Cross-room attack attempt blocked",
                player_id=player_id,
                npc_id=npc_id,
                player_room_id=player_room_id,
                npc_room_id=npc_room_id,
            )
            return False

        return True

    async def _setup_combat_uuids_and_mappings(
        self, player_id: str, npc_id: str, room_id: str, first_engagement: bool
    ) -> tuple[UUID, UUID]:
        """
        Convert string IDs to UUIDs and set up XP mappings.

        Args:
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            room_id: ID of the room where combat occurs
            first_engagement: Whether this is the first engagement with this NPC

        Returns:
            Tuple of (attacker_uuid, target_uuid)
        """
        try:
            attacker_uuid = self._uuid_mapping.convert_to_uuid(player_id)
            target_uuid = self._uuid_mapping.convert_to_uuid(npc_id)

            # Always store the UUID-to-string ID mapping when we have a string ID
            # This mapping is used later during XP calculation
            if not self._uuid_mapping.is_valid_uuid(npc_id):
                # Only store mapping for string IDs
                self._uuid_mapping.store_string_id_mapping(target_uuid, npc_id)

                # Also store the XP value directly for this UUID
                # This avoids the need to look it up from the lifecycle manager
                # during XP calculation, since NPCs may be removed by then
                await self._store_npc_xp_mapping(npc_id, target_uuid, room_id, player_id, first_engagement)

        except ValueError:
            attacker_uuid = uuid4()
            target_uuid = uuid4()
            # Don't store mapping for invalid UUIDs
            logger.debug("Skipping UUID mapping storage - invalid NPC ID", npc_id=npc_id)

        return attacker_uuid, target_uuid

    async def _store_npc_xp_mapping(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: XP mapping storage requires many parameters for context and mapping operations
        self, npc_id: str, target_uuid: UUID, room_id: str, player_id: str, first_engagement: bool
    ) -> None:
        """
        Store NPC XP mapping and apply encounter lucidity effect if first engagement.

        Args:
            npc_id: ID of the target NPC
            target_uuid: UUID of the target NPC
            room_id: ID of the room where combat occurs
            player_id: ID of the attacking player
            first_engagement: Whether this is the first engagement with this NPC
        """
        npc_definition = await self._data_provider.get_npc_definition(npc_id)
        logger.debug(
            "Retrieved NPC definition",
            npc_id=npc_id,
            has_definition=bool(npc_definition),
        )

        if npc_definition and first_engagement:
            await self._lucidity.apply_encounter_lucidity_effect(player_id, npc_id, npc_definition, room_id)

        if npc_definition:
            base_stats = npc_definition.get_base_stats()
            logger.debug(
                "Retrieved base stats",
                npc_id=npc_id,
                base_stats=base_stats,
            )
            if isinstance(base_stats, dict):
                xp_value = base_stats.get("xp_value", 0)  # Default to 0 if not found
                self._uuid_mapping.store_xp_mapping(target_uuid, xp_value)
            else:
                logger.debug(
                    "Base stats is not a dict",
                    npc_id=npc_id,
                    base_stats_type=type(base_stats),
                )
        else:
            logger.debug(
                "NPC definition not found",
                npc_id=npc_id,
            )

    async def _process_combat_attack(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat attack processing requires many parameters for context and attack logic
        self,
        player_id: str,
        room_id: str,
        attacker_uuid: UUID,
        target_uuid: UUID,
        damage: int,
        npc_instance: Any,
    ) -> Any:
        """
        Process combat attack, starting new combat or continuing existing one.

        Args:
            player_id: ID of the attacking player
            room_id: ID of the room where combat occurs
            attacker_uuid: UUID of the attacker
            target_uuid: UUID of the target
            damage: Damage amount
            npc_instance: NPC instance

        Returns:
            Combat result
        """
        # Lazy import to avoid circular dependency with lifespan
        from ..app.lifespan import (
            get_current_tick,  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import inside function to avoid circular import chain during module initialization, wrong import position is intentional
        )

        current_tick = get_current_tick()

        # Check if combat already exists, if not start new combat
        existing_combat = await self._combat_service.get_combat_by_participant(attacker_uuid)
        if existing_combat:
            # Queue action for next round instead of executing immediately
            queued = await self._combat_service.queue_combat_action(
                combat_id=existing_combat.combat_id,
                participant_id=attacker_uuid,
                action_type="attack",
                target_id=target_uuid,
                damage=damage,
            )
            if queued:
                logger.info(
                    "Combat action queued",
                    combat_id=existing_combat.combat_id,
                    participant_id=attacker_uuid,
                    target_id=target_uuid,
                    round=existing_combat.combat_round + 1,
                )
                # Return a success result indicating action was queued
                from server.models.combat import (
                    CombatResult,  # noqa: PLC0415  # Reason: Local import to avoid circular dependency
                )

                return CombatResult(
                    success=True,
                    damage=0,  # Damage will be applied when action executes
                    target_died=False,
                    combat_ended=False,
                    message="Action queued for next round",
                    combat_id=existing_combat.combat_id,
                )

            # Fallback to immediate execution if queuing failed
            logger.warning("Failed to queue action, executing immediately", participant_id=attacker_uuid)
            return await self._combat_service.process_attack(
                attacker_id=attacker_uuid, target_id=target_uuid, damage=damage
            )
        # Start new combat
        return await self._start_new_combat(
            player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance, current_tick
        )

    async def _start_new_combat(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat initialization requires many parameters for complete combat setup
        self,
        player_id: str,
        room_id: str,
        attacker_uuid: UUID,
        target_uuid: UUID,
        damage: int,
        npc_instance: Any,
        current_tick: int,
    ) -> Any:
        """
        Start a new combat and process initial attack.

        Args:
            player_id: ID of the attacking player
            room_id: ID of the room where combat occurs
            attacker_uuid: UUID of the attacker
            target_uuid: UUID of the target
            damage: Damage amount
            npc_instance: NPC instance
            current_tick: Current game tick

        Returns:
            Combat result
        """
        # Get player data
        player_name = await self._data_provider.get_player_name(player_id)
        attacker_data = await self._data_provider.get_player_combat_data(player_id, attacker_uuid, player_name)

        # Get NPC data
        target_data = self._data_provider.get_npc_combat_data(npc_instance, target_uuid)

        # Start combat with auto-progression
        await self._combat_service.start_combat(
            room_id=room_id,
            attacker=attacker_data,
            target=target_data,
            current_tick=current_tick,
        )

        # Now process the attack (initial attack, so skip turn order check)
        return await self._combat_service.process_attack(
            attacker_id=attacker_uuid, target_id=target_uuid, damage=damage, is_initial_attack=True
        )

    async def handle_npc_death(
        self,
        npc_id: str,
        room_id: str,
        killer_id: str | None = None,
        combat_id: str | None = None,
    ) -> bool:
        """
        Handle NPC death and related effects.

        Args:
            npc_id: ID of the dead NPC
            room_id: ID of the room where death occurred
            killer_id: ID of the entity that killed the NPC
            combat_id: ID of the combat if applicable

        Returns:
            bool: True if death was handled successfully

        BUGFIX: Enhanced logging and defensive exception handling to prevent player disconnections
        during NPC death operations. See: investigations/sessions/2025-11-20_combat-disconnect-bug-investigation.md
        """
        return await self._handlers.handle_npc_death(npc_id, room_id, killer_id, combat_id)

    def get_npc_combat_memory(self, npc_id: str) -> str | None:
        """
        Get the last attacker for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            str: ID of the last attacker, or None if no memory
        """
        return self._combat_memory.get_attacker(npc_id)

    def clear_npc_combat_memory(self, npc_id: str) -> bool:
        """
        Clear combat memory for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            bool: True if memory was cleared
        """
        return self._combat_memory.clear_memory(npc_id)

    def get_original_string_id(self, uuid_id: UUID) -> str | None:
        """
        Get the original string ID from a UUID.

        Args:
            uuid_id: The UUID to look up

        Returns:
            The original string ID if found, None otherwise
        """
        return self._uuid_mapping.get_original_string_id(uuid_id)
