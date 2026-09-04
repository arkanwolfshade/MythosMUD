"""Unit tests for admin setlucidity command helpers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.commands import admin_setlucidity_command as cmd
from server.exceptions import DatabaseError
from server.services.lucidity_service import LucidityUpdateResult


def test_extract_command_args_from_fields() -> None:
    target, lcd = cmd._extract_command_args({"target_player": "Alice", "lcd_value": 42})
    assert target == "Alice"
    assert lcd == 42


def test_extract_command_args_from_args_list() -> None:
    target, lcd = cmd._extract_command_args({"args": ["Bob", "10"]})
    assert target == "Bob"
    assert lcd == 10


def test_validate_lcd_value_none() -> None:
    val, err = cmd._validate_lcd_value(None, "Admin")
    assert val is None
    assert err is not None
    assert "Usage" in err["result"]


def test_validate_lcd_value_out_of_range() -> None:
    val, err = cmd._validate_lcd_value(200, "Admin")
    assert val is None
    assert "out of range" in err["result"]


def test_validate_lcd_value_valid() -> None:
    val, err = cmd._validate_lcd_value("50", "Admin")
    assert val == 50
    assert err is None


def test_get_player_service_from_container() -> None:
    svc = object()
    app = MagicMock()
    app.state.container.player_service = svc
    assert cmd._get_player_service_from_app(app) is svc


@pytest.mark.asyncio
async def test_handle_admin_setlucidity_missing_app() -> None:
    result = await cmd._handle_admin_set_lucidity_command({}, {}, None, None, "Admin")
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_setlucidity_missing_target() -> None:
    request = MagicMock()
    request.app = MagicMock()
    result = await cmd._handle_admin_set_lucidity_command({}, {}, request, None, "Admin")
    assert "Usage" in result["result"]


def test_get_player_service_missing() -> None:
    app = MagicMock()
    app.state.container = None
    app.state.player_service = None
    assert cmd._get_player_service_from_app(app) is None


def test_get_player_service_legacy_app_state() -> None:
    svc = object()
    app = MagicMock()
    app.state.container = None
    app.state.player_service = svc
    assert cmd._get_player_service_from_app(app) is svc


def test_get_catatonia_registry_from_container() -> None:
    reg = object()
    app = MagicMock()
    app.state.container.catatonia_registry = reg
    assert cmd._get_catatonia_registry_from_app(app) is reg


def test_validate_lcd_value_invalid_int() -> None:
    val, err = cmd._validate_lcd_value("xyzzy", "Admin")
    assert val is None
    assert err is not None
    assert "Invalid LCD value" in err["result"]


@pytest.mark.asyncio
async def test_check_admin_permissions_no_user_manager() -> None:
    app = MagicMock()
    app.state.user_manager = None
    _player, err = await cmd._check_admin_permissions(app, "Admin", MagicMock())
    assert err is not None
    assert "not available" in err["result"]


@pytest.mark.asyncio
async def test_check_admin_permissions_current_player_missing() -> None:
    app = MagicMock()
    app.state.user_manager = MagicMock()
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=None)
    _player, err = await cmd._check_admin_permissions(app, "Admin", player_service)
    assert err is not None
    assert "Current player not found" in err["result"]


@pytest.mark.asyncio
async def test_check_admin_permissions_denied() -> None:
    app = MagicMock()
    app.state.user_manager = MagicMock()
    app.state.user_manager.is_admin.return_value = False
    current = MagicMock(id=str(uuid.uuid4()))
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=current)
    _player, err = await cmd._check_admin_permissions(app, "Admin", player_service)
    assert err is not None
    assert "permission" in err["result"]


@pytest.mark.asyncio
async def test_check_admin_permissions_ok() -> None:
    app = MagicMock()
    app.state.user_manager = MagicMock()
    app.state.user_manager.is_admin.return_value = True
    current = MagicMock(id=str(uuid.uuid4()))
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=current)
    player, err = await cmd._check_admin_permissions(app, "Admin", player_service)
    assert err is None
    assert player is current


@pytest.mark.asyncio
async def test_resolve_target_player_not_found() -> None:
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=None)
    player_id, err = await cmd._resolve_target_player(player_service, "Missing")
    assert player_id is None
    assert "not found" in err["result"]


@pytest.mark.asyncio
async def test_resolve_target_player_success() -> None:
    target_uuid = uuid.uuid4()
    target = MagicMock(id=str(target_uuid))
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=target)
    player_id, err = await cmd._resolve_target_player(player_service, "Alice")
    assert err is None
    assert player_id == target_uuid


@pytest.mark.asyncio
async def test_get_current_lcd_default_when_missing() -> None:
    session = AsyncMock()
    result_mock = MagicMock()
    result_mock.scalar_one_or_none.return_value = None
    session.execute = AsyncMock(return_value=result_mock)
    lcd = await cmd._get_current_lcd(session, uuid.uuid4())
    assert lcd == 100


@pytest.mark.asyncio
async def test_get_current_lcd_from_record() -> None:
    session = AsyncMock()
    record = MagicMock(current_lcd=42)
    result_mock = MagicMock()
    result_mock.scalar_one_or_none.return_value = record
    session.execute = AsyncMock(return_value=result_mock)
    lcd = await cmd._get_current_lcd(session, uuid.uuid4())
    assert lcd == 42


@pytest.mark.asyncio
async def test_apply_lucidity_change_success() -> None:
    target_id = uuid.uuid4()
    adjustment = LucidityUpdateResult(
        player_id=target_id,
        previous_lcd=50,
        new_lcd=75,
        previous_tier="lucid",
        new_tier="lucid",
        delta=25,
        liabilities_added=[],
    )
    session = AsyncMock()
    lucidity_service = AsyncMock()
    lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=adjustment)
    with patch("server.commands.admin_setlucidity_command.get_admin_actions_logger") as log_cls:
        log_cls.return_value.log_admin_command = MagicMock()
        result = await cmd._apply_lucidity_change(
            cmd.LucidityChangeCtx(
                session=session,
                lucidity_service=lucidity_service,
                target_player_id=target_id,
                current_lcd=50,
                target_lcd=75,
                player_name="Admin",
                current_user_id="admin-id",
                target_player="Alice",
            )
        )
    assert result is not None
    assert "75" in result["result"]
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_apply_lucidity_change_adjustment_error() -> None:
    session = AsyncMock()
    lucidity_service = AsyncMock()
    lucidity_service.apply_lucidity_adjustment = AsyncMock(side_effect=DatabaseError("boom"))
    result = await cmd._apply_lucidity_change(
        cmd.LucidityChangeCtx(
            session=session,
            lucidity_service=lucidity_service,
            target_player_id=uuid.uuid4(),
            current_lcd=50,
            target_lcd=75,
            player_name="Admin",
            current_user_id="admin-id",
            target_player="Alice",
        )
    )
    assert result is not None
    assert "Error setting lucidity" in result["result"]
    session.rollback.assert_awaited_once()


async def _async_session_gen(session: AsyncMock):
    yield session


@pytest.mark.asyncio
async def test_execute_lucidity_change_success() -> None:
    target_id = uuid.uuid4()
    session = AsyncMock()
    with patch("server.commands.admin_setlucidity_command.get_async_session", return_value=_async_session_gen(session)):
        with patch.object(cmd, "_get_current_lcd", AsyncMock(return_value=60)):
            with patch.object(
                cmd,
                "_apply_lucidity_change",
                AsyncMock(return_value={"result": "Set Alice's LCD from 60 to 75 (lucid -> lucid)."}),
            ):
                result = await cmd._execute_lucidity_change(target_id, 75, None, "Admin", "admin-id", "Alice")
    assert result is not None
    assert "75" in result["result"]


@pytest.mark.asyncio
async def test_execute_lucidity_change_empty_session() -> None:
    async def empty_gen():
        if False:  # pragma: no cover - empty async generator
            yield None

    with patch("server.commands.admin_setlucidity_command.get_async_session", return_value=empty_gen()):
        result = await cmd._execute_lucidity_change(uuid.uuid4(), 50, None, "Admin", "admin-id", "Alice")
    assert result is not None
    assert "Database session could not be established" in result["result"]


@pytest.mark.asyncio
async def test_execute_lucidity_change_outer_error() -> None:
    with patch(
        "server.commands.admin_setlucidity_command.get_async_session",
        side_effect=SQLAlchemyError("connection lost"),
    ):
        with patch("server.commands.admin_setlucidity_command.get_admin_actions_logger") as log_cls:
            log_cls.return_value.log_admin_command = MagicMock()
            result = await cmd._execute_lucidity_change(uuid.uuid4(), 50, None, "Admin", "admin-id", "Alice")
    assert result is not None
    assert "Error setting lucidity" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_setlucidity_missing_player_service() -> None:
    request = MagicMock()
    request.app = MagicMock()
    request.app.state.container = MagicMock()
    request.app.state.container.player_service = None
    request.app.state.player_service = None
    result = await cmd._handle_admin_set_lucidity_command(
        {"target_player": "Alice", "lcd_value": 50}, {}, request, None, "Admin"
    )
    assert "Player service not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_setlucidity_success() -> None:
    request = MagicMock()
    request.app = MagicMock()
    player_service = MagicMock()
    request.app.state.container = MagicMock()
    request.app.state.container.player_service = player_service
    request.app.state.container.catatonia_registry = MagicMock()
    request.app.state.user_manager = MagicMock()
    request.app.state.user_manager.is_admin.return_value = True
    admin_player = MagicMock(id=str(uuid.uuid4()))
    target_uuid = uuid.uuid4()
    target_player = MagicMock(id=str(target_uuid))
    player_service.resolve_player_name = AsyncMock(side_effect=[admin_player, target_player])
    with patch.object(
        cmd,
        "_execute_lucidity_change",
        AsyncMock(return_value={"result": "Set Alice's LCD from 60 to 50 (lucid -> lucid)."}),
    ) as execute:
        result = await cmd._handle_admin_set_lucidity_command(
            {"target_player": "Alice", "lcd_value": 50}, {}, request, None, "Admin"
        )
    execute.assert_awaited_once()
    assert "Alice" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_setlucidity_permission_denied() -> None:
    request = MagicMock()
    request.app = MagicMock()
    player_service = MagicMock()
    request.app.state.container = MagicMock()
    request.app.state.container.player_service = player_service
    request.app.state.user_manager = MagicMock()
    request.app.state.user_manager.is_admin.return_value = False
    admin_player = MagicMock(id=str(uuid.uuid4()))
    player_service.resolve_player_name = AsyncMock(return_value=admin_player)
    result = await cmd._handle_admin_set_lucidity_command(
        {"target_player": "Alice", "lcd_value": 50}, {}, request, None, "Admin"
    )
    assert "permission" in result["result"]


def test_extract_command_args_target_name_and_value() -> None:
    target, lcd = cmd._extract_command_args({"target_name": "Carol", "value": 33})
    assert target == "Carol"
    assert lcd == 33


def test_extract_command_args_invalid_args_int() -> None:
    target, lcd = cmd._extract_command_args({"args": ["Bob", "not-a-number"]})
    assert target == "Bob"
    assert lcd is None


def test_get_catatonia_registry_legacy_app_state() -> None:
    reg = object()
    app = MagicMock()
    app.state.container = None
    app.state.catatonia_registry = reg
    assert cmd._get_catatonia_registry_from_app(app) is reg


def test_get_catatonia_registry_missing() -> None:
    app = MagicMock()
    app.state.container = None
    app.state.catatonia_registry = None
    assert cmd._get_catatonia_registry_from_app(app) is None


@pytest.mark.asyncio
async def test_validate_command_context_success() -> None:
    request = MagicMock()
    request.app = MagicMock()
    app, target, lcd, err = await cmd._validate_command_context(
        request, {"target_player": "Alice", "lcd_value": 40}, "Admin"
    )
    assert err is None
    assert app is request.app
    assert target == "Alice"
    assert lcd == 40


@pytest.mark.asyncio
async def test_validate_command_context_invalid_lcd() -> None:
    request = MagicMock()
    request.app = MagicMock()
    _app, _target, lcd, err = await cmd._validate_command_context(request, {"target_player": "Alice"}, "Admin")
    assert lcd is None
    assert err is not None


@pytest.mark.asyncio
async def test_setup_command_execution_target_not_found() -> None:
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(side_effect=[MagicMock(id=str(uuid.uuid4())), None])
    app = MagicMock()
    app.state.user_manager = MagicMock()
    app.state.user_manager.is_admin.return_value = True
    user_id, target_id, err = await cmd._setup_command_execution(app, "Admin", "Missing", player_service)
    assert user_id is not None
    assert target_id is None
    assert "not found" in err["result"]


@pytest.mark.asyncio
async def test_resolve_target_player_uuid_id() -> None:
    target_uuid = uuid.uuid4()
    target = MagicMock(id=target_uuid)
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock(return_value=target)
    player_id, err = await cmd._resolve_target_player(player_service, "Alice")
    assert err is None
    assert player_id == target_uuid


@pytest.mark.asyncio
async def test_apply_lucidity_change_admin_logger_failure() -> None:
    target_id = uuid.uuid4()
    adjustment = LucidityUpdateResult(
        player_id=target_id,
        previous_lcd=50,
        new_lcd=60,
        previous_tier="lucid",
        new_tier="lucid",
        delta=10,
        liabilities_added=[],
    )
    session = AsyncMock()
    lucidity_service = AsyncMock()
    lucidity_service.apply_lucidity_adjustment = AsyncMock(return_value=adjustment)
    with patch("server.commands.admin_setlucidity_command.get_admin_actions_logger") as log_cls:
        log_cls.return_value.log_admin_command = MagicMock(side_effect=OSError("log disk full"))
        result = await cmd._apply_lucidity_change(
            cmd.LucidityChangeCtx(
                session=session,
                lucidity_service=lucidity_service,
                target_player_id=target_id,
                current_lcd=50,
                target_lcd=60,
                player_name="Admin",
                current_user_id="admin-id",
                target_player="Alice",
            )
        )
    assert result is not None
    assert "60" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_setlucidity_target_not_found() -> None:
    request = MagicMock()
    request.app = MagicMock()
    player_service = MagicMock()
    request.app.state.container = MagicMock()
    request.app.state.container.player_service = player_service
    request.app.state.user_manager = MagicMock()
    request.app.state.user_manager.is_admin.return_value = True
    admin_player = MagicMock(id=str(uuid.uuid4()))
    player_service.resolve_player_name = AsyncMock(side_effect=[admin_player, None])
    result = await cmd._handle_admin_set_lucidity_command(
        {"target_player": "Ghost", "lcd_value": 50}, {}, request, None, "Admin"
    )
    assert "not found" in result["result"]
