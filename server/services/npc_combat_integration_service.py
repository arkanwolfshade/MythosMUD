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

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-locals,wrong-import-position  # Reason: Combat integration coordinates many services; imports after TYPE_CHECKING are intentional

from __future__ import annotations

from typing import TYPE_CHECKING, cast, final
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from ..config import get_config
from ..events.event_bus import EventBus
from ..game.mechanics import GameMechanicsService
from ..models.combat import CombatResult
from ..structured_logging.enhanced_logging_config import get_logger
from .combat_event_publisher import CombatEventPublisher
from .combat_messaging_integration import CombatMessagingIntegration
from .npc_combat_data_provider import NPCCombatDataProvider
from .npc_combat_grace import (
    is_npc_attack_on_player_blocked_by_login_grace_period,
    is_player_attack_blocked_by_login_grace_period,
)
from .npc_combat_handlers import NPCCombatHandlers
from .npc_combat_integration_combat_mixin import NPCCombatIntegrationCombatMixin
from .npc_combat_integration_validation_mixin import NPCCombatIntegrationValidationMixin
from .npc_combat_lifecycle import NPCCombatLifecycle
from .npc_combat_lucidity import NPCCombatLucidity
from .npc_combat_memory import NPCCombatMemory
from .npc_combat_rewards import NPCCombatRewards
from .npc_combat_uuid_mapping import NPCCombatUUIDMapping
from .player_combat_service import PlayerCombatService

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer
    from ..realtime.connection_manager import ConnectionManager
    from .combat_service import CombatService

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


