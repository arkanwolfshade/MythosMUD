"""Unit tests for admin summon command helpers."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands import admin_summon_command as cmd
from server.exceptions import DatabaseError
from server.game.items.item_factory import ItemFactoryError


def test_validate_summon_prerequisites_missing_item_services() -> None:
    state = MagicMock(item_factory=None, prototype_registry=None)
    admin_logger = MagicMock()
    err = cmd._validate_summon_prerequisites(state, MagicMock(), "Admin", admin_logger)
    assert err is not None
    assert "summoning matrix" in err["result"]


def test_validate_summon_prerequisites_missing_room_manager() -> None:
    state = MagicMock(item_factory=MagicMock(), prototype_registry=MagicMock())
    cm = MagicMock(room_manager=None)
    err = cmd._validate_summon_prerequisites(state, cm, "Admin", MagicMock())
    assert err is not None
    assert "Room inventory" in err["result"]


def test_validate_summon_prerequisites_ok() -> None:
    state = MagicMock(item_factory=MagicMock(), prototype_registry=MagicMock())
    cm = MagicMock(room_manager=MagicMock(add_room_drop=MagicMock()))
    assert cmd._validate_summon_prerequisites(state, cm, "Admin", MagicMock()) is None


def test_summon_npc_stub_response() -> None:
    admin_logger = MagicMock()
    result = cmd._summon_npc_stub_response("npc_1", "npc", 1, "room-a", "Admin", admin_logger)
    assert result is not None
    assert "NPC summoning" in result["result"]


def test_summon_npc_stub_response_item_type() -> None:
    assert cmd._summon_npc_stub_response("item_1", "item", 1, "room-a", "Admin", MagicMock()) is None


def test_create_summon_item_instance_success() -> None:
    factory = MagicMock()
    instance = MagicMock()
    factory.create_instance.return_value = instance
    got, err = cmd._create_summon_item_instance(factory, "proto_1", 2, "Admin", MagicMock(), "room-a", "item")
    assert got is instance
    assert err is None


def test_create_summon_item_instance_factory_error() -> None:
    factory = MagicMock()
    factory.create_instance.side_effect = ItemFactoryError("bad prototype")
    got, err = cmd._create_summon_item_instance(factory, "proto_1", 1, "Admin", MagicMock(), "room-a", "item")
    assert got is None
    assert "Summoning failed" in err["result"]


def test_parse_summon_command_data_missing_prototype() -> None:
    context = {"player_name_value": "Admin", "room_id": "room-a", "room_manager": MagicMock(), "dashboard": MagicMock()}
    context["dashboard"].alert_thresholds = {"summon_quantity_warning": 5}
    parsed, err = cmd._parse_summon_command_data({}, context)
    assert parsed is None
    assert "prototype_id" in err["result"]


def test_parse_summon_command_data_npc_stub() -> None:
    context = {
        "player_name_value": "Admin",
        "room_id": "room-a",
        "room_manager": MagicMock(),
        "dashboard": MagicMock(),
        "admin_logger": MagicMock(),
    }
    context["dashboard"].alert_thresholds = {"summon_quantity_warning": 5}
    parsed, err = cmd._parse_summon_command_data(
        {"prototype_id": "npc_1", "target_type": "npc", "quantity": 1}, context
    )
    assert parsed is None
    assert err is not None


def test_parse_summon_command_data_item_ok() -> None:
    context = {
        "player_name_value": "Admin",
        "room_id": "room-a",
        "room_manager": MagicMock(),
        "dashboard": MagicMock(),
        "admin_logger": MagicMock(),
    }
    context["dashboard"].alert_thresholds = {"summon_quantity_warning": 5}
    parsed, err = cmd._parse_summon_command_data({"prototype_id": "item_1", "quantity": 2}, context)
    assert err is None
    assert parsed["prototype_id"] == "item_1"
    assert parsed["quantity"] == 2


@pytest.mark.asyncio
async def test_persist_summoned_item_swallows_db_error() -> None:
    persistence = MagicMock()
    persistence.create_item_instance = AsyncMock(side_effect=DatabaseError("db down"))
    instance = MagicMock(item_instance_id="i1", prototype_id="p1", metadata={})
    await cmd._persist_summoned_item(persistence, "room-a", instance, 1, "Admin")


@pytest.mark.asyncio
async def test_persist_summoned_item_success() -> None:
    persistence = MagicMock()
    persistence.create_item_instance = AsyncMock()
    instance = MagicMock(item_instance_id="i1", prototype_id="p1", metadata={"k": "v"})
    await cmd._persist_summoned_item(persistence, "room-a", instance, 2, "Admin")
    persistence.create_item_instance.assert_awaited_once()


def test_parse_summon_command_data_quantity_spike() -> None:
    context = {
        "player_name_value": "Admin",
        "room_id": "room-a",
        "room_manager": MagicMock(),
        "dashboard": MagicMock(),
        "admin_logger": MagicMock(),
    }
    context["dashboard"].alert_thresholds = {"summon_quantity_warning": 3}
    context["dashboard"].record_summon_quantity_spike = MagicMock()
    parsed, err = cmd._parse_summon_command_data({"prototype_id": "item_1", "quantity": 10}, context)
    assert err is None
    assert parsed["quantity"] == 10
    context["dashboard"].record_summon_quantity_spike.assert_called_once()


def test_parse_summon_command_data_room_manager_missing_at_execution() -> None:
    context = {
        "player_name_value": "Admin",
        "room_id": "room-a",
        "room_manager": None,
        "dashboard": MagicMock(),
        "admin_logger": MagicMock(),
    }
    context["dashboard"].alert_thresholds = {"summon_quantity_warning": 5}
    parsed, err = cmd._parse_summon_command_data({"prototype_id": "item_1"}, context)
    assert parsed is None
    assert "Room inventory" in err["result"]


@pytest.mark.asyncio
async def test_complete_summon_success() -> None:
    factory = MagicMock()
    instance = MagicMock()
    instance.to_inventory_stack.return_value = {"item_id": "proto_1", "item_name": "Lantern"}
    factory.create_instance.return_value = instance
    room_manager = MagicMock()
    persistence = MagicMock()
    persistence.create_item_instance = AsyncMock()
    context = {
        "persistence": persistence,
        "connection_manager": MagicMock(),
        "player": MagicMock(player_id="p1"),
        "room_id": "room-a",
        "player_name_value": "Admin",
        "room_manager": room_manager,
        "item_factory": factory,
        "admin_logger": MagicMock(),
    }
    parsed = {"prototype_id": "proto_1", "quantity": 2, "target_type": "item"}
    with patch.object(cmd, "_broadcast_and_log_summon_success", AsyncMock()):
        result = await cmd._complete_summon(context, parsed)
    assert "summon 2x Lantern" in result["result"]
    room_manager.add_room_drop.assert_called_once()


@pytest.mark.asyncio
async def test_complete_summon_no_instance_without_error() -> None:
    factory = MagicMock()
    factory.create_instance.return_value = MagicMock()
    context = {
        "persistence": MagicMock(),
        "room_id": "room-a",
        "player_name_value": "Admin",
        "room_manager": MagicMock(),
        "item_factory": factory,
        "admin_logger": MagicMock(),
    }
    with patch.object(cmd, "_create_summon_item_instance", return_value=(None, None)):
        result = await cmd._complete_summon(context, {"prototype_id": "p1", "quantity": 1, "target_type": "item"})
    assert "internal error" in result["result"]


@pytest.mark.asyncio
async def test_broadcast_and_log_summon_success() -> None:
    context = {
        "connection_manager": MagicMock(),
        "player": MagicMock(player_id="player-1"),
        "room_id": "room-a",
        "player_name_value": "Admin",
        "admin_logger": MagicMock(),
    }
    parsed = {"prototype_id": "p1", "quantity": 1, "target_type": "item"}
    stack = {"item_id": "p1", "item_name": "Lantern"}
    with patch("server.commands.admin_summon_command.broadcast_room_event", AsyncMock()) as broadcast:
        with patch("server.commands.admin_summon_command.build_event", return_value={"event": "admin_summon"}):
            await cmd._broadcast_and_log_summon_success(context, parsed, stack, "Lantern")
    broadcast.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_summon_command_success() -> None:
    context = {"room_manager": MagicMock()}
    parsed = {"prototype_id": "p1", "quantity": 1, "target_type": "item"}
    with patch.object(cmd, "_resolve_summon_context", AsyncMock(return_value=(context, None))):
        with patch.object(cmd, "_parse_summon_command_data", return_value=(parsed, None)):
            with patch.object(cmd, "_complete_summon", AsyncMock(return_value={"result": "You summon 1x Lantern."})):
                result = await cmd.handle_summon_command({}, {}, MagicMock(), None, "Admin")
    assert "Lantern" in result["result"]


@pytest.mark.asyncio
async def test_handle_summon_command_context_error() -> None:
    with patch.object(cmd, "_resolve_summon_context", AsyncMock(return_value=(None, {"result": "denied"}))):
        result = await cmd.handle_summon_command({}, {}, MagicMock(), None, "Admin")
    assert result["result"] == "denied"


@pytest.mark.asyncio
async def test_handle_summon_command_parse_error() -> None:
    context = {"room_manager": MagicMock()}
    with patch.object(cmd, "_resolve_summon_context", AsyncMock(return_value=(context, None))):
        with patch.object(cmd, "_parse_summon_command_data", return_value=(None, {"result": "bad prototype"})):
            result = await cmd.handle_summon_command({}, {}, MagicMock(), None, "Admin")
    assert "bad prototype" in result["result"]


@pytest.mark.asyncio
async def test_resolve_summon_context_permission_denied() -> None:
    player = MagicMock(name="Admin")
    with patch("server.commands.admin_summon_command.resolve_state", return_value=(MagicMock(), MagicMock())):
        with patch("server.commands.admin_summon_command.resolve_player", AsyncMock(return_value=(player, None))):
            with patch("server.commands.admin_summon_command.validate_admin_permission", AsyncMock(return_value=False)):
                context, err = await cmd._resolve_summon_context(MagicMock(), "Admin", {})
    assert context is None
    assert "Restricted Archives" in err["result"]


def test_validate_summon_prerequisites_room_manager_no_add_drop() -> None:
    state = MagicMock(item_factory=MagicMock(), prototype_registry=MagicMock())
    cm = MagicMock(room_manager=MagicMock(spec=[]))
    err = cmd._validate_summon_prerequisites(state, cm, "Admin", MagicMock())
    assert err is not None
    assert "Room inventory" in err["result"]


def test_log_summon_success() -> None:
    admin_logger = MagicMock()
    context = {
        "player_name_value": "Admin",
        "admin_logger": admin_logger,
        "room_id": "room-a",
    }
    parsed = {"prototype_id": "p1", "quantity": 2, "target_type": "item"}
    cmd._log_summon_success(context, parsed, "Lantern")
    admin_logger.log_admin_command.assert_called_once()


@pytest.mark.asyncio
async def test_resolve_summon_context_success() -> None:
    player = MagicMock(name="Admin", current_room_id="room-a")
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock(item_factory=MagicMock(), prototype_registry=MagicMock())
    cm = MagicMock(room_manager=MagicMock(add_room_drop=MagicMock()))
    with patch("server.commands.admin_summon_command.resolve_state", return_value=(MagicMock(), cm)):
        with patch("server.commands.admin_summon_command.resolve_player", AsyncMock(return_value=(player, None))):
            with patch("server.commands.admin_summon_command.validate_admin_permission", AsyncMock(return_value=True)):
                with patch("server.commands.admin_summon_command.get_monitoring_dashboard", return_value=MagicMock()):
                    context, err = await cmd._resolve_summon_context(request, "Admin", {})
    assert err is None
    assert context is not None
    assert context["room_id"] == "room-a"


@pytest.mark.asyncio
async def test_resolve_summon_context_player_error() -> None:
    with patch("server.commands.admin_summon_command.resolve_state", return_value=(MagicMock(), MagicMock())):
        with patch(
            "server.commands.admin_summon_command.resolve_player",
            AsyncMock(return_value=(None, {"result": "Player missing"})),
        ):
            context, err = await cmd._resolve_summon_context(MagicMock(), "Admin", {})
    assert context is None
    assert err["result"] == "Player missing"


@pytest.mark.asyncio
async def test_complete_summon_factory_error() -> None:
    factory = MagicMock()
    factory.create_instance.side_effect = ItemFactoryError("unknown prototype")
    context = {
        "persistence": MagicMock(),
        "room_id": "room-a",
        "player_name_value": "Admin",
        "room_manager": MagicMock(),
        "item_factory": factory,
        "admin_logger": MagicMock(),
    }
    result = await cmd._complete_summon(context, {"prototype_id": "p1", "quantity": 1, "target_type": "item"})
    assert "Summoning failed" in result["result"]


@pytest.mark.asyncio
async def test_handle_summon_command_context_none() -> None:
    with patch.object(cmd, "_resolve_summon_context", AsyncMock(return_value=(None, None))):
        result = await cmd.handle_summon_command({}, {}, MagicMock(), None, "Admin")
    assert "internal error" in result["result"]
