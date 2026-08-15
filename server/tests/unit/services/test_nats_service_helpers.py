"""Additional NATSService coverage for helper and stats methods."""

# pylint: disable=protected-access  # Reason: white-box tests cover NATSService helpers
# pyright: reportPrivateUsage=false

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable, Coroutine
from inspect import CORO_CLOSED, getcoroutinestate
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.nats_exceptions import NATSUnsubscribeError
from server.services.nats_service import NATSService

# Subscribe callback shape used when capturing NATS message handlers in tests.
_NatsMsgHandler = Callable[[object], Awaitable[None]]


@pytest.fixture
def svc() -> NATSService:
    return NATSService()


def _mock_create_tracked_task(svc: NATSService) -> MagicMock:
    """Mock scheduler that closes the coro (MagicMock does not await it)."""

    def _side_effect(coro: object, *_args: object, **_kwargs: object) -> AsyncMock:
        if asyncio.iscoroutine(coro):
            coro.close()
        return AsyncMock()

    mock = MagicMock(side_effect=_side_effect)
    svc._create_tracked_task = mock
    return mock


def _assert_tracked_coro_closed(mock: MagicMock) -> None:
    """Assert the first positional arg to mock was a coroutine and is now closed."""
    assert mock.call_args is not None
    coro = cast(object, mock.call_args.args[0])
    assert asyncio.iscoroutine(coro)
    assert getcoroutinestate(coro) == CORO_CLOSED


def test_check_connection_allowed_when_permitted(svc: NATSService) -> None:
    assert svc.state_machine.state.id == "disconnected"
    svc.state_machine.can_attempt_connection = MagicMock(return_value=True)
    svc.state_machine.connect = MagicMock()
    assert svc._check_connection_allowed() is True
    svc.state_machine.connect.assert_called_once()


def test_check_connection_blocked_by_state_machine(svc: NATSService) -> None:
    svc.state_machine.can_attempt_connection = MagicMock(return_value=False)
    assert svc._check_connection_allowed() is False


def test_build_connect_options_includes_reconnect(svc: NATSService) -> None:
    opts = svc._build_connect_options()
    assert opts["max_reconnect_attempts"] == svc._max_retries


def test_configure_tls_noop_without_tls_config(svc: NATSService) -> None:
    opts = svc._build_connect_options()
    snapshot = dict(opts)
    svc._configure_tls(opts)
    assert opts == snapshot


def test_get_connection_stats(svc: NATSService) -> None:
    stats = svc.get_connection_stats()
    assert isinstance(stats, dict)


def test_get_active_subscriptions_empty(svc: NATSService) -> None:
    assert svc.get_active_subscriptions() == []


def test_get_subscription_count(svc: NATSService) -> None:
    assert svc.get_subscription_count() == 0


def test_is_connected_false_when_no_client(svc: NATSService) -> None:
    svc.nc = None
    assert svc.is_connected() is False


@pytest.mark.asyncio
async def test_decode_message_data_json(svc: NATSService) -> None:
    msg = MagicMock()
    msg.data = b'{"k": "v"}'
    decoded = await svc._decode_message_data(msg)
    assert decoded == {"k": "v"}


@pytest.mark.asyncio
async def test_call_callback_async(svc: NATSService) -> None:
    cb = AsyncMock()
    await svc._call_callback(cb, {"x": 1})
    cb.assert_awaited_once()


def test_verify_subscription_cleanup_report(svc: NATSService) -> None:
    report = svc.verify_subscription_cleanup()
    assert "active_subscriptions" in report


@pytest.mark.asyncio
async def test_unsubscribe_missing_subject_raises(svc: NATSService) -> None:
    with pytest.raises(NATSUnsubscribeError):
        await svc.unsubscribe("missing.subject")


def test_build_connect_options_with_token() -> None:
    from server.config.models import NATSConfig

    svc = NATSService(NATSConfig(url="nats://localhost:4222", token="secret"))
    opts = svc._build_connect_options()
    assert opts.get("token") == "secret"


@pytest.mark.asyncio
async def test_initialize_connection_pool_passes_auth_token() -> None:
    from server.config.models import NATSConfig

    svc = NATSService(NATSConfig(url="nats://localhost:4222", token="secret"))
    conn = AsyncMock()
    with patch("server.services.nats_service_pool.nats.connect", AsyncMock(return_value=conn)) as connect:
        svc.pool_size = 1
        await svc._initialize_connection_pool()
    assert connect.await_args is not None
    assert connect.await_args.kwargs["token"] == "secret"


