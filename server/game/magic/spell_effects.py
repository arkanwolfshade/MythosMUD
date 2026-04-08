"""
Spell effects processing engine.

This module handles applying spell effects to targets, including healing,
damage, status effects, stat modifications, and other magical effects.
"""

# pylint: disable=too-many-return-statements  # Reason: Spell effects require multiple return statements for early validation returns (target validation, effect validation, error handling)

import uuid
from collections.abc import Callable
from typing import assert_never, cast

from structlog.stdlib import BoundLogger

from server.game.magic.spell_effect_flee import run_flee_effect
from server.game.magic.spell_effect_types import (
    NpcSpellDamageTarget,
    PlayerPersistenceSpellPort,
    SpellEffectPlayer,
    SpellEffectsEngineHealPort,
)
from server.game.magic.spell_effects_heal import get_npc_instance_for_steal_life, run_heal_effect
from server.game.magic.spell_effects_internal import (
    coerce_effect_float_times_mastery_as_int,
    coerce_effect_int_times_mastery,
    combat_room_id_for_npc_spell,
)
from server.game.magic.spell_effects_status import run_status_effect
from server.game.magic.spell_effects_support import (
    process_create_object_effect,
    process_stat_modify_effect,
)
from server.game.movement_service import MovementService
from server.game.player_service import PlayerService
from server.models.spell import Spell, SpellEffectType
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository
from server.schemas.shared import TargetMatch, TargetType
from server.services.combat_service import CombatService
from server.services.combat_service_npc import get_combat_id_for_npc, resolve_npc_participant_id_in_combat
from server.structured_logging.enhanced_logging_config import get_logger

