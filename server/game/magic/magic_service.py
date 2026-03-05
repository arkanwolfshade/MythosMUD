"""
Core magic service for spellcasting.

This module provides the main magic service that handles MP management,
spell validation, casting rolls, and cost application.
"""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Magic service methods require multiple return statements for early validation returns (spell validation, MP checks, error handling). Magic service requires extensive spellcasting logic and MP management.

import random
import uuid
from typing import TYPE_CHECKING, Any, TypedDict, cast

from sqlalchemy.exc import SQLAlchemyError

from server.app.game_tick_processing import get_current_tick
from server.game.magic.casting_state_manager import CastingStateManager
from server.game.magic.magic_healing_events import MagicServiceHealingMixin
from server.game.magic.magic_service_completion import MagicServiceCompletionMixin
from server.game.magic.spell_costs import SpellCostsService
from server.game.magic.spell_effects import SpellEffects
from server.game.magic.spell_materials import SpellMaterialsService
from server.game.magic.spell_registry import SpellRegistry
from server.game.magic.spell_targeting import SpellTargetingService
from server.game.player_service import PlayerService
from server.models.spell import Spell
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.magic.spell_learning_service import SpellLearningService
    from server.services.combat_service import CombatService

logger = get_logger(__name__)


class MagicServiceOptionalDeps(TypedDict, total=False):
    """Optional dependencies for MagicService. All keys optional; defaults applied in __init__."""

    player_spell_repository: PlayerSpellRepository
    spell_learning_service: "SpellLearningService | None"
    casting_state_manager: CastingStateManager
    combat_service: "CombatService | None"
    spell_costs_service: SpellCostsService
    spell_materials_service: SpellMaterialsService


