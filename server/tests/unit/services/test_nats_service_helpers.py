"""Additional NATSService coverage for helper and stats methods."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.nats_exceptions import NATSUnsubscribeError
from server.services.nats_service import NATSService


@pytest.fixture
def svc() -> NATSService:
    return NATSService()


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
    opts: dict[str, object] = {}
    svc._configure_tls(opts)
    assert opts == {}


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
    assert opts["token"] == "secret"


def test_build_connect_options_with_user_password() -> None:
    from server.config.models import NATSConfig

    svc = NATSService(NATSConfig(url="nats://localhost:4222", user="u", password="p"))
    opts = svc._build_connect_options()
    assert opts["user"] == "u"
    assert opts["password"] == "p"


def test_setup_connection_handlers_registers_listeners(svc: NATSService) -> None:
    nc = MagicMock()
    svc.nc = nc
    svc._setup_connection_handlers()
    nc.add_error_listener.assert_called_once()
    nc.add_disconnect_listener.assert_called_once()
    nc.add_reconnect_listener.assert_called_once()


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
    sub = AsyncMock()
    svc.subscriptions = {"topic": sub}
    await svc._drain_subscriptions()
    sub.drain.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_all_subscriptions(svc: NATSService) -> None:
    sub = AsyncMock()
    svc.subscriptions = {"topic": sub}
    await svc._close_all_subscriptions()
    sub.unsubscribe.assert_awaited_once()
    assert svc._unsubscription_count == 1


@pytest.mark.asyncio
async def test_close_nats_connection(svc: NATSService) -> None:
    nc = AsyncMock()
    svc.nc = nc
    svc.state_machine.connect()
    svc.state_machine.connected_successfully()
    svc.subscriptions["x"] = MagicMock()
    await svc._close_nats_connection()
    nc.close.assert_awaited_once()
    assert svc.nc is None
    assert svc._running is False


@pytest.mark.asyncio
async def test_call_callback_sync(svc: NATSService) -> None:
    seen: list[dict[str, object]] = []

    def sync_cb(data: dict[str, object]) -> None:
        seen.append(data)

    await svc._call_callback(sync_cb, {"a": 1})
    assert seen == [{"a": 1}]


@pytest.mark.asyncio
async def test_acknowledge_message_without_ack(svc: NATSService) -> None:
    msg = MagicMock(spec=[])
    ok = await svc._acknowledge_message(msg, "sub", {"message_id": "1"})
    assert ok is False


@pytest.mark.asyncio
async def test_acknowledge_message_success(svc: NATSService) -> None:
    msg = MagicMock()
    msg.ack = AsyncMock()
    ok = await svc._acknowledge_message(msg, "sub", {"message_id": "1"})
    assert ok is True
    msg.ack.assert_awaited_once()


@pytest.mark.asyncio
async def test_negatively_acknowledge_message(svc: NATSService) -> None:
    msg = MagicMock()
    msg.nak = AsyncMock()
    await svc._negatively_acknowledge_message(msg, "sub")
    msg.nak.assert_awaited_once()


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
    svc._create_tracked_task = MagicMock()
    svc._on_error(RuntimeError("x"))
    svc._create_tracked_task.assert_called_once()


def test_on_disconnect_creates_tracked_task(svc: NATSService) -> None:
    svc._create_tracked_task = MagicMock()
    svc._on_disconnect()
    svc._create_tracked_task.assert_called_once()


def test_on_reconnect_creates_tracked_task(svc: NATSService) -> None:
    svc._create_tracked_task = MagicMock()
    svc._on_reconnect()
    svc._create_tracked_task.assert_called_once()


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
    with patch("server.services.nats_service.nats.connect", AsyncMock(return_value=conn)):
        svc.pool_size = 2
        await svc._initialize_connection_pool()
    assert svc._pool_initialized is True
    assert len(svc.connection_pool) == 2


@pytest.mark.asyncio
async def test_initialize_connection_pool_all_fail(svc: NATSService) -> None:
    from unittest.mock import patch

    with patch("server.services.nats_service.nats.connect", AsyncMock(side_effect=OSError("down"))):
        svc.pool_size = 1
        await svc._initialize_connection_pool()
    assert svc._pool_initialized is False


@pytest.mark.asyncio
async def test_cleanup_connection_pool(svc: NATSService) -> None:
    conn = AsyncMock()
    svc.connection_pool = [conn]
    svc._pool_initialized = True
    await svc._cleanup_connection_pool()
    conn.close.assert_awaited_once()
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
    conn = AsyncMock()
    svc._pool_initialized = True
    svc.connection_pool = [conn]
    svc.config.enable_subject_validation = False
    await svc.available_connections.put(conn)
    await svc.publish_with_pool("events.test", {"message_id": "1"})
    conn.publish.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_message_handler_delivers_payload(svc: NATSService) -> None:
    handlers: list[object] = []

    async def capture_subscribe(_subject: str, cb: object) -> MagicMock:
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
    handlers: list[object] = []

    async def capture_subscribe(_subject: str, cb: object) -> MagicMock:
        handlers.append(cb)
        return MagicMock()

    svc.nc = MagicMock()
    svc.nc.subscribe = capture_subscribe
    svc._running = True
    await svc.subscribe("chat.room", lambda _d: None)
    msg = MagicMock()
    msg.data = b"not-json"
    msg.nak = AsyncMock()
    await handlers[0](msg)
    msg.nak.assert_awaited_once()


@pytest.mark.asyncio
async def test_acknowledge_message_failure(svc: NATSService) -> None:
    msg = MagicMock()
    msg.ack = AsyncMock(side_effect=RuntimeError("ack failed"))
    ok = await svc._acknowledge_message(msg, "sub", {"message_id": "1"})
    assert ok is False


@pytest.mark.asyncio
async def test_start_health_monitoring_creates_task(svc: NATSService) -> None:
    svc.config.health_check_interval = 30
    svc._health_check_task = None
    svc._create_tracked_task = MagicMock(return_value=AsyncMock())
    await svc._start_health_monitoring()
    svc._create_tracked_task.assert_called_once()


def test_configure_tls_adds_ssl_context(svc: NATSService) -> None:
    svc.config.tls_enabled = True
    svc.config.tls_verify = False
    svc.config.tls_cert_file = None
    svc.config.tls_key_file = None
    svc.config.tls_ca_file = None
    opts: dict[str, object] = {}
    svc._configure_tls(opts)
    assert "tls" in opts


@pytest.mark.asyncio
async def test_initialize_connection_pool_partial_success(svc: NATSService) -> None:
    from unittest.mock import patch

    conn = AsyncMock()
    with patch(
        "server.services.nats_service.nats.connect",
        AsyncMock(side_effect=[conn, OSError("second failed")]),
    ):
        svc.pool_size = 2
        await svc._initialize_connection_pool()
    assert svc._pool_initialized is True
    assert len(svc.connection_pool) == 1
