"""
Core magic service for spellcasting.

This module provides the main magic service that handles MP management,
spell validation, casting rolls, and cost application.
"""

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
from server.structured_logging.enhanced_logging_config import get_logger
from server.models.spell import Spell
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.schemas.target_resolution import TargetMatch

logger = get_logger(__name__)


class MagicService:
    """
    Core magic service for spellcasting operations.

    Handles MP management, spell validation, casting mechanics,
    and coordinates with other services for spell effects.
    """

    def __init__(
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
        if stats.get("magic_points", 0) == 0 and stats.get("max_magic_points", 0) > 0:
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

        # Check if player is already casting
        if self.casting_state_manager.is_casting(player_id):
            casting_state = self.casting_state_manager.get_casting_state(player_id)
            if casting_state is None:
                # This should not happen if is_casting returns True, but handle defensively
                return {
                    "success": False,
                    "message": "You are already casting a spell. Use 'stop' to interrupt.",
                }
            return {
                "success": False,
                "message": f"You are already casting {casting_state.spell_name}. Use 'stop' to interrupt.",
            }

        # Get spell from registry
        spell = self.spell_registry.get_spell(spell_id)
        if not spell:
            # Try by name
            spell = self.spell_registry.get_spell_by_name(spell_id)
            if not spell:
                return {"success": False, "message": f"Spell '{spell_id}' not found."}

        # Check if can cast
        can_cast, error_msg = await self.can_cast_spell(player_id, spell)
        if not can_cast:
            return {"success": False, "message": error_msg}

        # Resolve target
        target, target_error = await self.spell_targeting_service.resolve_spell_target(player_id, spell, target_name)
        if not target:
            return {"success": False, "message": target_error}

        # Get player spell for mastery
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        mastery = int(player_spell.mastery) if player_spell else 0

        # Consume materials (before casting roll, so materials are consumed even on failure)
        if spell.materials:
            material_result = await self.spell_materials_service.consume_materials(player_id, spell)
            if not material_result.get("success"):
                return {"success": False, "message": material_result.get("message", "Failed to consume materials.")}

        # Perform casting roll (simplified CoC mechanics)
        casting_success = await self._casting_roll(player_id, spell, mastery)
        if not casting_success:
            # Still pay costs on failure
            await self.spell_costs_service.apply_costs(player_id, spell)
            return {
                "success": False,
                "message": f"{spell.name} failed! The cosmic forces resist your incantation.",
                "costs_paid": True,
            }

        # If casting time is 0, execute immediately (instant cast)
        if spell.casting_time_seconds == 0:
            # Apply costs
            await self.spell_costs_service.apply_costs(player_id, spell)

            # Process effect
            effect_result = await self.spell_effects.process_effect(spell, target, player_id, mastery)

            # Record spell cast
            await self.player_spell_repository.record_spell_cast(player_id, spell.spell_id)

            # Increase mastery on successful cast
            if self.spell_learning_service:
                await self.spell_learning_service.increase_mastery_on_cast(player_id, spell.spell_id, casting_success)

            # Combine results
            return {
                "success": True,
                "message": effect_result.get("message", f"{spell.name} cast successfully."),
                "spell_name": spell.name,
                "target": target.target_name,
                "effect_result": effect_result,
                "mastery": mastery,
            }

        # Casting time > 0: Start casting process
        current_tick = get_current_tick()
        combat_id = None
        next_initiative_tick = None

        # Check if in combat and handle initiative
        if self.combat_service:
            combat = await self.combat_service.get_combat_by_participant(player_id)
            if combat:
                combat_id = combat.combat_id
                current_participant = combat.get_current_turn_participant()
                # Check if it's player's turn
                if current_participant and current_participant.participant_id == player_id:
                    # It's their turn, start casting immediately
                    next_initiative_tick = None
                else:
                    # Not their turn, wait for next initiative
                    # Calculate next turn tick (6 ticks per turn)
                    next_initiative_tick = combat.next_turn_tick
                    # If next_turn_tick is 0 or in the past, calculate from current
                    if next_initiative_tick is None or next_initiative_tick <= current_tick:
                        next_initiative_tick = current_tick + combat.turn_interval_ticks

        # Start casting state
        try:
            # Store target_type as string value for later reconstruction
            target_type_str = (
                target.target_type.value if hasattr(target.target_type, "value") else str(target.target_type)
            )
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

        # Store target info for later use (we'll need it when casting completes)
        # The target is stored in casting_state, so we can retrieve it later

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
        roll = random.randint(1, 100)

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

    async def _complete_casting(self, player_id: uuid.UUID, casting_state: Any) -> None:
        """
        Complete a casting and apply spell effects.

        Args:
            player_id: Player ID
            casting_state: The casting state to complete
        """
        from server.schemas.target_resolution import TargetType

        spell = casting_state.spell

        # CRITICAL: Clear casting state IMMEDIATELY to prevent race conditions
        # If we clear it at the end, a second cast attempt might see the state and think it's still casting
        # But we need the state data, so we'll clear it in the finally block instead
        # Actually, we should clear it early but keep a local reference
        try:
            # Get player to get room_id
            player = await self.player_service.persistence.get_player_by_id(player_id)
            if not player:
                logger.error("Player not found when completing casting", player_id=player_id)
                self.casting_state_manager.complete_casting(player_id)
                return

            room_id = player.current_room_id or ""

            # Recreate target from stored state
            # Convert target_type string back to enum
            target_type_str = casting_state.target_type or "player"
            try:
                target_type = TargetType(target_type_str)
            except ValueError:
                # Fallback to player if invalid
                target_type = TargetType.PLAYER

            target = TargetMatch(
                target_id=casting_state.target_id or str(player_id),
                target_name=casting_state.target_name or player.name,
                target_type=target_type,
                room_id=room_id,
            )

            # CRITICAL: Clear casting state BEFORE processing effect to prevent race conditions
            # If we clear it after, a rapid second cast might see the state and think it's still casting
            # We've already extracted all needed data from casting_state, so it's safe to clear now
            self.casting_state_manager.complete_casting(player_id)

            # Apply costs (MP was not consumed at start, do it now)
            await self.spell_costs_service.apply_costs(player_id, spell)

            # Process effect
            effect_result = await self.spell_effects.process_effect(spell, target, player_id, casting_state.mastery)

            # Record spell cast
            await self.player_spell_repository.record_spell_cast(player_id, spell.spell_id)

            # Increase mastery on successful cast
            if self.spell_learning_service:
                await self.spell_learning_service.increase_mastery_on_cast(player_id, spell.spell_id, True)

            logger.info(
                "Completed casting",
                player_id=player_id,
                spell_id=spell.spell_id,
                effect_success=effect_result.get("success", False),
            )

            # Send spell completion message to player
            try:
                from server.realtime.connection_manager_api import send_game_event

                # Send completion message using command_response event type (client handles this)
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
                    # Send failure message
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
                # RuntimeError can occur when connection manager is not available (e.g., in tests)
                logger.warning(
                    "Failed to send spell completion message",
                    player_id=player_id,
                    spell_id=spell.spell_id,
                    error=str(msg_error),
                )

            # Send player_dp_updated event to refresh health display if healing occurred
            if (
                effect_result.get("success")
                and effect_result.get("effect_applied")
                and effect_result.get("heal_amount")
            ):
                try:
                    from server.container import ApplicationContainer
                    from server.events.event_types import PlayerDPUpdated

                    # Get updated player to calculate DP values
                    updated_player = await self.player_service.persistence.get_player_by_id(player_id)
                    if updated_player:
                        stats = updated_player.get_stats()
                        current_dp = stats.get("current_dp", 0)
                        max_dp = stats.get("max_dp", 0)
                        heal_amount = effect_result.get("heal_amount", 0)
                        old_dp = max(0, current_dp - heal_amount)  # Calculate old DP before healing

                        # Publish PlayerDPUpdated event for health UI update
                        container = ApplicationContainer.get_instance()
                        if container and container.event_bus:
                            dp_event = PlayerDPUpdated(
                                player_id=player_id,
                                old_dp=old_dp,
                                new_dp=current_dp,
                                max_dp=max_dp,
                                damage_taken=-heal_amount,  # Negative for healing
                                source_id=spell.spell_id,
                                room_id=room_id,
                            )
                            container.event_bus.publish(dp_event)
                        else:
                            # Fallback: send player_dp_updated event directly if event bus unavailable
                            from server.realtime.connection_manager_api import send_game_event

                            await send_game_event(
                                player_id,
                                "player_dp_updated",
                                {
                                    "old_dp": old_dp,
                                    "new_dp": current_dp,
                                    "max_dp": max_dp,
                                    "damage_taken": -heal_amount,  # Negative for healing
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
                                spell_id=spell.spell_id,
                            )
                except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as dp_error:
                    # RuntimeError can occur when connection manager is not available (e.g., in tests)
                    logger.warning(
                        "Failed to publish PlayerDPUpdated event after spell",
                        player_id=player_id,
                        spell_id=spell.spell_id,
                        error=str(dp_error),
                    )
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
            # Always remove casting state, even if an error occurred
            # This prevents infinite error loops from stuck castings
            # NOTE: State is already cleared before processing effect (line 473) to prevent race conditions
            # This finally block is a safety net in case of early returns
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
        else:
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
        roll = random.randint(1, 100)

        success = roll <= luck
        logger.debug(
            "LUCK check",
            player_id=player_id,
            luck=luck,
            roll=roll,
            success=success,
        )

        return success
