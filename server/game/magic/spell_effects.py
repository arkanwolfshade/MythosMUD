"""
Spell effects processing engine.

This module handles applying spell effects to targets, including healing,
damage, status effects, stat modifications, and other magical effects.
"""

# pylint: disable=too-many-return-statements  # Reason: Spell effects require multiple return statements for early validation returns (target validation, effect validation, error handling)

import uuid
from typing import Any, assert_never

from server.game.magic.spell_effect_flee import run_flee_effect
from server.game.magic.spell_effects_heal import _get_npc_instance_for_steal_life, run_heal_effect
from server.game.magic.spell_effects_stats import apply_stat_modifications
from server.game.magic.spell_effects_status import run_status_effect
from server.game.magic.spell_effects_support import (
    process_create_object_effect,
    process_stat_modify_effect,
)
from server.game.player_service import PlayerService
from server.models.game import StatusEffect, StatusEffectType
from server.models.spell import Spell, SpellEffectType
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.schemas.shared import TargetMatch, TargetType
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SpellEffects:  # pylint: disable=too-few-public-methods  # Reason: Utility class with focused responsibility, minimal public interface
    """
    Engine for processing spell effects.

    Handles applying various spell effects to targets, with mastery
    modifiers applied to effectiveness.
    """

    def __init__(
        self,
        player_service: PlayerService,
        player_spell_repository: PlayerSpellRepository | None = None,
        combat_service: Any = None,
        movement_service: Any = None,
        get_room_by_id: Any = None,
        connection_manager: Any = None,
    ) -> None:
        """
        Initialize the spell effects engine.

        Args:
            player_service: Player service for stat modifications
            player_spell_repository: Optional repository for mastery lookups
            combat_service: Optional combat service for flee effect
            movement_service: Optional movement service for flee effect
            get_room_by_id: Optional callable (room_id -> room) for flee effect
            connection_manager: Optional connection manager for login grace period checks
        """
        self.player_service = player_service
        self.player_spell_repository = player_spell_repository or PlayerSpellRepository()
        self._combat_service = combat_service
        self._movement_service = movement_service
        self._get_room_by_id = get_room_by_id
        self._connection_manager = connection_manager
        logger.info("SpellEffects initialized")

    @property
    def connection_manager(self) -> Any:
        """Connection manager for login grace period checks."""
        return self._connection_manager

    @property
    def combat_service(self) -> Any:
        """Combat service for flee effect."""
        return self._combat_service

    @property
    def movement_service(self) -> Any:
        """Movement service for flee effect."""
        return self._movement_service

    @property
    def get_room_by_id(self) -> Any:
        """Callable to resolve room by ID for flee effect."""
        return self._get_room_by_id

    async def process_effect(
        self,
        spell: Spell,
        target: TargetMatch,
        caster_id: uuid.UUID,
        mastery: int = 0,
    ) -> dict[str, Any]:
        """
        Process a spell effect on a target.

        Args:
            spell: The spell being cast
            target: The target match
            caster_id: ID of the caster
            mastery: Mastery level (0-100) for effectiveness modifier

        Returns:
            dict: Result information including success, messages, and effect details
        """
        logger.debug(
            "Processing spell effect",
            spell_id=spell.spell_id,
            target_id=target.target_id,
            caster_id=caster_id,
            mastery=mastery,
        )
        mastery_modifier = 1.0 + (mastery / 100.0)
        return await self._dispatch_effect(spell, target, caster_id, mastery_modifier)

    async def _dispatch_effect(
        self,
        spell: Spell,
        target: TargetMatch,
        caster_id: uuid.UUID,
        mastery_modifier: float,
    ) -> dict[str, Any]:
        """Route to the appropriate effect handler based on spell.effect_type."""
        match spell.effect_type:
            case SpellEffectType.HEAL:
                return await self._process_heal(spell, target, caster_id, mastery_modifier)
            case SpellEffectType.DAMAGE:
                return await self._process_damage(spell, target, caster_id, mastery_modifier)
            case SpellEffectType.STATUS_EFFECT:
                return await self._process_status_effect(spell, target, mastery_modifier)
            case SpellEffectType.STAT_MODIFY:
                return await self._process_stat_modify(spell, target, mastery_modifier)
            case SpellEffectType.LUCIDITY_ADJUST:
                return await self._process_lucidity_adjust(spell, target, mastery_modifier)
            case SpellEffectType.CORRUPTION_ADJUST:
                return await self._process_corruption_adjust(spell, target, mastery_modifier)
            case SpellEffectType.TELEPORT:
                return await self._process_teleport(spell, target, mastery_modifier)
            case SpellEffectType.CREATE_OBJECT:
                return await self._process_create_object(spell, target, mastery_modifier)
            case SpellEffectType.FLEE:
                return await run_flee_effect(
                    self._combat_service,
                    self._movement_service,
                    self._get_room_by_id,
                    target,
                )
            case _:
                # Exhaustive enum check: all SpellEffectType values must be handled above
                assert_never(spell.effect_type)

    async def _process_heal(
        self, spell: Spell, target: TargetMatch, caster_id: uuid.UUID, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process heal effect (normal heals and steal-life). Delegated to spell_effects_heal."""
        return await run_heal_effect(
            self, spell, target, caster_id, mastery_modifier, combat_service=self._combat_service
        )

    async def _process_damage(
        self, spell: Spell, target: TargetMatch, caster_id: uuid.UUID, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process damage effect."""
        if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
            return {"success": False, "message": "Damage can only target entities", "effect_applied": False}

        damage_amount = int(spell.effect_data.get("damage_amount", 0) * mastery_modifier)
        damage_type = spell.effect_data.get("damage_type", "magical")
        if damage_amount <= 0:
            return {"success": False, "message": "Invalid damage amount", "effect_applied": False}

        if target.target_type == TargetType.PLAYER:
            return await self._process_damage_to_player(target, damage_amount, damage_type)
        return await self._process_damage_to_npc(target, damage_amount, damage_type, caster_id)

    async def _process_damage_to_player(
        self, target: TargetMatch, damage_amount: int, damage_type: str
    ) -> dict[str, Any]:
        """Apply damage to a player target."""
        try:
            target_id = uuid.UUID(target.target_id)
            await self.player_service.damage_player(target_id, damage_amount, damage_type)
            return {
                "success": True,
                "message": f"Dealt {damage_amount} {damage_type} damage to {target.target_name}",
                "effect_applied": True,
                "damage_amount": damage_amount,
                "damage_type": damage_type,
            }
        except OSError as e:
            logger.error("Error damaging player", target_id=target.target_id, error=str(e))
            return {"success": False, "message": f"Failed to damage: {str(e)}", "effect_applied": False}

    async def _process_damage_to_npc(
        self, target: TargetMatch, damage_amount: int, damage_type: str, caster_id: uuid.UUID
    ) -> dict[str, Any]:
        """Apply damage to an NPC target; publish events and sync combat participant."""
        npc_instance = _get_npc_instance_for_steal_life(str(target.target_id), self._combat_service)
        if not npc_instance or not getattr(npc_instance, "is_alive", True):
            return {"success": False, "message": "Target is not available.", "effect_applied": False}
        ok = npc_instance.take_damage(damage_amount, damage_type, source_id=str(caster_id))
        if not ok:
            return {"success": False, "message": "Failed to damage target.", "effect_applied": False}
        await self._publish_npc_damage_and_death_events(npc_instance, target, damage_amount, caster_id)
        return {
            "success": True,
            "message": f"Dealt {damage_amount} {damage_type} damage to {target.target_name}",
            "effect_applied": True,
            "damage_amount": damage_amount,
            "damage_type": damage_type,
        }

    async def _publish_npc_damage_and_death_events(
        self, npc_instance: Any, target: TargetMatch, damage_amount: int, caster_id: uuid.UUID
    ) -> None:
        """Publish NPC damage event and death event if applicable; sync combat participant."""
        room_id = getattr(npc_instance, "current_room", None)
        if not self._combat_service or not room_id:
            return
        stats_after: dict[str, Any] = getattr(npc_instance, "get_combat_stats", lambda: {})()
        new_dp = int(stats_after.get("current_dp", 0))
        max_dp = int(stats_after.get("max_dp", 0))
        try:
            npc_id_ev: uuid.UUID | str = uuid.UUID(str(target.target_id))
        except (ValueError, TypeError):
            npc_id_ev = getattr(npc_instance, "npc_id", str(target.target_id))
        self._combat_service.sync_npc_participant_dp_after_spell_damage(str(target.target_id), new_dp)
        await self._combat_service.publish_npc_damage_event(
            room_id=room_id,
            npc_id=npc_id_ev,
            npc_name=target.target_name,
            damage=damage_amount,
            current_dp=new_dp,
            max_dp=max_dp,
        )
        is_dead = not getattr(npc_instance, "is_alive", True) or new_dp <= 0
        if is_dead:
            npc_id_str = getattr(npc_instance, "npc_id", str(target.target_id))
            await self._combat_service.publish_npc_died_event(
                room_id=room_id,
                npc_id=npc_id_str,
                npc_name=target.target_name,
                xp_reward=0,
                killer_id=str(caster_id),
            )
            await self._combat_service.end_combat_if_npc_died(npc_id_str)

    async def _process_status_effect(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process status effect. Delegated to spell_effects_status."""
        return await run_status_effect(self, spell, target, mastery_modifier)

    def _build_stat_modifications(self, spell: Spell) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        """
        Build normalized stat_modifications dict from spell.effect_data.

        Supports both full dict form and CoC shorthand {"stat": "...", "delta": N}.
        """
        stat_modifications = spell.effect_data.get("stat_modifications", {})
        if not stat_modifications:
            stat_name = spell.effect_data.get("stat")
            delta = spell.effect_data.get("delta")
            if stat_name and isinstance(delta, (int, float)):
                stat_modifications = {str(stat_name): delta}
        if not stat_modifications:
            return None, {
                "success": False,
                "message": "No stat modifications specified",
                "effect_applied": False,
            }
        return stat_modifications, None

    async def _apply_stat_modify_to_player(
        self,
        spell: Spell,
        target: TargetMatch,
        mastery_modifier: float,
        stat_modifications: dict[str, Any],
        duration: int,
    ) -> dict[str, Any]:
        """Apply stat modifications and optional temporary BUFF status to a player."""
        try:
            target_id = uuid.UUID(target.target_id)
            player = await self.player_service.persistence.get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            stats = player.get_stats()
            stats, stat_changes, modified_stats = apply_stat_modifications(
                stats,
                stat_modifications,
                mastery_modifier,
                spell.spell_id,
            )

            if duration > 0:
                status_effects = player.get_status_effects()
                temp_effect = StatusEffect(
                    effect_type=StatusEffectType.BUFF,
                    duration=duration,
                    intensity=1,
                    source=f"spell:{spell.spell_id}",
                )
                status_effects.append(temp_effect.model_dump())
                player.set_status_effects(status_effects)

            player.set_stats(stats)
            await self.player_service.persistence.save_player(player)

            stat_list = ", ".join(modified_stats)
            duration_text = f" for {duration} ticks" if duration > 0 else " permanently"
            return {
                "success": True,
                "message": f"Modified {target.target_name}'s stats{duration_text}: {stat_list}",
                "effect_applied": True,
                "stat_changes": stat_changes,
                "duration": duration,
            }
        except OSError as e:
            logger.error("Error modifying stats", target_id=target.target_id, error=str(e))
            return {
                "success": False,
                "message": f"Failed to modify stats: {str(e)}",
                "effect_applied": False,
            }

    async def _process_stat_modify(self, spell: Spell, target: TargetMatch, mastery_modifier: float) -> dict[str, Any]:
        """Process stat modification effect (delegated to support module)."""
        return await process_stat_modify_effect(self, spell, target, mastery_modifier)

    async def _process_lucidity_adjust(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process lucidity adjustment effect."""
        if target.target_type != TargetType.PLAYER:
            return {"success": False, "message": "Lucidity adjustment can only target players", "effect_applied": False}

        # Support both legacy key (adjust_amount) and CoC key (lucidity_delta)
        raw_adjust = spell.effect_data.get("adjust_amount", spell.effect_data.get("lucidity_delta", 0))
        adjust_amount = int(raw_adjust * mastery_modifier)
        if not adjust_amount:
            return {"success": False, "message": "Invalid lucidity adjustment amount", "effect_applied": False}

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self.player_service.persistence.get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            if adjust_amount > 0:
                await self.player_service.persistence.apply_lucidity_gain(
                    player, adjust_amount, f"spell:{spell.spell_id}"
                )
            else:
                await self.player_service.persistence.apply_lucidity_loss(
                    player, abs(adjust_amount), f"spell:{spell.spell_id}"
                )

            return {
                "success": True,
                "message": f"Adjusted {target.target_name}'s lucidity by {adjust_amount}",
                "effect_applied": True,
                "lucidity_adjust": adjust_amount,
            }
        except OSError as e:
            logger.error("Error adjusting lucidity", target_id=target.target_id, error=str(e))
            return {"success": False, "message": f"Failed to adjust lucidity: {str(e)}", "effect_applied": False}

    async def _process_corruption_adjust(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process corruption adjustment effect."""
        if target.target_type != TargetType.PLAYER:
            return {
                "success": False,
                "message": "Corruption adjustment can only target players",
                "effect_applied": False,
            }

        adjust_amount = int(spell.effect_data.get("adjust_amount", 0) * mastery_modifier)
        if not adjust_amount:
            return {"success": False, "message": "Invalid corruption adjustment amount", "effect_applied": False}

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self.player_service.persistence.get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            stats = player.get_stats()
            current_corruption = stats.get("corruption", 0)

            # Corruption is bounded 0-100
            new_corruption = max(0, min(100, current_corruption + adjust_amount))
            stats["corruption"] = new_corruption

            player.set_stats(stats)
            await self.player_service.persistence.save_player(player)

            direction = "increased" if adjust_amount > 0 else "decreased"
            return {
                "success": True,
                "message": f"{direction.capitalize()} {target.target_name}'s corruption by {abs(adjust_amount)}",
                "effect_applied": True,
                "corruption_adjust": adjust_amount,
                "new_corruption": new_corruption,
            }
        except OSError as e:
            logger.error("Error adjusting corruption", target_id=target.target_id, error=str(e))
            return {"success": False, "message": f"Failed to adjust corruption: {str(e)}", "effect_applied": False}

    async def _process_teleport(self, spell: Spell, target: TargetMatch, _mastery_modifier: float) -> dict[str, Any]:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future mastery-based teleport enhancement
        """Process teleport effect."""
        if target.target_type != TargetType.PLAYER:
            return {"success": False, "message": "Teleport can only target players", "effect_applied": False}

        # Get destination room ID from effect_data
        destination_room_id = spell.effect_data.get("destination_room_id")
        if not destination_room_id:
            return {"success": False, "message": "No destination room specified", "effect_applied": False}

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self.player_service.persistence.get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            # Use player service to update location
            # Note: This is a simplified teleport - full implementation would use MovementService
            # and handle room events, but for spell effects this is sufficient
            original_room_id = player.current_room_id
            success = await self.player_service.update_player_location(player.name, destination_room_id)

            if not success:
                return {"success": False, "message": "Failed to teleport player", "effect_applied": False}

            return {
                "success": True,
                "message": f"Teleported {target.target_name} to {destination_room_id}",
                "effect_applied": True,
                "destination_room_id": destination_room_id,
                "original_room_id": original_room_id,
            }
        except OSError as e:
            logger.error("Error teleporting player", target_id=target.target_id, error=str(e))
            return {"success": False, "message": f"Failed to teleport: {str(e)}", "effect_applied": False}

    async def _process_create_object(
        self,
        spell: Spell,
        target: TargetMatch,
        mastery_modifier: float,
    ) -> dict[str, Any]:
        """Process object creation effect (delegated to support module)."""
        return await process_create_object_effect(self, spell, target, mastery_modifier)
