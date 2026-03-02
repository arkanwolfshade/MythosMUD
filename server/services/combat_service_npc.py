"""
NPC combat lookup and participant room resolution for CombatService.

Extracted from combat_service.py to keep module line count under limit.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast
from uuid import UUID

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType

if TYPE_CHECKING:
    from server.services.combat_service import CombatService


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
    if not svc or not hasattr(svc, "_uuid_mapping"):
        return None
    mapping = getattr(svc, "_uuid_mapping", None)
    if mapping is None or not hasattr(mapping, "get_uuid_for_string_id"):
        return None
    uuid_key = mapping.get_uuid_for_string_id(npc_id_str)
    if uuid_key is not None and uuid_key in combat.participants:
        return cast(UUID, uuid_key)
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
    if not svc or not hasattr(svc, "_uuid_mapping"):
        return None
    mapping = getattr(svc, "_uuid_mapping", None)
    if mapping is None or not hasattr(mapping, "get_uuid_for_string_id"):
        return None
    uuid_key = mapping.get_uuid_for_string_id(npc_id_str)
    if uuid_key is not None:
        return service.get_combat_id_for_npc_uuid(uuid_key)
    return None


def npc_in_combat_by_uuid_lookup(service: CombatService, npc_id: str) -> bool:
    """True if npc_id parses as UUID and that UUID is in combat."""
    try:
        npc_uuid = UUID(npc_id) if isinstance(npc_id, str) else npc_id
        return service.get_combat_id_for_npc_uuid(npc_uuid) is not None
    except (ValueError, TypeError, AttributeError):
        return False


def npc_in_combat_by_string_id_mapping(service: CombatService, npc_id: str) -> bool:
    """True if integration service mapping has a UUID for npc_id that is in combat."""
    svc = service.get_npc_combat_integration_service()
    if not svc or not hasattr(svc, "_uuid_mapping"):
        return False
    mapping = getattr(svc, "_uuid_mapping", None)
    if mapping is None or not hasattr(mapping, "get_uuid_for_string_id"):
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
    data_provider: Any,
    svc: Any,
    participant: CombatParticipant,
) -> str | None:
    """Resolve current room for an NPC participant via uuid_mapping and data_provider."""
    uuid_mapping = getattr(svc, "_uuid_mapping", None) if svc else None
    if not uuid_mapping or not hasattr(uuid_mapping, "get_original_string_id"):
        return None
    npc_id = uuid_mapping.get_original_string_id(participant.participant_id)
    if not npc_id:
        return None
    npc_instance = data_provider.get_npc_instance(npc_id)
    if not npc_instance:
        return None
    return getattr(npc_instance, "current_room", None)


async def get_participant_current_room(service: CombatService, participant: CombatParticipant) -> str | None:
    """Get current room ID for a combat participant (player or NPC)."""
    svc = service.get_npc_combat_integration_service()
    data_provider = getattr(svc, "_data_provider", None) if svc else None
    if not data_provider:
        return None
    if participant.participant_type == CombatParticipantType.PLAYER:
        result = await data_provider.get_player_room_id(str(participant.participant_id))
        return cast(str | None, result)
    return get_npc_participant_current_room(service, data_provider, svc, participant)
