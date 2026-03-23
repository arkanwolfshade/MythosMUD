"""
NPC combat lookup and participant room resolution for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Protocol, cast
from uuid import UUID

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType

if TYPE_CHECKING:
    from server.services.combat_service import CombatService


class UUIDMappingProtocol(Protocol):
    """Protocol for NPC string/UUID reverse mapping."""

    def get_uuid_for_string_id(self, string_id: str) -> UUID | None:
        """Resolve a string NPC id to its mapped UUID."""

    def get_original_string_id(self, uuid_id: UUID) -> str | None:
        """Resolve a mapped UUID back to its original string NPC id."""


class DataProviderProtocol(Protocol):
    """Protocol for room and NPC lookups used by combat helpers."""

    async def get_player_room_id(self, player_id: str) -> str | None:
        """Return current room id for a player id."""

    def get_npc_instance(self, npc_id: str) -> object | None:
        """Return NPC instance for a string NPC id."""


class NPCInstanceWithRoomProtocol(Protocol):
    """Protocol for NPC instances exposing current room."""

    current_room: str | None


def _get_uuid_mapping(svc: object | None) -> UUIDMappingProtocol | None:
    """Safely fetch UUID mapping from integration service."""
    if svc is None:
        return None
    mapping_obj = cast(object | None, getattr(svc, "_uuid_mapping", None))
    if mapping_obj is None:
        return None
    get_uuid_for_string_id = getattr(mapping_obj, "get_uuid_for_string_id", None)
    get_original_string_id = getattr(mapping_obj, "get_original_string_id", None)
    if not callable(get_uuid_for_string_id) or not callable(get_original_string_id):
        return None
    return cast(UUIDMappingProtocol, mapping_obj)


def _get_data_provider(svc: object | None) -> DataProviderProtocol | None:
    """Safely fetch data provider from integration service."""
    if svc is None:
        return None
    data_provider_obj = cast(object | None, getattr(svc, "_data_provider", None))
    if data_provider_obj is None:
        return None
    get_player_room_id = getattr(data_provider_obj, "get_player_room_id", None)
    get_npc_instance = getattr(data_provider_obj, "get_npc_instance", None)
    if not callable(get_player_room_id) or not callable(get_npc_instance):
        return None
    return cast(DataProviderProtocol, data_provider_obj)


def _iter_active_combats(service: CombatService) -> Mapping[UUID, CombatInstance]:
    """
    Return active combats map when available.

    Uses getattr to avoid direct protected-member access in this helper module.
    """
    active_combats = getattr(service, "_active_combats", None)
    if isinstance(active_combats, Mapping):
        return cast(Mapping[UUID, CombatInstance], active_combats)
    return {}


def sync_npc_participant_dp_after_spell_damage(service: CombatService, npc_id: str, new_dp: int) -> None:
    """Sync CombatParticipant.current_dp after spell damage to an NPC in combat."""
    combat_id = get_combat_id_for_npc(service, npc_id)
    if not combat_id:
        return
    combat = service.get_combat(combat_id)
    if not combat:
        return
    participant_id = resolve_npc_participant_id_in_combat(service, combat, npc_id)
    if participant_id is not None:
        participant = combat.participants.get(participant_id)
        if participant is not None:
            participant.current_dp = new_dp


def resolve_npc_participant_id_in_combat(service: CombatService, combat: CombatInstance, npc_id: str) -> UUID | None:
    """Resolve string npc_id to participant UUID in the given combat."""
    try:
        participant_id = UUID(str(npc_id))
        if participant_id in combat.participants:
            return participant_id
    except (ValueError, TypeError):
        pass
    return find_participant_uuid_by_string_id(service, combat, npc_id)


def find_participant_uuid_by_string_id(service: CombatService, combat: CombatInstance, npc_id_str: str) -> UUID | None:
    """Find participant UUID in combat by string npc_id via integration service mapping."""
    svc = service.get_npc_combat_integration_service()
    mapping = _get_uuid_mapping(svc)
    if mapping is None:
        return None
    uuid_key = mapping.get_uuid_for_string_id(npc_id_str)
    if uuid_key is not None and uuid_key in combat.participants:
        return uuid_key
    return None


def get_combat_by_participant(service: CombatService, participant_id: UUID) -> CombatInstance | None:
    """Get combat instance for a specific participant (player or NPC)."""
    combat_id = service.get_combat_id_for_participant(participant_id)
    return service.get_combat(combat_id) if combat_id else None


def get_combat_id_for_npc(service: CombatService, npc_id: UUID | str) -> UUID | None:
    """Return combat_id if this NPC is in combat, else None."""
    if isinstance(npc_id, UUID):
        return service.get_combat_id_for_npc_uuid(npc_id)
    try:
        npc_uuid = UUID(str(npc_id))
        return service.get_combat_id_for_npc_uuid(npc_uuid)
    except (ValueError, TypeError):
        pass
    return get_combat_id_for_npc_via_mapping(service, str(npc_id))


def get_combat_id_for_npc_via_mapping(service: CombatService, npc_id_str: str) -> UUID | None:
    """Resolve string npc_id to combat_id via integration service UUID mapping."""
    svc = service.get_npc_combat_integration_service()
    mapping = _get_uuid_mapping(svc)
    if mapping is None:
        return _fallback_find_combat_id_for_npc(service, npc_id_str)
    uuid_key = mapping.get_uuid_for_string_id(npc_id_str)
    if uuid_key is not None:
        combat_id = service.get_combat_id_for_npc_uuid(uuid_key)
        if combat_id is not None:
            return combat_id
    return _fallback_find_combat_id_for_npc(service, npc_id_str)


def _fallback_find_combat_id_for_npc(service: CombatService, npc_id_str: str) -> UUID | None:
    """
    Fallback combat lookup when uuid_mapping misses.

    This scans active combats and matches NPC participants by either:
    - participant_id string equality (for direct UUID-like ids), or
    - reverse lookup from participant UUID to original string npc_id.
    """
    svc = service.get_npc_combat_integration_service()
    mapping = _get_uuid_mapping(svc)
    for combat_id, combat in _iter_active_combats(service).items():
        for participant in combat.participants.values():
            if _participant_matches_npc_id(participant, npc_id_str, mapping):
                return combat_id
    return None


def _participant_matches_npc_id(
    participant: CombatParticipant,
    npc_id_str: str,
    mapping: UUIDMappingProtocol | None,
) -> bool:
    """True when participant maps to npc_id_str using direct or reverse mapping."""
    if participant.participant_type != CombatParticipantType.NPC:
        return False
    if str(participant.participant_id) == npc_id_str:
        return True
    if mapping is not None:
        original_id = mapping.get_original_string_id(participant.participant_id)
        return original_id == npc_id_str
    return False


def npc_in_combat_by_uuid_lookup(service: CombatService, npc_id: str) -> bool:
    """True if npc_id parses as UUID and that UUID is in combat."""
    try:
        npc_uuid = UUID(npc_id)
        return service.get_combat_id_for_npc_uuid(npc_uuid) is not None
    except (ValueError, TypeError, AttributeError):
        return False


def npc_in_combat_by_string_id_mapping(service: CombatService, npc_id: str) -> bool:
    """True if integration service mapping has a UUID for npc_id that is in combat."""
    svc = service.get_npc_combat_integration_service()
    mapping = _get_uuid_mapping(svc)
    if mapping is None:
        return False
    uuid_key = mapping.get_uuid_for_string_id(npc_id)
    return uuid_key is not None and service.get_combat_id_for_npc_uuid(uuid_key) is not None


def is_npc_in_combat_sync(service: CombatService, npc_id: str) -> bool:
    """Check if an NPC (by string id or UUID string) is currently in combat."""
    if npc_in_combat_by_uuid_lookup(service, npc_id):
        return True
    return npc_in_combat_by_string_id_mapping(service, npc_id)


def get_npc_participant_current_room(
    _service: CombatService,
    data_provider: DataProviderProtocol,
    svc: object | None,
    participant: CombatParticipant,
) -> str | None:
    """Resolve current room for an NPC participant via uuid_mapping and data_provider."""
    uuid_mapping = _get_uuid_mapping(svc)
    if uuid_mapping is None:
        return None
    npc_id = uuid_mapping.get_original_string_id(participant.participant_id)
    if not npc_id:
        return None
    npc_instance = data_provider.get_npc_instance(npc_id)
    if not npc_instance:
        return None
    current_room = getattr(cast(NPCInstanceWithRoomProtocol, npc_instance), "current_room", None)
    if current_room is None or isinstance(current_room, str):
        return current_room
    return None


async def get_participant_current_room(service: CombatService, participant: CombatParticipant) -> str | None:
    """Get current room ID for a combat participant (player or NPC)."""
    svc = service.get_npc_combat_integration_service()
    data_provider = _get_data_provider(svc)
    if not data_provider:
        return None
    if participant.participant_type == CombatParticipantType.PLAYER:
        return await data_provider.get_player_room_id(str(participant.participant_id))
    return get_npc_participant_current_room(service, data_provider, svc, participant)
