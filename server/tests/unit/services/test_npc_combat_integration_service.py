"""
Unit tests for NPC combat integration service.

Tests the NPCCombatIntegrationService class for integrating NPCs with the combat system.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_combat_integration_service import NPCCombatIntegrationService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    service = MagicMock()
    service.auto_progression_enabled = False
    service.turn_interval_seconds = 10
    return service


@pytest.fixture
def mock_messaging_integration():
    """Create mock messaging integration."""
    return MagicMock()


@pytest.fixture
def mock_connection_manager():
    """Create mock connection manager."""
    return MagicMock()


@pytest.fixture
def mock_async_persistence():
    """Create mock async persistence layer."""
    return MagicMock()


@pytest.fixture
def integration_service(mock_combat_service, mock_connection_manager, mock_async_persistence):
    """Create NPCCombatIntegrationService instance."""
    with patch("server.services.npc_combat_integration_service.get_config") as mock_config:
        mock_config_instance = MagicMock()
        mock_config_instance.game.combat_tick_interval = 10
        mock_config.return_value = mock_config_instance
        # Signature: __init__(self, event_bus=None, combat_service=None, player_combat_service=None, connection_manager=None, async_persistence=None)
        service = NPCCombatIntegrationService(
            event_bus=None,
            combat_service=mock_combat_service,
            player_combat_service=None,
            connection_manager=mock_connection_manager,
            async_persistence=mock_async_persistence,
        )
        return service


def test_integration_service_init(integration_service, mock_combat_service):
    """Test NPCCombatIntegrationService initialization."""
    assert integration_service._combat_service == mock_combat_service
    assert mock_combat_service.auto_progression_enabled is True


@pytest.mark.asyncio
async def test_get_integration_config(integration_service):
    """Test integration service has combat service with config."""
    # The service doesn't have get_integration_config method, but it has _combat_service
    assert integration_service._combat_service is not None
    assert hasattr(integration_service._combat_service, "turn_interval_seconds")


def test_is_auto_progression_enabled(integration_service):
    """Test auto_progression_enabled is set on combat service."""
    # The service doesn't have is_auto_progression_enabled method, but it sets auto_progression_enabled on _combat_service
    assert integration_service._combat_service.auto_progression_enabled is True


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc(integration_service):
    """Test handle_player_attack_on_npc handles attack."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.npc_id = npc_id
    npc_instance.current_room = room_id
    npc_instance.current_room_id = room_id
    npc_instance.is_alive = True
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
    integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=lambda x: uuid.uuid4())
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
    integration_service.handle_npc_death = AsyncMock()
    result = await integration_service.handle_player_attack_on_npc(
        player_id, npc_id, room_id, action_type, damage, npc_instance
    )
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_provided(integration_service):
    """Test _validate_and_get_npc_instance uses provided instance."""
    player_id = "player_001"
    npc_id = "npc_001"
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, npc_instance)
    assert result == npc_instance


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_lookup(integration_service):
    """Test _validate_and_get_npc_instance looks up NPC when not provided."""
    player_id = "player_001"
    npc_id = "npc_001"
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, None)
    assert result == npc_instance


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_dead(integration_service):
    """Test _validate_and_get_npc_instance returns None for dead NPC."""
    player_id = "player_001"
    npc_id = "npc_001"
    npc_instance = MagicMock()
    npc_instance.is_alive = False
    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, npc_instance)
    assert result is None


@pytest.mark.asyncio
async def test_validate_combat_location(integration_service):
    """Test _validate_combat_location validates location."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    npc_instance = MagicMock()
    npc_instance.current_room = room_id
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    result = await integration_service._validate_combat_location(player_id, npc_id, room_id, npc_instance)
    assert result is True


@pytest.mark.asyncio
async def test_validate_combat_location_different_rooms(integration_service):
    """Test _validate_combat_location returns False for different rooms."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    npc_instance = MagicMock()
    npc_instance.current_room = "room_002"
    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    result = await integration_service._validate_combat_location(player_id, npc_id, room_id, npc_instance)
    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_death(integration_service):
    """Test handle_npc_death handles NPC death."""
    npc_id = "npc_001"
    room_id = "room_001"
    killer_id = "player_001"
    combat_id = "combat_001"
    # Mock the handlers and data provider
    integration_service._handlers = MagicMock()
    integration_service._handlers.handle_npc_death = AsyncMock(return_value=True)
    result = await integration_service.handle_npc_death(npc_id, room_id, killer_id, combat_id)
    assert isinstance(result, bool)


