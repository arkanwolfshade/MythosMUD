"""
Validation and UUID-mapping helpers for NPC combat integration (mixin).
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: UUID and XP mapping APIs require full combat context

import uuid
from typing import Protocol, cast
from uuid import UUID, uuid4

from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger
from .combat_service import CombatService
from .npc_combat_data_provider import NPCCombatDataProvider
from .npc_combat_lucidity import NPCCombatLucidity
from .npc_combat_uuid_mapping import NPCCombatUUIDMapping
from .room_data_validator import RoomDataValidator

logger: BoundLogger = get_logger(__name__)


def _coerce_xp_mapping_value(raw: object) -> int:
    """Parse xp_value from NPC base_stats JSON; bool maps to 0 (avoid True -> 1)."""
    if isinstance(raw, bool):
        return 0
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(raw)
    if isinstance(raw, str):
        try:
            return int(raw)
        except ValueError:
            return 0
    return 0


def _warn_attacked_dead_npc(player_id: str, npc_id: str, npc_instance: object, npc_instance_provided: bool) -> None:
    """Log when a player targets an NPC that exists but is not alive."""
    logger.warning(
        "Player attacked dead NPC - NPC exists but is_alive is False",
        player_id=player_id,
        npc_id=npc_id,
        npc_name=getattr(npc_instance, "name", "unknown"),
        is_alive=False,
        npc_instance_provided=npc_instance_provided,
    )


class _NPCCombatIntegrationValidationDeps(Protocol):
    """
    Attributes supplied by NPCCombatIntegrationService (mixin cannot initialize them;
    avoids reportUninitializedInstanceVariable).
    """

    # pylint: disable=too-few-public-methods  # Reason: Structural typing Protocol; methods declare the mixin/host contract.

    def get_combat_service(self) -> CombatService:
        """Return combat service dependency."""
        raise NotImplementedError

    def get_data_provider(self) -> NPCCombatDataProvider:
        """Return data provider dependency."""
        raise NotImplementedError

    def get_uuid_mapping(self) -> NPCCombatUUIDMapping:
        """Return UUID mapping dependency."""
        raise NotImplementedError

    def get_lucidity_service(self) -> NPCCombatLucidity:
        """Return lucidity dependency."""
        raise NotImplementedError

    async def store_npc_xp_mapping_for_mixin(
        self,
        npc_id: str,
        target_uuid: UUID,
        room_id: str,
        player_id: str,
        first_engagement: bool,
    ) -> None:
        """Store XP mapping for NPC combat setup from validation mixin."""
        raise NotImplementedError


class NPCCombatIntegrationValidationMixin:
    """Room checks, NPC resolution, UUID mapping, and XP mapping for combat integration."""

    # pylint: disable=too-few-public-methods  # Reason: Mixin exposes behavior via host class; methods are underscore-prefixed.

    async def _validate_and_get_npc_instance(
        self: _NPCCombatIntegrationValidationDeps,
        player_id: str,
        npc_id: str,
        npc_instance: object | None,
    ) -> object | None:
        """Validate NPC instance (lookup when missing). Return instance or None."""
        npc_instance_provided = npc_instance is not None
        if npc_instance is None:
            logger.debug(
                "Performing NPC instance lookup",
                player_id=player_id,
                npc_id=npc_id,
            )
            npc_instance = self.get_data_provider().get_npc_instance(npc_id)
        else:
            logger.debug(
                "Using provided NPC instance - avoiding redundant lookup",
                player_id=player_id,
                npc_id=npc_id,
                npc_name=getattr(npc_instance, "name", "unknown"),
            )

        if not npc_instance:
            logger.warning(
                "Player attacked non-existent NPC - NPC not found in lifecycle manager",
                player_id=player_id,
                npc_id=npc_id,
                npc_instance_provided=npc_instance_provided,
            )
            return None

        alive = bool(getattr(npc_instance, "is_alive", False))
        if not alive:
            _warn_attacked_dead_npc(player_id, npc_id, npc_instance, npc_instance_provided)
            return None

        return npc_instance

    async def _validate_combat_location(
        self: _NPCCombatIntegrationValidationDeps,
        player_id: str,
        npc_id: str,
        room_id: str,
        npc_instance: object,
    ) -> bool:
        """Validate that player and NPC are in the same room."""
        if not RoomDataValidator.is_valid_room_id(room_id):
            logger.warning(
                "Combat room ID format invalid",
                player_id=player_id,
                npc_id=npc_id,
                combat_room_id=room_id,
            )
            return False

        player_room_id = await self.get_data_provider().get_player_room_id(player_id)
        npc_room_id = getattr(npc_instance, "current_room", None)

        logger.debug(
            "Room validation check",
            player_id=player_id,
            npc_id=npc_id,
            player_room_id=player_room_id,
            npc_room_id=npc_room_id,
            combat_room_id=room_id,
        )

        if player_room_id != npc_room_id:
            logger.warning(
                "Cross-room attack attempt blocked",
                player_id=player_id,
                npc_id=npc_id,
                player_room_id=player_room_id,
                npc_room_id=npc_room_id,
            )
            return False

        if player_room_id != room_id or npc_room_id != room_id:
            logger.warning(
                "Combat room mismatch - room_id does not match participant rooms",
                player_id=player_id,
                npc_id=npc_id,
                player_room_id=player_room_id,
                npc_room_id=npc_room_id,
                combat_room_id=room_id,
            )
            return False

        return True

    async def _end_combat_if_participant_in_combat(
        self: _NPCCombatIntegrationValidationDeps, player_id: str, npc_id: str
    ) -> None:
        """End any active combat that includes this player when room validation fails."""
        try:
            player_uuid = uuid.UUID(player_id)
        except (ValueError, TypeError):
            logger.debug(
                "Could not parse player_id for combat end check",
                player_id=player_id,
                npc_id=npc_id,
            )
            return
        existing_combat = await self.get_combat_service().get_combat_by_participant(player_uuid)
        if existing_combat:
            reason = "Invalid combat location - participants not in same room"
            logger.info(
                "Ending combat due to room mismatch",
                combat_id=existing_combat.combat_id,
                player_id=player_id,
                npc_id=npc_id,
                reason=reason,
            )
            await self.get_combat_service().end_combat(existing_combat.combat_id, reason)

    async def _setup_combat_uuids_and_mappings(
        self: _NPCCombatIntegrationValidationDeps,
        player_id: str,
        npc_id: str,
        room_id: str,
        first_engagement: bool,
    ) -> tuple[UUID, UUID]:
        """Convert string IDs to UUIDs and set up XP mappings."""
        try:
            uuid_mapping = self.get_uuid_mapping()
            attacker_uuid = uuid_mapping.convert_to_uuid(player_id)
            target_uuid = uuid_mapping.convert_to_uuid(npc_id)

            if not uuid_mapping.is_valid_uuid(npc_id):
                uuid_mapping.store_string_id_mapping(target_uuid, npc_id)

            await self.store_npc_xp_mapping_for_mixin(npc_id, target_uuid, room_id, player_id, first_engagement)

        except ValueError:
            attacker_uuid = uuid4()
            target_uuid = uuid4()
            logger.debug("Skipping UUID mapping storage - invalid NPC ID", npc_id=npc_id)

        return attacker_uuid, target_uuid

    def _setup_combat_uuids_npc_attacker(
        self: _NPCCombatIntegrationValidationDeps, npc_id: str, player_id: str
    ) -> tuple[UUID, UUID]:
        """Set up UUIDs for NPC-as-attacker combat (aggro). Returns (npc_uuid, player_uuid)."""
        try:
            uuid_mapping = self.get_uuid_mapping()
            attacker_uuid = uuid_mapping.convert_to_uuid(npc_id)
            target_uuid = uuid_mapping.convert_to_uuid(player_id)
            if not uuid_mapping.is_valid_uuid(npc_id):
                uuid_mapping.store_string_id_mapping(attacker_uuid, npc_id)
            return attacker_uuid, target_uuid
        except ValueError:
            return uuid4(), uuid4()

    async def store_npc_xp_mapping_for_mixin(
        self: _NPCCombatIntegrationValidationDeps,
        npc_id: str,
        target_uuid: UUID,
        room_id: str,
        player_id: str,
        first_engagement: bool,
    ) -> None:
        """Store NPC XP mapping and apply encounter lucidity effect if first engagement."""
        data_provider = self.get_data_provider()
        npc_definition: object | None = await data_provider.get_npc_definition(npc_id)
        logger.debug(
            "Retrieved NPC definition",
            npc_id=npc_id,
            has_definition=bool(npc_definition),
        )

        if npc_definition is not None and first_engagement:
            await self.get_lucidity_service().apply_encounter_lucidity_effect(
                player_id, npc_id, npc_definition, room_id
            )

        if npc_definition is not None:
            get_base_stats = getattr(npc_definition, "get_base_stats", None)
            base_stats = get_base_stats() if callable(get_base_stats) else None
            logger.debug(
                "Retrieved base stats",
                npc_id=npc_id,
                base_stats=base_stats,
            )
            if isinstance(base_stats, dict):
                stats_dict = cast(dict[str, object], base_stats)
                raw_xp: object = stats_dict.get("xp_value", 0)
                xp_value = _coerce_xp_mapping_value(raw_xp)
                self.get_uuid_mapping().store_xp_mapping(target_uuid, xp_value)
            else:
                logger.debug(
                    "Base stats is not a dict",
                    npc_id=npc_id,
                    base_stats_type=type(base_stats),
                )
        else:
            logger.debug(
                "NPC definition not found",
                npc_id=npc_id,
            )
