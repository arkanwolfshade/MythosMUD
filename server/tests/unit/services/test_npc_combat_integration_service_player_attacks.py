"""
Unit tests for NPC combat integration service - player-initiated combat paths.
"""

# pyright: reportPrivateUsage=false
# These tests patch NPCCombatIntegrationService underscore-prefixed collaborators; that is intentional.

import uuid
from typing import TYPE_CHECKING, cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from .test_npc_combat_integration_service import (
    integration_service,
    mock_async_persistence,
    mock_combat_service,
    mock_connection_manager,
)

_PYGTEST_SERVICE_FIXTURES: tuple[object, ...] = (
    integration_service,
    mock_async_persistence,
    mock_combat_service,
    mock_connection_manager,
)

if TYPE_CHECKING:
    from server.services.npc_combat_integration_service import NPCCombatIntegrationService

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which triggers this warning but is the standard pytest pattern
# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_with_existing_combat(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_player_attack_on_npc queues action when combat exists."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.npc_id = npc_id
    npc_instance.current_room_id = room_id
    npc_instance.is_alive = True
    mock_combat = MagicMock()
    mock_combat.combat_id = "combat_001"
    mock_get_combat = AsyncMock(return_value=mock_combat)
    mock_queue_action = AsyncMock(return_value=True)
    integration_service._combat_service.get_combat_by_participant = mock_get_combat
    integration_service._combat_service.queue_combat_action = mock_queue_action
    mock_data_provider = MagicMock()
    mock_data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    mock_data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    integration_service._data_provider = mock_data_provider
    result = await integration_service.handle_player_attack_on_npc(
        player_id, npc_id, room_id, action_type, damage, npc_instance
    )
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_login_grace_period_blocked(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_player_attack_on_npc blocks attack when player is in login grace period."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.is_alive = True

    with patch(
        "server.services.npc_combat_integration_service.is_player_attack_blocked_by_login_grace_period",
        return_value=True,
    ):
        result = await integration_service.handle_player_attack_on_npc(
            player_id, npc_id, room_id, action_type, damage, npc_instance
        )
        assert result is False


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_grace_period_check_fails(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_player_attack_on_npc continues when grace period check fails."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.npc_id = npc_id
    npc_instance.current_room = room_id
    npc_instance.is_alive = True

    with patch("server.services.npc_combat_integration_service.get_config") as mock_get_config:
        mock_get_config.side_effect = AttributeError("No config")

        # Setup mocks for successful attack path
        mock_data_provider = MagicMock()
        mock_data_provider.get_player_room_id = AsyncMock(return_value=room_id)
        mock_data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
        mock_data_provider.get_player_name = AsyncMock(return_value="TestPlayer")
        mock_data_provider.get_player_combat_data = AsyncMock(return_value={})
        mock_data_provider.get_npc_combat_data = MagicMock(return_value={})
        mock_data_provider.get_npc_definition = AsyncMock(return_value=None)
        integration_service._data_provider = mock_data_provider
        integration_service._combat_memory = MagicMock()
        integration_service._combat_memory.record_attack = MagicMock(return_value=True)
        integration_service._uuid_mapping = MagicMock()

        def _convert_to_uuid_random(_entity_id: str) -> uuid.UUID:
            return uuid.uuid4()

        integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=_convert_to_uuid_random)
        integration_service._uuid_mapping.is_valid_uuid = MagicMock(return_value=False)
        integration_service._uuid_mapping.store_string_id_mapping = MagicMock()
        integration_service._combat_service = MagicMock()
        integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=None)
        integration_service._combat_service.start_combat = AsyncMock()
        mock_combat_result = MagicMock()
        mock_combat_result.success = True
        integration_service._combat_service.process_attack = AsyncMock(return_value=mock_combat_result)
        integration_service._handlers = MagicMock()
        integration_service._handlers.handle_combat_result = AsyncMock(return_value=True)

        result = await integration_service.handle_player_attack_on_npc(
            player_id, npc_id, room_id, action_type, damage, npc_instance
        )
        assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_npc_not_found(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_player_attack_on_npc returns False when NPC not found."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=None)

    result = await integration_service.handle_player_attack_on_npc(
        player_id, npc_id, room_id, action_type, damage, None
    )
    assert result is False


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_error_handling(
    integration_service: "NPCCombatIntegrationService",
):
    """Test handle_player_attack_on_npc handles exceptions gracefully."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.is_alive = True

    # Make _validate_and_get_npc_instance raise an exception
    integration_service._validate_and_get_npc_instance = AsyncMock(side_effect=ValueError("Test error"))

    result = await integration_service.handle_player_attack_on_npc(
        player_id, npc_id, room_id, action_type, damage, npc_instance
    )
    assert result is False


@pytest.mark.asyncio
async def test_setup_combat_uuids_and_mappings_value_error(
    integration_service: "NPCCombatIntegrationService",
):
    """Test _setup_combat_uuids_and_mappings handles ValueError."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    first_engagement = True

    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=ValueError("Invalid UUID"))

    attacker_uuid, target_uuid = await integration_service._setup_combat_uuids_and_mappings(
        player_id, npc_id, room_id, first_engagement
    )
    assert attacker_uuid is not None
    assert target_uuid is not None


