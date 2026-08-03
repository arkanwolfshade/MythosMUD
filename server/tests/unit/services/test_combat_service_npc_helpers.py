"""Unit tests for combat_service_npc helper functions."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.services.combat_service_npc import (
    find_participant_uuid_by_string_id,
    get_combat_by_participant,
    get_combat_id_for_npc,
    get_combat_id_for_npc_via_mapping,
    get_participant_current_room,
    is_npc_in_combat_sync,
    npc_in_combat_by_string_id_mapping,
    npc_in_combat_by_uuid_lookup,
    resolve_npc_participant_id_in_combat,
    sync_npc_participant_dp_after_spell_damage,
)


@pytest.fixture
def combat_service():
    service = MagicMock()
    service.get_combat = MagicMock()
    service.get_combat_id_for_participant = MagicMock()
    service.get_combat_id_for_npc_uuid = MagicMock()
    service.get_npc_combat_integration_service = MagicMock(return_value=None)
    service._active_combats = {}
    return service


def test_get_combat_id_for_npc_uuid(combat_service):
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    combat_service.get_combat_id_for_npc_uuid = MagicMock(return_value=combat_id)
    assert get_combat_id_for_npc(combat_service, npc_uuid) == combat_id


def test_get_combat_id_for_npc_string_uuid(combat_service):
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    combat_service.get_combat_id_for_npc_uuid = MagicMock(return_value=combat_id)
    assert get_combat_id_for_npc(combat_service, str(npc_uuid)) == combat_id


def test_get_combat_id_for_npc_via_mapping(combat_service):
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    mapping = MagicMock()
    mapping.get_uuid_for_string_id = MagicMock(return_value=npc_uuid)
    integration = MagicMock()
    integration._uuid_mapping = mapping
    combat_service.get_npc_combat_integration_service = MagicMock(return_value=integration)
    combat_service.get_combat_id_for_npc_uuid = MagicMock(return_value=combat_id)
    assert get_combat_id_for_npc_via_mapping(combat_service, "cultist_1") == combat_id


def test_resolve_npc_participant_id_in_combat_by_uuid(combat_service):
    npc_uuid = uuid.uuid4()
    combat = CombatInstance(
        combat_id=uuid.uuid4(),
        room_id="room_1",
        participants={
            npc_uuid: CombatParticipant(
                participant_id=npc_uuid,
                participant_type=CombatParticipantType.NPC,
                name="Ghoul",
                current_dp=10,
                max_dp=10,
                dexterity=5,
                is_active=True,
            )
        },
    )
    assert resolve_npc_participant_id_in_combat(combat_service, combat, str(npc_uuid)) == npc_uuid


def test_find_participant_uuid_by_string_id(combat_service):
    npc_uuid = uuid.uuid4()
    combat = CombatInstance(combat_id=uuid.uuid4(), room_id="room_1", participants={npc_uuid: MagicMock()})
    mapping = MagicMock()
    mapping.get_uuid_for_string_id = MagicMock(return_value=npc_uuid)
    integration = MagicMock()
    integration._uuid_mapping = mapping
    combat_service.get_npc_combat_integration_service = MagicMock(return_value=integration)
    assert find_participant_uuid_by_string_id(combat_service, combat, "ghoul_1") == npc_uuid


def test_get_combat_by_participant(combat_service):
    participant_id = uuid.uuid4()
    combat_id = uuid.uuid4()
    combat = CombatInstance(combat_id=combat_id, room_id="room_1", participants={})
    combat_service.get_combat_id_for_participant = MagicMock(return_value=combat_id)
    combat_service.get_combat = MagicMock(return_value=combat)
    assert get_combat_by_participant(combat_service, participant_id) is combat


def test_sync_npc_participant_dp_after_spell_damage(combat_service):
    npc_uuid = uuid.uuid4()
    combat_id = uuid.uuid4()
    participant = CombatParticipant(
        participant_id=npc_uuid,
        participant_type=CombatParticipantType.NPC,
        name="Ghoul",
        current_dp=20,
        max_dp=20,
        dexterity=5,
        is_active=True,
    )
    combat = CombatInstance(combat_id=combat_id, room_id="room_1", participants={npc_uuid: participant})
    combat_service.get_combat = MagicMock(return_value=combat)
    with patch(
        "server.services.combat_service_npc.get_combat_id_for_npc",
        return_value=combat_id,
    ):
        sync_npc_participant_dp_after_spell_damage(combat_service, str(npc_uuid), 5)
    assert participant.current_dp == 5


def test_npc_in_combat_by_uuid_lookup(combat_service):
    npc_uuid = uuid.uuid4()
    combat_service.get_combat_id_for_npc_uuid = MagicMock(return_value=uuid.uuid4())
    assert npc_in_combat_by_uuid_lookup(combat_service, str(npc_uuid)) is True
    assert npc_in_combat_by_uuid_lookup(combat_service, "not-a-uuid") is False


def test_npc_in_combat_by_string_id_mapping(combat_service):
    npc_uuid = uuid.uuid4()
    mapping = MagicMock()
    mapping.get_uuid_for_string_id = MagicMock(return_value=npc_uuid)
    integration = MagicMock()
    integration._uuid_mapping = mapping
    combat_service.get_npc_combat_integration_service = MagicMock(return_value=integration)
    combat_service.get_combat_id_for_npc_uuid = MagicMock(return_value=uuid.uuid4())
    assert npc_in_combat_by_string_id_mapping(combat_service, "ghoul_1") is True


def test_is_npc_in_combat_sync(combat_service):
    combat_service._active_combats = {}
    assert is_npc_in_combat_sync(combat_service, "unknown_npc") is False


@pytest.mark.asyncio
async def test_get_participant_current_room_player(combat_service):
    player_id = uuid.uuid4()
    participant = CombatParticipant(
        participant_id=player_id,
        participant_type=CombatParticipantType.PLAYER,
        name="Hero",
        current_dp=50,
        max_dp=50,
        dexterity=10,
        is_active=True,
    )
    data_provider = MagicMock()
    data_provider.get_player_room_id = AsyncMock(return_value="room_1")
    integration = MagicMock()
    integration._data_provider = data_provider
    combat_service.get_npc_combat_integration_service = MagicMock(return_value=integration)
    room = await get_participant_current_room(combat_service, participant)
    assert room == "room_1"


def test_get_combat_id_for_npc_invalid_string(combat_service):
    combat_service.get_npc_combat_integration_service = MagicMock(return_value=None)
    combat_service._active_combats = {}
    assert get_combat_id_for_npc(combat_service, "not-a-valid-uuid") is None


def test_sync_npc_dp_no_combat_returns_early(combat_service):
    combat_service.get_combat = MagicMock()
    with patch(
        "server.services.combat_service_npc.get_combat_id_for_npc",
        return_value=None,
    ):
        sync_npc_participant_dp_after_spell_damage(combat_service, "missing", 1)
    combat_service.get_combat.assert_not_called()
