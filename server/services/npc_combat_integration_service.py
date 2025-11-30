"""
NPC Combat Integration Service for MythosMUD.

This service provides integration between NPCs and the combat system,
including combat memory management and basic combat interactions.

As documented in the Cultes des Goules, proper combat integration is essential
for maintaining the balance between mortal investigators and the eldritch
entities they encounter in our world.
"""

from typing import Any
from uuid import UUID, uuid4

from ..database import get_async_session
from ..events.event_bus import EventBus
from ..game.mechanics import GameMechanicsService
from ..logging.enhanced_logging_config import get_logger
from ..models.combat import CombatParticipantType
from ..persistence import get_persistence
from .active_sanity_service import ActiveSanityService, UnknownEncounterCategoryError
from .combat_event_publisher import CombatEventPublisher
from .combat_messaging_integration import CombatMessagingIntegration
from .combat_service import CombatService
from .player_combat_service import PlayerCombatService

logger = get_logger(__name__)


class NPCCombatIntegrationService:
    """
    Service for integrating NPCs with the combat system.

    This service handles:
    - NPC combat memory management
    - Basic combat interactions
    - Event publishing and messaging
    """

    def __init__(
        self,
        event_bus: EventBus | None = None,
        combat_service: "CombatService | None" = None,
        player_combat_service=None,
        connection_manager=None,
    ):
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
        """
        self.event_bus = event_bus or EventBus()
        self._persistence = get_persistence(event_bus)
        logger.debug(
            "NPCCombatIntegrationService constructor",
            persistence_type=type(self._persistence).__name__,
            persistence_is_none=self._persistence is None,
        )
        # Initialize GameMechanicsService for proper XP awards and stat updates
        self._game_mechanics = GameMechanicsService(self._persistence)

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

        # Combat memory - NPCs remember who attacked them
        self._npc_combat_memory: dict[str, str] = {}

        # UUID to string ID mapping for reverse lookup during XP calculation
        self._uuid_to_string_id_mapping: dict[UUID, str] = {}

        # UUID to XP value mapping for direct XP lookup
        self._uuid_to_xp_mapping: dict[UUID, int] = {}

        if combat_service is not None:
            self._combat_service = combat_service
            # CRITICAL FIX: Update the CombatService to use our PlayerCombatService with UUID mapping
            self._combat_service._player_combat_service = self._player_combat_service
            self._combat_service._npc_combat_integration_service = self
        else:
            # Only create a new CombatService if one was not provided
            # (this is primarily for testing)
            self._combat_service = CombatService(self._player_combat_service, npc_combat_integration_service=self)

        # Enable auto-progression features
        self._combat_service.auto_progression_enabled = True
        self._combat_service.turn_interval_seconds = 6

        # CRITICAL FIX: Pass connection_manager to CombatMessagingIntegration
        # If not provided, it will try to lazy-load from container (for backward compatibility)
        self._messaging_integration = CombatMessagingIntegration(connection_manager=connection_manager)
        self._event_publisher = CombatEventPublisher(event_bus)

        logger.info("NPC Combat Integration Service initialized with auto-progression enabled")

    async def handle_player_attack_on_npc(
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
                npc_instance = self._get_npc_instance(npc_id)
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
                return False

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
                return False

            # Validate that player and NPC are in the same room
            player_room_id = self._get_player_room_id(player_id)
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

            # Store combat memory - NPC remembers who attacked it
            first_engagement = npc_id not in self._npc_combat_memory
            self._npc_combat_memory[npc_id] = player_id

            # Convert string IDs to UUIDs for combat service
            try:
                attacker_uuid = UUID(player_id) if self._is_valid_uuid(player_id) else uuid4()
                target_uuid = UUID(npc_id) if self._is_valid_uuid(npc_id) else uuid4()

                # Always store the UUID-to-string ID mapping when we have a string ID
                # This mapping is used later during XP calculation
                if not self._is_valid_uuid(npc_id):
                    # Only store mapping for string IDs
                    self._uuid_to_string_id_mapping[target_uuid] = npc_id

                    # Also store the XP value directly for this UUID
                    # This avoids the need to look it up from the lifecycle manager
                    # during XP calculation, since NPCs may be removed by then
                    npc_definition = self._get_npc_definition(npc_id)
                    logger.debug(
                        "Retrieved NPC definition",
                        npc_id=npc_id,
                        has_definition=bool(npc_definition),
                    )
                    if npc_definition and first_engagement:
                        await self._apply_encounter_sanity_effect(player_id, npc_id, npc_definition, room_id)
                    if npc_definition:
                        base_stats = npc_definition.get_base_stats()
                        logger.debug(
                            "Retrieved base stats",
                            npc_id=npc_id,
                            base_stats=base_stats,
                        )
                        if isinstance(base_stats, dict):
                            xp_value = base_stats.get("xp_value", 0)  # Default to 0 if not found
                            self._uuid_to_xp_mapping[target_uuid] = xp_value
                            logger.debug(
                                "Stored UUID-to-XP mapping",
                                npc_id=npc_id,
                                target_uuid=target_uuid,
                                xp_value=xp_value,
                            )
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

                    logger.debug(
                        "Stored UUID-to-string ID mapping",
                        npc_id=npc_id,
                        target_uuid=target_uuid,
                    )

            except ValueError:
                attacker_uuid = uuid4()
                target_uuid = uuid4()
                # Don't store mapping for invalid UUIDs
                logger.debug("Skipping UUID mapping storage - invalid NPC ID", npc_id=npc_id)

            # Get current game tick
            from ..app.lifespan import get_current_tick

            current_tick = get_current_tick()

            # Check if combat already exists, if not start new combat
            existing_combat_id = self._combat_service._player_combats.get(attacker_uuid)
            if existing_combat_id:
                # Use existing combat
                combat_result = await self._combat_service.process_attack(
                    attacker_id=attacker_uuid, target_id=target_uuid, damage=damage
                )
            else:
                # Start new combat first
                player_name = self._get_player_name(player_id)

                # Fetch actual player stats from persistence to ensure correct HP
                # BUGFIX: Was hardcoded to 100, causing HP to reset between combats
                # Convert player_id to UUID if it's a string
                player_id_uuid = UUID(player_id) if isinstance(player_id, str) else player_id
                player = self._persistence.get_player(player_id_uuid)
                if not player:
                    logger.error("Player not found when starting combat", player_id=player_id)
                    return False

                player_stats = player.get_stats()
                attacker_hp = player_stats.get("current_health", 100)
                attacker_max_hp = player_stats.get("max_health", 100)
                attacker_dex = player_stats.get("dexterity", 10)

                logger.info(
                    "Starting combat with player stats",
                    player_id=player_id,
                    current_hp=attacker_hp,
                    max_hp=attacker_max_hp,
                    dex=attacker_dex,
                )

                # Get NPC stats properly from the NPC instance
                npc_stats = npc_instance.get_stats()
                npc_current_hp = npc_stats.get("hp", 100)
                npc_max_hp = npc_stats.get("max_hp", 100)
                npc_dexterity = npc_stats.get("dexterity", 10)

                # Start combat with auto-progression - fix parameter order
                await self._combat_service.start_combat(
                    room_id=room_id,
                    attacker_id=attacker_uuid,
                    target_id=target_uuid,
                    attacker_name=player_name,
                    target_name=npc_instance.name,
                    attacker_hp=attacker_hp,
                    attacker_max_hp=attacker_max_hp,
                    attacker_dex=attacker_dex,
                    target_hp=npc_current_hp,
                    target_max_hp=npc_max_hp,
                    target_dex=npc_dexterity,
                    current_tick=current_tick,
                    attacker_type=CombatParticipantType.PLAYER,
                    target_type=CombatParticipantType.NPC,
                )

                # Now process the attack (initial attack, so skip turn order check)
                combat_result = await self._combat_service.process_attack(
                    attacker_id=attacker_uuid, target_id=target_uuid, damage=damage, is_initial_attack=True
                )

            if combat_result.success:
                # Broadcast attack message with health info
                await self._messaging_integration.broadcast_combat_attack(
                    room_id=room_id,
                    attacker_name=self._get_player_name(player_id),
                    target_name=npc_instance.name,
                    damage=damage,
                    action_type=action_type,
                    combat_id=str(combat_result.combat_id) if combat_result.combat_id else str(uuid4()),
                    attacker_id=player_id,
                )

                # If combat ended, handle NPC death
                # BUGFIX: Add defensive exception handling to prevent disconnections during NPC death
                # As documented in investigation: 2025-11-20_combat-disconnect-bug-investigation.md
                # NPC death operations can fail and disconnect players if not properly handled
                if combat_result.combat_ended:
                    logger.info(
                        "Combat ended, handling NPC death",
                        player_id=player_id,
                        npc_id=npc_id,
                        combat_id=str(combat_result.combat_id),
                        room_id=room_id,
                    )
                    try:
                        # Check player connection state before handling death
                        from ..realtime.connection_manager import get_global_connection_manager

                        connection_manager = get_global_connection_manager()
                        player_uuid = UUID(player_id) if self._is_valid_uuid(player_id) else None
                        if player_uuid and connection_manager is not None:
                            has_websocket = player_uuid in connection_manager.player_websockets
                            has_sse = player_uuid in connection_manager.active_sse_connections
                            logger.debug(
                                "Player connection state before NPC death handling",
                                player_id=player_id,
                                has_websocket=has_websocket,
                                has_sse=has_sse,
                            )

                        self.handle_npc_death(npc_id, room_id, player_id, str(combat_result.combat_id))
                        logger.info(
                            "NPC death handled successfully",
                            player_id=player_id,
                            npc_id=npc_id,
                            combat_id=str(combat_result.combat_id),
                        )
                    except Exception as death_error:
                        # CRITICAL: Log but don't fail - prevent disconnection
                        logger.error(
                            "Error handling NPC death - preventing disconnect",
                            player_id=player_id,
                            npc_id=npc_id,
                            combat_id=str(combat_result.combat_id),
                            error=str(death_error),
                            exc_info=True,
                        )
                        # Continue execution - don't raise exception that could disconnect player

                logger.info(
                    "Player attack on NPC handled with auto-progression",
                    player_id=player_id,
                    npc_id=npc_id,
                    damage=damage,
                    combat_ended=combat_result.combat_ended,
                    message=combat_result.message,
                )

                return combat_result.success
            else:
                logger.warning(
                    "Combat attack failed",
                    player_id=player_id,
                    npc_id=npc_id,
                    message=combat_result.message,
                )
                return combat_result.success

        except Exception as e:
            logger.error(
                "Error handling player attack on NPC",
                error=str(e),
                player_id=player_id,
                npc_id=npc_id,
            )
            return False

    def handle_npc_death(
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
        logger.info(
            "NPC death handling started",
            npc_id=npc_id,
            room_id=room_id,
            killer_id=killer_id,
            combat_id=combat_id,
        )
        try:
            # Get NPC instance
            npc_instance = self._get_npc_instance(npc_id)
            if not npc_instance:
                logger.warning(
                    "Attempted to handle death for non-existent NPC",
                    npc_id=npc_id,
                )
                return False

            # Get NPC definition for XP reward
            npc_definition = self._get_npc_definition(npc_id)
            xp_reward = 0
            if npc_definition:
                # Use the get_base_stats() method to parse the JSON string
                base_stats = npc_definition.get_base_stats()
                if isinstance(base_stats, dict):
                    # Use xp_value from the database (not xp_reward)
                    xp_reward = base_stats.get("xp_value", xp_reward)

            # Award XP to killer if it's a player
            # BUGFIX: Enhanced exception handling with connection state preservation
            if killer_id:
                logger.info(
                    "Awarding XP to player for NPC kill",
                    player_id=killer_id,
                    npc_id=npc_id,
                    xp_reward=xp_reward,
                )
                # Check connection state before XP award
                try:
                    from ..realtime.connection_manager import get_global_connection_manager

                    connection_manager = get_global_connection_manager()
                    player_uuid = UUID(killer_id) if self._is_valid_uuid(killer_id) else None
                    if player_uuid and connection_manager is not None:
                        has_websocket = player_uuid in connection_manager.player_websockets
                        has_sse = player_uuid in connection_manager.active_sse_connections
                        logger.debug(
                            "Player connection state before XP award",
                            player_id=killer_id,
                            has_websocket=has_websocket,
                            has_sse=has_sse,
                        )
                except Exception as conn_check_error:
                    logger.warning(
                        "Could not check connection state before XP award",
                        player_id=killer_id,
                        error=str(conn_check_error),
                    )

                # CRITICAL FIX: Use GameMechanicsService.gain_experience() to prevent
                # XP awards from overwriting combat damage with stale health values
                try:
                    success, message = self._game_mechanics.gain_experience(killer_id, xp_reward, f"killed_{npc_id}")
                    if success:
                        logger.info(
                            "Awarded XP to player",
                            player_id=killer_id,
                            xp_reward=xp_reward,
                            npc_id=npc_id,
                        )
                    else:
                        logger.warning(
                            "Failed to award XP to player",
                            player_id=killer_id,
                            xp_reward=xp_reward,
                            message=message,
                        )
                except Exception as e:
                    # CRITICAL: Don't let XP award errors disconnect player
                    logger.error(
                        "Error awarding XP to player - preventing disconnect",
                        player_id=killer_id,
                        error=str(e),
                        exc_info=True,
                    )
                    # Continue - don't raise exception

            # Note: NPCDiedEvent is now published by CombatService to avoid duplication
            # The CombatService handles the npc_died event publishing when combat ends
            # We no longer call broadcast_combat_death() to prevent duplicate messages

            # Clear combat memory for this NPC
            logger.debug("Clearing combat memory for NPC", npc_id=npc_id)
            if str(npc_id) in self._npc_combat_memory:
                del self._npc_combat_memory[str(npc_id)]

            # Despawn NPC with defensive error handling
            logger.debug("Despawning NPC", npc_id=npc_id, room_id=room_id)
            try:
                self._despawn_npc(str(npc_id), room_id)
                logger.debug("NPC despawned successfully", npc_id=npc_id, room_id=room_id)
            except Exception as despawn_error:
                # CRITICAL: Don't let despawn errors disconnect player
                logger.error(
                    "Error despawning NPC - preventing disconnect",
                    npc_id=npc_id,
                    room_id=room_id,
                    error=str(despawn_error),
                    exc_info=True,
                )
                # Continue - despawn failure shouldn't disconnect player

            logger.info(
                "NPC death handled successfully",
                npc_id=npc_id,
                killer_id=killer_id,
                xp_reward=xp_reward,
                combat_id=combat_id,
            )

            return True

        except Exception as e:
            # CRITICAL: Prevent NPC death handling errors from disconnecting players
            logger.error(
                "Error handling NPC death - preventing player disconnect",
                npc_id=npc_id,
                room_id=room_id,
                killer_id=killer_id,
                combat_id=combat_id,
                error=str(e),
                exc_info=True,
            )
            # Return False but don't raise - prevents exception propagation
            return False

    def get_npc_combat_memory(self, npc_id: str) -> str | None:
        """
        Get the last attacker for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            str: ID of the last attacker, or None if no memory
        """
        return self._npc_combat_memory.get(npc_id)

    def clear_npc_combat_memory(self, npc_id: str) -> bool:
        """
        Clear combat memory for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            bool: True if memory was cleared
        """
        if npc_id in self._npc_combat_memory:
            del self._npc_combat_memory[npc_id]
            logger.debug("Cleared combat memory for NPC", npc_id=npc_id)
            return True
        return False

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """Get NPC instance from the spawning service."""
        try:
            # Use the same approach as the combat handler
            from .npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    return lifecycle_manager.active_npcs[npc_id]

            return None

        except Exception as e:
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    def _get_npc_definition(self, npc_id: str) -> Any | None:
        """Get NPC definition for an NPC instance."""
        try:
            # Try to get from lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = self._persistence.get_npc_lifecycle_manager()
                if lifecycle_manager:
                    keys = list(lifecycle_manager.lifecycle_records.keys())
                else:
                    keys = []
                logger.debug(
                    "_get_npc_definition lookup",
                    npc_id=npc_id,
                    has_lifecycle_manager=bool(lifecycle_manager),
                    lifecycle_records_count=len(keys),
                    npc_id_in_keys=npc_id in keys if lifecycle_manager else False,
                )
                if lifecycle_manager and npc_id in lifecycle_manager.lifecycle_records:
                    return lifecycle_manager.lifecycle_records[npc_id].definition

            return None

        except Exception as e:
            logger.error("Error getting NPC definition", npc_id=npc_id, error=str(e))
            return None

    def _get_player_name(self, player_id: str) -> str:
        """Get player name for messaging."""
        try:
            # Convert player_id to UUID if it's a string
            player_id_uuid = UUID(player_id) if isinstance(player_id, str) else player_id
            player = self._persistence.get_player(player_id_uuid)
            return str(player.name) if player else "Unknown Player"
        except (OSError, ValueError, TypeError, Exception) as e:
            logger.error("Error getting player name", player_id=player_id, error=str(e), error_type=type(e).__name__)
            return "Unknown Player"

    def _despawn_npc(self, npc_id: str, _room_id: str) -> None:
        """Despawn an NPC."""
        try:
            # Try lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = self._persistence.get_npc_lifecycle_manager()
                if lifecycle_manager:
                    # Record the death for 30-second respawn suppression
                    lifecycle_manager.record_npc_death(npc_id)
                    lifecycle_manager.despawn_npc(npc_id, "combat_death")
                    return

            # Fallback: try lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = self._persistence.get_npc_lifecycle_manager()
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    del lifecycle_manager.active_npcs[npc_id]

        except Exception as e:
            logger.error("Error despawning NPC", npc_id=npc_id, error=str(e))

    def _get_player_room_id(self, player_id: str) -> str | None:
        """
        Get the current room ID for a player.

        Args:
            player_id: ID of the player

        Returns:
            Room ID if found, None otherwise
        """
        try:
            # Convert player_id to UUID if it's a string
            player_id_uuid = UUID(player_id) if isinstance(player_id, str) else player_id
            player = self._persistence.get_player(player_id_uuid)
            if player:
                return str(player.current_room_id)
            return None
        except Exception as e:
            logger.error("Error getting player room ID", player_id=player_id, error=str(e))
            return None

    def _is_valid_uuid(self, uuid_string: str) -> bool:
        """Check if a string is a valid UUID."""
        try:
            UUID(uuid_string)
            return True
        except ValueError:
            return False

    def get_original_string_id(self, uuid_id: UUID) -> str | None:
        """
        Get the original string ID from a UUID.

        Args:
            uuid_id: The UUID to look up

        Returns:
            The original string ID if found, None otherwise
        """
        result = self._uuid_to_string_id_mapping.get(uuid_id)
        logger.debug(
            "UUID to string ID lookup",
            uuid_id=uuid_id,
            result=result,
            mapping_size=len(self._uuid_to_string_id_mapping),
        )
        return result

    async def _apply_encounter_sanity_effect(
        self,
        player_id: str,
        npc_id: str,
        npc_definition: Any | None,
        room_id: str,
    ) -> None:
        """Apply sanity loss when a player engages an eldritch entity."""

        definition_name: str | None = None
        if npc_definition is not None:
            potential_name = getattr(npc_definition, "name", None)
            if isinstance(potential_name, str) and potential_name.strip():
                definition_name = potential_name

        archetype = definition_name or npc_id
        category = self._resolve_sanity_category(npc_definition)

        async for session in get_async_session():
            service = ActiveSanityService(session)
            try:
                await service.apply_encounter_sanity_loss(
                    player_id=str(player_id),
                    entity_archetype=str(archetype),
                    category=category,
                    location_id=room_id,
                )
                await session.commit()
            except UnknownEncounterCategoryError:
                await session.rollback()
                logger.warning(
                    "Encounter SAN category unavailable, defaulting to disturbing",
                    npc_id=npc_id,
                    provided_category=category,
                )
                try:
                    await service.apply_encounter_sanity_loss(
                        player_id=str(player_id),
                        entity_archetype=str(archetype),
                        category="disturbing",
                        location_id=room_id,
                    )
                    await session.commit()
                except Exception as nested_exc:  # pragma: no cover - defensive logging
                    await session.rollback()
                    logger.error(
                        "Failed to apply fallback encounter sanity loss",
                        npc_id=npc_id,
                        player_id=player_id,
                        error=str(nested_exc),
                    )
            except Exception as exc:  # pragma: no cover - defensive logging
                await session.rollback()
                logger.error(
                    "Active encounter sanity adjustment failed",
                    npc_id=npc_id,
                    player_id=player_id,
                    room_id=room_id,
                    error=str(exc),
                )
            else:
                logger.info(
                    "Applied encounter sanity loss",
                    npc_id=npc_id,
                    player_id=player_id,
                    archetype=archetype,
                    category=category,
                )
            break

    def _resolve_sanity_category(self, npc_definition: Any | None) -> str:
        """Determine encounter category based on NPC definition metadata."""

        if npc_definition is None:
            return "disturbing"

        try:
            base_stats = npc_definition.get_base_stats()
        except Exception:
            base_stats = {}

        try:
            behavior_config = npc_definition.get_behavior_config()
        except Exception:
            behavior_config = {}

        for source in (base_stats, behavior_config):
            if isinstance(source, dict):
                category = source.get("sanity_category") or source.get("mythos_tier")
                if isinstance(category, str):
                    return category.lower()

        npc_type = getattr(npc_definition, "npc_type", "")
        if npc_type == "aggressive_mob":
            return "horrific"
        if npc_type == "passive_mob":
            return "disturbing"
        return "disturbing"