def test_build_connect_options_with_user_password() -> None:
    from server.config.models import NATSConfig

    svc = NATSService(NATSConfig(url="nats://localhost:4222", user="u", password="p"))
    opts = svc._build_connect_options()
    assert opts.get("user") == "u"
    assert opts.get("password") == "p"


def test_setup_connection_handlers_registers_listeners(svc: NATSService) -> None:
    nc: MagicMock = MagicMock()
    add_error: MagicMock = MagicMock()
    add_disconnect: MagicMock = MagicMock()
    add_reconnect: MagicMock = MagicMock()
    nc.add_error_listener = add_error
    nc.add_disconnect_listener = add_disconnect
    nc.add_reconnect_listener = add_reconnect
    svc.nc = nc
    svc._setup_connection_handlers()
    add_error.assert_called_once()
    add_disconnect.assert_called_once()
    add_reconnect.assert_called_once()


def test_setup_connection_handlers_noop_without_client(svc: NATSService) -> None:
    svc.nc = None
    svc._setup_connection_handlers()


def test_verify_subscription_cleanup_success_logs(svc: NATSService) -> None:
    svc._verify_subscription_cleanup(["a.sub"])
    assert svc._last_cleanup_time is not None


def test_verify_subscription_cleanup_warns_on_remainder(svc: NATSService) -> None:
    svc.subscriptions["leftover"] = MagicMock()
    svc._verify_subscription_cleanup(["leftover", "other"])


@pytest.mark.asyncio
async def test_drain_subscriptions(svc: NATSService) -> None:
    sub: AsyncMock = AsyncMock()
    drain: AsyncMock = AsyncMock()
    sub.drain = drain
    svc.subscriptions = {"topic": sub}
    await svc._drain_subscriptions()
    drain.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_all_subscriptions(svc: NATSService) -> None:
    sub: AsyncMock = AsyncMock()
    unsubscribe: AsyncMock = AsyncMock()
    sub.unsubscribe = unsubscribe
    svc.subscriptions = {"topic": sub}
    await svc._close_all_subscriptions()
    unsubscribe.assert_awaited_once()
    assert svc._unsubscription_count == 1


@pytest.mark.asyncio
async def test_close_nats_connection(svc: NATSService) -> None:
    nc: AsyncMock = AsyncMock()
    close: AsyncMock = AsyncMock()
    nc.close = close
    svc.nc = nc
    svc.state_machine.connect()
    svc.state_machine.connected_successfully()
    svc.subscriptions["x"] = MagicMock()
    await svc._close_nats_connection()
    close.assert_awaited_once()
    assert svc.nc is None
    assert svc._running is False


@pytest.mark.asyncio
async def test_call_callback_sync(svc: NATSService) -> None:
    seen: list[dict[str, object]] = []

    def sync_cb(message_data: dict[str, object]) -> None:
        seen.append(message_data)

    await svc._call_callback(sync_cb, {"a": 1})
    assert seen == [{"a": 1}]


@pytest.mark.asyncio
async def test_acknowledge_message_without_ack(svc: NATSService) -> None:
    msg = MagicMock(spec=[])
    ok = await svc._acknowledge_message(msg, "sub", {"message_id": "1"})
    assert ok is False


@pytest.mark.asyncio
async def test_acknowledge_message_success(svc: NATSService) -> None:
    msg: MagicMock = MagicMock()
    ack: AsyncMock = AsyncMock()
    msg.ack = ack
    ok = await svc._acknowledge_message(msg, "sub", {"message_id": "1"})
    assert ok is True
    ack.assert_awaited_once()


@pytest.mark.asyncio
async def test_negatively_acknowledge_message(svc: NATSService) -> None:
    msg: MagicMock = MagicMock()
    nak: AsyncMock = AsyncMock()
    msg.nak = nak
    await svc._negatively_acknowledge_message(msg, "sub")
    nak.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_error_async_degrades_when_connected(svc: NATSService) -> None:
    svc.state_machine.connect()
    svc.state_machine.connected_successfully()
    svc.state_machine.degrade = MagicMock(wraps=svc.state_machine.degrade)
    await svc._handle_error_async(RuntimeError("boom"))
    svc.state_machine.degrade.assert_called_once()


