# pylint: disable=too-many-lines  # Reason: NPC combat integration is a central coordination module; splitting further would scatter tightly related combat behaviors and harm readability of the end-to-end flow.
"""
NPC Combat Integration for MythosMUD.

This module provides integration between NPCs and the existing combat system,
including damage calculation, combat events, and interaction with the game
mechanics service.

As documented in the Cultes des Goules, proper combat integration is essential
for maintaining the balance between mortal investigators and the eldritch
entities they encounter.
"""

import uuid
from typing import TYPE_CHECKING, Protocol, cast

from structlog.stdlib import BoundLogger

from ..async_persistence import AsyncPersistenceLayer
from ..config import get_config
from ..events import EventBus
from ..events.combat_events import PlayerAttackedEvent
from ..events.event_types import NPCAttacked, PlayerDPUpdated
from ..exceptions import DatabaseError, ValidationError
from ..game.mechanics import GameMechanicsService
from ..realtime.login_grace_period import is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .lifecycle_manager import NPCLifecycleManager

# Removed: from ..persistence import get_persistence - now using async_persistence

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class _CombatEventPublisherProtocol(Protocol):
    """Protocol for combat event publisher (avoids importing CombatEventPublisher)."""

    async def publish_player_attacked(self, event: PlayerAttackedEvent) -> bool:
        """Publish a PlayerAttackedEvent to the combat event stream."""
        return False


class _NpcCombatServiceProtocol(Protocol):
    """Protocol for npc_combat_service to get typed handle_npc_attack_on_player."""

    async def handle_npc_attack_on_player(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        npc_instance: object | None = None,
    ) -> bool:
        """Handle an NPC attack against a player via the main combat service."""
        return False


