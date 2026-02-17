"""
NPC Combat Event Handlers.

This module handles combat result processing and NPC death handling,
with defensive error handling to prevent player disconnections.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat handlers require many parameters for context and combat processing

from typing import Any, cast
from uuid import UUID, uuid4

from sqlalchemy.exc import SQLAlchemyError

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_combat_data_provider import NPCCombatDataProvider
from .npc_combat_lifecycle import NPCCombatLifecycle
from .npc_combat_memory import NPCCombatMemory
from .npc_combat_rewards import NPCCombatRewards

logger = get_logger(__name__)


class NPCCombatHandlers:
    """Handles combat result processing and NPC death operations."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat handler initialization requires many service dependencies
        self,
        data_provider: NPCCombatDataProvider,
        rewards: NPCCombatRewards,
        combat_memory: NPCCombatMemory,
        lifecycle: NPCCombatLifecycle,
        messaging_integration: Any,
    ) -> None:
        """
        Initialize the combat handlers.

        Args:
            data_provider: NPC combat data provider
            rewards: NPC combat rewards manager
            combat_memory: NPC combat memory manager
            lifecycle: NPC combat lifecycle manager
            messaging_integration: Combat messaging integration service
        """
        self._data_provider = data_provider
        self._rewards = rewards
        self._combat_memory = combat_memory
        self._lifecycle = lifecycle
        self._messaging_integration = messaging_integration

    async def handle_combat_result(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat result handling requires many parameters for context and result processing
        self,
        combat_result: Any,
        player_id: str,
        npc_id: str,
        room_id: str,
        action_type: str,
        damage: int,
        npc_instance: Any,
        handle_npc_death_callback: Any,
    ) -> bool:
        """
        Handle combat result, including broadcasting messages and handling NPC death.

        Args:
            combat_result: Result of the combat attack
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            room_id: ID of the room where combat occurs
            action_type: Type of attack action
            damage: Damage amount
            npc_instance: NPC instance
            handle_npc_death_callback: Callback function to handle NPC death

        Returns:
            True if attack was handled successfully
        """
        if combat_result.success:
            # Broadcast attack message with health info
            try:
                await self._messaging_integration.broadcast_combat_attack(
                    room_id=room_id,
                    attacker_name=await self._data_provider.get_player_name(player_id),
                    target_name=npc_instance.name,
                    damage=damage,
                    action_type=action_type,
                    combat_id=str(combat_result.combat_id) if combat_result.combat_id else str(uuid4()),
                    attacker_id=player_id,
                )
            except (ConnectionError, OSError, RuntimeError, ValueError, AttributeError, TypeError) as e:
                # Broadcasting is non-critical - catch specific exceptions to prevent combat flow interruption
                # ConnectionError/OSError: Network/connection issues with message broadcasting
                # RuntimeError: Runtime issues in connection manager
                # ValueError: Invalid parameters or data format issues
                # AttributeError: Missing attributes on npc_instance or data_provider
                # TypeError: Type mismatches in parameter passing
                logger.error(
                    "Error broadcasting combat attack",
                    player_id=player_id,
                    npc_id=npc_id,
                    error=str(e),
                    error_type=type(e).__name__,
                    exc_info=True,
                )

            # If combat ended, handle NPC death
            if combat_result.combat_ended:
                await self._handle_npc_death_on_combat_end(
                    player_id, npc_id, room_id, combat_result, handle_npc_death_callback
                )

            logger.info(
                "Player attack on NPC handled with auto-progression",
                player_id=player_id,
                npc_id=npc_id,
                damage=damage,
                combat_ended=combat_result.combat_ended,
                message=combat_result.message,
            )

            return cast(bool, combat_result.success)
        logger.warning(
            "Combat attack failed",
            player_id=player_id,
            npc_id=npc_id,
            message=combat_result.message,
        )
        return cast(bool, combat_result.success)

    async def _handle_npc_death_on_combat_end(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: NPC death handling requires many parameters for context and death processing
        self, player_id: str, npc_id: str, room_id: str, combat_result: Any, handle_npc_death_callback: Any
    ) -> None:
        """
        Handle NPC death when combat ends, with defensive exception handling.

        Args:
            player_id: ID of the attacking player
            npc_id: ID of the target NPC
            room_id: ID of the room where combat occurs
            combat_result: Result of the combat attack
            handle_npc_death_callback: Callback function to handle NPC death
        """
        logger.info(
            "Combat ended, handling NPC death",
            player_id=player_id,
            npc_id=npc_id,
            combat_id=str(combat_result.combat_id),
            room_id=room_id,
        )
        try:
            # Check player connection state before handling death
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            connection_manager = getattr(container, "connection_manager", None) if container else None
            player_uuid = UUID(player_id) if self._is_valid_uuid(player_id) else None
            if player_uuid and connection_manager is not None:
                has_websocket = player_uuid in connection_manager.player_websockets
                has_sse = False  # SSE connections not supported in WebSocket-only system
                logger.debug(
                    "Player connection state before NPC death handling",
                    player_id=player_id,
                    has_websocket=has_websocket,
                    has_sse=has_sse,
                )

            await handle_npc_death_callback(npc_id, room_id, player_id, str(combat_result.combat_id))
            logger.info(
                "NPC death handled successfully",
                player_id=player_id,
                npc_id=npc_id,
                combat_id=str(combat_result.combat_id),
            )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as death_error:
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
            npc_instance = self._data_provider.get_npc_instance(npc_id)
            if not npc_instance:
                logger.warning(
                    "Attempted to handle death for non-existent NPC",
                    npc_id=npc_id,
                )
                return False

            # Get NPC definition and calculate XP reward
            npc_definition = await self._data_provider.get_npc_definition(npc_id)
            xp_reward = await self._rewards.calculate_xp_reward(npc_definition)

            # Award XP to killer if it's a player
            if killer_id:
                await self._rewards.award_xp_to_killer(killer_id, npc_id, xp_reward)

            # Note: NPCDiedEvent is now published by CombatService to avoid duplication
            # The CombatService handles the npc_died event publishing when combat ends
            # We no longer call broadcast_combat_death() to prevent duplicate messages

            # Clear combat memory and despawn NPC
            self._combat_memory.clear_memory(npc_id)
            await self._lifecycle.despawn_npc_safely(npc_id, room_id)

            logger.info(
                "NPC death handled successfully",
                npc_id=npc_id,
                killer_id=killer_id,
                xp_reward=xp_reward,
                combat_id=combat_id,
            )

            return True

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
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

    def _is_valid_uuid(self, uuid_string: str) -> bool:
        """Check if a string is a valid UUID."""
        try:
            UUID(uuid_string)
            return True
        except ValueError:
            return False