class _MagicServiceCore(MagicServiceCompletionMixin, MagicServiceHealingMixin):  # pylint: disable=too-many-instance-attributes  # Reason: Magic service requires many configuration and state tracking attributes
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
        optional_deps: MagicServiceOptionalDeps | None = None,
    ) -> None:
        """
        Initialize the magic service.

        Args:
            spell_registry: Registry for spell lookups
            player_service: Player service for stat modifications
            spell_targeting_service: Service for target resolution
            spell_effects: Engine for processing spell effects
            optional_deps: Optional dict with player_spell_repository, spell_learning_service,
                casting_state_manager, combat_service, spell_costs_service, spell_materials_service
        """
        opt = optional_deps or {}
        self.spell_registry = spell_registry
        self.player_service = player_service
        self.spell_targeting_service = spell_targeting_service
        self.spell_effects = spell_effects
        self.player_spell_repository = opt.get("player_spell_repository") or PlayerSpellRepository()
        self.spell_learning_service = opt.get("spell_learning_service")
        self.casting_state_manager = opt.get("casting_state_manager") or CastingStateManager()
        self.combat_service = opt.get("combat_service")
        self.spell_costs_service = opt.get("spell_costs_service") or SpellCostsService(player_service)
        self.spell_materials_service = opt.get("spell_materials_service") or SpellMaterialsService(player_service)
        logger.info("MagicService initialized")

    async def _get_player_and_normalized_stats(self, player_id: uuid.UUID) -> tuple[Any | None, dict[str, Any] | None]:
        """Load player and return normalized stats (MP/max_MP). Returns (player, stats) or (None, None)."""
        import math

        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return None, None
        stats = player.get_stats()
        pow_val = stats.get("power", 50)
        if "max_magic_points" not in stats:
            stats["max_magic_points"] = math.ceil(pow_val * 0.2)
        if not stats.get("magic_points", 0) and stats.get("max_magic_points", 0) > 0:
            stats["magic_points"] = stats["max_magic_points"]
        return player, stats

    def _check_mp_sufficient(self, stats: dict[str, Any], spell: Spell) -> tuple[bool, str]:
        """Return (False, message) if not enough MP, else (True, '')."""
        current_mp = stats.get("magic_points", 0)
        if current_mp < spell.mp_cost:
            return False, f"Not enough magic points. You need {spell.mp_cost} MP, but only have {current_mp}."
        return True, ""

    def _check_lucidity_sufficient(self, stats: dict[str, Any], spell: Spell) -> tuple[bool, str]:
        """Return (False, message) if Mythos spell and not enough lucidity, else (True, '')."""
        if not (spell.is_mythos() and spell.requires_lucidity()):
            return True, ""
        current_lucidity = stats.get("lucidity", 100)
        if current_lucidity < spell.lucidity_cost:
            return (
                False,
                f"Not enough lucidity. You need {spell.lucidity_cost} lucidity, but only have {current_lucidity}.",
            )
        return True, ""

    async def _check_player_knows_spell(self, player_id: uuid.UUID, spell: Spell) -> tuple[bool, str]:
        """Return (False, message) if player has not learned the spell, else (True, '')."""
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        if not player_spell:
            return False, f"You have not learned {spell.name}."
        return True, ""

    async def _check_materials_available(self, player_id: uuid.UUID, spell: Spell) -> tuple[bool, str]:
        """Return (False, message) if spell requires materials and any are missing, else (True, '')."""
        if not spell.materials:
            return True, ""
        missing_materials = await self.spell_materials_service.check_materials(player_id, spell)
        if not missing_materials:
            return True, ""
        material_list = ", ".join(missing_materials)
        return False, f"You are missing required materials: {material_list}."

    async def can_cast_spell(self, player_id: uuid.UUID, spell: Spell) -> tuple[bool, str]:
        """
        Check if a player can cast a spell.

        Args:
            player_id: Player ID
            spell: Spell to check

        Returns:
            tuple[bool, str]: (can_cast, error_message)
        """
        player, stats = await self._get_player_and_normalized_stats(player_id)
        if player is None or stats is None:
            return False, "You are not recognized by the cosmic forces."

        ok, msg = self._check_mp_sufficient(stats, spell)
        if not ok:
            return False, msg
        ok, msg = self._check_lucidity_sufficient(stats, spell)
        if not ok:
            return False, msg
        ok, msg = await self._check_player_knows_spell(player_id, spell)
        if not ok:
            return False, msg
        ok, msg = await self._check_materials_available(player_id, spell)
        if not ok:
            return False, msg
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

    def _calculate_initiative_tick(self, combat: Any, current_tick: int) -> int | None:
        """
        Calculate next initiative tick for combat casting.

        In round-based combat, spells complete casting and are queued for the next round.
        This method returns the next round tick when the spell will execute.
        """
        # In round-based combat, spells are queued for the next round when casting completes
        # Return the next round tick
        next_initiative_tick = combat.next_turn_tick
        if next_initiative_tick is None or next_initiative_tick <= current_tick:
            next_initiative_tick = current_tick + combat.turn_interval_ticks
        return cast(int | None, next_initiative_tick)

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
                next_initiative_tick = self._calculate_initiative_tick(combat, current_tick)

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

    @staticmethod
    def _resolve_heal_spell_id(spell_id: str, target_name: str | None) -> str:
        """Normalize 'heal' to heal_self or heal_other when command_data passes literal 'heal' (e.g. from client)."""
        if not spell_id or spell_id.strip().lower() != "heal":
            return spell_id
        if not target_name or not target_name.strip():
            return "heal_self"
        if target_name.strip().lower() in ("self", "me"):
            return "heal_self"
        return "heal_other"

    async def _get_spell_and_validate_target(
        self, player_id: uuid.UUID, spell_id: str, target_name: str | None
    ) -> tuple[Any | None, Any | None, dict[str, Any] | None]:
        """Resolve spell from registry and validate casting/target. Returns (spell, target, error_dict)."""
        spell = self._get_spell_from_registry(spell_id)
        if not spell:
            return None, None, {"success": False, "message": f"Spell '{spell_id}' not found."}
        target, validation_error = await self._validate_spell_casting(player_id, spell, target_name)
        if validation_error:
            return spell, None, {"success": False, "message": validation_error}
        return spell, target, None

    async def _consume_materials_if_required(self, player_id: uuid.UUID, spell: Any) -> dict[str, Any] | None:
        """Consume materials when spell requires them. Returns error dict to return, or None to continue."""
        if not spell.materials:
            return None
        material_result = await self.spell_materials_service.consume_materials(player_id, spell)
        if not material_result.get("success"):
            return {
                "success": False,
                "message": material_result.get("message", "Failed to consume materials."),
            }
        return None

    async def _casting_roll_or_fail_result(
        self, player_id: uuid.UUID, spell: Any, mastery: int
    ) -> dict[str, Any] | None:
        """Perform casting roll; on failure apply costs and return fail result. Returns None on success."""
        casting_success = await self._casting_roll(player_id, spell, mastery)
        if not casting_success:
            await self.spell_costs_service.apply_costs(player_id, spell)
            return {
                "success": False,
                "message": f"{spell.name} failed! The cosmic forces resist your incantation.",
                "costs_paid": True,
            }
        return None

    async def _execute_instant_or_delayed_cast(
        self, player_id: uuid.UUID, spell: Any, target: Any, mastery: int
    ) -> dict[str, Any]:
        """Run instant cast or start delayed cast; send healing event for instant heal when applicable."""
        if not spell.casting_time_seconds:
            result = await self._handle_instant_cast(player_id, spell, target, mastery)
            await self._send_instant_heal_event_if_applied(player_id, spell, target, result)
            return result
        current_tick = get_current_tick()
        return await self._start_delayed_cast(player_id, spell, target, mastery, current_tick)

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
        spell_id = self._resolve_heal_spell_id(spell_id, target_name)

        already_casting = self._check_already_casting(player_id)
        if already_casting:
            return already_casting

        spell, target, err = await self._get_spell_and_validate_target(player_id, spell_id, target_name)
        if err is not None:
            return err
        if spell is None or target is None:
            raise RuntimeError("spell and target must be set when err is None")

        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        mastery = int(player_spell.mastery) if player_spell else 0

        err = await self._consume_materials_if_required(player_id, spell)
        if err is not None:
            return err

        err = await self._casting_roll_or_fail_result(player_id, spell, mastery)
        if err is not None:
            return err

        return await self._execute_instant_or_delayed_cast(player_id, spell, target, mastery)

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

        success: bool = roll <= base_chance
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

    async def send_spell_execution_notifications(
        self, player_id: uuid.UUID, spell_id: str, effect_result: dict[str, Any], room_id: str
    ) -> None:
        """
        Send notifications after spell execution (completion messages and healing events).

        This public method should be used when executing spells outside the normal casting flow,
        such as when executing queued spells in combat.

        Args:
            player_id: ID of the player who cast the spell
            spell_id: ID of the spell that was executed
            effect_result: Result dictionary from spell effect processing
            room_id: ID of the room where the spell was executed
        """
        await self._send_spell_completion_message(player_id, spell_id, effect_result)
        await self._send_healing_update_event(player_id, effect_result, spell_id, room_id)

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

        success: bool = roll <= luck
        logger.debug(
            "LUCK check",
            player_id=player_id,
            luck=luck,
            roll=roll,
            success=success,
        )

        return success


class MagicService(_MagicServiceCore):
    """Public API: composition of completion, healing, and core spellcasting logic."""