class NPCCombatIntegration:
    """
    Integrates NPCs with the existing combat and game mechanics systems.

    This class provides methods for NPCs to interact with the combat system,
    including damage calculation, combat events, and integration with the
    game mechanics service for lucidity, fear, and corruption effects.
    """

    event_bus: EventBus
    _persistence: AsyncPersistenceLayer
    _game_mechanics: GameMechanicsService

    def __init__(
        self, event_bus: EventBus | None = None, async_persistence: AsyncPersistenceLayer | None = None
    ) -> None:
        """
        Initialize the NPC combat integration.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global
                instance.
            async_persistence: Async persistence layer instance (required)
        """
        if async_persistence is None:
            raise ValueError("async_persistence is required for NPCCombatIntegration")
        self.event_bus = event_bus or EventBus()
        self._persistence = async_persistence
        self._game_mechanics = GameMechanicsService(async_persistence)
        logger.debug("NPC combat integration initialized")

    def calculate_damage(
        self,
        attacker_stats: dict[str, int],
        target_stats: dict[str, int],  # kept for API compatibility; CON does not affect damage
        weapon_damage: int = 0,
        damage_type: str = "physical",
    ) -> int:
        """
        Calculate damage based on attacker and target stats.

        Args:
            attacker_stats: Stats of the attacking entity (NPC or player)
            target_stats: Stats of the target entity
            weapon_damage: Base damage from weapon or attack
            damage_type: Type of damage being dealt

        Returns:
            int: Calculated damage amount
        """
        try:
            # Explicitly mark target_stats as used to satisfy strict linters while preserving API compatibility.
            _ = target_stats

            # Base damage calculation
            base_damage = weapon_damage

            # Add strength modifier only for unarmed (physical) attacks.
            # Weapon attacks (slashing, piercing, etc.) use weapon dice only (e.g. 1d4+0).
            if damage_type == "physical":
                strength_mod = attacker_stats.get("strength", 50)
                strength_bonus = max(0, (strength_mod - 50) // 2)
                base_damage += strength_bonus

            # CON does not provide damage protection; use base_damage as final
            final_damage = max(1, base_damage)

            logger.debug(
                "Damage calculated",
                base_damage=base_damage,
                final_damage=final_damage,
                damage_type=damage_type,
                target_stats_snapshot=target_stats,
            )

            return final_damage

        except (TypeError, ValueError, ArithmeticError) as e:
            logger.error("Error calculating damage", error=str(e))
            return 1  # Minimum damage

    async def apply_combat_effects(
        self, target_id: str, damage: int, damage_type: str, source_id: str | None = None
    ) -> bool:
        """
        Apply combat effects to a target (player or NPC).

        Args:
            target_id: ID of the target entity
            damage: Amount of damage to apply
            damage_type: Type of damage
            source_id: ID of the source entity

        Returns:
            bool: True if effects were applied successfully
        """
        try:
            target_id_uuid = self._convert_target_id_to_uuid(target_id)
            player = await self._persistence.get_player_by_id(target_id_uuid)
            if player:
                return await self._apply_player_combat_effects(target_id, damage, damage_type)
            # If not a player, assume it's an NPC
            logger.debug("Target is not a player, assuming NPC", target_id=target_id)
            return True
        except AttributeError as e:
            self._handle_attribute_error(target_id, damage, damage_type, source_id, e)
            raise
        except ValidationError as e:
            return self._handle_validation_error(target_id, damage, damage_type, e)
        except Exception as e:
            self._handle_unexpected_error(target_id, damage, damage_type, e)
            raise

    def _convert_target_id_to_uuid(self, target_id: str | uuid.UUID) -> uuid.UUID:
        """Convert target_id to UUID, accepting either string or UUID input."""
        return target_id if isinstance(target_id, uuid.UUID) else uuid.UUID(target_id)

    async def _apply_player_combat_effects(self, target_id: str, damage: int, damage_type: str) -> bool:
        """Apply combat effects to a player."""
        # Check if target is in login grace period - block damage if so
        try:
            config = get_config()
            app_raw = getattr(config, "_app_instance", None)
            if app_raw:
                app = cast(object, app_raw)
                state_raw = getattr(app, "state", None)
                if not state_raw:
                    return False
                state = cast(object, state_raw)
                connection_manager = getattr(state, "connection_manager", None)
                if connection_manager:
                    target_uuid = self._convert_target_id_to_uuid(target_id)
                    if is_player_in_login_grace_period(target_uuid, connection_manager):
                        logger.info(
                            "NPC damage blocked - target in login grace period",
                            target_id=target_id,
                            damage=damage,
                            damage_type=damage_type,
                        )
                        return False  # Damage blocked
        except (AttributeError, ImportError, TypeError, ValueError) as e:
            # If we can't check grace period, proceed with damage (fail open)
            logger.debug("Could not check login grace period for NPC damage", target_id=target_id, error=str(e))

        # Apply damage to player using game mechanics service
        success, _ = await self._game_mechanics.damage_player(target_id, damage, damage_type)

        # Apply mental/occult effects
        await self._apply_mental_effects(target_id, damage, damage_type)

        logger.info("Combat effects applied to player", target_id=target_id, damage=damage, damage_type=damage_type)
        return success

    async def _apply_mental_effects(self, target_id: str, damage: int, damage_type: str) -> None:
        """Apply mental/occult effects (lucidity loss and fear) based on damage type."""
        # Apply lucidity loss for certain damage types
        if damage_type in ["mental", "occult"]:
            lucidity_loss = min(damage // 2, 10)  # Cap lucidity loss
            _, _ = await self._game_mechanics.apply_lucidity_loss(target_id, lucidity_loss, f"combat_{damage_type}")

        # Apply fear for certain damage types
        if damage_type in ["occult", "eldritch"]:
            fear_gain = min(damage // 3, 5)  # Cap fear gain
            _, _ = await self._game_mechanics.apply_fear(target_id, fear_gain, f"combat_{damage_type}")

    def _handle_attribute_error(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Error handling requires many parameters for context and error reporting
        self, target_id: str, damage: int, damage_type: str, source_id: str | None, error: AttributeError
    ) -> None:
        """Handle AttributeError (critical programming error)."""
        logger.critical(
            "CRITICAL: Missing persistence method called",
            target_id=target_id,
            error=str(error),
            error_type="AttributeError",
            damage=damage,
            damage_type=damage_type,
            source_id=source_id,
            exc_info=True,
        )

    def _handle_validation_error(self, target_id: str, damage: int, damage_type: str, error: ValidationError) -> bool:
        """Handle ValidationError (expected validation error)."""
        logger.warning(
            "Validation error in combat effects",
            target_id=target_id,
            error=str(error),
            damage=damage,
            damage_type=damage_type,
        )
        return False

    def _handle_unexpected_error(self, target_id: str, damage: int, damage_type: str, error: Exception) -> None:
        """Handle unexpected errors."""
        logger.error(
            "Unexpected error applying combat effects",
            target_id=target_id,
            error=str(error),
            error_type=type(error).__name__,
            damage=damage,
            damage_type=damage_type,
            exc_info=True,
        )

    async def handle_npc_attack(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: NPC attack handling requires many parameters for context and attack state
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
        Handle an NPC attack on a target.

        This is a thin wrapper around _handle_npc_attack_core that centralizes error handling.
        """
        try:
            return await self._handle_npc_attack_core(
                npc_id=npc_id,
                target_id=target_id,
                room_id=room_id,
                attack_damage=attack_damage,
                attack_type=attack_type,
                npc_stats=npc_stats,
                npc_instance=npc_instance,
            )
        except (ValueError, TypeError, AttributeError, ArithmeticError, ValidationError) as e:
            logger.error("Error handling NPC attack", npc_id=npc_id, target_id=target_id, error=str(e))
            return False
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Fire-and-forget task must log any unexpected error
            logger.error(
                "Unexpected error handling NPC attack",
                npc_id=npc_id,
                target_id=target_id,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            return False

    async def _handle_npc_attack_core(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        attack_type: str,
        npc_stats: dict[str, int] | None,
        npc_instance: object | None,
    ) -> bool:
        """
        Core implementation for handling an NPC attack on a target.

        When the app has NPCCombatIntegrationService (full combat path), delegates to
        handle_npc_attack_on_player so aggro uses the same combat codepath as player-initiated combat.
        Otherwise falls back to direct damage and event publishing (e.g. tests).
        """
        delegated_result = await self._try_delegate_npc_attack_to_combat_service(
            npc_id, target_id, room_id, attack_damage, npc_instance
        )
        if delegated_result is not None:
            return delegated_result

        if await self._is_target_in_login_grace_period(target_id):
            logger.info(
                "NPC attack blocked - target in login grace period",
                npc_id=npc_id,
                target_id=target_id,
            )
            return False

        await self._perform_direct_npc_attack(
            npc_id=npc_id,
            target_id=target_id,
            room_id=room_id,
            attack_damage=attack_damage,
            attack_type=attack_type,
            npc_stats=npc_stats,
        )
        return True

    async def _perform_direct_npc_attack(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        attack_type: str,
        npc_stats: dict[str, int] | None,
    ) -> None:
        """
        Execute the direct NPC attack path (no full combat service available).
        """
        target_stats = await self._get_target_stats(target_id)
        int_target_stats: dict[str, int] = {}
        for key, value in target_stats.items():
            if isinstance(value, (int, float)):
                int_target_stats[key] = int(value)
            elif isinstance(value, str) and value.isdigit():
                int_target_stats[key] = int(value)

        resolved_npc_stats = self._get_npc_stats(npc_stats)
        actual_damage = self.calculate_damage(resolved_npc_stats, int_target_stats, attack_damage, attack_type)
        effects_applied = await self.apply_combat_effects(target_id, actual_damage, attack_type, npc_id)
        if effects_applied:
            await self._publish_player_dp_updated_after_npc_damage(target_id, actual_damage, room_id)
        self._publish_attack_event(npc_id, target_id, room_id, actual_damage, attack_type)
        await self._publish_npc_attack_to_nats(npc_id, target_id, room_id, actual_damage, attack_type)
        logger.info(
            "NPC attack handled", npc_id=npc_id, target_id=target_id, damage=actual_damage, attack_type=attack_type
        )

    async def _try_delegate_npc_attack_to_combat_service(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
        npc_instance: object | None,
    ) -> bool | None:
        """
        Prefer full combat codepath (same as player-initiated combat) when available.

        Returns:
            bool | None: True/False if delegated, None if delegation is not possible.
        """
        try:
            config = get_config()
            app_raw = getattr(config, "_app_instance", None)
            if not app_raw:
                return None
            app = cast(object, app_raw)

            from ..commands.combat_loader import get_combat_command_handler

            handler = get_combat_command_handler(app)
            service_raw = getattr(handler, "npc_combat_service", None)
            service = cast(_NpcCombatServiceProtocol | None, service_raw)
            if not service:
                return None

            return await service.handle_npc_attack_on_player(
                npc_id=npc_id,
                target_id=target_id,
                room_id=room_id,
                attack_damage=attack_damage,
                npc_instance=npc_instance,
            )
        except (RuntimeError, AttributeError, ImportError, TypeError) as e:
            logger.debug(
                "Using direct NPC attack path (combat service unavailable)",
                npc_id=npc_id,
                target_id=target_id,
                error=str(e),
            )
            return None

    async def _is_target_in_login_grace_period(self, target_id: str) -> bool:
        """
        Return True if the target player is currently in login grace period.
        """
        try:
            config = get_config()
            app_raw = getattr(config, "_app_instance", None)
            if not app_raw:
                return False
            app = cast(object, app_raw)
            state_raw = getattr(app, "state", None)
            if not state_raw:
                return False
            state = cast(object, state_raw)
            connection_manager = getattr(state, "connection_manager", None)
            if not connection_manager:
                return False
            target_uuid = self._convert_target_id_to_uuid(target_id)
            return is_player_in_login_grace_period(target_uuid, connection_manager)
        except (AttributeError, ImportError, TypeError, ValueError) as e:
            # If we can't check grace period, proceed with attack (fail open)
            logger.debug("Could not check login grace period for NPC attack", target_id=target_id, error=str(e))
            return False

    async def _get_target_stats(self, target_id: str) -> dict[str, object]:
        """Get target stats from player or use defaults."""
        target_id_uuid = uuid.UUID(target_id)
        player = await self._persistence.get_player_by_id(target_id_uuid)
        if player:
            # player.stats is already a mapping of stat keys to primitive values
            stats = player.get_stats() if hasattr(player, "get_stats") else player.stats
            result: dict[str, object] = stats  # stats is already dict-like; normalize to dict[str, object]
            return result
        # For NPC vs NPC combat, we'd need the target NPC stats
        # This is a limitation of the current design
        return {"constitution": 50}  # Default stats

    def _get_npc_stats(self, npc_stats: dict[str, int] | None) -> dict[str, int]:
        """Get NPC stats or use defaults."""
        if not npc_stats:
            return {"strength": 50, "constitution": 50}  # Default stats
        return npc_stats

    def _get_npc_display_name(self, npc_id: str) -> str:
        """Resolve NPC instance display name from lifecycle manager, or derive from npc_id."""
        lifecycle_name = self._get_npc_name_from_lifecycle(npc_id)
        if lifecycle_name:
            return lifecycle_name
        return self._derive_npc_name_from_id(npc_id)

    def _get_npc_name_from_lifecycle(self, npc_id: str) -> str | None:
        """
        Best-effort lookup of NPC name from the lifecycle manager.
        """
        try:
            lifecycle_manager = self._get_npc_lifecycle_manager()
            if not lifecycle_manager:
                return None
            instance = lifecycle_manager.active_npcs.get(npc_id)
            if instance:
                name_obj = getattr(instance, "name", None)
                if isinstance(name_obj, str) and name_obj:
                    return name_obj
        except Exception:  # pylint: disable=broad-exception-caught  # Best-effort name resolution
            return None
        return None

    def _get_npc_lifecycle_manager(self) -> "NPCLifecycleManager | None":
        """
        Resolve the NPC lifecycle manager from the app state, if available.
        """
        config = get_config()
        app_raw = getattr(config, "_app_instance", None)
        if not app_raw:
            return None
        app = cast(object, app_raw)
        state_raw = getattr(app, "state", None)
        if not state_raw:
            return None
        state = cast(object, state_raw)
        manager = getattr(state, "npc_lifecycle_manager", None)
        return cast("NPCLifecycleManager | None", manager)

    def _derive_npc_name_from_id(self, npc_id: str) -> str:
        """
        Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... -> Nightgaunt).
        """
        parts = npc_id.split("_")
        return parts[0].title() if parts else npc_id

    async def _publish_player_dp_updated_after_npc_damage(self, target_id: str, damage: int, room_id: str) -> None:
        """Publish PlayerDPUpdated so the client's health/DP bar updates after NPC damage."""
        try:
            target_uuid, player = await self._get_player_for_dp_update(target_id)
            if not player or not self.event_bus:
                return

            old_dp, new_dp, max_dp = self._compute_dp_update_fields(player, damage)
            self._publish_player_dp_updated_event(
                target_uuid=target_uuid,
                old_dp=old_dp,
                new_dp=new_dp,
                max_dp=max_dp,
                damage=damage,
                room_id=room_id,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # Must not fail the attack
            logger.warning(
                "Failed to publish PlayerDPUpdated after NPC damage",
                target_id=target_id,
                error=str(e),
            )

    async def _get_player_for_dp_update(self, target_id: str) -> tuple[uuid.UUID, object | None]:
        """
        Resolve the player and UUID needed for DP update events.
        """
        target_uuid = self._convert_target_id_to_uuid(target_id)
        player = await self._persistence.get_player_by_id(target_uuid)
        return target_uuid, player

    def _compute_dp_update_fields(self, player: object, damage: int) -> tuple[int, int, int]:
        """
        Compute old_dp, new_dp, and max_dp values for PlayerDPUpdated.
        """
        get_stats_fn = getattr(player, "get_stats", None)
        raw_stats = get_stats_fn() if callable(get_stats_fn) else getattr(player, "stats", {})
        stats: dict[str, object]
        if isinstance(raw_stats, dict):
            # Normalize to dict[str, object] so downstream helpers see a fully-typed mapping
            normalized_stats: dict[object, object] = cast(dict[object, object], raw_stats)
            stats = {str(key): value for key, value in normalized_stats.items()}
        else:
            stats = {}

        new_dp = self._get_int_stat(stats, "current_dp")
        if new_dp is None:
            new_dp = self._get_int_stat(stats, "dp", 0) or 0

        old_dp = new_dp + damage
        max_dp = self._calculate_max_dp(stats)
        return old_dp, new_dp, max_dp

    def _publish_player_dp_updated_event(
        self,
        target_uuid: uuid.UUID,
        old_dp: int,
        new_dp: int,
        max_dp: int,
        damage: int,
        room_id: str,
    ) -> None:
        """
        Publish the PlayerDPUpdated event to the event bus.
        """
        if not self.event_bus:
            return
        self.event_bus.publish(
            PlayerDPUpdated(
                player_id=target_uuid,
                old_dp=old_dp,
                new_dp=new_dp,
                max_dp=max_dp,
                damage_taken=damage,
                source_id=None,
                combat_id=None,
                room_id=room_id,
            )
        )

    def _publish_attack_event(self, npc_id: str, target_id: str, room_id: str, damage: int, attack_type: str) -> None:  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event publishing requires many parameters for complete event context
        """Publish NPC attack event to event bus."""
        if self.event_bus:
            self.event_bus.publish(
                NPCAttacked(
                    npc_id=npc_id,
                    target_id=target_id,
                    room_id=room_id,
                    damage=damage,
                    attack_type=attack_type,
                )
            )

    async def _publish_npc_attack_to_nats(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        damage: int,
        attack_type: str,
    ) -> None:
        """
        Publish NPC-on-player attack as player_attacked to NATS so the client receives it.

        When an NPC attacks a player, damage is applied and NPCAttacked is published to the
        event bus, but nothing forwards that to NATS. The client only receives combat
        events via NATS (player_attacked). This method builds a PlayerAttackedEvent and
        publishes it via the combat event publisher so the victim sees "X attacks you".
        """
        try:
            publisher = self._get_combat_event_publisher()
            if not publisher:
                return

            target_uuid, player, stats = await self._get_player_and_stats_for_nats(target_id)
            if not player or not stats:
                return

            event = self._build_player_attacked_event(
                npc_id=npc_id,
                room_id=room_id,
                target_uuid=target_uuid,
                player=player,
                stats=stats,
                damage=damage,
                attack_type=attack_type,
            )
            _ = await publisher.publish_player_attacked(event)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: NATS publish must not fail the attack; log and continue
            logger.warning(
                "Failed to publish NPC attack to NATS (damage still applied)",
                npc_id=npc_id,
                target_id=target_id,
                room_id=room_id,
                error=str(e),
            )

    def _get_combat_event_publisher(self) -> _CombatEventPublisherProtocol | None:
        """
        Resolve the combat event publisher used to send PlayerAttacked events to NATS.
        """
        config = get_config()
        app_raw = getattr(config, "_app_instance", None)
        if not app_raw:
            return None
        app = cast(object, app_raw)
        state_raw = getattr(app, "state", None)
        if not state_raw:
            return None
        state = cast(object, state_raw)
        container_raw = getattr(state, "container", None)
        container = cast(object, container_raw) if container_raw is not None else None
        combat_service = getattr(container, "combat_service", None) if container is not None else None
        if not combat_service:
            return None
        service_obj = cast(object, combat_service)
        publisher = getattr(service_obj, "_combat_event_publisher", None)
        return cast(_CombatEventPublisherProtocol | None, publisher)

    async def _get_player_and_stats_for_nats(
        self,
        target_id: str,
    ) -> tuple[uuid.UUID, object | None, dict[str, object] | None]:
        """
        Resolve target UUID, player object, and stats needed for NATS attack event.
        """
        target_uuid = self._convert_target_id_to_uuid(target_id)
        player = await self._persistence.get_player_by_id(target_uuid)
        if not player:
            return target_uuid, None, None
        stats = player.get_stats() if hasattr(player, "get_stats") else getattr(player, "stats", {})
        return target_uuid, player, stats

    def _build_player_attacked_event(
        self,
        npc_id: str,
        room_id: str,
        target_uuid: uuid.UUID,
        player: object,
        stats: dict[str, object],
        damage: int,
        attack_type: str,
    ) -> PlayerAttackedEvent:
        """
        Construct the PlayerAttackedEvent payload for NATS publication.
        """
        target_name = getattr(player, "name", "Unknown")
        target_current_dp = self._get_int_stat(stats, "current_dp")
        if target_current_dp is None:
            target_current_dp = self._get_int_stat(stats, "dp", 0) or 0
        target_max_dp = self._calculate_max_dp(stats)

        # No combat instance for NPC-initiated attack; use nil UUID so clients still get the event.
        combat_id_nil = uuid.UUID(int=0)
        attacker_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, npc_id)
        attacker_name = self._get_npc_display_name(npc_id)

        return PlayerAttackedEvent(
            combat_id=combat_id_nil,
            room_id=room_id,
            attacker_id=attacker_uuid,
            attacker_name=attacker_name,
            target_id=target_uuid,
            target_name=target_name,
            damage=damage,
            action_type=attack_type,
            target_current_dp=target_current_dp,
            target_max_dp=target_max_dp,
        )

    async def handle_npc_death(
        self, npc_id: str, room_id: str, cause: str = "unknown", killer_id: str | None = None
    ) -> bool:
        """
        Handle NPC death and related effects.

        Args:
            npc_id: ID of the dead NPC
            room_id: ID of the room where death occurred
            cause: Cause of death
            killer_id: ID of the entity that killed the NPC

        Returns:
            bool: True if death was handled successfully
        """
        try:
            # Calculate XP reward for the killer
            xp_reward = 0

            if killer_id is not None:
                # Use default XP reward for NPC kills
                # Future enhancement: Calculate XP based on NPC definition data (level, type, etc.)
                # This would require access to NPC definition service or lifecycle manager
                xp_reward = 10  # Default XP reward for aggressive mobs

                # Apply effects to killer if it's a player
                killer_id_uuid = uuid.UUID(killer_id)
                player = await self._persistence.get_player_by_id(killer_id_uuid)
                if player:
                    # Gain occult knowledge for killing NPCs
                    occult_gain = 5  # Small amount of occult knowledge
                    _ = await self._game_mechanics.gain_occult_knowledge(killer_id, occult_gain, f"killed_{npc_id}")

                    # Apply lucidity loss for killing (even aggressive NPCs)
                    lucidity_loss = 2  # Small lucidity loss for taking a life
                    _ = await self._game_mechanics.apply_lucidity_loss(killer_id, lucidity_loss, f"killed_{npc_id}")

            # Note: NPCDied event is now published by CombatService via NATS
            # This prevents duplicate event publishing and ensures consistent event handling

            logger.info(
                "NPC death handled",
                npc_id=npc_id,
                room_id=room_id,
                cause=cause,
                killer_id=killer_id,
                xp_reward=xp_reward,
            )
            return True

        except (ValueError, TypeError, AttributeError, ValidationError) as e:
            logger.error("Error handling NPC death", npc_id=npc_id, error=str(e))
            return False

    def _get_int_stat(self, stats: dict[str, object], key: str, default: int | None = None) -> int | None:
        """Return an integer stat from stats[key], handling common primitive types."""
        value = stats.get(key)
        if isinstance(value, (int, float)):
            return int(value)
        if isinstance(value, str) and value.isdigit():
            return int(value)
        return default

    def _calculate_max_dp(self, stats: dict[str, object]) -> int:
        """Calculate max_dp from stats with fallbacks."""
        max_dp = self._get_int_stat(stats, "max_dp")
        if max_dp is not None:
            return max_dp

        max_health = self._get_int_stat(stats, "max_health")
        if max_health is not None:
            return max_health

        con = self._get_int_stat(stats, "constitution", 50) or 50
        siz = self._get_int_stat(stats, "size", 50) or 50
        return (con + siz) // 5 if con and siz else 100

    def _get_player_combat_stats(self, stats: dict[str, object]) -> dict[str, object]:
        """Get combat stats for a player."""
        raw_current_dp = stats.get("current_dp", 100)
        if isinstance(raw_current_dp, (int, float)):
            current_dp = int(raw_current_dp)
        elif isinstance(raw_current_dp, str) and raw_current_dp.isdigit():
            current_dp = int(raw_current_dp)
        else:
            current_dp = 100

        max_dp = self._calculate_max_dp(stats)

        return {
            "dp": current_dp,
            "max_dp": max_dp,
            "strength": stats.get("strength", 50),
            "constitution": stats.get("constitution", 50),
            "lucidity": stats.get("lucidity", 100),
            "fear": stats.get("fear", 0),
            "corruption": stats.get("corruption", 0),
        }

    def _normalize_npc_stats(self, npc_stats: dict[str, object]) -> dict[str, object]:
        """Normalize NPC stats to include 'hp' for backward compatibility."""
        normalized_stats = dict(npc_stats)
        if "hp" not in normalized_stats:
            hp_value = normalized_stats.get("determination_points")
            if hp_value is None:
                hp_value = normalized_stats.get("dp")
            if hp_value is not None:
                normalized_stats["hp"] = hp_value
        return normalized_stats

    async def get_combat_stats(self, entity_id: str, npc_stats: dict[str, object] | None = None) -> dict[str, object]:
        """
        Get combat-relevant stats for an entity.

        Args:
            entity_id: ID of the entity
            npc_stats: Optional NPC stats (for NPC entities)

        Returns:
            dict: Combat stats
        """
        try:
            entity_id_uuid = uuid.UUID(entity_id)
            player = await self._persistence.get_player_by_id(entity_id_uuid)
            if player:
                # player.stats is already a dict[str, Any], no need for model_dump()
                stats = player.get_stats() if hasattr(player, "get_stats") else player.stats
                return self._get_player_combat_stats(stats)  # stats is already dict[str, Any], no cast needed

            if npc_stats:
                return self._normalize_npc_stats(npc_stats)

            logger.warning("Entity not found for combat stats", entity_id=entity_id)
            return {}

        except (ValueError, TypeError, AttributeError, DatabaseError, ValidationError) as e:
            if npc_stats:
                logger.debug(
                    "Error getting combat stats, returning provided NPC stats", entity_id=entity_id, error=str(e)
                )
                return self._normalize_npc_stats(npc_stats)
            logger.error("Error getting combat stats", entity_id=entity_id, error=str(e))
            return {}
