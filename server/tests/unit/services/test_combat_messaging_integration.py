"""
Unit tests for combat messaging integration.

Tests the CombatMessagingIntegration class for integrating combat messages
with the real-time messaging system.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.combat_messaging_integration import CombatMessagingIntegration

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_connection_manager():
    """Create mock connection manager."""
    manager = MagicMock()
    manager.broadcast_to_room = AsyncMock(return_value={"sent": 5, "failed": 0})
    manager.send_personal_message = AsyncMock(return_value={"sent": True})
    return manager


@pytest.fixture
def messaging_integration(mock_connection_manager):
    """Create CombatMessagingIntegration instance."""
    return CombatMessagingIntegration(connection_manager=mock_connection_manager)


def test_messaging_integration_init(messaging_integration, mock_connection_manager):
    """Test CombatMessagingIntegration initialization."""
    assert messaging_integration.connection_manager == mock_connection_manager


def test_messaging_integration_init_no_connection_manager():
    """Test CombatMessagingIntegration initialization without connection manager."""
    integration = CombatMessagingIntegration(connection_manager=None)
    assert integration._connection_manager is None


def test_connection_manager_property_lazy_load(messaging_integration):
    """Test connection_manager property lazy loads from container."""
    messaging_integration._connection_manager = None
    mock_manager = MagicMock()
    with patch.object(messaging_integration, "_resolve_connection_manager_from_container", return_value=mock_manager):
        result = messaging_integration.connection_manager
        assert result == mock_manager


def test_resolve_connection_manager_from_container(messaging_integration):
    """Test _resolve_connection_manager_from_container resolves manager."""
    mock_manager = MagicMock()
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.connection_manager = mock_manager
        mock_container.get_instance.return_value = mock_instance
        result = messaging_integration._resolve_connection_manager_from_container()
        assert result == mock_manager


def test_resolve_connection_manager_from_container_no_manager(messaging_integration):
    """Test _resolve_connection_manager_from_container raises when no manager."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.connection_manager = None
        mock_container.get_instance.return_value = mock_instance
        with pytest.raises(RuntimeError, match="not available"):
            messaging_integration._resolve_connection_manager_from_container()


def test_resolve_connection_manager_from_container_error(messaging_integration):
    """Test _resolve_connection_manager_from_container handles errors."""
    with patch("server.container.ApplicationContainer.get_instance", side_effect=ImportError("No container")):
        with pytest.raises(RuntimeError):
            messaging_integration._resolve_connection_manager_from_container()


