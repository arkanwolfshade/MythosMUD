"""
Spell effects processing engine.

This module handles applying spell effects to targets, including healing,
damage, status effects, stat modifications, and other magical effects.
"""

# pylint: disable=too-many-return-statements  # Reason: Spell effects require multiple return statements for early validation returns (target validation, effect validation, error handling)

import uuid
from typing import Any, assert_never

from server.config import get_config
from server.game.player_service import PlayerService
from server.models.game import StatusEffect, StatusEffectType
from server.models.spell import Spell, SpellEffectType
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.realtime.login_grace_period import is_player_in_login_grace_period
from server.schemas.target_resolution import TargetMatch, TargetType
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
    ) -> None:
        """
        Initialize the spell effects engine.

        Args:
            player_service: Player service for stat modifications
            player_spell_repository: Optional repository for mastery lookups
        """
        self.player_service = player_service
        self.player_spell_repository = player_spell_repository or PlayerSpellRepository()
        logger.info("SpellEffects initialized")

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

        # Calculate mastery modifier (1.0 to 2.0 based on mastery 0-100)
        mastery_modifier = 1.0 + (mastery / 100.0)

        # Route to appropriate effect handler
        match spell.effect_type:
            case SpellEffectType.HEAL:
                return await self._process_heal(spell, target, caster_id, mastery_modifier)
            case SpellEffectType.DAMAGE:
                return await self._process_damage(spell, target, mastery_modifier)
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
            case _:
                # Exhaustive enum check: all SpellEffectType values must be handled above
                assert_never(spell.effect_type)

    async def _process_heal(
        self, spell: Spell, target: TargetMatch, caster_id: uuid.UUID, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process heal effect."""
        if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
            return {"success": False, "message": "Heal can only target entities", "effect_applied": False}

        # Heal Other cannot target self
        if spell.spell_id == "heal_other" and str(target.target_id) == str(caster_id):
            return {
                "success": False,
                "message": f"{spell.name} can only target others, not yourself.",
                "effect_applied": False,
            }
        heal_amount = int(spell.effect_data.get("heal_amount", 0) * mastery_modifier)
        if heal_amount <= 0:
            return {"success": False, "message": "Invalid heal amount", "effect_applied": False}

        if target.target_type == TargetType.PLAYER:
            try:
                target_id = uuid.UUID(target.target_id)
                await self.player_service.heal_player(target_id, heal_amount)
                return {
                    "success": True,
                    "message": f"Healed {target.target_name} for {heal_amount} health",
                    "effect_applied": True,
                    "heal_amount": heal_amount,
                }
            except OSError as e:
                logger.error("Error healing player", target_id=target.target_id, error=str(e))
                return {"success": False, "message": f"Failed to heal: {str(e)}", "effect_applied": False}

        # NPC healing not yet implemented
        return {
            "success": True,
            "message": f"Healed {target.target_name} for {heal_amount} health",
            "effect_applied": True,
        }

    async def _process_damage(self, spell: Spell, target: TargetMatch, mastery_modifier: float) -> dict[str, Any]:
        """Process damage effect."""
        if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
            return {"success": False, "message": "Damage can only target entities", "effect_applied": False}

        damage_amount = int(spell.effect_data.get("damage_amount", 0) * mastery_modifier)
        damage_type = spell.effect_data.get("damage_type", "magical")
        if damage_amount <= 0:
            return {"success": False, "message": "Invalid damage amount", "effect_applied": False}

        if target.target_type == TargetType.PLAYER:
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

        # NPC damage not yet implemented
        return {
            "success": True,
            "message": f"Dealt {damage_amount} {damage_type} damage to {target.target_name}",
            "effect_applied": True,
        }

    async def _process_status_effect(  # pylint: disable=too-many-locals  # Reason: Status effect processing requires many intermediate variables for complex effect logic
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process status effect."""
        if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
            return {"success": False, "message": "Status effects can only target entities", "effect_applied": False}

        effect_type_str = spell.effect_data.get("status_effect_type", "")
        duration = int(spell.effect_data.get("duration", 0) * mastery_modifier)
        intensity = min(10, max(1, int(spell.effect_data.get("intensity", 1) * mastery_modifier)))

        try:
            effect_type = StatusEffectType(effect_type_str)
        except ValueError:
            return {
                "success": False,
                "message": f"Invalid status effect type: {effect_type_str}",
                "effect_applied": False,
            }

        if target.target_type == TargetType.PLAYER:  # pylint: disable=too-many-nested-blocks  # Reason: Spell effects require complex nested logic for target validation, grace period checks, and effect application
            try:
                target_id = uuid.UUID(target.target_id)

                # Check if target is in login grace period - block negative effects
                try:
                    config = get_config()
                    app = getattr(config, "_app_instance", None)
                    if app:
                        connection_manager = getattr(app.state, "connection_manager", None)
                        if connection_manager:
                            if is_player_in_login_grace_period(target_id, connection_manager):
                                # Check if this is a negative effect
                                # Negative effects from StatusEffectType enum: STUNNED, POISONED, HALLUCINATING, PARANOID, TREMBLING, CORRUPTED, DELIRIOUS
                                # Positive effects: BUFF
                                negative_effect_types = {
                                    StatusEffectType.STUNNED,
                                    StatusEffectType.POISONED,
                                    StatusEffectType.HALLUCINATING,
                                    StatusEffectType.PARANOID,
                                    StatusEffectType.TREMBLING,
                                    StatusEffectType.CORRUPTED,
                                    StatusEffectType.DELIRIOUS,
                                }
                                if effect_type in negative_effect_types:
                                    logger.info(
                                        "Negative status effect blocked - target in login grace period",
                                        target_id=target.target_id,
                                        effect_type=effect_type.value,
                                    )
                                    return {
                                        "success": False,
                                        "message": f"Target is protected and immune to {effect_type.value}",
                                        "effect_applied": False,
                                    }
                                # Allow positive effects to proceed
                except (AttributeError, ImportError, TypeError, ValueError) as e:
                    # If we can't check grace period, proceed with effect (fail open)
                    logger.debug(
                        "Could not check login grace period for status effect",
                        target_id=target.target_id,
                        error=str(e),
                    )

                player = await self.player_service.persistence.get_player_by_id(target_id)
                if not player:
                    return {"success": False, "message": "Target player not found", "effect_applied": False}

                # Get current status effects
                status_effects = player.get_status_effects()
                # Add new status effect
                new_effect = StatusEffect(
                    effect_type=effect_type,
                    duration=duration,
                    intensity=intensity,
                    source=f"spell:{spell.spell_id}",
                )
                status_effects.append(new_effect.model_dump())
                player.set_status_effects(status_effects)
                await self.player_service.persistence.save_player(player)

                return {
                    "success": True,
                    "message": f"Applied {effect_type.value} to {target.target_name}",
                    "effect_applied": True,
                    "status_effect": effect_type.value,
                }
            except OSError as e:
                logger.error("Error applying status effect", target_id=target.target_id, error=str(e))
                return {
                    "success": False,
                    "message": f"Failed to apply status effect: {str(e)}",
                    "effect_applied": False,
                }

        return {
            "success": True,
            "message": f"Applied {effect_type.value} to {target.target_name}",
            "effect_applied": True,
        }

    async def _process_stat_modify(self, spell: Spell, target: TargetMatch, mastery_modifier: float) -> dict[str, Any]:  # pylint: disable=too-many-locals  # Reason: Stat modification requires many intermediate variables for complex stat calculation logic
        """Process stat modification effect."""
        if target.target_type != TargetType.PLAYER:
            return {"success": False, "message": "Stat modification can only target players", "effect_applied": False}

        # Get stat modifications from effect_data
        stat_modifications = spell.effect_data.get("stat_modifications", {})
        if not stat_modifications:
            return {"success": False, "message": "No stat modifications specified", "effect_applied": False}

        # Get duration (0 = permanent, >0 = temporary in ticks)
        duration = int(spell.effect_data.get("duration", 0))

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self.player_service.persistence.get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            stats = player.get_stats()
            modified_stats = []
            stat_changes = {}

            # Valid stat names
            valid_stats = [
                "strength",
                "dexterity",
                "constitution",
                "size",
                "intelligence",
                "power",
                "education",
                "charisma",
                "luck",
            ]

            # Apply stat modifications
            for stat_name, change_amount in stat_modifications.items():
                if stat_name not in valid_stats:
                    logger.warning("Invalid stat name in spell effect", stat_name=stat_name, spell_id=spell.spell_id)
                    continue

                # Apply mastery modifier to change amount
                adjusted_change = int(change_amount * mastery_modifier)
                current_value = stats.get(stat_name, 50)
                new_value = max(1, min(100, current_value + adjusted_change))

                stats[stat_name] = new_value
                stat_changes[stat_name] = adjusted_change
                modified_stats.append(f"{stat_name} ({adjusted_change:+d})")

            # If temporary, add a status effect to track the modification
            if duration > 0:
                status_effects = player.get_status_effects()
                # Create a status effect to track temporary stat modifications
                temp_effect = StatusEffect(
                    effect_type=StatusEffectType.BUFF,  # Using BUFF as a generic positive effect
                    duration=duration,
                    intensity=1,
                    source=f"spell:{spell.spell_id}",
                )
                # Store stat changes in metadata (would need to extend StatusEffect model for this)
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
            return {"success": False, "message": f"Failed to modify stats: {str(e)}", "effect_applied": False}

    async def _process_lucidity_adjust(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process lucidity adjustment effect."""
        if target.target_type != TargetType.PLAYER:
            return {"success": False, "message": "Lucidity adjustment can only target players", "effect_applied": False}

        adjust_amount = int(spell.effect_data.get("adjust_amount", 0) * mastery_modifier)
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
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, Any]:
        """Process object creation effect."""
        # Get item prototype ID and quantity from effect_data
        prototype_id = spell.effect_data.get("prototype_id")
        if not prototype_id:
            return {
                "success": False,
                "message": "No prototype ID specified for object creation",
                "effect_applied": False,
            }

        quantity = int(spell.effect_data.get("quantity", 1) * mastery_modifier)
        quantity = max(1, quantity)  # Ensure at least 1 item

        # Determine where to create the item
        # If target is a player, add to their inventory; if room, add to room drops
        if target.target_type == TargetType.PLAYER:
            try:
                target_id = uuid.UUID(target.target_id)
                player = await self.player_service.persistence.get_player_by_id(target_id)
                if not player:
                    return {"success": False, "message": "Target player not found", "effect_applied": False}

                # Add item to player inventory
                # Note: This is a simplified version - full implementation would use ItemFactory
                # and proper item instance creation. For now, we'll add a basic item entry.
                inventory = player.get_inventory()
                new_item = {
                    "item_id": prototype_id,
                    "prototype_id": prototype_id,
                    "quantity": quantity,
                    "item_name": prototype_id,  # Would be resolved from prototype registry
                }
                inventory.append(new_item)
                player.set_inventory(inventory)
                await self.player_service.persistence.save_player(player)

                return {
                    "success": True,
                    "message": f"Created {quantity} {prototype_id} in {target.target_name}'s inventory",
                    "effect_applied": True,
                    "prototype_id": prototype_id,
                    "quantity": quantity,
                }
            except OSError as e:
                logger.error("Error creating object in inventory", target_id=target.target_id, error=str(e))
                return {"success": False, "message": f"Failed to create object: {str(e)}", "effect_applied": False}

        elif target.target_type == TargetType.ROOM:
            # For room targets, we would need room_manager and ItemFactory
            # This is a placeholder - full implementation requires those services
            logger.warning(
                "Room item creation requires ItemFactory and room_manager",
                spell_id=spell.spell_id,
                room_id=target.room_id,
            )
            return {
                "success": False,
                "message": "Room item creation requires additional services (ItemFactory, room_manager)",
                "effect_applied": False,
            }

        return {
            "success": False,
            "message": f"Object creation cannot target {target.target_type.value}",
            "effect_applied": False,
        }