@pytest.mark.asyncio
async def test_handle_disconnect_async_starts_reconnect(svc: NATSService) -> None:
    svc.state_machine.connect()
    svc.state_machine.connected_successfully()
    await svc._handle_disconnect_async()
    assert svc._running is False
    assert svc.state_machine.state.id == "reconnecting"


@pytest.mark.asyncio
async def test_handle_reconnect_async_from_reconnecting(svc: NATSService) -> None:
    svc.state_machine.connect()
    svc.state_machine.connected_successfully()
    await svc._handle_disconnect_async()
    assert svc.state_machine.state.id == "reconnecting"
    await svc._handle_reconnect_async()
    assert svc._running is True
    assert svc.state_machine.state.id == "connected"


def test_on_error_creates_tracked_task(svc: NATSService) -> None:
    mock = _mock_create_tracked_task(svc)
    svc._on_error(RuntimeError("x"))
    mock.assert_called_once()
    _assert_tracked_coro_closed(mock)


def test_on_disconnect_creates_tracked_task(svc: NATSService) -> None:
    mock = _mock_create_tracked_task(svc)
    svc._on_disconnect()
    mock.assert_called_once()
    _assert_tracked_coro_closed(mock)


def test_on_reconnect_creates_tracked_task(svc: NATSService) -> None:
    mock = _mock_create_tracked_task(svc)
    svc._on_reconnect()
    mock.assert_called_once()
    _assert_tracked_coro_closed(mock)


def test_is_connected_stale_health_check(svc: NATSService) -> None:
    import time

    svc.nc = MagicMock()
    svc._running = True
    svc.config.health_check_interval = 30
    svc._last_health_check = time.monotonic() - 100
    assert svc.is_connected() is False


def test_is_connected_too_many_failures(svc: NATSService) -> None:
    svc.nc = MagicMock()
    svc._running = True
    svc.config.health_check_interval = 30
    svc._last_health_check = 0
    svc._consecutive_health_failures = 3
    assert svc.is_connected() is False


@pytest.mark.asyncio
async def test_initialize_connection_pool_success(svc: NATSService) -> None:
    from unittest.mock import patch

    conn = AsyncMock()
    with patch("server.services.nats_service_pool.nats.connect", AsyncMock(return_value=conn)):
        svc.pool_size = 2
        await svc._initialize_connection_pool()
    assert svc._pool_initialized is True
    assert len(svc.connection_pool) == 2


@pytest.mark.asyncio
async def test_initialize_connection_pool_all_fail(svc: NATSService) -> None:
    from unittest.mock import patch

    with patch("server.services.nats_service_pool.nats.connect", AsyncMock(side_effect=OSError("down"))):
        svc.pool_size = 1
        await svc._initialize_connection_pool()
    assert svc._pool_initialized is False


@pytest.mark.asyncio
async def test_cleanup_connection_pool(svc: NATSService) -> None:
    conn: AsyncMock = AsyncMock()
    close: AsyncMock = AsyncMock()
    conn.close = close
    svc.connection_pool = [conn]
    svc._pool_initialized = True
    await svc._cleanup_connection_pool()
    close.assert_awaited_once()
    assert svc.connection_pool == []
    assert svc._pool_initialized is False


@pytest.mark.asyncio
async def test_initialize_connection_pool_skips_when_ready(svc: NATSService) -> None:
    svc._pool_initialized = True
    await svc._initialize_connection_pool()


@pytest.mark.asyncio
async def test_get_and_return_connection(svc: NATSService) -> None:
    conn = AsyncMock()
    svc._pool_initialized = True
    svc.connection_pool = [conn]
    await svc.available_connections.put(conn)
    got = await svc._get_connection()
    assert got is conn
    await svc._return_connection(conn)
    assert not svc.available_connections.empty()


@pytest.mark.asyncio
async def test_publish_with_pool_success(svc: NATSService) -> None:
    conn: AsyncMock = AsyncMock()
    publish: AsyncMock = AsyncMock()
    conn.publish = publish
    svc._pool_initialized = True
    svc.connection_pool = [conn]
    svc.config.enable_subject_validation = False
    await svc.available_connections.put(conn)
    await svc.publish_with_pool("events.test", {"message_id": "1"})
    publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_message_handler_delivers_payload(svc: NATSService) -> None:
    handlers: list[_NatsMsgHandler] = []

    async def capture_subscribe(_subject: str, cb: _NatsMsgHandler) -> MagicMock:
        handlers.append(cb)
        return MagicMock()

    svc.nc = MagicMock()
    svc.nc.subscribe = capture_subscribe
    svc._running = True
    user_cb = AsyncMock()
    await svc.subscribe("chat.room", user_cb)
    msg = MagicMock()
    msg.data = b'{"message_id": "m1", "sender_id": "p1"}'
    await handlers[0](msg)
    user_cb.assert_awaited_once_with({"message_id": "m1", "sender_id": "p1"})