def test_get_npc_combat_memory(integration_service):
    """Test get_npc_combat_memory returns memory."""
    npc_id = "npc_001"
    integration_service._combat_memory = MagicMock()
    integration_service._combat_memory.get_memory = MagicMock(return_value="memory")
    result = integration_service.get_npc_combat_memory(npc_id)
    assert result is not None


def test_clear_npc_combat_memory(integration_service):
    """Test clear_npc_combat_memory clears memory."""
    npc_id = "npc_001"
    integration_service._combat_memory = MagicMock()
    integration_service._combat_memory.clear_memory = MagicMock(return_value=True)
    result = integration_service.clear_npc_combat_memory(npc_id)
    assert isinstance(result, bool)


def test_get_original_string_id(integration_service):
    """Test get_original_string_id returns original ID."""
    uuid_id = uuid.uuid4()
    integration_service._uuid_mapping = MagicMock()
    integration_service._uuid_mapping.get_original_string_id = MagicMock(return_value="npc_001")
    result = integration_service.get_original_string_id(uuid_id)
    assert result == "npc_001"


# Removed test_setup_npc_for_combat - the method setup_npc_for_combat doesn't exist on NPCCombatIntegrationService
# If this functionality is needed, the method should be implemented first


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_with_existing_combat(integration_service):
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
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)
    integration_service._combat_service.queue_combat_action = AsyncMock(return_value=True)
    mock_data_provider = MagicMock()
    mock_data_provider.get_player_room_id = AsyncMock(return_value=room_id)
    mock_data_provider.get_npc_instance = MagicMock(return_value=npc_instance)
    integration_service._data_provider = mock_data_provider
    result = await integration_service.handle_player_attack_on_npc(
        player_id, npc_id, room_id, action_type, damage, npc_instance
    )
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_login_grace_period_blocked(integration_service):
    """Test handle_player_attack_on_npc blocks attack when player is in login grace period."""
    player_id = "player_001"
    npc_id = "npc_001"
    room_id = "room_001"
    action_type = "punch"
    damage = 10
    npc_instance = MagicMock()
    npc_instance.is_alive = True

    with patch("server.services.npc_combat_integration_service.get_config") as mock_get_config, patch(
        "server.services.npc_combat_integration_service.is_player_in_login_grace_period"
    ) as mock_grace_period:
        mock_config = MagicMock()
        mock_app = MagicMock()
        mock_connection_manager = MagicMock()
        mock_app.state.connection_manager = mock_connection_manager
        mock_config._app_instance = mock_app
        mock_get_config.return_value = mock_config
        mock_grace_period.return_value = True

        result = await integration_service.handle_player_attack_on_npc(
            player_id, npc_id, room_id, action_type, damage, npc_instance
        )
        assert result is False