@pytest.mark.asyncio
async def test_broadcast_combat_start(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_start broadcasts combat start event."""
    result = await messaging_integration.broadcast_combat_start("room_001", "Attacker", "Target", "combat_001")
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_attack(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_attack broadcasts attack event."""
    result = await messaging_integration.broadcast_combat_attack(
        "room_001", "Attacker", "Target", 10, "punch", "combat_001", "attacker_001"
    )
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()
    mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_attack_personal_message_error(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_attack handles personal message errors gracefully."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=ConnectionError("Connection error"))
    # Should not raise
    result = await messaging_integration.broadcast_combat_attack(
        "room_001", "Attacker", "Target", 10, "punch", "combat_001", "attacker_001"
    )
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_broadcast_combat_death(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_death broadcasts death event."""
    result = await messaging_integration.broadcast_combat_death("room_001", "NPC", 100, "combat_001")
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_ended(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_ended broadcasts combat ended event."""
    # Note: broadcast_combat_ended doesn't exist, using broadcast_combat_end instead
    result = await messaging_integration.broadcast_combat_end("room_001", "combat_001", None)
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_end(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_end broadcasts combat end event."""
    result = await messaging_integration.broadcast_combat_end("room_001", "combat_001", "victory")
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_error(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_error sends error to player."""
    mock_connection_manager.send_personal_message = AsyncMock(return_value={"sent": True})
    result = await messaging_integration.broadcast_combat_error("room_001", "Error message", "player_001")
    # Method returns delivery_status, not necessarily a dict
    assert result is not None
    mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_player_mortally_wounded(messaging_integration, mock_connection_manager):
    """Test broadcast_player_mortally_wounded broadcasts message."""
    result = await messaging_integration.broadcast_player_mortally_wounded("player_001", "PlayerName", None, "room_001")
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_player_died(messaging_integration, mock_connection_manager):
    """Test broadcast_player_died broadcasts death message."""
    result = await messaging_integration.broadcast_player_death("player_001", "PlayerName", "room_001", "Location")
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_player_mortally_wounded_with_attacker(messaging_integration, mock_connection_manager):
    """Test broadcast_player_mortally_wounded with attacker name."""
    mock_connection_manager.send_personal_message = AsyncMock()
    result = await messaging_integration.broadcast_player_mortally_wounded(
        "player_001", "PlayerName", "Attacker", "room_001"
    )
    assert isinstance(result, dict)
    mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_player_mortally_wounded_no_attacker(messaging_integration, mock_connection_manager):
    """Test broadcast_player_mortally_wounded without attacker."""
    mock_connection_manager.send_personal_message = AsyncMock()
    result = await messaging_integration.broadcast_player_mortally_wounded("player_001", "PlayerName", None, "room_001")
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_broadcast_player_respawn(messaging_integration, mock_connection_manager):
    """Test broadcast_player_respawn broadcasts respawn message."""
    result = await messaging_integration.broadcast_player_respawn("player_001", "PlayerName", "room_001")
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_player_respawn_personal_message_error(messaging_integration, mock_connection_manager):
    """Test broadcast_player_respawn handles personal message errors."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=OSError("OS error"))
    result = await messaging_integration.broadcast_player_respawn("player_001", "PlayerName", "room_001")
    # Should not raise, just log warning
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_error_send_error(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_error handles send_personal_message errors."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=RuntimeError("Send error"))
    # Should not raise, error handling added
    result = await messaging_integration.broadcast_combat_error("room_001", "Error message", "player_001")
    assert isinstance(result, dict)
    assert result.get("success") is False


@pytest.mark.asyncio
async def test_connection_manager_lazy_load_called(messaging_integration):
    """Test connection_manager property calls lazy load when None."""
    messaging_integration._connection_manager = None
    mock_manager = MagicMock()
    with patch.object(
        messaging_integration, "_resolve_connection_manager_from_container", return_value=mock_manager
    ) as mock_resolve:
        result = messaging_integration.connection_manager
        assert result == mock_manager
        mock_resolve.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_combat_attack_with_attacker_id(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_attack sends personal message to attacker."""
    mock_connection_manager.send_personal_message = AsyncMock()
    result = await messaging_integration.broadcast_combat_attack(
        "room_001", "Attacker", "Target", 10, "kick", "combat_001", "attacker_001"
    )
    assert isinstance(result, dict)
    mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_combat_attack_no_attacker_id(messaging_integration, mock_connection_manager):
    """Test broadcast_combat_attack without attacker_id."""
    result = await messaging_integration.broadcast_combat_attack(
        "room_001", "Attacker", "Target", 10, "punch", "combat_001", None
    )
    assert isinstance(result, dict)
    mock_connection_manager.broadcast_to_room.assert_awaited_once()
    # Should not send personal message when no attacker_id
    mock_connection_manager.send_personal_message.assert_not_awaited()


@pytest.mark.asyncio
async def test_broadcast_player_mortally_wounded_personal_message_error(messaging_integration, mock_connection_manager):
    """Test broadcast_player_mortally_wounded handles personal message errors."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=ConnectionError("Connection error"))
    result = await messaging_integration.broadcast_player_mortally_wounded("player_001", "PlayerName", None, "room_001")
    # Should not raise, just log warning
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_broadcast_player_death_personal_message_error(messaging_integration, mock_connection_manager):
    """Test broadcast_player_death handles personal message errors."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=ValueError("Error"))
    result = await messaging_integration.broadcast_player_death("player_001", "PlayerName", "room_001", "Location")
    # Should not raise, just log warning
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_send_dp_decay_message(messaging_integration, mock_connection_manager):
    """Test send_dp_decay_message sends DP decay message."""
    mock_connection_manager.send_personal_message = AsyncMock(return_value={"success": True})
    result = await messaging_integration.send_dp_decay_message("player_001", 5)
    assert isinstance(result, dict)
    mock_connection_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_dp_decay_message_error(messaging_integration, mock_connection_manager):
    """Test send_dp_decay_message handles errors gracefully."""
    mock_connection_manager.send_personal_message = AsyncMock(side_effect=RuntimeError("Error"))
    # Should not raise, just log error and return error status
    result = await messaging_integration.send_dp_decay_message("player_001", 5)
    assert isinstance(result, dict)
    assert result.get("success") is False


def test_connection_manager_setter(messaging_integration):
    """Test connection_manager setter updates value."""
    new_manager = MagicMock()
    messaging_integration.connection_manager = new_manager
    assert messaging_integration._connection_manager == new_manager


def test_connection_manager_setter_overrides_lazy_load(messaging_integration):
    """Test connection_manager setter overrides lazy load mechanism."""
    new_manager = MagicMock()
    messaging_integration._connection_manager = None
    messaging_integration.connection_manager = new_manager
    assert messaging_integration.connection_manager == new_manager