@pytest.mark.asyncio
async def test_setup_combat_uuids_and_mappings_valid_uuid(
    integration_service: "NPCCombatIntegrationService",
):
    """Test _setup_combat_uuids_and_mappings with valid UUID."""
    player_id = "player_001"
    npc_id = str(uuid.uuid4())  # Valid UUID
    room_id = "room_001"
    first_engagement = True

    integration_service._uuid_mapping = MagicMock()
    attacker_uuid_val = uuid.uuid4()
    target_uuid_val = uuid.uuid4()

    def _convert_to_uuid_by_string_id(entity_id: str) -> uuid.UUID:
        return attacker_uuid_val if entity_id == player_id else target_uuid_val

    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=_convert_to_uuid_by_string_id)
    integration_service._uuid_mapping.is_valid_uuid = MagicMock(return_value=True)

    attacker_uuid, target_uuid = await integration_service._setup_combat_uuids_and_mappings(
        player_id, npc_id, room_id, first_engagement
    )
    assert attacker_uuid == attacker_uuid_val
    assert target_uuid == target_uuid_val


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_no_definition(
    integration_service: "NPCCombatIntegrationService",
):
    """Test store_npc_xp_mapping_for_mixin when NPC definition is not found."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = True

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=None)
    mock_store_xp_mapping = MagicMock()
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.store_xp_mapping = mock_store_xp_mapping

    await integration_service.store_npc_xp_mapping_for_mixin(npc_id, target_uuid, room_id, player_id, first_engagement)
    mock_store_xp_mapping.assert_not_called()


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_non_dict_base_stats(
    integration_service: "NPCCombatIntegrationService",
):
    """Test store_npc_xp_mapping_for_mixin when base_stats is not a dict."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = False

    mock_npc_definition = MagicMock()
    mock_npc_definition.get_base_stats = MagicMock(return_value="not_a_dict")

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=mock_npc_definition)
    mock_store_xp_mapping = MagicMock()
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.store_xp_mapping = mock_store_xp_mapping

    await integration_service.store_npc_xp_mapping_for_mixin(npc_id, target_uuid, room_id, player_id, first_engagement)
    mock_store_xp_mapping.assert_not_called()


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_first_engagement(
    integration_service: "NPCCombatIntegrationService",
):
    """Test store_npc_xp_mapping_for_mixin applies lucidity effect on first engagement."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = True

    mock_npc_definition = MagicMock()
    mock_npc_definition.get_base_stats = MagicMock(return_value={"xp_value": 100})

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=mock_npc_definition)
    mock_apply_lucidity = AsyncMock()
    integration_service._lucidity = MagicMock()
    integration_service._lucidity.apply_encounter_lucidity_effect = mock_apply_lucidity
    mock_store_xp_mapping = MagicMock()
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.store_xp_mapping = mock_store_xp_mapping

    await integration_service.store_npc_xp_mapping_for_mixin(npc_id, target_uuid, room_id, player_id, first_engagement)
    mock_apply_lucidity.assert_called_once()
    mock_store_xp_mapping.assert_called_once_with(target_uuid, 100)


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_no_xp_value(
    integration_service: "NPCCombatIntegrationService",
):
    """Test store_npc_xp_mapping_for_mixin defaults to 0 when xp_value not in base_stats."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = False

    mock_npc_definition = MagicMock()
    mock_npc_definition.get_base_stats = MagicMock(return_value={})  # No xp_value key

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=mock_npc_definition)
    mock_store_xp_mapping = MagicMock()
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.store_xp_mapping = mock_store_xp_mapping

    await integration_service.store_npc_xp_mapping_for_mixin(npc_id, target_uuid, room_id, player_id, first_engagement)
    mock_store_xp_mapping.assert_called_once_with(target_uuid, 0)


@pytest.mark.asyncio
async def test_process_combat_attack_queue_failure(
    integration_service: "NPCCombatIntegrationService",
):
    """Test _process_combat_attack falls back to immediate execution when queuing fails."""
    player_id = "player_001"
    room_id = "room_001"
    attacker_uuid = uuid.uuid4()
    target_uuid = uuid.uuid4()
    damage = 10
    npc_instance = MagicMock()

    mock_combat = MagicMock()
    mock_combat.combat_id = "combat_001"
    mock_combat_result = MagicMock()
    mock_combat_result.success = True

    mock_process_attack = AsyncMock(return_value=mock_combat_result)
    integration_service._combat_service = MagicMock()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)
    integration_service._combat_service.queue_combat_action = AsyncMock(return_value=False)  # Queue fails
    integration_service._combat_service.process_attack = mock_process_attack

    with patch("server.app.lifespan.get_current_tick", return_value=1):
        result = cast(
            MagicMock,
            await integration_service._process_combat_attack(
                player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance
            ),
        )
        assert result == mock_combat_result
        mock_process_attack.assert_called_once()


@pytest.mark.asyncio
async def test_process_combat_attack_start_new_combat(
    integration_service: "NPCCombatIntegrationService",
):
    """Test _process_combat_attack starts new combat when none exists."""
    player_id = "player_001"
    room_id = "room_001"
    attacker_uuid = uuid.uuid4()
    target_uuid = uuid.uuid4()
    damage = 10
    npc_instance = MagicMock()

    mock_combat_result = MagicMock()
    mock_combat_result.success = True

    integration_service._combat_service = MagicMock()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=None)
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_name = AsyncMock(return_value="TestPlayer")
    integration_service._data_provider.get_player_combat_data = AsyncMock(return_value={})
    integration_service._data_provider.get_npc_combat_data = MagicMock(return_value={})
    mock_start_combat = AsyncMock()
    integration_service._combat_service.start_combat = mock_start_combat
    integration_service._combat_service.process_attack = AsyncMock(return_value=mock_combat_result)

    with patch("server.app.lifespan.get_current_tick", return_value=1):
        result = cast(
            MagicMock,
            await integration_service._process_combat_attack(
                player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance
            ),
        )
        assert result == mock_combat_result
        mock_start_combat.assert_called_once()


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_not_found(
    integration_service: "NPCCombatIntegrationService",
):
    """Test _validate_and_get_npc_instance returns None when NPC not found."""
    player_id = "player_001"
    npc_id = "npc_001"

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=None)

    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, None)
    assert result is None