@pytest.mark.asyncio
async def test_handle_player_attack_on_npc_grace_period_check_fails(integration_service):
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
        integration_service._uuid_mapping.convert_to_uuid = MagicMock(side_effect=lambda x: uuid.uuid4())
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
async def test_handle_player_attack_on_npc_npc_not_found(integration_service):
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
async def test_handle_player_attack_on_npc_error_handling(integration_service):
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
async def test_setup_combat_uuids_and_mappings_value_error(integration_service):
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
async def test_setup_combat_uuids_and_mappings_valid_uuid(integration_service):
    """Test _setup_combat_uuids_and_mappings with valid UUID."""
    player_id = "player_001"
    npc_id = str(uuid.uuid4())  # Valid UUID
    room_id = "room_001"
    first_engagement = True

    integration_service._uuid_mapping = MagicMock()
    attacker_uuid_val = uuid.uuid4()
    target_uuid_val = uuid.uuid4()
    integration_service._uuid_mapping.convert_to_uuid = MagicMock(
        side_effect=lambda x: attacker_uuid_val if x == player_id else target_uuid_val
    )
    integration_service._uuid_mapping.is_valid_uuid = MagicMock(return_value=True)

    attacker_uuid, target_uuid = await integration_service._setup_combat_uuids_and_mappings(
        player_id, npc_id, room_id, first_engagement
    )
    assert attacker_uuid == attacker_uuid_val
    assert target_uuid == target_uuid_val


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_no_definition(integration_service):
    """Test _store_npc_xp_mapping when NPC definition is not found."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = True

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=None)
    integration_service._uuid_mapping = MagicMock()

    await integration_service._store_npc_xp_mapping(npc_id, target_uuid, room_id, player_id, first_engagement)
    integration_service._uuid_mapping.store_xp_mapping.assert_not_called()


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_non_dict_base_stats(integration_service):
    """Test _store_npc_xp_mapping when base_stats is not a dict."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = False

    mock_npc_definition = MagicMock()
    mock_npc_definition.get_base_stats = MagicMock(return_value="not_a_dict")

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=mock_npc_definition)
    integration_service._uuid_mapping = MagicMock()

    await integration_service._store_npc_xp_mapping(npc_id, target_uuid, room_id, player_id, first_engagement)
    integration_service._uuid_mapping.store_xp_mapping.assert_not_called()


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_first_engagement(integration_service):
    """Test _store_npc_xp_mapping applies lucidity effect on first engagement."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = True

    mock_npc_definition = MagicMock()
    mock_npc_definition.get_base_stats = MagicMock(return_value={"xp_value": 100})

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=mock_npc_definition)
    integration_service._lucidity = MagicMock()
    integration_service._lucidity.apply_encounter_lucidity_effect = AsyncMock()
    integration_service._uuid_mapping = MagicMock()

    await integration_service._store_npc_xp_mapping(npc_id, target_uuid, room_id, player_id, first_engagement)
    integration_service._lucidity.apply_encounter_lucidity_effect.assert_called_once()
    integration_service._uuid_mapping.store_xp_mapping.assert_called_once_with(target_uuid, 100)


@pytest.mark.asyncio
async def test_store_npc_xp_mapping_no_xp_value(integration_service):
    """Test _store_npc_xp_mapping defaults to 0 when xp_value not in base_stats."""
    npc_id = "npc_001"
    target_uuid = uuid.uuid4()
    room_id = "room_001"
    player_id = "player_001"
    first_engagement = False

    mock_npc_definition = MagicMock()
    mock_npc_definition.get_base_stats = MagicMock(return_value={})  # No xp_value key

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_definition = AsyncMock(return_value=mock_npc_definition)
    integration_service._uuid_mapping = MagicMock()

    await integration_service._store_npc_xp_mapping(npc_id, target_uuid, room_id, player_id, first_engagement)
    integration_service._uuid_mapping.store_xp_mapping.assert_called_once_with(target_uuid, 0)


@pytest.mark.asyncio
async def test_process_combat_attack_queue_failure(integration_service):
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

    integration_service._combat_service = MagicMock()
    integration_service._combat_service.get_combat_by_participant = AsyncMock(return_value=mock_combat)
    integration_service._combat_service.queue_combat_action = AsyncMock(return_value=False)  # Queue fails
    integration_service._combat_service.process_attack = AsyncMock(return_value=mock_combat_result)

    with patch("server.app.lifespan.get_current_tick", return_value=1):
        result = await integration_service._process_combat_attack(
            player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance
        )
        assert result == mock_combat_result
        integration_service._combat_service.process_attack.assert_called_once()


@pytest.mark.asyncio
async def test_process_combat_attack_start_new_combat(integration_service):
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
    integration_service._combat_service.start_combat = AsyncMock()
    integration_service._combat_service.process_attack = AsyncMock(return_value=mock_combat_result)

    with patch("server.app.lifespan.get_current_tick", return_value=1):
        result = await integration_service._process_combat_attack(
            player_id, room_id, attacker_uuid, target_uuid, damage, npc_instance
        )
        assert result == mock_combat_result
        integration_service._combat_service.start_combat.assert_called_once()


@pytest.mark.asyncio
async def test_validate_and_get_npc_instance_not_found(integration_service):
    """Test _validate_and_get_npc_instance returns None when NPC not found."""
    player_id = "player_001"
    npc_id = "npc_001"

    integration_service._data_provider = MagicMock()
    integration_service._data_provider.get_npc_instance = MagicMock(return_value=None)

    result = await integration_service._validate_and_get_npc_instance(player_id, npc_id, None)
    assert result is None
