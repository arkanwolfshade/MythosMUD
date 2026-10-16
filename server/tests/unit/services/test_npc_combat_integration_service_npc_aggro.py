"""
Unit tests for NPC combat integration service - NPC-initiated aggro combat paths.
"""

# pyright: reportPrivateUsage=false
# These tests patch NPCCombatIntegrationService underscore-prefixed collaborators; that is intentional.

import uuid
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from .test_npc_combat_integration_service import (
    integration_service,
    mock_async_persistence,
    mock_combat_service,
    mock_connection_manager,
)

if TYPE_CHECKING:
    from server.services.npc_combat_integration_service import NPCCombatIntegrationService

# pylint: disable=redefined-outer-name  # pytest injects fixtures by parameter name
# pylint: disable=protected-access  # tests assert on service internals

# Pytest registers imported @pytest.fixture callables; the tuple keeps imports "used" for
# basedpyright/Ruff without changing fixture registration names.
_PYGTEST_SERVICE_FIXTURES: tuple[object, ...] = (
    integration_service,
    mock_async_persistence,
    mock_combat_service,
    mock_connection_manager,
)


def _wire_npc_aggro_mocks(
    service: "NPCCombatIntegrationService",
    *,
    npc_id: str,
    room_id: str,
    npc_definition: object | None,
) -> tuple[MagicMock, AsyncMock, AsyncMock]:
    """Wire the service so handle_npc_attack_on_player reaches the damage step with no existing combat.

    Returns (npc_instance, start_combat mock, process_attack mock).
    """
    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    npc_instance.is_alive = True

    # Configure data provider for player and NPC data
    mock_data_provider = MagicMock()
    mock_data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    mock_data_provider.get_npc_definition = AsyncMock(return_value=npc_definition)
    mock_data_provider.get_player_name = AsyncMock(return_value="TestPlayer")
    mock_data_provider.get_npc_combat_data = MagicMock(return_value={})
    mock_data_provider.get_player_combat_data = AsyncMock(return_value={})
    service._data_provider = mock_data_provider

    # UUID mapping for NPC attacker and player target
    npc_uuid = uuid.uuid4()
    player_uuid = uuid.uuid4()
    service._uuid_mapping = MagicMock()

    def _mock_convert_to_uuid(entity_id: str) -> uuid.UUID:
        return npc_uuid if entity_id == npc_id else player_uuid

    service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=_mock_convert_to_uuid)
    service._uuid_mapping.is_valid_uuid = MagicMock(return_value=False)
    service._uuid_mapping.store_string_id_mapping = MagicMock()

    # Combat service: no existing combat, start new combat and process attack
    mock_combat_result = MagicMock()
    mock_combat_result.success = True
    mock_start_combat = AsyncMock()
    mock_process_attack = AsyncMock(return_value=mock_combat_result)
    service._combat_service = MagicMock()
    service._combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    service._combat_service.start_combat = mock_start_combat
    service._combat_service.process_attack = mock_process_attack

    # Skip full location validation details here; covered in dedicated tests
    service._validate_combat_location = AsyncMock(return_value=True)
    return npc_instance, mock_start_combat, mock_process_attack


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_happy_path(integration_service: "NPCCombatIntegrationService"):
    """Test handle_npc_attack_on_player starts combat and processes attack on happy path."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"
    attack_damage = 10

    npc_instance, mock_start_combat, mock_process_attack = _wire_npc_aggro_mocks(
        integration_service, npc_id=npc_id, room_id=room_id, npc_definition=None
    )

    with patch("server.services.npc_combat_integration_combat_mixin.get_current_tick", return_value=1):
        result = await integration_service.handle_npc_attack_on_player(
            npc_id=npc_id,
            target_id=target_id,
            room_id=room_id,
            attack_damage=attack_damage,
            npc_instance=npc_instance,
        )

    assert result is True
    mock_start_combat.assert_awaited_once()
    mock_process_attack.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_applies_encounter_lucidity_once(
    integration_service: "NPCCombatIntegrationService",
):
    """An aggro-started fight shocks the target once on first sight, not again on later attacks."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"
    npc_definition = MagicMock()

    npc_instance, _start, _process = _wire_npc_aggro_mocks(
        integration_service, npc_id=npc_id, room_id=room_id, npc_definition=npc_definition
    )
    apply_effect = AsyncMock()
    integration_service._lucidity = MagicMock()
    integration_service._lucidity.apply_encounter_lucidity_effect = apply_effect

    with patch("server.services.npc_combat_integration_combat_mixin.get_current_tick", return_value=1):
        for _ in range(2):
            attacked = await integration_service.handle_npc_attack_on_player(
                npc_id=npc_id,
                target_id=target_id,
                room_id=room_id,
                attack_damage=10,
                npc_instance=npc_instance,
            )
            assert attacked is True

    apply_effect.assert_awaited_once_with(target_id, npc_id, npc_definition, room_id)


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_grace_period_blocked(integration_service: "NPCCombatIntegrationService"):
    """Test handle_npc_attack_on_player blocks attack when player is in login grace period."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    with patch(
        "server.services.npc_combat_integration_service.is_npc_attack_on_player_blocked_by_login_grace_period",
        return_value=True,
    ):
        result = await integration_service.handle_npc_attack_on_player(
            npc_id=npc_id,
            target_id=target_id,
            room_id=room_id,
            attack_damage=10,
            npc_instance=None,
        )
        assert result is False


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_npc_not_found(integration_service: "NPCCombatIntegrationService"):
    """Test handle_npc_attack_on_player returns False when NPC instance cannot be found."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=None)

    result = await integration_service.handle_npc_attack_on_player(
        npc_id=npc_id,
        target_id=target_id,
        room_id=room_id,
        attack_damage=10,
        npc_instance=None,
    )

    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_npc_dead(integration_service: "NPCCombatIntegrationService"):
    """Test handle_npc_attack_on_player returns False when NPC is dead."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    npc_instance = MagicMock()
    npc_instance.is_alive = False
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)

    result = await integration_service.handle_npc_attack_on_player(
        npc_id=npc_id,
        target_id=target_id,
        room_id=room_id,
        attack_damage=10,
        npc_instance=None,
    )

    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_invalid_location(integration_service: "NPCCombatIntegrationService"):
    """Test handle_npc_attack_on_player returns False when combat location is invalid."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    npc_instance = MagicMock()
    npc_instance.is_alive = True
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)

    integration_service._validate_combat_location = AsyncMock(return_value=False)
    mock_start_combat = AsyncMock()
    combat_id = uuid.uuid4()
    integration_service._combat_service = MagicMock()
    integration_service._combat_service.start_combat = mock_start_combat
    integration_service._combat_service.get_combat_by_participant = AsyncMock(
        return_value=MagicMock(combat_id=combat_id)
    )
    mock_remove_participant: AsyncMock = AsyncMock()
    integration_service._combat_service.remove_participant = mock_remove_participant

    result = await integration_service.handle_npc_attack_on_player(
        npc_id=npc_id,
        target_id=target_id,
        room_id=room_id,
        attack_damage=10,
        npc_instance=None,
    )

    assert result is False
    mock_start_combat.assert_not_awaited()
    mock_remove_participant.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_no_combat_service(integration_service: "NPCCombatIntegrationService"):
    """Test handle_npc_attack_on_player returns False when combat service is missing."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    npc_instance.is_alive = True
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)

    object.__setattr__(integration_service, "_combat_service", None)

    integration_service._validate_combat_location = AsyncMock(return_value=True)

    result = await integration_service.handle_npc_attack_on_player(
        npc_id=npc_id,
        target_id=target_id,
        room_id=room_id,
        attack_damage=10,
        npc_instance=None,
    )

    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_existing_combat_with_same_npc(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_npc_attack_on_player returns True when combat already exists with same NPC."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    npc_instance.is_alive = True

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    integration_service._validate_combat_location = AsyncMock(return_value=True)

    npc_uuid = uuid.uuid4()
    player_uuid = uuid.uuid4()
    integration_service._setup_combat_uuids_npc_attacker = MagicMock(
        return_value=(npc_uuid, player_uuid),
    )

    mock_combat = MagicMock()
    mock_combat.participants = [npc_uuid]

    integration_service._combat_service = MagicMock()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    result = await integration_service.handle_npc_attack_on_player(
        npc_id=npc_id,
        target_id=target_id,
        room_id=room_id,
        attack_damage=10,
        npc_instance=None,
    )

    assert result is True


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_existing_combat_with_other_npc(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_npc_attack_on_player returns False when player is in combat with different NPC."""
    npc_id = "npc_001"
    target_id = str(uuid.uuid4())
    room_id = "room_001"

    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    npc_instance.is_alive = True

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    integration_service._validate_combat_location = AsyncMock(return_value=True)

    npc_uuid = uuid.uuid4()
    other_npc_uuid = uuid.uuid4()
    player_uuid = uuid.uuid4()
    integration_service._setup_combat_uuids_npc_attacker = MagicMock(
        return_value=(npc_uuid, player_uuid),
    )

    mock_combat = MagicMock()
    mock_combat.participants = [other_npc_uuid]

    integration_service._combat_service = MagicMock()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)

    result = await integration_service.handle_npc_attack_on_player(
        npc_id=npc_id,
        target_id=target_id,
        room_id=room_id,
        attack_damage=10,
        npc_instance=None,
    )

    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_attack_on_player_skips_already_dead_target(
    integration_service: "NPCCombatIntegrationService",
):
    """ValueError from combat path when player is dead must not log as error."""
    target_id = str(uuid.uuid4())
    with patch(
        "server.services.npc_combat_integration_service.is_npc_attack_on_player_blocked_by_login_grace_period",
        return_value=False,
    ):
        integration_service._run_npc_attack_on_player_after_grace = AsyncMock(  # type: ignore[method-assign]
            side_effect=ValueError("Target is already dead")
        )
        result = await integration_service.handle_npc_attack_on_player(
            npc_id="npc_001",
            target_id=target_id,
            room_id="room_1",
            attack_damage=10,
        )
    assert result is False