@final
class NPCCombatIntegrationService(NPCCombatIntegrationValidationMixin, NPCCombatIntegrationCombatMixin):
    """
    Service for integrating NPCs with the combat system.

    This service handles:
    - NPC combat memory management
    - Basic combat interactions
    - Event publishing and messaging
    """

    event_bus: EventBus
    _persistence: AsyncPersistenceLayer
    _game_mechanics: GameMechanicsService
    _player_combat_service: PlayerCombatService
    _combat_memory: NPCCombatMemory
    _uuid_mapping: NPCCombatUUIDMapping
    _data_provider: NPCCombatDataProvider
    _rewards: NPCCombatRewards
    _lucidity: NPCCombatLucidity
    _lifecycle: NPCCombatLifecycle
    _combat_service: CombatService
    _messaging_integration: CombatMessagingIntegration
    _event_publisher: CombatEventPublisher
    _handlers: NPCCombatHandlers

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Combat integration initialization requires many service dependencies
        self,
        event_bus: EventBus | None = None,
        combat_service: CombatService | None = None,
        player_combat_service: PlayerCombatService | None = None,
        connection_manager: ConnectionManager | None = None,
        async_persistence: AsyncPersistenceLayer | None = None,
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
        self._init_persistence_and_event_bus(event_bus, async_persistence)
        self._init_player_combat_service(player_combat_service)
        self._init_npc_submodules(async_persistence)
        self._init_combat_service(combat_service)
        self._init_messaging_handlers_and_publisher(connection_manager)
        logger.info("NPC Combat Integration Service initialized with auto-progression enabled")

    def _init_persistence_and_event_bus(
        self,
        event_bus: EventBus | None,
        async_persistence: AsyncPersistenceLayer,
    ) -> None:
        self.event_bus = event_bus or EventBus()
        self._persistence = async_persistence
        logger.debug(
            "NPCCombatIntegrationService constructor",
            persistence_type=type(self._persistence).__name__,
        )
        self._game_mechanics = GameMechanicsService(async_persistence)

    def _init_player_combat_service(self, player_combat_service: PlayerCombatService | None) -> None:
        if player_combat_service is not None:
            self._player_combat_service = player_combat_service
            self._player_combat_service.set_npc_combat_integration_service(self)
            logger.info(
                "Using shared PlayerCombatService instance and updated NPC combat integration reference",
                instance_id=id(player_combat_service),
            )
        else:
            self._player_combat_service = PlayerCombatService(self._persistence, self.event_bus, self)
            logger.warning(
                "Created NEW PlayerCombatService instance - this should only happen in tests!",
                instance_id=id(self._player_combat_service),
            )

    def _init_npc_submodules(self, async_persistence: AsyncPersistenceLayer) -> None:
        self._combat_memory = NPCCombatMemory()
        self._uuid_mapping = NPCCombatUUIDMapping()
        self._data_provider = NPCCombatDataProvider(async_persistence)
        self._rewards = NPCCombatRewards(async_persistence, self._game_mechanics)
        self._lucidity = NPCCombatLucidity()
        self._lifecycle = NPCCombatLifecycle(async_persistence)

    def _init_combat_service(self, combat_service: CombatService | None) -> None:
        if combat_service is not None:
            self._combat_service = combat_service
            self._combat_service.set_player_combat_service(self._player_combat_service)
            self._combat_service.set_npc_combat_integration_service(self)
        else:
            from .combat_service import (
                CombatService,  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import breaks circular import at module load
            )

            self._combat_service = CombatService(self._player_combat_service, npc_combat_integration_service=self)

        self._combat_service.auto_progression_enabled = True
        combat_config = get_config()
        self._combat_service.turn_interval_seconds = combat_config.game.combat_tick_interval

    def _init_messaging_handlers_and_publisher(self, connection_manager: ConnectionManager | None) -> None:
        self._messaging_integration = CombatMessagingIntegration(connection_manager=connection_manager)
        self._event_publisher = CombatEventPublisher(nats_service=None)
        self._handlers = NPCCombatHandlers(
            self._data_provider,
            self._rewards,
            self._combat_memory,
            self._lifecycle,
            self._messaging_integration,
        )

    def get_messaging_integration(self) -> CombatMessagingIntegration:
        """Return combat messaging integration for room broadcasts (e.g. aggro switches)."""
        return self._messaging_integration

    def get_combat_service(self) -> CombatService:
        """Return combat service dependency for integration collaborators."""
        return self._combat_service

    def get_data_provider(self) -> NPCCombatDataProvider:
        """Return NPC data provider dependency for integration collaborators."""
        return self._data_provider

    def get_uuid_mapping(self) -> NPCCombatUUIDMapping:
        """Return UUID mapping dependency for integration collaborators."""
        return self._uuid_mapping

    def get_rewards_service(self) -> NPCCombatRewards:
        """Return rewards dependency for integration collaborators."""
        return self._rewards

    def get_lucidity_service(self) -> NPCCombatLucidity:
        """Return lucidity dependency for integration collaborators."""
        return self._lucidity

    async def _complete_player_attack_on_npc_after_grace(
        self,
        player_id: str,
        npc_id: str,
        room_id: str,
        action_type: str,
        damage: int,
        npc_instance: object | None,
    ) -> bool:
        """Player attack path after login grace check passes."""
        npc_instance = await self._validate_and_get_npc_instance(player_id, npc_id, npc_instance)
        if not npc_instance:
            return False

        if not await self._validate_combat_location(player_id, npc_id, room_id, npc_instance):
            await self._end_combat_if_participant_in_combat(player_id, npc_id)
            return False

        first_engagement = self._combat_memory.record_attack(npc_id, player_id)
        attacker_uuid, target_uuid = await self._setup_combat_uuids_and_mappings(
            player_id, npc_id, room_id, first_engagement
        )

        combat_result: CombatResult = await self._process_combat_attack(
            player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance
        )

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

    async def _run_npc_attack_on_player_after_grace(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        npc_instance: object | None,
    ) -> bool:
        """NPC attack path after login grace check passes."""
        npc_instance = npc_instance or self._data_provider.get_npc_instance(npc_id)
        if not npc_instance or not getattr(npc_instance, "is_alive", True):
            return False

        if not await self._validate_combat_location(target_id, npc_id, room_id, npc_instance):
            return False

        if not self._combat_service:
            logger.warning("NPC attack on player skipped - no combat service")
            return False

        npc_uuid, player_uuid = self._setup_combat_uuids_npc_attacker(npc_id, target_id)

        existing_combat = await self._combat_service.get_combat_by_participant(player_uuid)
        if existing_combat:
            if npc_uuid in existing_combat.participants:
                return True
            return False

        await self._apply_npc_attack_damage_for_npc_initiated_combat(
            room_id=room_id,
            target_id=target_id,
            npc_instance=npc_instance,
            npc_uuid=npc_uuid,
            player_uuid=player_uuid,
            attack_damage=attack_damage,
        )
        self._broadcast_npc_attack_on_player_started(
            npc_id=npc_id,
            target_id=target_id,
            room_id=room_id,
            attack_damage=attack_damage,
        )
        return True

    async def handle_player_attack_on_npc(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Attack handling matches external API
        self,
        player_id: str,
        npc_id: str,
        room_id: str,
        action_type: str = "punch",
        damage: int = 10,
        npc_instance: object | None = None,
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
            if is_player_attack_blocked_by_login_grace_period(player_id):
                logger.info(
                    "Player attack on NPC blocked - player in login grace period",
                    player_id=player_id,
                    npc_id=npc_id,
                )
                return False

            return await self._complete_player_attack_on_npc_after_grace(
                player_id, npc_id, room_id, action_type, damage, npc_instance
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error(
                "Error handling player attack on NPC",
                error=str(e),
                player_id=player_id,
                npc_id=npc_id,
            )
            return False

    async def handle_npc_attack(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        attack_type: str = "physical",
        npc_stats: dict[str, int] | None = None,
        npc_instance: object | None = None,
    ) -> bool:
        """
        Aggressive-mob entrypoint; matches NPCCombatIntegration.handle_npc_attack for interchangeability.

        The full combat path resolves stats via the data provider; attack_type and npc_stats are ignored here.
        """
        _ = attack_type, npc_stats
        return await self.handle_npc_attack_on_player(
            npc_id, target_id, room_id, attack_damage, npc_instance=npc_instance
        )

    async def handle_npc_attack_on_player(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int = 10,
        npc_instance: object | None = None,
    ) -> bool:
        """
        Handle an NPC attacking a player (aggro) using the same combat codepath as player-initiated combat.

        Starts a combat instance with the NPC as attacker and the player as target, then processes
        the initial attack. Subsequent rounds are handled by the combat turn processor.
        """
        try:
            target_uuid = UUID(target_id)

            if is_npc_attack_on_player_blocked_by_login_grace_period(target_uuid):
                logger.info(
                    "NPC attack on player blocked - player in login grace period",
                    npc_id=npc_id,
                    target_id=target_id,
                )
                return False

            return await self._run_npc_attack_on_player_after_grace(
                npc_id, target_id, room_id, attack_damage, npc_instance
            )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error(
                "Error handling NPC attack on player",
                error=str(e),
                npc_id=npc_id,
                target_id=target_id,
            )
            return False

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
        result = await self._handlers.handle_npc_death(npc_id, room_id, killer_id, combat_id)
        if result and killer_id and room_id:
            await self._broadcast_room_after_npc_death(npc_id, room_id, killer_id)
        return result

    def get_npc_combat_memory(self, npc_id: str) -> str | None:
        """Get the last attacker for an NPC."""
        return self._combat_memory.get_attacker(npc_id)

    def clear_npc_combat_memory(self, npc_id: str) -> bool:
        """Clear combat memory for an NPC."""
        return self._combat_memory.clear_memory(npc_id)

    def get_original_string_id(self, uuid_id: UUID) -> str | None:
        """Get the original string ID from a UUID."""
        return self._uuid_mapping.get_original_string_id(uuid_id)
