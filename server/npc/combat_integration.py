"""
NPC Combat Integration for MythosMUD.

This module provides integration between NPCs and the existing combat system,
including damage calculation, combat events, and interaction with the game
mechanics service.

Implementation is split with :mod:`combat_integration_base` so file size stays
within Codacy Lizard limits while preserving a single public class.
"""

import uuid
from typing import TYPE_CHECKING, cast, override

from ..config import get_config
from ..events.combat_events import PlayerAttackedEvent
from ..events.event_types import NPCAttacked, PlayerDPUpdated
from ..exceptions import DatabaseError, ValidationError
from .combat_integration_base import NPCCombatIntegrationBase, logger
from .combat_integration_protocols import CombatEventPublisherProtocol

if TYPE_CHECKING:
    from .lifecycle_manager import NPCLifecycleManager


class NPCCombatIntegration(NPCCombatIntegrationBase):
    """
    Integrates NPCs with the existing combat and game mechanics systems.

    Extends the base with event publishing (bus, NATS), NPC death handling, and combat stat helpers.
    """

    @override
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

    @override
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

    @override
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

    @override
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

    def _get_combat_event_publisher(self) -> CombatEventPublisherProtocol | None:
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
        return cast(CombatEventPublisherProtocol | None, publisher)

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
        if isinstance(value, int | float):
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
        if isinstance(raw_current_dp, int | float):
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


__all__ = ["NPCCombatIntegration"]