def test_setup_combat_uuids_npc_attacker_valid(integration_service: "NPCCombatIntegrationService"):
    """Test _setup_combat_uuids_npc_attacker with valid UUID mapping."""
    npc_id = "npc_001"
    player_id = "player_001"

    npc_uuid = uuid.uuid4()
    player_uuid = uuid.uuid4()

    integration_service._uuid_mapping = MagicMock()

    def _mock_convert_to_uuid(entity_id: str) -> uuid.UUID:
        return npc_uuid if entity_id == npc_id else player_uuid

    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=_mock_convert_to_uuid)
    integration_service._uuid_mapping.is_valid_uuid = MagicMock(return_value=False)
    mock_store_string_id_mapping = MagicMock()
    integration_service._uuid_mapping.store_string_id_mapping = mock_store_string_id_mapping

    attacker_uuid, target_uuid = integration_service._setup_combat_uuids_npc_attacker(npc_id, player_id)

    assert attacker_uuid == npc_uuid
    assert target_uuid == player_uuid
    mock_store_string_id_mapping.assert_called_once_with(attacker_uuid, npc_id)


def test_setup_combat_uuids_npc_attacker_value_error(integration_service: "NPCCombatIntegrationService"):
    """Test _setup_combat_uuids_npc_attacker falls back to random UUIDs on ValueError."""
    npc_id = "npc_001"
    player_id = "player_001"

    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=ValueError("Invalid UUID"))

    attacker_uuid, target_uuid = integration_service._setup_combat_uuids_npc_attacker(npc_id, player_id)

    assert isinstance(attacker_uuid, uuid.UUID)
    assert isinstance(target_uuid, uuid.UUID)
