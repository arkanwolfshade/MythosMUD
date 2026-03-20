"""
Aggressive mob NPC type for MythosMUD.

This module provides the AggressiveMobNPC class with hunting and territorial behaviors.
"""

from typing import TYPE_CHECKING, Protocol, cast, override

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_base import NPCBase

if TYPE_CHECKING:
    from ..events import EventBus
    from ..models.npc import NPCDefinition
    from .combat_integration import NPCCombatIntegration
    from .event_reaction_system import NPCEventReactionSystem

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


class _RoomPersistence(Protocol):
    """Protocol for persistence with get_room_by_id."""

    def get_room_by_id(self, room_id: str) -> object | None:
        """Return the room object for the given room_id, or None if not found."""


class AggressiveMobNPC(NPCBase):
    """Aggressive mob NPC type with hunting and territorial behaviors."""

    def __init__(
        self,
        definition: "NPCDefinition",
        npc_id: str,
        event_bus: "EventBus | None" = None,
        event_reaction_system: "NPCEventReactionSystem | None" = None,
    ) -> None:
        """Initialize aggressive mob NPC."""
        super().__init__(definition, npc_id, event_bus, event_reaction_system)
        self._targets: list[str] = []
        # Avoid direct access to prevent potential lazy loading issues
        self._territory_center: str | None = getattr(definition, "room_id", None)
        self._setup_aggressive_mob_behavior_rules()

    def _setup_aggressive_mob_behavior_rules(self) -> None:
        """Setup aggressive mob-specific behavior rules."""
        aggressive_mob_rules = [
            {
                "name": "hunt_players",
                "condition": "player_in_range == true",
                "action": "hunt_target",
                "priority": 7,
            },
            {
                "name": "attack_on_sight",
                "condition": "enemy_nearby == true",
                "action": "attack_target",
                "priority": 8,
            },
            {
                "name": "flee_when_low_dp",
                "condition": "dp < flee_threshold",
                "action": "flee",
                "priority": 9,
            },
            {
                "name": "patrol_territory",
                "condition": "time_since_last_action > 120",
                "action": "patrol_territory",
                "priority": 3,
            },
        ]

        for rule in aggressive_mob_rules:
            _ = self._behavior_engine.add_rule(rule)

        # Register aggressive mob action handlers
        _ = self._behavior_engine.register_action_handler("hunt_target", self._handle_hunt_target)
        _ = self._behavior_engine.register_action_handler("attack_target", self._handle_attack_target)
        _ = self._behavior_engine.register_action_handler("flee", self._handle_flee)
        _ = self._behavior_engine.register_action_handler("patrol_territory", self._handle_patrol_territory)

    @override
    def get_behavior_rules(self) -> list[dict[str, object]]:
        """Get aggressive mob-specific behavior rules."""
        return self._behavior_engine.get_rules()

    def _compute_player_context(self, room_id: str) -> tuple[bool, bool, str | None]:
        """
        Get player_in_range, enemy_nearby, and target_id from persistence.
        Returns (player_in_range, enemy_nearby, target_id or None).
        """
        from ..services.npc_instance_service import get_npc_instance_service

        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
            return (False, False, None)

        lifecycle_manager = npc_instance_service.lifecycle_manager
        persistence_raw = getattr(lifecycle_manager, "persistence", None)
        if not persistence_raw:
            return (False, False, None)

        from collections.abc import Sequence

        persistence = cast(_RoomPersistence, persistence_raw)
        room: object | None = persistence.get_room_by_id(room_id)
        players: Sequence[str] = []
        if room is not None:
            get_players = getattr(room, "get_players", None)
            if callable(get_players):
                players = cast(Sequence[str], get_players())
        if players:
            return (True, True, players[0])
        return (False, False, None)

    def _log_context_enriched(self, context: dict[str, object], room_id: str, players_count: int) -> None:
        """Debug log for context enrichment (best-effort, must not fail)."""
        logger.debug(
            "Aggressive mob context enriched",
            npc_id=self.npc_id,
            room_id=room_id,
            players_count=players_count,
            player_in_range=context.get("player_in_range"),
            enemy_nearby=context.get("enemy_nearby"),
            target_id=context.get("target_id"),
        )

    @override
    def _enrich_behavior_context(self, context: dict[str, object]) -> None:
        """
        Populate player_in_range, enemy_nearby, and target_id for attack rules.
        Uses persistence from lifecycle manager to get players in current room.
        """
        room_id = self.current_room
        if not room_id:
            context["player_in_range"] = False
            context["enemy_nearby"] = False
            return

        try:
            player_in_range, enemy_nearby, target_id = self._compute_player_context(room_id)
            context["player_in_range"] = player_in_range
            context["enemy_nearby"] = enemy_nearby
            if target_id is not None:
                context["target_id"] = target_id
            players_count = 1 if target_id is not None else 0
            self._log_context_enriched(context, room_id, players_count)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904
            logger.warning(
                "Failed to enrich aggressive mob context",
                npc_id=self.npc_id,
                room_id=room_id,
                error_message=str(e),
            )
            context["player_in_range"] = False
            context["enemy_nearby"] = False

    def hunt_target(self, target_id: str) -> bool:
        """Hunt a specific target."""
        try:
            if target_id not in self._targets:
                self._targets.append(target_id)

            logger.debug("NPC is hunting target", npc_id=self.npc_id, target_id=target_id)
            return True
        except (TypeError, AttributeError) as e:
            logger.error(
                "Error hunting target",
                npc_id=self.npc_id,
                error_message=str(e),
                error_type=type(e).__name__,
            )
            return False

    def _get_attack_damage(self) -> int:
        """Resolve attack_damage from behavior config with robust typing."""
        raw_attack_damage = self._behavior_config.get("attack_damage", 1)
        if isinstance(raw_attack_damage, bool):
            return 1 if raw_attack_damage else 0
        if isinstance(raw_attack_damage, (int, float)):
            return int(raw_attack_damage)
        if isinstance(raw_attack_damage, str):
            return int(raw_attack_damage) if raw_attack_damage.isdigit() else 1
        return 1

    def _attack_via_combat_integration(self, target_id: str, attack_damage: int) -> bool | None:
        """
        Try to handle the attack via combat integration.

        Returns:
            True/False if handled, or None if combat integration is unavailable.
        """
        if not hasattr(self, "combat_integration") or not self.combat_integration:
            return None

        import asyncio
        from collections.abc import Coroutine

        try:
            _ = asyncio.get_running_loop()
        except RuntimeError:
            # No running loop - delegate via event bus if available, otherwise drop
            if self.event_bus:
                from ..events.event_types import NPCAttacked

                self.event_bus.publish(
                    NPCAttacked(
                        npc_id=self.npc_id,
                        target_id=target_id,
                        room_id=self.current_room or "unknown",
                        damage=attack_damage,
                        attack_type="physical",
                    )
                )
                return True
            logger.warning(
                "NPC attack called without event loop and no event_bus; attack dropped",
                npc_id=self.npc_id,
                target_id=target_id,
            )
            return False

        # Fire-and-forget: create task for async call
        combat_integration = cast("NPCCombatIntegration", self.combat_integration)
        coro = cast(
            Coroutine[object, object, bool],
            combat_integration.handle_npc_attack(
                self.npc_id,
                target_id,
                self.current_room or "unknown",
                attack_damage,
                "physical",
                self.get_combat_stats(),
            ),
        )
        _ = asyncio.create_task(coro)
        return True

    def _attack_target_impl(self, target_id: str) -> bool:
        """Internal implementation for attacking a target."""
        attack_damage = self._get_attack_damage()
        logger.info("NPC attacked target", npc_id=self.npc_id, target_id=target_id, damage=attack_damage)

        handled = self._attack_via_combat_integration(target_id, attack_damage)
        if handled is not None:
            return handled

        # Fallback to direct event publishing
        if self.event_bus:
            from ..events.event_types import NPCAttacked

            self.event_bus.publish(
                NPCAttacked(
                    npc_id=self.npc_id,
                    target_id=target_id,
                    room_id=self.current_room or "unknown",
                    damage=attack_damage,
                    attack_type="physical",
                )
            )
        return True

    def attack_target(self, target_id: str) -> bool:
        """Attack a specific target."""
        try:
            return self._attack_target_impl(target_id)
        except (TypeError, KeyError, AttributeError, RuntimeError) as e:
            logger.error(
                "Error attacking target",
                npc_id=self.npc_id,
                error_message=str(e),
                error_type=type(e).__name__,
            )
            return False

    def flee(self) -> bool:
        """Flee from current situation."""
        try:
            _ = self.speak("I must retreat!")
            logger.debug("NPC is fleeing", npc_id=self.npc_id)
            return True
        except (AttributeError, TypeError, RuntimeError) as e:
            logger.error(
                "Error fleeing",
                npc_id=self.npc_id,
                error_message=str(e),
                error_type=type(e).__name__,
            )
            return False

    def patrol_territory(self) -> bool:
        """Patrol the NPC's territory."""
        try:
            logger.debug("NPC is patrolling territory", npc_id=self.npc_id)
            return True
        except (TypeError, AttributeError) as e:
            logger.error(
                "Error patrolling territory",
                npc_id=self.npc_id,
                error_message=str(e),
                error_type=type(e).__name__,
            )
            return False

    def _handle_hunt_target(self, context: dict[str, object]) -> bool:
        """Handle hunting target action."""
        target_id = str(context.get("target_id", "unknown"))
        return self.hunt_target(target_id)

    def _handle_attack_target(self, context: dict[str, object]) -> bool:
        """Handle attacking target action."""
        target_id = str(context.get("target_id", "unknown"))
        return self.attack_target(target_id)

    def _handle_flee(self, _context: dict[str, object]) -> bool:
        """Handle fleeing action."""
        return self.flee()

    def _handle_patrol_territory(self, _context: dict[str, object]) -> bool:
        """Handle patrolling territory action."""
        return self.patrol_territory()
