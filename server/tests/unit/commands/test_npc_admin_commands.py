"""
Unit tests for NPC admin command handlers.

Tests the NPC admin command functionality.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_command,
    handle_npc_create_command,
    handle_npc_delete_command,
    handle_npc_despawn_command,
    handle_npc_list_command,
    handle_npc_move_command,
    handle_npc_spawn_command,
    handle_npc_stats_command,
    validate_npc_admin_permission,
)


@pytest.mark.asyncio
async def test_handle_npc_command_no_player_service():
    """Test handle_npc_command() when player service is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_command_player_not_found():
    """Test handle_npc_command() when player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_command_no_permission():
    """Test handle_npc_command() when player lacks admin permission."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = False
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "permission" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_command_no_args():
    """Test handle_npc_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"] or "subcommand" in result["result"].lower()


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_no_player():
    """Test validate_npc_admin_permission() with no player."""
    result = validate_npc_admin_permission(None, "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_not_admin():
    """Test validate_npc_admin_permission() when player is not admin."""
    mock_player = MagicMock()
    mock_player.is_admin = False
    result = validate_npc_admin_permission(mock_player, "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_admin():
    """Test validate_npc_admin_permission() when player is admin."""
    mock_player = MagicMock()
    mock_player.is_admin = True
    result = validate_npc_admin_permission(mock_player, "TestPlayer")
    assert result is True


@pytest.mark.asyncio
async def test_handle_npc_create_command_no_args():
    """Test handle_npc_create_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_create_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_list_command():
    """Test handle_npc_list_command() lists NPCs."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.npc_admin.definition.npc_service") as mock_npc_service:
        mock_npc_service.list_npc_definitions.return_value = []
        result = await handle_npc_list_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result


@pytest.mark.asyncio
async def test_handle_npc_delete_command_no_args():
    """Test handle_npc_delete_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_delete_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_create_command_invalid_type():
    """Test handle_npc_create_command() with invalid NPC type."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_create_command(
        {"args": ["create", "TestNPC", "invalid_type", "zone1", "room1"]}, {}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "Invalid NPC type" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_create_command_no_database():
    """Test handle_npc_create_command() when database is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app
    del mock_app.state.db_session_maker

    result = await handle_npc_create_command(
        {"args": ["create", "TestNPC", "passive_mob", "zone1", "room1"]}, {}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not available" in result["result"] or "Database" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_spawn_command_no_args():
    """Test handle_npc_spawn_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_spawn_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_spawn_command_name_not_found():
    """Test handle_npc_spawn_command() when NPC name is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_session_maker = MagicMock(return_value=mock_session)
    mock_state.db_session_maker = mock_session_maker
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.npc_admin.instance.npc_service") as mock_npc_svc:
        mock_npc_svc.get_npc_definition_by_name = AsyncMock(return_value=None)

        result = await handle_npc_spawn_command(
            {"args": ["spawn", "NonexistentNPC"]}, {}, mock_request, None, "TestPlayer"
        )

    assert "result" in result
    assert "No NPC definition named" in result["result"]
    assert "NonexistentNPC" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_spawn_command_name_success():
    """Test handle_npc_spawn_command() with name-based spawn."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player.current_room_id = "room_123"
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_session_maker = MagicMock(return_value=mock_session)
    mock_state.db_session_maker = mock_session_maker
    mock_app.state = mock_state
    mock_request.app = mock_app

    mock_definition = MagicMock()
    mock_definition.id = 42
    mock_definition.name = "Nightgaunt"

    with patch("server.commands.npc_admin.instance.npc_service") as mock_npc_svc:
        mock_npc_svc.get_npc_definition_by_name = AsyncMock(return_value=mock_definition)
        with patch("server.commands.npc_admin.instance.get_npc_instance_service") as mock_get_svc:
            mock_instance_svc = MagicMock()
            mock_instance_svc.spawn_npc_instance = AsyncMock()
            mock_get_svc.return_value = mock_instance_svc

            result = await handle_npc_spawn_command(
                {"args": ["spawn", "Nightgaunt", "1", "npc"]}, {}, mock_request, None, "TestPlayer"
            )

    assert "result" in result
    assert "spawned successfully" in result["result"]
    mock_instance_svc.spawn_npc_instance.assert_called_once_with(42, "room_123")


@pytest.mark.asyncio
async def test_spawn_command_regression_routing_via_npc_command():
    """
    Regression: Ensure /spawn (npc spawn) command is reachable and not removed.

    Catches: spawn removed from subcommand_map, handle_npc_spawn_command removed,
    or routing broken. The spawn command must route through handle_npc_command.
    """
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player.current_room_id = "room_123"
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    mock_definition = MagicMock()
    mock_definition.id = 42
    mock_definition.name = "Nightgaunt"

    # Simulates /spawn Nightgaunt 1 npc -> npc spawn with args (subcommand prepended by handler)
    command_data = {
        "args": ["Nightgaunt", "1", "npc"],
        "subcommand": "spawn",
    }

    with patch("server.commands.npc_admin.instance.npc_service") as mock_npc_svc:
        mock_npc_svc.get_npc_definition_by_name = AsyncMock(return_value=mock_definition)
        with patch("server.commands.npc_admin.instance.get_npc_instance_service") as mock_get_svc:
            mock_instance_svc = MagicMock()
            mock_instance_svc.spawn_npc_instance = AsyncMock()
            mock_get_svc.return_value = mock_instance_svc

            result = await handle_npc_command(command_data, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "spawned successfully" in result["result"]
    mock_instance_svc.spawn_npc_instance.assert_called_once_with(42, "room_123")


@pytest.mark.asyncio
async def test_handle_npc_despawn_command_no_args():
    """Test handle_npc_despawn_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_despawn_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_move_command_no_args():
    """Test handle_npc_move_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_move_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_stats_command():
    """Test handle_npc_stats_command() displays NPC stats."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.npc_admin.instance.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.get_npc_instance = AsyncMock(return_value=None)
        mock_get_service.return_value = mock_service
        result = await handle_npc_stats_command({"args": ["stats", "npc_001"]}, {}, mock_request, None, "TestPlayer")
        assert "result" in result


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_exception():
    """Test validate_npc_admin_permission() handles exceptions."""

    # Create a player object that raises an exception when accessing is_admin
    class ExceptionPlayer:
        """Player that raises exception when accessing is_admin."""

        @property
        def is_admin(self):
            """Raise AttributeError to simulate permission check failure."""
            raise AttributeError("Test error")

    mock_player = ExceptionPlayer()

    # Mock the logger to avoid logging configuration issues in parallel test execution
    # This prevents WarningOnlyFilter errors that occur when logging happens during exception handling
    with patch("server.commands.npc_admin.router.logger") as mock_logger:
        result = validate_npc_admin_permission(mock_player, "TestPlayer")
        assert result is False
        # Verify error was logged
        mock_logger.error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_npc_command_unknown_subcommand():
    """Test handle_npc_command() with unknown subcommand."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({"args": ["unknown"]}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Unknown" in result["result"] or "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_behavior_command_usage():
    """Test handle_npc_behavior_command() requires npc id and behavior type."""
    from server.commands.npc_admin.behavior import handle_npc_behavior_command

    result = await handle_npc_behavior_command({"args": ["behavior"]}, {}, MagicMock(), None, "TestPlayer")
    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_behavior_command_invalid_type():
    """Test handle_npc_behavior_command() rejects invalid behavior types."""
    from server.commands.npc_admin.behavior import handle_npc_behavior_command

    result = await handle_npc_behavior_command(
        {"args": ["behavior", "npc-1", "fly-away"]}, {}, MagicMock(), None, "TestPlayer"
    )
    assert "Invalid behavior type" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_behavior_command_not_implemented():
    """Test handle_npc_behavior_command() returns not-implemented for valid input."""
    from server.commands.npc_admin.behavior import handle_npc_behavior_command

    with patch("server.commands.npc_admin.behavior.get_npc_instance_service", return_value=MagicMock()):
        result = await handle_npc_behavior_command(
            {"args": ["behavior", "npc-1", "passive"]}, {}, MagicMock(), None, "TestPlayer"
        )
    assert "not yet implemented" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_react_command_invalid_reaction():
    """Test handle_npc_react_command() rejects invalid reaction types."""
    from server.commands.npc_admin.behavior import handle_npc_react_command

    result = await handle_npc_react_command({"args": ["react", "npc-1", "dance"]}, {}, MagicMock(), None, "TestPlayer")
    assert "Invalid reaction type" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_stop_command_usage():
    """Test handle_npc_stop_command() requires npc id."""
    from server.commands.npc_admin.behavior import handle_npc_stop_command

    result = await handle_npc_stop_command({"args": ["stop"]}, {}, MagicMock(), None, "TestPlayer")
    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_population_command_success():
    """Test handle_npc_population_command() formats stats."""
    from server.commands.npc_admin.monitoring import handle_npc_population_command

    mock_service = AsyncMock()
    mock_service.get_population_stats = AsyncMock(
        return_value={"total_npcs": 3, "by_type": {"passive_mob": 2}, "by_zone": {"arkham": 3}}
    )
    with patch("server.commands.npc_admin.monitoring.get_npc_instance_service", return_value=mock_service):
        result = await handle_npc_population_command({}, {}, MagicMock(), None, "TestPlayer")

    assert "NPC Population Statistics" in result["result"]
    assert "passive_mob" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_zone_command_success():
    """Test handle_npc_zone_command() formats zone stats."""
    from server.commands.npc_admin.monitoring import handle_npc_zone_command

    mock_service = AsyncMock()
    mock_service.get_zone_stats = AsyncMock(
        return_value={
            "total_zones": 1,
            "total_npcs": 2,
            "zones": [{"zone_key": "arkham", "npc_count": 2, "active_npcs": ["guard-1"]}],
        }
    )
    with patch("server.commands.npc_admin.monitoring.get_npc_instance_service", return_value=mock_service):
        result = await handle_npc_zone_command({"args": ["zone", "arkham"]}, {}, MagicMock(), None, "TestPlayer")

    assert "NPC Zone Statistics" in result["result"]
    assert "guard-1" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_status_command_success():
    """Test handle_npc_status_command() formats system status."""
    from server.commands.npc_admin.monitoring import handle_npc_status_command

    mock_service = AsyncMock()
    mock_service.get_system_stats = AsyncMock(
        return_value={
            "system_status": "healthy",
            "active_npcs": 4,
            "lifecycle_manager_status": "running",
            "population_controller_status": "running",
            "spawn_queue_size": 0,
        }
    )
    with patch("server.commands.npc_admin.monitoring.get_npc_instance_service", return_value=mock_service):
        result = await handle_npc_status_command({}, {}, MagicMock(), None, "TestPlayer")

    assert "NPC System Status" in result["result"]
    assert "healthy" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_test_occupants_command_success():
    """Test handle_npc_test_occupants_command() lists room occupants."""
    from server.commands.npc_admin.test_occupants import handle_npc_test_occupants_command

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "room-42"
    mock_player_service = MagicMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_event_handler = MagicMock()
    mock_event_handler._get_room_occupants.return_value = [
        {"player_name": "Alice"},
        {"npc_name": "Guard"},
    ]
    mock_event_handler.send_room_occupants_update = AsyncMock()
    mock_state.event_handler = mock_event_handler
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_test_occupants_command({}, {}, mock_request, None, "TestPlayer")
    assert "Occupants in room: room-42" in result["result"]
    assert "Alice" in result["result"]
    assert "Guard" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_edit_command_invalid_id():
    """Test handle_npc_edit_command() rejects non-numeric ids."""
    from server.commands.npc_admin.definition import handle_npc_edit_command

    result = await handle_npc_edit_command(
        {"args": ["edit", "abc", "name", "NewName"]}, {}, MagicMock(), None, "TestPlayer"
    )
    assert "Invalid NPC ID" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_delete_command_success():
    """Test handle_npc_delete_command() deletes definition by id."""
    from server.commands.npc_admin.definition import handle_npc_delete_command

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_state.db_session_maker = MagicMock(return_value=mock_session)
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.npc_admin.definition.npc_service") as mock_npc_service:
        mock_npc_service.delete_npc_definition = AsyncMock(return_value=True)
        result = await handle_npc_delete_command({"args": ["delete", "7"]}, {}, mock_request, None, "TestPlayer")

    assert "deleted successfully" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_list_command_with_definitions():
    """Test handle_npc_list_command() renders definition rows."""
    from server.commands.npc_admin.definition import handle_npc_list_command

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_state.db_session_maker = MagicMock(return_value=mock_session)
    mock_app.state = mock_state
    mock_request.app = mock_app

    definition = MagicMock()
    definition.id = 9
    definition.name = "Shoggoth"
    definition.npc_type = "aggressive_mob"
    definition.sub_zone_id = "arkham"
    definition.room_id = "room-1"

    with patch("server.commands.npc_admin.definition.npc_service") as mock_npc_service:
        mock_npc_service.get_npc_definitions = AsyncMock(return_value=[definition])
        result = await handle_npc_list_command({}, {}, mock_request, None, "TestPlayer")
        assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_handle_npc_react_command_success():
    """Test handle_npc_react_command() accepts valid reaction types."""
    from server.commands.npc_admin.behavior import handle_npc_react_command

    with patch("server.commands.npc_admin.behavior.get_npc_instance_service", return_value=MagicMock()):
        result = await handle_npc_react_command(
            {"args": ["react", "npc-1", "greet"]}, {}, MagicMock(), None, "TestPlayer"
        )
    assert "not yet implemented" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_stop_command_success():
    """Test handle_npc_stop_command() accepts npc id."""
    from server.commands.npc_admin.behavior import handle_npc_stop_command

    with patch("server.commands.npc_admin.behavior.get_npc_instance_service", return_value=MagicMock()):
        result = await handle_npc_stop_command({"args": ["stop", "npc-1"]}, {}, MagicMock(), None, "TestPlayer")
    assert "not yet implemented" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_behavior_command_exception():
    """Test handle_npc_behavior_command() handles service exceptions."""
    from server.commands.npc_admin.behavior import handle_npc_behavior_command

    with patch(
        "server.commands.npc_admin.behavior.get_npc_instance_service",
        side_effect=RuntimeError("service down"),
    ):
        result = await handle_npc_behavior_command(
            {"args": ["behavior", "npc-1", "idle"]}, {}, MagicMock(), None, "TestPlayer"
        )
    assert "Error setting NPC behavior" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_create_command_success():
    """Test handle_npc_create_command() creates definition in database."""
    from server.commands.npc_admin.definition import handle_npc_create_command

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_state.db_session_maker = MagicMock(return_value=mock_session)
    mock_app.state = mock_state
    mock_request.app = mock_app

    definition = MagicMock()
    definition.id = 11

    with patch("server.commands.npc_admin.definition.npc_service") as mock_npc_service:
        mock_npc_service.create_npc_definition = AsyncMock(return_value=definition)
        result = await handle_npc_create_command(
            {"args": ["create", "Rat", "passive_mob", "arkham", "room-1"]},
            {},
            mock_request,
            None,
            "TestPlayer",
        )

    assert "created successfully" in result["result"]
    assert "11" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_edit_command_success():
    """Test handle_npc_edit_command() updates definition field."""
    from server.commands.npc_admin.definition import handle_npc_edit_command

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    mock_state.db_session_maker = MagicMock(return_value=mock_session)
    mock_app.state = mock_state
    mock_request.app = mock_app

    definition = MagicMock()
    with patch("server.commands.npc_admin.definition.npc_service") as mock_npc_service:
        mock_npc_service.update_npc_definition = AsyncMock(return_value=definition)
        result = await handle_npc_edit_command(
            {"args": ["edit", "3", "name", "Renamed"]}, {}, mock_request, None, "TestPlayer"
        )

    assert "updated successfully" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_spawn_command_numeric_id():
    """Test handle_npc_spawn_command() with numeric definition id."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "room-99"
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.npc_admin.instance.get_npc_instance_service") as mock_get_svc:
        mock_instance_svc = MagicMock()
        mock_instance_svc.spawn_npc_instance = AsyncMock()
        mock_get_svc.return_value = mock_instance_svc

        result = await handle_npc_spawn_command(
            {"args": ["spawn", "5", "room-99"]}, {}, mock_request, None, "TestPlayer"
        )

    assert "spawned successfully" in result["result"]
    mock_instance_svc.spawn_npc_instance.assert_awaited_once_with(5, "room-99")


@pytest.mark.asyncio
async def test_handle_npc_despawn_command_success():
    """Test handle_npc_despawn_command() despawns by instance id."""
    mock_request = MagicMock()

    with patch("server.commands.npc_admin.instance.get_npc_instance_service") as mock_get_svc:
        mock_instance_svc = MagicMock()
        mock_instance_svc.despawn_npc_instance = AsyncMock(return_value=True)
        mock_get_svc.return_value = mock_instance_svc

        result = await handle_npc_despawn_command(
            {"args": ["despawn", "instance-7"]}, {}, mock_request, None, "TestPlayer"
        )

    assert "despawned successfully" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_move_command_success():
    """Test handle_npc_move_command() moves npc instance to room."""
    mock_request = MagicMock()

    with patch("server.commands.npc_admin.instance.get_npc_instance_service") as mock_get_svc:
        mock_instance_svc = MagicMock()
        mock_instance_svc.move_npc_instance = AsyncMock(return_value=True)
        mock_get_svc.return_value = mock_instance_svc

        result = await handle_npc_move_command(
            {"args": ["move", "instance-7", "room-2"]}, {}, mock_request, None, "TestPlayer"
        )

    assert "moved to room-2" in result["result"]
