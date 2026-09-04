"""
Base segment of NPC combat integration (damage, effects, attack orchestration).

Split from combat_integration to keep per-file line counts within tooling limits.
Public API remains ``NPCCombatIntegration`` in ``combat_integration``.
"""

from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from typing import cast

from structlog.stdlib import BoundLogger

from ..async_persistence import AsyncPersistenceLayer
from ..config import get_config
from ..events import EventBus
from ..exceptions import ValidationError
from ..game.mechanics import GameMechanicsService
from ..realtime.login_grace_period import is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger
from .combat_integration_protocols import NpcCombatServiceProtocol

logger: BoundLogger = get_logger(__name__)


def _resolve_npc_combat_service_raw(app: object) -> object | None:
    """
    Return the live NPC combat integration service for delegation.

    Prefer ``CombatService.get_npc_combat_integration_service`` when wired (same instance as
    ``CombatCommandHandler.npc_combat_service``). If still unwired, load ``combat_loader`` via
    ``importlib`` so basedpyright does not see a static import edge (loader imports handler,
    handler imports npc integration, which eventually imports this package).
    """
    service_raw: object | None = None
    state_raw = getattr(app, "state", None)
    if state_raw:
        state = cast(object, state_raw)
        container = getattr(state, "container", None)
        if container is not None:
            combat_service = getattr(container, "combat_service", None)
            if combat_service is not None:
                getter = getattr(combat_service, "get_npc_combat_integration_service", None)
                if callable(getter):
                    service_raw = getter()
    if service_raw is None:
        import importlib as importlib_stdlib

        combat_loader = importlib_stdlib.import_module("server.commands.combat_loader")
        get_handler = combat_loader.get_combat_command_handler
        handler = get_handler(app)
        service_raw = getattr(handler, "npc_combat_service", None)
    return service_raw


class NPCCombatIntegrationBase(ABC):
    """
    Base implementation: damage, combat effects, and NPC attack orchestration.

    Extended by ``NPCCombatIntegration`` with event publishing, NATS, death, and stat helpers.
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
            if isinstance(value, int | float):
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

            service_raw = _resolve_npc_combat_service_raw(app)
            service = cast(NpcCombatServiceProtocol | None, service_raw)
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

    @abstractmethod
    def _get_npc_stats(self, npc_stats: dict[str, int] | None) -> dict[str, int]:
        """Subclasses provide NPC stat defaults for damage resolution."""

    @abstractmethod
    async def _publish_player_dp_updated_after_npc_damage(self, target_id: str, damage: int, room_id: str) -> None:
        """Subclasses publish DP updates after direct NPC damage."""

    @abstractmethod
    def _publish_attack_event(self, npc_id: str, target_id: str, room_id: str, damage: int, attack_type: str) -> None:
        """Subclasses publish NPCAttacked to the event bus."""

    @abstractmethod
    async def _publish_npc_attack_to_nats(
        self,
        npc_id: str,
        target_id: str,
        room_id: str,
        damage: int,
        attack_type: str,
    ) -> None:
        """Subclasses forward NPC attacks to NATS for clients."""
