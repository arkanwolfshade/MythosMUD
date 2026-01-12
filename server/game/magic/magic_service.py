"""
Core magic service for spellcasting.

This module provides the main magic service that handles MP management,
spell validation, casting rolls, and cost application.
"""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Magic service methods require multiple return statements for early validation returns (spell validation, MP checks, error handling). Magic service requires extensive spellcasting logic and MP management.

import random
import uuid
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from server.app.game_tick_processing import get_current_tick
from server.game.magic.casting_state_manager import CastingStateManager
from server.game.magic.spell_costs import SpellCostsService
from server.game.magic.spell_effects import SpellEffects
from server.game.magic.spell_materials import SpellMaterialsService
from server.game.magic.spell_registry import SpellRegistry
from server.game.magic.spell_targeting import SpellTargetingService
from server.game.player_service import PlayerService
from server.models.spell import Spell
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.schemas.target_resolution import TargetMatch
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MagicService:  # pylint: disable=too-many-instance-attributes  # Reason: Magic service requires many configuration and state tracking attributes
    """
    Core magic service for spellcasting operations.

    Handles MP management, spell validation, casting mechanics,
    and coordinates with other services for spell effects.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Magic service initialization requires many service dependencies
        self,
        spell_registry: SpellRegistry,
        player_service: PlayerService,
        spell_targeting_service: SpellTargetingService,
        spell_effects: SpellEffects,
        player_spell_repository: PlayerSpellRepository | None = None,
        spell_learning_service=None,
        casting_state_manager: CastingStateManager | None = None,
        combat_service=None,
        spell_costs_service: SpellCostsService | None = None,
        spell_materials_service: SpellMaterialsService | None = None,
    ):
        """
        Initialize the magic service.

        Args:
            spell_registry: Registry for spell lookups
            player_service: Player service for stat modifications
            spell_targeting_service: Service for target resolution
            spell_effects: Engine for processing spell effects
            player_spell_repository: Optional repository for mastery tracking
            spell_learning_service: Optional spell learning service for mastery progression
            casting_state_manager: Optional casting state manager for tracking active castings
            combat_service: Optional combat service for combat integration
            spell_costs_service: Optional service for applying spell costs
            spell_materials_service: Optional service for handling spell materials
        """
        self.spell_registry = spell_registry
        self.player_service = player_service
        self.spell_targeting_service = spell_targeting_service
        self.spell_effects = spell_effects
        self.player_spell_repository = player_spell_repository or PlayerSpellRepository()
        self.spell_learning_service = spell_learning_service
        self.casting_state_manager = casting_state_manager or CastingStateManager()
        self.combat_service = combat_service
        self.spell_costs_service = spell_costs_service or SpellCostsService(player_service)
        self.spell_materials_service = spell_materials_service or SpellMaterialsService(player_service)
        logger.info("MagicService initialized")

    async def can_cast_spell(self, player_id: uuid.UUID, spell: Spell) -> tuple[bool, str]:
        """
        Check if a player can cast a spell.

        Args:
            player_id: Player ID
            spell: Spell to check

        Returns:
            tuple[bool, str]: (can_cast, error_message)
        """
        # Get player
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return False, "You are not recognized by the cosmic forces."

        stats = player.get_stats()

        # Apply same MP normalization as _convert_player_to_schema (UI uses this logic)
        # Initialize magic_points to max if it's 0 (full MP at character creation)
        import math

        pow_val = stats.get("power", 50)
        if "max_magic_points" not in stats:
            stats["max_magic_points"] = math.ceil(pow_val * 0.2)
        if not stats.get("magic_points", 0) and stats.get("max_magic_points", 0) > 0:
            stats["magic_points"] = stats["max_magic_points"]

        # Check MP cost
        current_mp = stats.get("magic_points", 0)
        if current_mp < spell.mp_cost:
            return False, f"Not enough magic points. You need {spell.mp_cost} MP, but only have {current_mp}."

        # Check lucidity cost for Mythos spells
        if spell.is_mythos() and spell.requires_lucidity():
            current_lucidity = stats.get("lucidity", 100)
            if current_lucidity < spell.lucidity_cost:
                return (
                    False,
                    f"Not enough lucidity. You need {spell.lucidity_cost} lucidity, but only have {current_lucidity}.",
                )

        # Check if player knows the spell
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        if not player_spell:
            return False, f"You have not learned {spell.name}."

        # Check materials
        if spell.materials:
            missing_materials = await self.spell_materials_service.check_materials(player_id, spell)
            if missing_materials:
                material_list = ", ".join(missing_materials)
                return False, f"You are missing required materials: {material_list}."

        return True, ""

    def _check_already_casting(self, player_id: uuid.UUID) -> dict[str, Any] | None:
        """Check if player is already casting a spell."""
        if not self.casting_state_manager.is_casting(player_id):
            return None

        casting_state = self.casting_state_manager.get_casting_state(player_id)
        if casting_state is None:
            return {
                "success": False,
                "message": "You are already casting a spell. Use 'stop' to interrupt.",
            }
        return {
            "success": False,
            "message": f"You are already casting {casting_state.spell_name}. Use 'stop' to interrupt.",
        }

    def _get_spell_from_registry(self, spell_id: str) -> Any | None:
        """Get spell from registry by ID or name."""
        spell = self.spell_registry.get_spell(spell_id)
        if not spell:
            spell = self.spell_registry.get_spell_by_name(spell_id)
        return spell

    async def _validate_spell_casting(
        self, player_id: uuid.UUID, spell: Any, target_name: str | None
    ) -> tuple[Any | None, str | None]:
        """Validate spell can be cast and resolve target."""
        can_cast, error_msg = await self.can_cast_spell(player_id, spell)
        if not can_cast:
            return None, error_msg

        target, target_error = await self.spell_targeting_service.resolve_spell_target(player_id, spell, target_name)
        if not target:
            return None, target_error

        return target, None

    async def _handle_instant_cast(self, player_id: uuid.UUID, spell: Any, target: Any, mastery: int) -> dict[str, Any]:
        """Handle instant cast (casting_time == 0)."""
        await self.spell_costs_service.apply_costs(player_id, spell)
        effect_result = await self.spell_effects.process_effect(spell, target, player_id, mastery)
        await self.player_spell_repository.record_spell_cast(player_id, spell.spell_id)

        if self.spell_learning_service:
            await self.spell_learning_service.increase_mastery_on_cast(player_id, spell.spell_id, True)

        return {
            "success": True,
            "message": effect_result.get("message", f"{spell.name} cast successfully."),
            "spell_name": spell.name,
            "target": target.target_name,
            "effect_result": effect_result,
            "mastery": mastery,
        }

    def _calculate_initiative_tick(self, combat: Any, current_tick: int, player_id: uuid.UUID) -> int | None:
        """Calculate next initiative tick for combat casting."""
        current_participant = combat.get_current_turn_participant()
        if current_participant and current_participant.participant_id == player_id:
            return None  # It's their turn, start casting immediately

        next_initiative_tick = combat.next_turn_tick
        if next_initiative_tick is None or next_initiative_tick <= current_tick:
            next_initiative_tick = current_tick + combat.turn_interval_ticks
        return next_initiative_tick

    async def _start_delayed_cast(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Delayed cast requires many parameters for spell context and timing
        self, player_id: uuid.UUID, spell: Any, target: Any, mastery: int, current_tick: int
    ) -> dict[str, Any]:
        """Start delayed cast (casting_time > 0)."""
        combat_id = None
        next_initiative_tick = None

        if self.combat_service:
            combat = await self.combat_service.get_combat_by_participant(player_id)
            if combat:
                combat_id = combat.combat_id
                next_initiative_tick = self._calculate_initiative_tick(combat, current_tick, player_id)

        target_type_str = target.target_type.value if hasattr(target.target_type, "value") else str(target.target_type)

        try:
            self.casting_state_manager.start_casting(
                player_id=player_id,
                spell=spell,
                start_tick=current_tick,
                combat_id=combat_id,
                next_initiative_tick=next_initiative_tick,
                target_name=target.target_name,
                target_id=target.target_id,
                target_type=target_type_str,
                mastery=mastery,
            )
        except ValueError as e:
            return {"success": False, "message": str(e)}

        message = f"You begin casting {spell.name}..."
        if next_initiative_tick is not None:
            message += " (waiting for your turn in combat)"
        elif spell.casting_time_seconds > 0:
            message += f" ({spell.casting_time_seconds} seconds)"

        return {
            "success": True,
            "message": message,
            "spell_name": spell.name,
            "casting_time": spell.casting_time_seconds,
            "is_casting": True,
        }

    async def cast_spell(self, player_id: uuid.UUID, spell_id: str, target_name: str | None = None) -> dict[str, Any]:
        """
        Cast a spell.

        Args:
            player_id: Player ID
            spell_id: Spell ID to cast
            target_name: Optional target name

        Returns:
            dict: Result with success, messages, and effect details
        """
        logger.info("Casting spell", player_id=player_id, spell_id=spell_id, target_name=target_name)

        # Check if already casting
        already_casting = self._check_already_casting(player_id)
        if already_casting:
            return already_casting

        # Get spell from registry
        spell = self._get_spell_from_registry(spell_id)
        if not spell:
            return {"success": False, "message": f"Spell '{spell_id}' not found."}

        # Validate spell casting and resolve target
        target, validation_error = await self._validate_spell_casting(player_id, spell, target_name)
        if validation_error:
            return {"success": False, "message": validation_error}

        # Get player spell for mastery
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        mastery = int(player_spell.mastery) if player_spell else 0

        # Consume materials (before casting roll, so materials are consumed even on failure)
        if spell.materials:
            material_result = await self.spell_materials_service.consume_materials(player_id, spell)
            if not material_result.get("success"):
                return {"success": False, "message": material_result.get("message", "Failed to consume materials.")}

        # Perform casting roll
        casting_success = await self._casting_roll(player_id, spell, mastery)
        if not casting_success:
            await self.spell_costs_service.apply_costs(player_id, spell)
            return {
                "success": False,
                "message": f"{spell.name} failed! The cosmic forces resist your incantation.",
                "costs_paid": True,
            }

        # Handle instant cast or delayed cast
        if not spell.casting_time_seconds:
            return await self._handle_instant_cast(player_id, spell, target, mastery)

        current_tick = get_current_tick()
        return await self._start_delayed_cast(player_id, spell, target, mastery, current_tick)

    async def _casting_roll(self, player_id: uuid.UUID, spell: Spell, mastery: int) -> bool:
        """
        Perform a casting roll (simplified CoC mechanics).

        Args:
            player_id: Player ID
            spell: Spell being cast
            mastery: Mastery level (0-100)

        Returns:
            bool: True if casting succeeds
        """
        # Get player stats
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return False

        stats = player.get_stats()
        intelligence = stats.get("intelligence", 50)

        # Base success chance: Intelligence + mastery
        # Simplified: roll d100, succeed if roll <= (intelligence + mastery)
        base_chance = intelligence + mastery
        roll = random.randint(1, 100)  # nosec B311: Game mechanics dice roll, not cryptographic

        success = roll <= base_chance
        logger.debug(
            "Casting roll",
            player_id=player_id,
            spell_id=spell.spell_id,
            intelligence=intelligence,
            mastery=mastery,
            base_chance=base_chance,
            roll=roll,
            success=success,
        )

        return success

    async def restore_mp(self, player_id: uuid.UUID, amount: int) -> dict[str, Any]:
        """
        Restore magic points to a player.

        Args:
            player_id: Player ID
            amount: Amount of MP to restore

        Returns:
            dict: Result message
        """
        return await self.spell_costs_service.restore_mp(player_id, amount)

    async def check_casting_progress(self, current_tick: int) -> None:
        """
        Check and process casting progress for all active castings.

        Called by game tick processing to advance casting timers.

        Args:
            current_tick: Current game tick
        """
        casting_players = self.casting_state_manager.get_all_casting_players()
        for player_id in casting_players:
            casting_state = self.casting_state_manager.get_casting_state(player_id)
            if not casting_state:
                continue

            # Update progress
            is_complete = self.casting_state_manager.update_casting_progress(player_id, current_tick)
            if is_complete:
                # Casting is complete, process it
                await self._complete_casting(player_id, casting_state)

    async def _get_player_and_room(self, player_id: uuid.UUID) -> tuple[Any, str] | None:
        """
        Get player and room_id for casting completion.

        Returns:
            Tuple of (player, room_id) if successful, None otherwise
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            logger.error("Player not found when completing casting", player_id=player_id)
            self.casting_state_manager.complete_casting(player_id)
            return None

        room_id = player.current_room_id or ""
        return player, room_id

    def _recreate_target_from_state(self, casting_state: Any, player_id: uuid.UUID, player: Any, room_id: str) -> Any:
        """
        Recreate target from stored casting state.

        Args:
            casting_state: The casting state
            player_id: Player ID
            player: Player object
            room_id: Room ID

        Returns:
            TargetMatch object
        """
        from server.schemas.target_resolution import TargetType

        target_type_str = casting_state.target_type or "player"
        try:
            target_type = TargetType(target_type_str)
        except ValueError:
            target_type = TargetType.PLAYER

        return TargetMatch(
            target_id=casting_state.target_id or str(player_id),
            target_name=casting_state.target_name or player.name,
            target_type=target_type,
            room_id=room_id,
        )

    async def _apply_spell_costs_and_effects(
        self, player_id: uuid.UUID, spell: Any, target: Any, casting_state: Any
    ) -> dict[str, Any]:
        """
        Apply spell costs and process effects.

        Args:
            player_id: Player ID
            spell: Spell object
            target: TargetMatch object
            casting_state: Casting state

        Returns:
            Effect result dictionary
        """
        await self.spell_costs_service.apply_costs(player_id, spell)
        effect_result = await self.spell_effects.process_effect(spell, target, player_id, casting_state.mastery)
        await self.player_spell_repository.record_spell_cast(player_id, spell.spell_id)

        if self.spell_learning_service:
            await self.spell_learning_service.increase_mastery_on_cast(player_id, spell.spell_id, True)

        return effect_result

    async def _send_spell_completion_message(
        self, player_id: uuid.UUID, spell_id: str, effect_result: dict[str, Any]
    ) -> None:
        """Send spell completion message to player."""
        try:
            from server.realtime.connection_manager_api import send_game_event

            if effect_result.get("success") and effect_result.get("message"):
                await send_game_event(
                    player_id,
                    "command_response",
                    {
                        "result": effect_result.get("message", ""),
                        "game_log_message": effect_result.get("message", ""),
                        "game_log_channel": "game-log",
                    },
                )
            elif not effect_result.get("success"):
                failure_message = effect_result.get("message", "The spell failed.")
                await send_game_event(
                    player_id,
                    "command_response",
                    {
                        "result": failure_message,
                        "game_log_message": failure_message,
                        "game_log_channel": "game-log",
                    },
                )
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as msg_error:
            logger.warning(
                "Failed to send spell completion message",
                player_id=player_id,
                spell_id=spell_id,
                error=str(msg_error),
            )

    async def _send_healing_update_event(  # pylint: disable=too-many-locals  # Reason: Healing event requires many intermediate variables for complex event processing
        self, player_id: uuid.UUID, effect_result: dict[str, Any], spell_id: str, room_id: str
    ) -> None:
        """Send player_dp_updated event if healing occurred."""
        if not (
            effect_result.get("success") and effect_result.get("effect_applied") and effect_result.get("heal_amount")
        ):
            return

        try:
            from server.container import ApplicationContainer
            from server.events.event_types import PlayerDPUpdated

            updated_player = await self.player_service.persistence.get_player_by_id(player_id)
            if not updated_player:
                return

            stats = updated_player.get_stats()
            current_dp = stats.get("current_dp", 0)
            max_dp = stats.get("max_dp", 0)
            heal_amount = effect_result.get("heal_amount", 0)
            old_dp = max(0, current_dp - heal_amount)

            container = ApplicationContainer.get_instance()
            if container and container.event_bus:
                dp_event = PlayerDPUpdated(
                    player_id=player_id,
                    old_dp=old_dp,
                    new_dp=current_dp,
                    max_dp=max_dp,
                    damage_taken=-heal_amount,
                    source_id=spell_id,
                    room_id=room_id,
                )
                container.event_bus.publish(dp_event)
            else:
                from server.realtime.connection_manager_api import send_game_event

                await send_game_event(
                    player_id,
                    "player_dp_updated",
                    {
                        "old_dp": old_dp,
                        "new_dp": current_dp,
                        "max_dp": max_dp,
                        "damage_taken": -heal_amount,
                        "player": {
                            "stats": {
                                "current_dp": current_dp,
                                "max_dp": max_dp,
                            },
                        },
                    },
                )
                logger.warning(
                    "Event bus not available for DP update after spell",
                    player_id=player_id,
                    spell_id=spell_id,
                )
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as dp_error:
            logger.warning(
                "Failed to publish PlayerDPUpdated event after spell",
                player_id=player_id,
                spell_id=spell_id,
                error=str(dp_error),
            )

    async def _complete_casting(self, player_id: uuid.UUID, casting_state: Any) -> None:
        """
        Complete a casting and apply spell effects.

        Args:
            player_id: Player ID
            casting_state: The casting state to complete
        """
        spell = casting_state.spell

        try:
            player_result = await self._get_player_and_room(player_id)
            if player_result is None:
                return

            player, room_id = player_result

            target = self._recreate_target_from_state(casting_state, player_id, player, room_id)
            self.casting_state_manager.complete_casting(player_id)

            effect_result = await self._apply_spell_costs_and_effects(player_id, spell, target, casting_state)

            logger.info(
                "Completed casting",
                player_id=player_id,
                spell_id=spell.spell_id,
                effect_success=effect_result.get("success", False),
            )

            await self._send_spell_completion_message(player_id, spell.spell_id, effect_result)
            await self._send_healing_update_event(player_id, effect_result, spell.spell_id, room_id)

        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError) as e:
            logger.error(
                "Error completing casting - clearing stuck state",
                player_id=player_id,
                spell_id=spell.spell_id if spell else None,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
        finally:
            if self.casting_state_manager.is_casting(player_id):
                self.casting_state_manager.complete_casting(player_id)

    async def interrupt_casting(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Interrupt a casting with LUCK check.

        Args:
            player_id: Player ID

        Returns:
            dict: Result with success, message, and MP loss status
        """
        casting_state = self.casting_state_manager.get_casting_state(player_id)
        if not casting_state:
            return {"success": False, "message": "You are not casting a spell."}

        # Perform LUCK check
        luck_check_passed = await self._perform_luck_check(player_id)

        # Remove casting state
        self.casting_state_manager.interrupt_casting(player_id)

        if luck_check_passed:
            # Passed LUCK check: don't lose MP
            return {
                "success": True,
                "message": f"You interrupt your casting of {casting_state.spell_name}. Your luck preserves your magic points.",
                "mp_lost": False,
            }

        # Failed LUCK check: lose MP
        await self.spell_costs_service.apply_costs(player_id, casting_state.spell)
        return {
            "success": True,
            "message": f"You interrupt your casting of {casting_state.spell_name}. The disruption costs you {casting_state.mp_cost} MP.",
            "mp_lost": True,
            "mp_cost": casting_state.mp_cost,
        }

    async def _perform_luck_check(self, player_id: uuid.UUID) -> bool:
        """
        Perform a LUCK check for the player.

        Args:
            player_id: Player ID

        Returns:
            bool: True if LUCK check passes (roll <= LUCK stat), False otherwise
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return False

        stats = player.get_stats()
        luck = stats.get("luck", 50)
        roll = random.randint(1, 100)  # nosec B311: Game mechanics dice roll, not cryptographic

        success = roll <= luck
        logger.debug(
            "LUCK check",
            player_id=player_id,
            luck=luck,
            roll=roll,
            success=success,
        )

        return success