logger: BoundLogger = get_logger(__name__)


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
        combat_service: CombatService | None = None,
        movement_service: MovementService | None = None,
        get_room_by_id: Callable[[str], object] | None = None,
        connection_manager: object | None = None,
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
        self.player_service: PlayerService = player_service
        self.player_spell_repository: PlayerSpellRepository = player_spell_repository or PlayerSpellRepository()
        self._combat_service: CombatService | None = combat_service
        self._movement_service: MovementService | None = movement_service
        self._get_room_by_id: Callable[[str], object] | None = get_room_by_id
        self._connection_manager: object | None = connection_manager
        logger.info("SpellEffects initialized")

    def _spell_player_persistence(self) -> PlayerPersistenceSpellPort:
        """Narrow persistence for spell paths (PlayerService.persistence is untyped)."""
        return cast(PlayerPersistenceSpellPort, self.player_service.persistence)

    @property
    def connection_manager(self) -> object | None:
        """Connection manager for login grace period checks."""
        return self._connection_manager

    @property
    def combat_service(self) -> CombatService | None:
        """Combat service for flee effect."""
        return self._combat_service

    @property
    def movement_service(self) -> MovementService | None:
        """Movement service for flee effect."""
        return self._movement_service

    @property
    def get_room_by_id(self) -> Callable[[str], object] | None:
        """Callable to resolve room by ID for flee effect."""
        return self._get_room_by_id

    async def process_effect(
        self,
        spell: Spell,
        target: TargetMatch,
        caster_id: uuid.UUID,
        mastery: int = 0,
    ) -> dict[str, object]:
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
    ) -> dict[str, object]:
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
                return cast(
                    dict[str, object],
                    await run_flee_effect(
                        self._combat_service,
                        self._movement_service,
                        self._get_room_by_id,
                        target,
                    ),
                )
            case _:
                # Exhaustive enum check: all SpellEffectType values must be handled above
                assert_never(spell.effect_type)

    async def _process_heal(
        self, spell: Spell, target: TargetMatch, caster_id: uuid.UUID, mastery_modifier: float
    ) -> dict[str, object]:
        """Process heal effect (normal heals and steal-life). Delegated to spell_effects_heal."""
        # Cast via object: SpellEffects.player_service is PlayerService; Protocol wants PlayerServiceHealPort.
        # PlayerService.persistence is Any at definition site, so structural match fails; pyright needs object hop.
        return await run_heal_effect(
            cast(SpellEffectsEngineHealPort, cast(object, self)),
            spell,
            target,
            caster_id,
            mastery_modifier,
            combat_service=self._combat_service,
        )

    async def _process_damage(
        self, spell: Spell, target: TargetMatch, caster_id: uuid.UUID, mastery_modifier: float
    ) -> dict[str, object]:
        """Process damage effect."""
        if target.target_type not in (TargetType.PLAYER, TargetType.NPC):
            return {"success": False, "message": "Damage can only target entities", "effect_applied": False}

        dmg_raw = cast(object, spell.effect_data.get("damage_amount", 0))
        damage_amount = coerce_effect_int_times_mastery(dmg_raw, mastery_modifier)
        damage_type = str(cast(object, spell.effect_data.get("damage_type", "magical")))
        if damage_amount <= 0:
            return {"success": False, "message": "Invalid damage amount", "effect_applied": False}

        if target.target_type == TargetType.PLAYER:
            return await self._process_damage_to_player(target, damage_amount, damage_type)
        return await self._process_damage_to_npc(target, damage_amount, damage_type, caster_id)

    async def _process_damage_to_player(
        self, target: TargetMatch, damage_amount: int, damage_type: str
    ) -> dict[str, object]:
        """Apply damage to a player target."""
        try:
            target_id = uuid.UUID(target.target_id)
            _ = await self.player_service.damage_player(target_id, damage_amount, damage_type)
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
    ) -> dict[str, object]:
        """Apply damage to an NPC target; publish events and sync combat participant."""
        npc_raw = get_npc_instance_for_steal_life(str(target.target_id), self._combat_service)
        if not npc_raw or not npc_raw.is_alive:
            return {"success": False, "message": "Target is not available.", "effect_applied": False}
        npc_instance: NpcSpellDamageTarget = npc_raw
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

    def _add_spell_damage_threat_to_combat(self, target: TargetMatch, caster_id: uuid.UUID, damage_amount: int) -> None:
        """ADR-016: Add spell damage threat to NPC's hate list for the caster. No-op if not in combat."""
        cs = self._combat_service
        if cs is None:
            return
        combat_id = get_combat_id_for_npc(cs, str(target.target_id))
        if not combat_id:
            return
        combat = cs.get_combat(combat_id)
        if not combat:
            return
        from server.services.aggro_threat import add_damage_threat

        npc_participant_id = resolve_npc_participant_id_in_combat(cs, combat, str(target.target_id))
        if npc_participant_id is None:
            return
        npc_part = combat.participants.get(npc_participant_id)
        add_damage_threat(combat, npc_participant_id, caster_id, damage_amount, npc_participant=npc_part)

    def _resolve_room_for_npc_spell_publish(self, npc_instance: NpcSpellDamageTarget, npc_target_id: str) -> str:
        """Prefer NPC current_room; fall back to active combat.room_id for NATS payloads."""
        combat_room = combat_room_id_for_npc_spell(self._combat_service, npc_target_id)
        room_raw = npc_instance.current_room
        return (room_raw if isinstance(room_raw, str) and room_raw.strip() else None) or combat_room or ""

    async def _publish_npc_damage_and_death_events(
        self, npc_instance: NpcSpellDamageTarget, target: TargetMatch, damage_amount: int, caster_id: uuid.UUID
    ) -> None:
        """Publish NPC damage event and death event if applicable; sync combat participant."""
        cs = self._combat_service
        if cs is None:
            return

        stats_after = npc_instance.get_combat_stats()
        new_dp = int(stats_after.get("current_dp", 0))
        max_dp = int(stats_after.get("max_dp", 0))
        try:
            npc_id_ev: uuid.UUID | str = uuid.UUID(str(target.target_id))
        except (ValueError, TypeError):
            npc_id_ev = npc_instance.npc_id

        # Spell damage updates the live NPC instance first (take_damage). Combat UI and melee
        # use CombatParticipant.current_dp; always sync participant from instance even when
        # current_room is unset (participant room comes from combat.room_id).
        cs.sync_npc_participant_dp_after_spell_damage(str(target.target_id), new_dp)
        self._add_spell_damage_threat_to_combat(target, caster_id, damage_amount)

        room_id = self._resolve_room_for_npc_spell_publish(npc_instance, str(target.target_id))
        if not room_id:
            logger.warning(
                "Spell NPC damage: cannot resolve room for NATS publish; combat participant DP synced",
                npc_id=str(target.target_id),
                new_dp=new_dp,
                damage=damage_amount,
            )
            is_dead = not npc_instance.is_alive or new_dp <= 0
            if is_dead:
                npc_id_str = str(npc_instance.npc_id)
                _ = await cs.end_combat_if_npc_died(npc_id_str)
            return

        _ = await cs.publish_npc_damage_event(
            room_id=room_id,
            npc_id=npc_id_ev,
            npc_name=target.target_name,
            damage=damage_amount,
            current_dp=new_dp,
            max_dp=max_dp,
        )
        is_dead = not npc_instance.is_alive or new_dp <= 0
        if is_dead:
            npc_id_str = str(npc_instance.npc_id)
            _ = await cs.publish_npc_died_event(
                room_id=room_id,
                npc_id=npc_id_str,
                npc_name=target.target_name,
                xp_reward=0,
                killer_id=str(caster_id),
            )
            _ = await cs.end_combat_if_npc_died(npc_id_str)

    async def _process_status_effect(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, object]:
        """Process status effect. Delegated to spell_effects_status."""
        return cast(dict[str, object], await run_status_effect(self, spell, target, mastery_modifier))

    async def _process_stat_modify(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, object]:
        """Process stat modification effect (delegated to support module)."""
        return cast(dict[str, object], await process_stat_modify_effect(self, spell, target, mastery_modifier))

    async def _process_lucidity_adjust(
        self, spell: Spell, target: TargetMatch, mastery_modifier: float
    ) -> dict[str, object]:
        """Process lucidity adjustment effect."""
        if target.target_type != TargetType.PLAYER:
            return {"success": False, "message": "Lucidity adjustment can only target players", "effect_applied": False}

        # Support both legacy key (adjust_amount) and CoC key (lucidity_delta)
        lucidity_delta = cast(object, spell.effect_data.get("lucidity_delta", 0))
        raw_obj = cast(object, spell.effect_data.get("adjust_amount", lucidity_delta))
        adjust_amount = coerce_effect_float_times_mastery_as_int(raw_obj, mastery_modifier)
        if not adjust_amount:
            return {"success": False, "message": "Invalid lucidity adjustment amount", "effect_applied": False}

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self._spell_player_persistence().get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            pe_player = cast(SpellEffectPlayer, player)
            persistence = self._spell_player_persistence()
            if adjust_amount > 0:
                await persistence.apply_lucidity_gain(pe_player, adjust_amount, f"spell:{spell.spell_id}")
            else:
                await persistence.apply_lucidity_loss(pe_player, abs(adjust_amount), f"spell:{spell.spell_id}")

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
    ) -> dict[str, object]:
        """Process corruption adjustment effect."""
        if target.target_type != TargetType.PLAYER:
            return {
                "success": False,
                "message": "Corruption adjustment can only target players",
                "effect_applied": False,
            }

        adj_raw = cast(object, spell.effect_data.get("adjust_amount", 0))
        adjust_amount = coerce_effect_int_times_mastery(adj_raw, mastery_modifier)
        if not adjust_amount:
            return {"success": False, "message": "Invalid corruption adjustment amount", "effect_applied": False}

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self._spell_player_persistence().get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            pe_player = cast(SpellEffectPlayer, player)
            stats = dict(pe_player.get_stats())
            co = stats.get("corruption", 0)
            current_corruption = int(co) if isinstance(co, (int, float)) else 0

            # Corruption is bounded 0-100
            new_corruption = max(0, min(100, current_corruption + adjust_amount))
            stats["corruption"] = new_corruption

            pe_player.set_stats(stats)
            await self._spell_player_persistence().save_player(player)

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

    async def _process_teleport(self, spell: Spell, target: TargetMatch, _mastery_modifier: float) -> dict[str, object]:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future mastery-based teleport enhancement
        """Process teleport effect."""
        if target.target_type != TargetType.PLAYER:
            return {"success": False, "message": "Teleport can only target players", "effect_applied": False}

        # Get destination room ID from effect_data
        dest_raw = cast(object, spell.effect_data.get("destination_room_id"))
        if dest_raw is None or not dest_raw:
            return {"success": False, "message": "No destination room specified", "effect_applied": False}
        destination_room_id = str(dest_raw).strip()
        if not destination_room_id:
            return {"success": False, "message": "No destination room specified", "effect_applied": False}

        try:
            target_id = uuid.UUID(target.target_id)
            player = await self._spell_player_persistence().get_player_by_id(target_id)
            if not player:
                return {"success": False, "message": "Target player not found", "effect_applied": False}

            pe_player = cast(SpellEffectPlayer, player)
            # Use player service to update location
            # Note: This is a simplified teleport - full implementation would use MovementService
            # and handle room events, but for spell effects this is sufficient
            original_room_id = pe_player.current_room_id
            success = await self.player_service.update_player_location(pe_player.name, destination_room_id)

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
    ) -> dict[str, object]:
        """Process object creation effect (delegated to support module)."""
        return cast(dict[str, object], await process_create_object_effect(self, spell, target, mastery_modifier))
