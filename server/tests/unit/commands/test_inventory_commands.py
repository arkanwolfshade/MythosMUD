"""
Unit tests for inventory command handlers.

Tests the inventory command handler functions.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.inventory_commands import (
    handle_drop_command,
    handle_equip_command,
    handle_get_command,
    handle_inventory_command,
    handle_pickup_command,
    handle_put_command,
    handle_unequip_command,
)


@pytest.mark.asyncio
async def test_handle_inventory_command():
    """Test handle_inventory_command() displays inventory."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_player.get_equipped_items = MagicMock(return_value={})
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_wearable_service = AsyncMock()
        mock_wearable_service.get_wearable_containers_for_player = AsyncMock(return_value=[])
        mock_get_services.return_value = (MagicMock(), mock_wearable_service, MagicMock())

        result = await handle_inventory_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

        assert "result" in result
        assert "inventory" in result
        assert "equipped" in result


@pytest.mark.asyncio
async def test_handle_inventory_command_no_persistence():
    """Test handle_inventory_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_inventory_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert (
        "not available" in result["result"].lower()
        or "not found" in result["result"].lower()
        or "error" in result["result"].lower()
    )


@pytest.mark.asyncio
async def test_handle_pickup_command():
    """Test handle_pickup_command() picks up item."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.current_room_id = "room_001"
    mock_player.get_inventory = MagicMock(return_value=[])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_inventory_service = MagicMock()
        mock_inventory_service.add_item_to_inventory = AsyncMock(return_value={"success": True})
        mock_get_services.return_value = (mock_inventory_service, MagicMock(), MagicMock())

        result = await handle_pickup_command(
            {"target": "sword"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

        assert "result" in result


@pytest.mark.asyncio
async def test_handle_pickup_command_no_target():
    """Test handle_pickup_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_pickup_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "usage" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_drop_command():
    """Test handle_drop_command() drops item."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.current_room_id = "room_001"
    mock_player.get_inventory = MagicMock(return_value=[{"item_name": "sword", "item_id": "sword_001"}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_inventory_service = MagicMock()
        mock_inventory_service.remove_item_from_inventory = AsyncMock(return_value={"success": True})
        mock_get_services.return_value = (mock_inventory_service, MagicMock(), MagicMock())

        result = await handle_drop_command(
            {"target": "sword"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

        assert "result" in result


@pytest.mark.asyncio
async def test_handle_drop_command_no_target():
    """Test handle_drop_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_drop_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "usage" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_equip_command():
    """Test handle_equip_command() equips item."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.current_room_id = "room_001"
    mock_player.get_inventory = MagicMock(return_value=[{"item_name": "sword", "item_id": "sword_001"}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_inventory_service = MagicMock()
        mock_equipment_service = MagicMock()
        mock_equipment_service.equip_item = AsyncMock(return_value={"success": True})
        mock_get_services.return_value = (mock_inventory_service, MagicMock(), mock_equipment_service)

        result = await handle_equip_command(
            {"target": "sword"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

        assert "result" in result


@pytest.mark.asyncio
async def test_handle_equip_command_no_target():
    """Test handle_equip_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_equip_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "usage" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_unequip_command():
    """Test handle_unequip_command() unequips item."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.current_room_id = "room_001"
    mock_player.get_equipped_items = MagicMock(
        return_value={"main_hand": {"item_name": "sword", "item_id": "sword_001"}}
    )
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_inventory_service = MagicMock()
        mock_equipment_service = MagicMock()
        mock_equipment_service.unequip_item = AsyncMock(return_value={"success": True})
        mock_get_services.return_value = (mock_inventory_service, MagicMock(), mock_equipment_service)

        result = await handle_unequip_command(
            {"target": "sword"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

        assert "result" in result


@pytest.mark.asyncio
async def test_handle_unequip_command_no_target():
    """Test handle_unequip_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_unequip_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "usage" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_put_command():
    """Test handle_put_command() puts item in container."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.current_room_id = "room_001"
    mock_player.get_inventory = MagicMock(return_value=[{"item_name": "sword", "item_id": "sword_001"}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_inventory_service = MagicMock()
        mock_wearable_service = AsyncMock()
        mock_wearable_service.add_item_to_container = AsyncMock(return_value={"success": True})
        mock_get_services.return_value = (mock_inventory_service, mock_wearable_service, MagicMock())

        result = await handle_put_command(
            {"target": "sword", "container": "backpack"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

        assert "result" in result


@pytest.mark.asyncio
async def test_handle_put_command_no_target():
    """Test handle_put_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_put_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "usage" in result["result"].lower() or "target" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_get_command():
    """Test handle_get_command() gets item from container."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_connection_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.player_id = "player_id_001"
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.inventory_commands._get_shared_services") as mock_get_services:
        mock_inventory_service = MagicMock()
        mock_wearable_service = AsyncMock()
        mock_wearable_service.remove_item_from_container = AsyncMock(return_value={"success": True})
        mock_get_services.return_value = (mock_inventory_service, mock_wearable_service, MagicMock())

        result = await handle_get_command(
            {"target": "sword", "container": "backpack"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

        assert "result" in result


@pytest.mark.asyncio
async def test_handle_get_command_no_target():
    """Test handle_get_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.container = MagicMock()
    mock_state.container.async_persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_get_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "usage" in result["result"].lower() or "target" in result["result"].lower()
