"""
Unit tests for NPC combat handlers.

Tests the NPCCombatHandlers class for combat result processing and NPC death handling.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_combat_handlers import NPCCombatHandlers

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_data_provider():
    """Create mock data provider."""
    provider = MagicMock()
    provider.get_player_name = AsyncMock(return_value="TestPlayer")
    return provider


@pytest.fixture
def mock_rewards():
    """Create mock rewards manager."""
    return MagicMock()


@pytest.fixture
def mock_combat_memory():
    """Create mock combat memory manager."""
    return MagicMock()


@pytest.fixture
def mock_lifecycle():
    """Create mock lifecycle manager."""
    return MagicMock()


@pytest.fixture
def mock_messaging_integration():
    """Create mock messaging integration."""
    integration = MagicMock()
    integration.broadcast_combat_attack = AsyncMock(return_value={"sent": 5})
    return integration


@pytest.fixture
def npc_combat_handlers(
    mock_data_provider, mock_rewards, mock_combat_memory, mock_lifecycle, mock_messaging_integration
):
    """Create NPCCombatHandlers instance."""
    return NPCCombatHandlers(
        mock_data_provider, mock_rewards, mock_combat_memory, mock_lifecycle, mock_messaging_integration
    )


@pytest.fixture
def mock_combat_result():
    """Create mock combat result."""
    result = MagicMock()
    result.success = True
    result.combat_ended = False
    result.combat_id = "combat_001"
    result.message = "Attack successful"
    return result


@pytest.fixture
def mock_npc_instance():
    """Create mock NPC instance."""
    npc = MagicMock()
    npc.name = "TestNPC"
    return npc


@pytest.mark.asyncio
async def test_handle_combat_result_success(
    npc_combat_handlers, mock_combat_result, mock_npc_instance, mock_messaging_integration
):
    """Test handle_combat_result handles successful attack."""
    handle_death = AsyncMock()
    result = await npc_combat_handlers.handle_combat_result(
        mock_combat_result, "player_001", "npc_001", "room_001", "punch", 10, mock_npc_instance, handle_death
    )
    assert result is True
    mock_messaging_integration.broadcast_combat_attack.assert_awaited_once()
    handle_death.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_combat_result_combat_ended(npc_combat_handlers, mock_combat_result, mock_npc_instance):
    """Test handle_combat_result handles combat end."""
    mock_combat_result.combat_ended = True
    handle_death = AsyncMock()
    with patch.object(npc_combat_handlers, "_handle_npc_death_on_combat_end", new_callable=AsyncMock) as mock_death:
        result = await npc_combat_handlers.handle_combat_result(
            mock_combat_result, "player_001", "npc_001", "room_001", "punch", 10, mock_npc_instance, handle_death
        )
        assert result is True
        mock_death.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_combat_result_broadcast_error(
    npc_combat_handlers, mock_combat_result, mock_npc_instance, mock_messaging_integration
):
    """Test handle_combat_result handles broadcast errors gracefully."""
    # Use ConnectionError which is one of the specific exceptions we catch
    mock_messaging_integration.broadcast_combat_attack = AsyncMock(side_effect=ConnectionError("Broadcast error"))
    handle_death = AsyncMock()
    # Should not raise
    result = await npc_combat_handlers.handle_combat_result(
        mock_combat_result, "player_001", "npc_001", "room_001", "punch", 10, mock_npc_instance, handle_death
    )
    assert result is True


@pytest.mark.asyncio
async def test_handle_combat_result_unsuccessful(npc_combat_handlers, mock_npc_instance):
    """Test handle_combat_result handles unsuccessful attack."""
    mock_combat_result = MagicMock()
    mock_combat_result.success = False
    handle_death = AsyncMock()
    result = await npc_combat_handlers.handle_combat_result(
        mock_combat_result, "player_001", "npc_001", "room_001", "punch", 0, mock_npc_instance, handle_death
    )
    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_death_on_combat_end(npc_combat_handlers, mock_combat_result):
    """Test _handle_npc_death_on_combat_end handles NPC death."""
    handle_death = AsyncMock()
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_manager = MagicMock()
        mock_manager.player_websockets = {}
        mock_instance.connection_manager = mock_manager
        mock_container.get_instance.return_value = mock_instance
        await npc_combat_handlers._handle_npc_death_on_combat_end(
            "player_001", "npc_001", "room_001", mock_combat_result, handle_death
        )
        handle_death.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_npc_death_on_combat_end_error(npc_combat_handlers, mock_combat_result):
    """Test _handle_npc_death_on_combat_end handles errors gracefully."""
    handle_death = AsyncMock(side_effect=ValueError("Death handler error"))
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_manager = MagicMock()
        mock_manager.player_websockets = {}
        mock_instance.connection_manager = mock_manager
        mock_container.get_instance.return_value = mock_instance
        # Should not raise
        await npc_combat_handlers._handle_npc_death_on_combat_end(
            "player_001", "npc_001", "room_001", mock_combat_result, handle_death
        )


@pytest.mark.asyncio
async def test_handle_npc_death(npc_combat_handlers, mock_data_provider, mock_rewards, mock_lifecycle):
    """Test handle_npc_death handles NPC death."""
    mock_npc_instance = MagicMock()
    mock_data_provider.get_npc_instance = MagicMock(return_value=mock_npc_instance)
    mock_data_provider.get_npc_definition = AsyncMock(return_value=None)
    mock_rewards.calculate_xp_reward = AsyncMock(return_value=100)
    mock_rewards.award_xp_to_killer = AsyncMock()
    mock_lifecycle.despawn_npc_safely = AsyncMock()
    npc_combat_handlers._data_provider = mock_data_provider
    npc_combat_handlers._rewards = mock_rewards
    npc_combat_handlers._lifecycle = mock_lifecycle
    npc_combat_handlers._combat_memory = MagicMock()
    result = await npc_combat_handlers.handle_npc_death("npc_001", "room_001", "player_001", "combat_001")
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_handle_npc_death_no_npc(npc_combat_handlers, mock_data_provider):
    """Test handle_npc_death handles non-existent NPC."""
    mock_data_provider.get_npc_instance = MagicMock(return_value=None)
    npc_combat_handlers._data_provider = mock_data_provider
    result = await npc_combat_handlers.handle_npc_death("npc_001", "room_001", "player_001", "combat_001")
    assert result is False


@pytest.mark.asyncio
async def test_handle_npc_death_error(npc_combat_handlers, mock_data_provider):
    """Test handle_npc_death handles errors gracefully."""
    mock_data_provider.get_npc_instance = MagicMock(side_effect=ValueError("Error"))
    npc_combat_handlers._data_provider = mock_data_provider
    # Should not raise
    result = await npc_combat_handlers.handle_npc_death("npc_001", "room_001", "player_001", "combat_001")
    assert result is False


def test_is_valid_uuid(npc_combat_handlers):
    """Test _is_valid_uuid validates UUID."""
    assert npc_combat_handlers._is_valid_uuid(str(uuid.uuid4())) is True
    assert npc_combat_handlers._is_valid_uuid("invalid") is False
