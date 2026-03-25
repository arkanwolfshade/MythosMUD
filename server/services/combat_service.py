"""Core combat service for managing combat state and logic."""

# pyright: reportImportCycles=false
# Runtime cycle is broken via lazy imports; checker still sees in-function imports as edges.
# pylint: disable=too-many-lines  # Reason: Combat service is the central coordinator for combat state and handlers; splitting would obscure control flow.

from typing import TYPE_CHECKING, cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from server.config import get_config
from server.events.combat_events import CombatStartedEvent, NPCDiedEvent, NPCTookDamageEvent
from server.events.event_bus import EventBus
from server.models.combat import (
    CombatInstance,
    CombatParticipant,
    CombatParticipantType,
    CombatResult,
)
from server.services.combat_attack_handler import CombatAttackHandler
from server.services.combat_cleanup_handler import CombatCleanupHandler
from server.services.combat_death_handler import CombatDeathHandler, CombatServiceDeps
from server.services.combat_event_handler import CombatEventHandler
from server.services.combat_event_publisher import CombatEventPublisher
from server.services.combat_flee_handler import check_involuntary_flee as check_involuntary_flee_fn
from server.services.combat_initialization import CombatInitializer
from server.services.combat_persistence_handler import CombatPersistenceHandler
from server.services.combat_service_npc import (
    get_combat_by_participant as get_combat_by_participant_impl,
)
from server.services.combat_service_npc import (
    get_combat_id_for_npc,
)
from server.services.combat_service_npc import (
    get_npc_participant_current_room as get_npc_participant_current_room_impl,
)
from server.services.combat_service_npc import (
    get_participant_current_room as get_participant_current_room_impl,
)
from server.services.combat_service_npc import (
    is_npc_in_combat_sync as is_npc_in_combat_sync_impl,
)
from server.services.combat_service_npc import (
    sync_npc_participant_dp_after_spell_damage as sync_npc_dp_impl,
)
from server.services.combat_service_state import (  # noqa: PLC0415  # Reason: Lazy import would break circular dependency resolution, this import must be at module level for service state management
    COMBAT_SERVICE,
    get_combat_service,
    set_combat_service,
)
from server.services.combat_service_types import PlayerLifecycleServices
from server.services.combat_turn_processor import CombatTurnProcessor
from server.services.combat_types import CombatParticipantData
from server.services.nats_service import NATSService
from server.services.nats_subject_manager import NATSSubjectManager
from server.services.player_combat_service import PlayerCombatService
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.magic.magic_service import MagicService
    from server.services.npc_combat_data_provider import NPCCombatDataProvider
    from server.services.npc_combat_integration_service import NPCCombatIntegrationService
    from server.services.player_death_service import PlayerDeathService
    from server.services.player_respawn_service import PlayerRespawnService

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class CombatService:  # pylint: disable=too-many-instance-attributes  # Reason: Combat service requires many state tracking and service attributes
    """
    Service for managing combat instances and state.
    """

    _combat_timeout_minutes: int
    _player_combat_service: PlayerCombatService | None
    _nats_service: NATSService | None
    _npc_combat_integration_service: "NPCCombatIntegrationService | None"
    _player_death_service: "PlayerDeathService | None"
    _player_respawn_service: "PlayerRespawnService | None"
    magic_service: "MagicService | None"
    _event_bus: EventBus
    _combat_event_publisher: CombatEventPublisher
    _auto_progression_enabled: bool
    _turn_interval_seconds: int
    _turn_processor: CombatTurnProcessor
    _attack_handler: CombatAttackHandler
    _death_handler: CombatDeathHandler
    _event_handler: CombatEventHandler
    _persistence_handler: CombatPersistenceHandler
    _cleanup_handler: CombatCleanupHandler

    def __init__(
        self,
        player_combat_service: PlayerCombatService | None = None,
        nats_service: NATSService | None = None,
        npc_combat_integration_service: "NPCCombatIntegrationService | None" = None,
        subject_manager: NATSSubjectManager | None = None,
        player_lifecycle_services: "PlayerLifecycleServices | None" = None,
        event_bus: EventBus | None = None,
        magic_service: "MagicService | None" = None,
    ) -> None:
        """Initialize the combat service."""
        self._active_combats: dict[UUID, CombatInstance] = {}
        self._player_combats: dict[UUID, UUID] = {}  # player_id -> combat_id
        self._npc_combats: dict[UUID, UUID] = {}  # npc_id -> combat_id
        self._combat_timeout_minutes = 30  # Configurable timeout
        self._player_combat_service = player_combat_service
        self._nats_service = nats_service
        self._npc_combat_integration_service = npc_combat_integration_service
        life = player_lifecycle_services
        self._player_death_service = life.player_death_service if life else None
        self._player_respawn_service = life.player_respawn_service if life else None
        self.magic_service = magic_service  # For casting state checks
        # CRITICAL: Use shared EventBus instance, not a new one
        self._event_bus = event_bus or EventBus()
        # Create combat event publisher with proper NATS service and subject_manager
        logger.debug("Creating CombatEventPublisher with NATS service", nats_service_available=bool(nats_service))
        try:
            logger.debug("Creating CombatEventPublisher")
            # If no subject_manager provided, create one with default settings
            if subject_manager is None and nats_service is not None:
                subject_manager = NATSSubjectManager()
                logger.debug("Created NATSSubjectManager with default settings")
            self._combat_event_publisher = CombatEventPublisher(nats_service, subject_manager)
            logger.debug("CombatEventPublisher created successfully")
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: CombatEventPublisher creation errors unpredictable, must handle gracefully
            logger.error(
                "CRITICAL ERROR: Failed to create CombatEventPublisher",
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise
        # Auto-progression configuration
        self._auto_progression_enabled = True
        # Get combat round interval from config (defaults to 10 seconds = 100 ticks)
        config = get_config()
        self._turn_interval_seconds = int(config.game.combat_tick_interval)

        # Initialize helper handlers
        self._turn_processor = CombatTurnProcessor(self)
        self._attack_handler = CombatAttackHandler(self)
        self._death_handler = CombatDeathHandler(cast(CombatServiceDeps, self))
        self._event_handler = CombatEventHandler(self)
        self._persistence_handler = CombatPersistenceHandler(self)
        self._cleanup_handler = CombatCleanupHandler(self)

    @property
    def auto_progression_enabled(self) -> bool:
        """Return whether auto-progression is enabled."""
        return self._auto_progression_enabled

    @auto_progression_enabled.setter
    def auto_progression_enabled(self, value: bool) -> None:
        """Enable or disable combat auto-progression."""
        self._auto_progression_enabled = value

    @property
    def turn_interval_seconds(self) -> int:
        """Return the turn interval in seconds."""
        return self._turn_interval_seconds

    @turn_interval_seconds.setter
    def turn_interval_seconds(self, value: int) -> None:
        """Set the turn interval in seconds."""
        self._turn_interval_seconds = value

    async def start_combat(
        self,
        room_id: str,
        attacker: CombatParticipantData,
        target: CombatParticipantData,
        current_tick: int,
    ) -> CombatInstance:
        """Start a new combat instance between two participants."""
        from server.services.combat_service_start import (
            check_attacker_grace_period as check_attacker_grace_period_impl,
        )
        from server.services.combat_service_start import (
            check_target_rest_and_grace_period as check_target_rest_and_grace_period_impl,
        )
        from server.services.combat_service_start import (
            publish_combat_started_event as publish_combat_started_event_impl,
        )
        from server.services.combat_service_start import (
            register_combat as register_combat_impl,
        )
        from server.services.combat_service_start import (
            validate_combat_can_start as validate_combat_can_start_impl,
        )

        logger.info("Starting combat", attacker=attacker.name, target=target.name, room_id=room_id)

        await check_target_rest_and_grace_period_impl(self, target, attacker)
        await check_attacker_grace_period_impl(self, attacker, target)
        await validate_combat_can_start_impl(self, attacker, target)

        combat = CombatInitializer.create_combat_instance(
            room_id=room_id,
            attacker=attacker,
            target=target,
            current_tick=current_tick,
            auto_progression_enabled=self._auto_progression_enabled,
            turn_interval_seconds=self._turn_interval_seconds,
        )

        await register_combat_impl(self, combat, attacker, room_id)

        logger.info("Combat started", combat_id=combat.combat_id, turn_order=combat.turn_order)

        await publish_combat_started_event_impl(self, combat, room_id)

        return combat

    async def publish_npc_damage_event(
        self,
        room_id: str,
        npc_id: UUID | str,
        npc_name: str,
        damage: int,
        current_dp: int,
        max_dp: int,
        combat_id: UUID | None = None,
    ) -> bool:
        """Publish an npc_took_damage event for non-combat damage."""
        from server.services.combat_service_events import (
            publish_npc_damage_event as publish_npc_damage_event_impl,
        )

        return await publish_npc_damage_event_impl(
            self, room_id, npc_id, npc_name, damage, current_dp, max_dp, combat_id
        )

    async def publish_npc_died_event(
        self,
        room_id: str,
        npc_id: UUID | str,
        npc_name: str,
        xp_reward: int = 0,
        killer_id: str | None = None,
    ) -> bool:
        """Publish an npc_died event when non-combat damage kills an NPC."""
        from server.services.combat_service_events import (
            publish_npc_died_event as publish_npc_died_event_impl,
        )

        return await publish_npc_died_event_impl(self, room_id, npc_id, npc_name, xp_reward, killer_id)

    def sync_npc_participant_dp_after_spell_damage(self, npc_id: str, new_dp: int) -> None:
        """Sync NPC CombatParticipant.current_dp after spell damage."""
        sync_npc_dp_impl(self, npc_id, new_dp)

    def _get_combat_id_for_npc(self, npc_id: UUID | str) -> UUID | None:
        """Return combat_id if this NPC is in combat, else None."""
        return get_combat_id_for_npc(self, npc_id)

    async def end_combat_if_npc_died(self, npc_id: UUID | str) -> bool:
        """End combat if the given NPC is in combat (e.g. steal-life kill)."""
        combat_id = get_combat_id_for_npc(self, npc_id)
        if not combat_id:
            return False
        await self.end_combat(combat_id, "Combat ended - NPC slain")
        return True

    async def process_game_tick(self, current_tick: int) -> None:
        """Process a game tick for combat auto-progression."""
        await self._turn_processor.process_game_tick(current_tick, self._active_combats, self._auto_progression_enabled)

    def get_combat(self, combat_id: UUID) -> CombatInstance | None:
        """Return the active combat for combat_id, or None if not found."""
        return self._active_combats.get(combat_id)

    def get_npc_combat_integration_service(self) -> "NPCCombatIntegrationService | None":
        """Return the NPC combat integration service."""
        return self._npc_combat_integration_service

    def set_npc_combat_integration_service(self, service: "NPCCombatIntegrationService | None") -> None:
        """Attach or replace the NPC combat integration service."""
        self._npc_combat_integration_service = service

    def set_player_combat_service(self, service: PlayerCombatService | None) -> None:
        """Attach or replace the player combat service (shared instance wiring)."""
        self._player_combat_service = service

    def get_combat_id_for_participant(self, participant_id: UUID) -> UUID | None:
        """Return combat_id if a participant is in combat, else None."""
        return self._player_combats.get(participant_id) or self._npc_combats.get(participant_id)

    def get_combat_id_for_npc_uuid(self, npc_uuid: UUID) -> UUID | None:
        """Return combat_id if an NPC UUID is in combat, else None."""
        return self._npc_combats.get(npc_uuid)

    async def get_combat_by_participant(self, participant_id: UUID) -> CombatInstance | None:
        """Return the combat instance for a specific participant, if any."""
        return get_combat_by_participant_impl(self, participant_id)

    async def broadcast_aggro_target_switches(
        self,
        room_id: str,
        combat_id: UUID,
        switches: list[tuple[UUID, str, str]],
    ) -> None:
        """
        Broadcast one room message per aggro target switch (ADR-016).
        switches: list of (npc_id, npc_name, new_target_name).
        """
        from server.services.combat_service_events import (
            broadcast_aggro_target_switches as broadcast_aggro_target_switches_impl,
        )

        await broadcast_aggro_target_switches_impl(self, room_id, combat_id, switches)

    def is_npc_in_combat_sync(self, npc_id: str) -> bool:
        """Return True if an NPC (string or UUID) is currently in combat."""
        return is_npc_in_combat_sync_impl(self, npc_id)

    def _get_npc_participant_current_room(
        self,
        data_provider: "NPCCombatDataProvider",
        svc: "NPCCombatIntegrationService",
        participant: CombatParticipant,
    ) -> str | None:
        """Return current room for an NPC participant, or None if unavailable."""
        return get_npc_participant_current_room_impl(self, data_provider, svc, participant)

    async def get_participant_current_room(self, participant: CombatParticipant) -> str | None:
        """Return current room ID for a combat participant, or None."""
        return await get_participant_current_room_impl(self, participant)

    async def validate_melee_location(
        self, combat: CombatInstance, attacker: CombatParticipant, target: CombatParticipant
    ) -> tuple[bool, str | None]:
        """Validate both participants are still in combat.room_id for melee."""
        from server.services.combat_service_attack import validate_melee_location as validate_melee_location_impl

        return await validate_melee_location_impl(self, combat, attacker, target)

    async def _handle_player_dp_update(self, target: CombatParticipant, old_dp: int, combat: CombatInstance) -> None:
        """Handle player DP update, persistence, and event publishing."""
        await self._persistence_handler.publish_player_dp_update_event(
            target.participant_id,
            old_dp,
            target.current_dp,
            target.max_dp,
            combat_id=str(combat.combat_id),
            room_id=combat.room_id,
        )
        self._persistence_handler.persist_player_dp_background(
            target.participant_id,
            target.current_dp,
            old_dp,
            target.max_dp,
            combat.room_id,
            str(combat.combat_id),
        )

    async def check_involuntary_flee(self, target: CombatParticipant, damage: int, combat: CombatInstance) -> bool:
        """Return True if player should involuntarily flee due to lucidity effects."""
        _ = combat  # Intentionally unused - reserved for future combat context needs
        return await check_involuntary_flee_fn(target, damage)

    async def validate_and_get_combat_participants(
        self, attacker_id: UUID, target_id: UUID, is_initial_attack: bool
    ) -> tuple[CombatInstance, CombatParticipant, CombatParticipant]:
        """Validate attack and retrieve combat and participants."""
        return await self._attack_handler.validate_and_get_combat_participants(
            attacker_id, target_id, is_initial_attack
        )

    async def apply_attack_damage(
        self, combat: CombatInstance, target: CombatParticipant, damage: int
    ) -> tuple[int, bool, bool]:
        """Apply damage to target and update combat state."""
        old_dp, target_died, target_mortally_wounded = await self._attack_handler.apply_attack_damage(
            combat, target, damage
        )
        if target.participant_type == CombatParticipantType.PLAYER:
            await self._handle_player_dp_update(target, old_dp, combat)
        return old_dp, target_died, target_mortally_wounded

    async def handle_target_state_changes(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: State change handling requires many parameters for context and state updates
        self,
        target: CombatParticipant,
        current_participant: CombatParticipant,
        target_mortally_wounded: bool,
        target_died: bool,
        combat: CombatInstance,
    ) -> None:
        """Handle mortally wounded and death state changes for target."""
        await self._death_handler.handle_target_state_changes(
            target, current_participant, target_mortally_wounded, target_died, combat
        )

    async def handle_attack_events_and_xp(
        self,
        current_participant: CombatParticipant,
        target: CombatParticipant,
        damage: int,
        combat: CombatInstance,
        target_died: bool,
        target_id: UUID,
    ) -> int | None:
        """Publish attack events and calculate XP reward if target died."""
        return await self._event_handler.handle_attack_events_and_xp(
            current_participant, target, damage, combat, target_died, target_id
        )

    async def award_xp_to_player(
        self, current_participant: CombatParticipant, target: CombatParticipant, target_id: UUID, xp_amount: int | None
    ) -> None:
        """Award XP to player for defeating an NPC."""
        await self._event_handler.award_xp_to_player(current_participant, target, target_id, xp_amount)

    async def handle_combat_completion(self, combat: CombatInstance, combat_ended: bool) -> None:
        """Handle combat completion or continuation."""
        from server.services.combat_service_attack import handle_combat_completion as handle_combat_completion_impl

        await handle_combat_completion_impl(self, combat, combat_ended)

    async def queue_combat_action(
        self,
        combat_id: UUID,
        participant_id: UUID,
        action_type: str,
        target_id: UUID | None = None,
        damage: int | None = None,
        spell_id: str | None = None,
        spell_name: str | None = None,
    ) -> bool:
        """Queue a combat action for a participant to execute in the next round."""
        from server.services.combat_service_attack import queue_combat_action as queue_combat_action_impl

        return await queue_combat_action_impl(
            self, combat_id, participant_id, action_type, target_id, damage, spell_id, spell_name
        )

    async def validate_melee_or_end_combat(
        self,
        combat: CombatInstance,
        current_participant: CombatParticipant,
        target: CombatParticipant,
        attacker_id: UUID,
        target_id: UUID,
    ) -> CombatResult | None:
        """Validate melee location; if invalid, end combat and return early result."""
        from server.services.combat_service_attack import (
            validate_melee_or_end_combat as validate_melee_or_end_combat_impl,
        )

        return await validate_melee_or_end_combat_impl(
            self, combat, current_participant, target, attacker_id, target_id
        )

    async def apply_damage_and_check_involuntary_flee(
        self,
        combat: CombatInstance,
        current_participant: CombatParticipant,
        target: CombatParticipant,
        damage: int,
    ) -> tuple[bool, bool, CombatResult | None]:
        """Apply attack damage and check for involuntary flee."""
        from server.services.combat_service_attack import (
            apply_damage_and_check_involuntary_flee as apply_damage_and_check_involuntary_flee_impl,
        )

        return await apply_damage_and_check_involuntary_flee_impl(self, combat, current_participant, target, damage)

    async def finalize_attack_result(
        self,
        combat: CombatInstance,
        current_participant: CombatParticipant,
        target: CombatParticipant,
        damage: int,
        target_died: bool,
        target_mortally_wounded: bool,
        target_id: UUID,
    ) -> CombatResult:
        """Build result, handle state changes, events, XP, and combat completion."""
        from server.services.combat_service_attack import (
            finalize_attack_result as finalize_attack_result_impl,
        )

        return await finalize_attack_result_impl(
            self, combat, current_participant, target, damage, target_died, target_mortally_wounded, target_id
        )

    async def process_attack(
        self,
        attacker_id: UUID,
        target_id: UUID,
        damage: int = 10,
        is_initial_attack: bool = False,
        damage_type: str = "physical",
    ) -> CombatResult:
        """Process an attack action in combat."""
        from server.services.combat_service_attack import process_attack as process_attack_impl

        return await process_attack_impl(self, attacker_id, target_id, damage, is_initial_attack, damage_type)

    async def register_combat_state(
        self,
        combat: CombatInstance,
        attacker_id: UUID,
        attacker_name: str,
        room_id: str,
    ) -> None:
        """Register combat in tracking dicts and notify player combat service."""
        self._active_combats[combat.combat_id] = combat
        self._player_combats[attacker_id] = combat.combat_id
        target_id = next(
            (p.participant_id for p in combat.participants.values() if p.participant_id != attacker_id),
            None,
        )
        if target_id:
            self._npc_combats[target_id] = combat.combat_id
        if self._player_combat_service:
            await self._player_combat_service.track_player_combat_state(
                player_id=attacker_id,
                player_name=attacker_name,
                combat_id=combat.combat_id,
                room_id=room_id,
            )

    async def publish_combat_started_event(self, event: CombatStartedEvent) -> None:
        """Publish a combat started event to NATS."""
        _ = await self._combat_event_publisher.publish_combat_started(event)

    async def publish_npc_took_damage_event_to_nats(self, event: NPCTookDamageEvent) -> bool:
        """Publish NPC took damage event to NATS."""
        return await self._combat_event_publisher.publish_npc_took_damage(event)

    async def publish_npc_died_event_to_nats(self, event: NPCDiedEvent) -> bool:
        """Publish NPC died event to NATS."""
        return await self._combat_event_publisher.publish_npc_died(event)

    def cleanup_combat_tracking(self, combat: CombatInstance) -> None:
        """Remove combat from tracking dictionaries."""
        self._cleanup_handler.cleanup_combat_tracking(combat)

    def check_connection_state(self, room_id: str) -> None:
        """Check connection state before publishing combat ended event."""
        self._cleanup_handler.check_connection_state(room_id)

    async def notify_player_combat_ended(self, combat_id: UUID) -> None:
        """Notify player combat service that combat ended."""
        if self._player_combat_service:
            await self._player_combat_service.handle_combat_end(combat_id)

    async def publish_combat_ended_event(self, combat: CombatInstance, reason: str) -> None:
        """Publish combat ended event."""
        await self._event_handler.publish_combat_ended_event(combat, reason)

    async def end_combat(self, combat_id: UUID, reason: str = "Combat ended") -> None:
        """End a combat instance."""
        from server.services.combat_service_end import end_combat as end_combat_impl

        await end_combat_impl(self, combat_id, reason)

    async def cleanup_stale_combats(self) -> int:
        """Clean up combats that have been inactive for too long."""
        return await self._cleanup_handler.cleanup_stale_combats(self._combat_timeout_minutes)

    async def get_combat_stats(self) -> dict[str, int]:
        """Return basic statistics about active combats."""
        return {
            "active_combats": len(self._active_combats),
            "player_combats": len(self._player_combats),
            "npc_combats": len(self._npc_combats),
        }


__all__ = ["COMBAT_SERVICE", "CombatService", "PlayerLifecycleServices", "get_combat_service", "set_combat_service"]
