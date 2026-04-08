"""
Combat pipeline helpers for NPC combat integration (mixin).
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Combat pipeline mirrors CombatService APIs

import uuid
from typing import Protocol, cast
from uuid import UUID

from structlog.stdlib import BoundLogger

from ..models.combat import CombatResult
from ..structured_logging.enhanced_logging_config import get_logger
from .combat_messaging_integration import CombatMessagingIntegration
from .combat_service import CombatService
from .npc_combat_data_provider import NPCCombatDataProvider

logger: BoundLogger = get_logger(__name__)


class _NPCCombatIntegrationDeps(Protocol):
    """
    Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize them; avoids reportUninitializedInstanceVariable).
    """

    # pylint: disable=too-few-public-methods  # Reason: Structural typing Protocol; methods declare the mixin/host contract.

    def get_combat_service(self) -> CombatService:
        """Return combat service dependency."""
        raise NotImplementedError

    def get_data_provider(self) -> NPCCombatDataProvider:
        """Return data provider dependency."""
        raise NotImplementedError

    def get_messaging_integration(self) -> CombatMessagingIntegration:
        """Return messaging integration dependency."""
        raise NotImplementedError

    async def start_new_combat_for_mixin(
        self,
        player_id: str,
        room_id: str,
        attacker_uuid: UUID,
        target_uuid: UUID,
        damage: int,
        npc_instance: object,
        current_tick: int,
    ) -> CombatResult:
        """Start a new combat from mixin combat pipeline."""
        raise NotImplementedError


class NPCCombatIntegrationCombatMixin:
    """start_combat / process_attack paths and post-death broadcast."""

    # pylint: disable=too-few-public-methods  # Reason: Mixin exposes behavior via host class; methods are underscore-prefixed.

    async def _apply_npc_attack_damage_for_npc_initiated_combat(
        self: _NPCCombatIntegrationDeps,
        room_id: str,
        target_id: str,
        npc_instance: object,
        npc_uuid: UUID,
        player_uuid: UUID,
        attack_damage: int,
    ) -> None:
        """
        Resolve participant combat data and apply the initial attack damage through CombatService.

        Damage amount is the caller-supplied ``attack_damage``; combat resolution (armor, etc.)
        is handled inside ``process_attack``.
        """
        from ..app.lifespan import (
            get_current_tick,  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import avoids circular import at module load
        )

        current_tick = get_current_tick()
        data_provider = self.get_data_provider()
        player_name = await data_provider.get_player_name(target_id)
        attacker_data = data_provider.get_npc_combat_data(npc_instance, npc_uuid)
        target_data = await data_provider.get_player_combat_data(target_id, player_uuid, player_name)

        _ = await self.get_combat_service().start_combat(
            room_id=room_id,
            attacker=attacker_data,
            target=target_data,
            current_tick=current_tick,
        )
        _ = await self.get_combat_service().process_attack(
            attacker_id=npc_uuid,
            target_id=player_uuid,
            damage=attack_damage,
            is_initial_attack=True,
            damage_type="physical",
        )

    def _broadcast_npc_attack_on_player_started(
        self: _NPCCombatIntegrationDeps,
        npc_id: str,
        target_id: str,
        room_id: str,
        attack_damage: int,
    ) -> None:
        """Structured logging / observability trail when NPC-initiated combat begins."""
        logger.info(
            "NPC-initiated combat started",
            npc_id=npc_id,
            target_id=target_id,
            room_id=room_id,
            damage=attack_damage,
        )

    async def _process_combat_attack(
        self: _NPCCombatIntegrationDeps,
        player_id: str,
        room_id: str,
        attacker_uuid: UUID,
        target_uuid: UUID,
        damage: int,
        npc_instance: object,
    ) -> CombatResult:
        """Process combat attack, starting new combat or continuing existing one."""
        from ..app.lifespan import (
            get_current_tick,  # noqa: E402  # pylint: disable=wrong-import-position  # Reason: Lazy import avoids circular import at module load
        )

        current_tick = get_current_tick()

        combat_service = self.get_combat_service()
        existing_combat = await combat_service.get_combat_by_participant(attacker_uuid)
        if existing_combat:
            queued = await combat_service.queue_combat_action(
                combat_id=existing_combat.combat_id,
                participant_id=attacker_uuid,
                action_type="attack",
                target_id=target_uuid,
                damage=damage,
            )
            if queued:
                logger.info(
                    "Combat action queued",
                    combat_id=existing_combat.combat_id,
                    participant_id=attacker_uuid,
                    target_id=target_uuid,
                    round=existing_combat.combat_round + 1,
                )
                return CombatResult(
                    success=True,
                    damage=0,
                    target_died=False,
                    combat_ended=False,
                    message="Action queued for next round",
                    combat_id=existing_combat.combat_id,
                )

            logger.warning("Failed to queue action, executing immediately", participant_id=attacker_uuid)
            return await combat_service.process_attack(attacker_id=attacker_uuid, target_id=target_uuid, damage=damage)
        return await self.start_new_combat_for_mixin(
            player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance, current_tick
        )

    async def start_new_combat_for_mixin(
        self: _NPCCombatIntegrationDeps,
        player_id: str,
        room_id: str,
        attacker_uuid: UUID,
        target_uuid: UUID,
        damage: int,
        npc_instance: object,
        current_tick: int,
    ) -> CombatResult:
        """Start a new combat and process initial attack."""
        data_provider = self.get_data_provider()
        player_name = await data_provider.get_player_name(player_id)
        attacker_data = await data_provider.get_player_combat_data(player_id, attacker_uuid, player_name)

        target_data = data_provider.get_npc_combat_data(npc_instance, target_uuid)

        combat_service = self.get_combat_service()
        _ = await combat_service.start_combat(
            room_id=room_id,
            attacker=attacker_data,
            target=target_data,
            current_tick=current_tick,
        )

        return await combat_service.process_attack(
            attacker_id=attacker_uuid, target_id=target_uuid, damage=damage, is_initial_attack=True
        )

    async def _broadcast_room_after_npc_death(
        self: _NPCCombatIntegrationDeps, npc_id: str, room_id: str, killer_id: str
    ) -> None:
        """Broadcast room occupants update to killer's room after NPC death. Swallows errors (non-fatal)."""
        try:
            from ..realtime.connection_manager import ConnectionManager
            from ..realtime.websocket_room_updates import broadcast_room_update

            conn_mgr_raw = getattr(self.get_messaging_integration(), "connection_manager", None)
            conn_mgr: ConnectionManager | None = cast(ConnectionManager | None, conn_mgr_raw)
            broadcast_room_id: str = room_id
            if conn_mgr:
                try:
                    killer_uuid = uuid.UUID(str(killer_id))
                    killer_player = await conn_mgr.get_player(killer_uuid)
                    current_rid_raw = (
                        getattr(killer_player, "current_room_id", None) if killer_player is not None else None
                    )
                    if isinstance(current_rid_raw, str):
                        broadcast_room_id = current_rid_raw
                except (ValueError, TypeError, AttributeError):
                    pass
            await broadcast_room_update(
                str(killer_id),
                broadcast_room_id,
                connection_manager=conn_mgr,
            )
            logger.debug("Broadcast room occupants after NPC death", npc_id=npc_id, room_id=broadcast_room_id)
        except Exception as broadcast_err:  # pylint: disable=broad-exception-caught  # Reason: Broadcast failure must not affect NPC death handling
            err_text: str = f"{broadcast_err!s}"
            logger.warning(
                "Failed to broadcast room occupants after NPC death (non-fatal)",
                npc_id=npc_id,
                room_id=room_id,
                error=err_text,
            )