@pytest.mark.asyncio
async def test_subscribe_message_handler_bad_json_with_manual_ack(svc: NATSService) -> None:
    from server.config.models import NATSConfig

    svc = NATSService(NATSConfig(url="nats://localhost:4222", manual_ack=True))
    handlers: list[_NatsMsgHandler] = []

    async def capture_subscribe(_subject: str, cb: _NatsMsgHandler) -> MagicMock:
        handlers.append(cb)
        return MagicMock()

    svc.nc = MagicMock()
    svc.nc.subscribe = capture_subscribe
    svc._running = True

    def unused_cb(message_data: dict[str, object]) -> None:
        _ = message_data

    await svc.subscribe("chat.room", unused_cb)
    msg: MagicMock = MagicMock()
    nak: AsyncMock = AsyncMock()
    msg.data = b"not-json"
    msg.nak = nak
    await handlers[0](msg)
    nak.assert_awaited_once()


@pytest.mark.asyncio
async def test_acknowledge_message_failure(svc: NATSService) -> None:
    msg = MagicMock()
    msg.ack = AsyncMock(side_effect=RuntimeError("ack failed"))
    ok = await svc._acknowledge_message(msg, "sub", {"message_id": "1"})
    assert ok is False


@pytest.mark.asyncio
async def test_start_health_monitoring_creates_task(svc: NATSService) -> None:
    """Regression: mocked _create_tracked_task must close _health_check_loop coro."""
    svc.config.health_check_interval = 30
    svc._health_check_task = None
    mock = _mock_create_tracked_task(svc)
    await svc._start_health_monitoring()
    mock.assert_called_once()
    _assert_tracked_coro_closed(mock)


def test_configure_tls_adds_ssl_context(svc: NATSService) -> None:
    svc.config.tls_enabled = True
    svc.config.tls_verify = False
    svc.config.tls_cert_file = None
    svc.config.tls_key_file = None
    svc.config.tls_ca_file = None
    opts = svc._build_connect_options()
    svc._configure_tls(opts)
    assert "tls" in opts


@pytest.mark.asyncio
async def test_initialize_connection_pool_partial_success(svc: NATSService) -> None:
    from unittest.mock import patch

    conn = AsyncMock()
    with patch(
        "server.services.nats_service_pool.nats.connect",
        AsyncMock(side_effect=[conn, OSError("second failed")]),
    ):
        svc.pool_size = 2
        await svc._initialize_connection_pool()
    assert svc._pool_initialized is True
    assert len(svc.connection_pool) == 1


def test_create_tracked_task_closes_coro_when_create_task_fails(
    svc: NATSService, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Regression: unscheduled coro is closed when create_task has no loop."""

    async def _noop() -> None:
        return None

    def _boom(*_args: object, **_kwargs: object) -> None:
        raise RuntimeError("no running event loop")

    monkeypatch.setattr(asyncio, "create_task", _boom)
    coro = _noop()
    with pytest.raises(RuntimeError):
        _ = svc._create_tracked_task(coro, task_name="no_loop")
    assert getcoroutinestate(coro) == CORO_CLOSED


def test_on_error_closes_coro_when_create_task_fails(svc: NATSService, monkeypatch: pytest.MonkeyPatch) -> None:
    """Regression: _on_error must close _handle_error_async when scheduling fails."""
    created: list[Coroutine[object, object, None]] = []
    original = svc._handle_error_async

    def _tracking_handler(error: BaseException) -> Coroutine[object, object, None]:
        coro = original(error)
        created.append(coro)
        return coro

    def _boom(*_args: object, **_kwargs: object) -> None:
        raise RuntimeError("no running event loop")

    monkeypatch.setattr(asyncio, "create_task", _boom)
    monkeypatch.setattr(svc, "_handle_error_async", _tracking_handler)
    svc._on_error(RuntimeError("nats blew up"))
    assert len(created) == 1
    assert getcoroutinestate(created[0]) == CORO_CLOSED
