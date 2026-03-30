# pyright: reportPrivateUsage=false
# Tests call monitoring module-private resolvers and singleton state intentionally.
"""Unit tests for server.api.monitoring routes and resolvers."""

from __future__ import annotations

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request

from server.api.monitoring import (
    _resolve_cache_manager_from_request,
    _resolve_connection_manager_from_request,
    _resolve_event_bus_from_request,
    _resolve_memory_leak_collector,
    force_memory_cleanup,
    get_cache_metrics,
    get_connection_health_stats,
    get_dual_connection_stats,
    get_eventbus_metrics,
    get_memory_alerts,
    get_memory_leak_metrics,
    get_memory_stats,
    get_movement_metrics,
    get_performance_stats,
    get_performance_summary,
    get_system_alerts,
    get_task_metrics,
    monitoring_router,
    reset_metrics,
    validate_room_integrity,
)
from server.exceptions import LoggedHTTPException
from server.game.movement_monitor import MovementMonitor
from server.models.health import HealthResponse, HealthStatus
from server.monitoring.memory_leak_metrics import MemoryLeakMetricsCollector


def _request_with_container(**attrs: MagicMock | None) -> MagicMock:
    container: MagicMock = MagicMock()
    for key, value in attrs.items():
        setattr(container, key, value)
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    return req


@pytest.mark.asyncio
async def test_get_movement_metrics_uses_monitor() -> None:
    monitor = MovementMonitor()
    with patch("server.api.monitoring.get_movement_monitor", return_value=monitor):
        out = await get_movement_metrics(MagicMock(spec=Request))
    assert out.total_movements == 0
    assert isinstance(out.timestamp, str)


@pytest.mark.asyncio
async def test_get_movement_metrics_logged_http_on_failure() -> None:
    with patch("server.api.monitoring.get_movement_monitor", side_effect=RuntimeError("x")):
        with pytest.raises(LoggedHTTPException):
            _ = await get_movement_metrics(MagicMock(spec=Request))


@pytest.mark.asyncio
async def test_validate_room_integrity_builds_room_map() -> None:
    monitor = MovementMonitor()
    room: MagicMock = MagicMock()
    room.id = "r1"
    get_players_m: MagicMock = MagicMock(return_value=[])
    room.get_players = get_players_m
    persistence: MagicMock = MagicMock()
    list_rooms_m: MagicMock = MagicMock(return_value=[room])
    persistence.list_rooms = list_rooms_m
    with patch("server.api.monitoring.get_movement_monitor", return_value=monitor):
        out = await validate_room_integrity(MagicMock(spec=Request), persistence)
    assert out.total_rooms == 1
    assert isinstance(out.timestamp, str)


@pytest.mark.asyncio
async def test_get_system_alerts_returns_counts() -> None:
    monitor = MovementMonitor()
    with patch("server.api.monitoring.get_movement_monitor", return_value=monitor):
        out = await get_system_alerts(MagicMock(spec=Request))
    assert isinstance(out.alerts, list)
    assert out.alert_count == len(out.alerts)


@pytest.mark.asyncio
async def test_reset_movement_metrics_calls_reset() -> None:
    with patch("server.game.movement_monitor.reset_movement_monitor") as rm_patch:
        reset_m: MagicMock = rm_patch
        out = await reset_metrics(MagicMock(spec=Request))
        reset_m.assert_called_once()
    assert "reset" in out.message.lower()


@pytest.mark.asyncio
async def test_get_performance_summary_delegates_to_monitor() -> None:
    monitor: MagicMock = MagicMock()
    perf_m: MagicMock = MagicMock(
        return_value={"summary": {}, "alerts": [], "timestamp": "t"},
    )
    monitor.get_performance_summary = perf_m
    with patch("server.api.monitoring.get_movement_monitor", return_value=monitor):
        out = await get_performance_summary(MagicMock(spec=Request))
    assert out.timestamp == "t"


def _connection_manager_stub() -> MagicMock:
    cm: MagicMock = MagicMock()
    cm.get_memory_stats = MagicMock(
        return_value={
            "memory": {},
            "connections": {},
            "data_structures": {},
            "cleanup_stats": {},
            "memory_monitor": {},
        },
    )
    cm.get_memory_alerts = MagicMock(return_value=[])
    cm.force_cleanup = AsyncMock()
    cm.get_dual_connection_stats = MagicMock(
        return_value={
            "connection_distribution": {},
            "connection_health": {},
            "session_metrics": {},
            "connection_lifecycle": {},
            "performance_metrics": {},
            "timestamp": 0.0,
        },
    )
    cm.get_performance_stats = MagicMock(
        return_value={
            "connection_establishment": {},
            "message_delivery": {},
            "disconnections": {},
            "session_management": {},
            "health_monitoring": {},
            "timestamp": 0.0,
        },
    )
    cm.get_connection_health_stats = MagicMock(
        return_value={
            "overall_health": {},
            "connection_type_health": {},
            "connection_lifecycle": {},
            "session_health": {},
            "health_trends": {},
            "timestamp": 0.0,
        },
    )
    return cm


@pytest.mark.asyncio
async def test_get_memory_stats_with_leak_collector() -> None:
    cm = _connection_manager_stub()
    req = _request_with_container(connection_manager=cm)
    mock_coll: MagicMock = MagicMock()
    collect_m: MagicMock = MagicMock(
        return_value={"connection": {}, "event": {}, "cache": {}, "task": {}, "nats": {}},
    )
    check_alerts_m: MagicMock = MagicMock(return_value=[])
    mock_coll.collect_all_metrics = collect_m
    mock_coll.check_alerts = check_alerts_m
    with patch("server.api.monitoring.resolve_connection_manager", return_value=cm):
        with patch("server.api.monitoring._resolve_memory_leak_collector", return_value=mock_coll):
            out = await get_memory_stats(req)
    collect_m.assert_called()
    assert out.timestamp


@pytest.mark.asyncio
async def test_get_memory_stats_leak_collector_warning_branch() -> None:
    cm = _connection_manager_stub()
    req = _request_with_container(connection_manager=cm)

    def _boom() -> None:
        raise RuntimeError("no collector")

    with patch("server.api.monitoring.resolve_connection_manager", return_value=cm):
        with patch("server.api.monitoring._resolve_memory_leak_collector", side_effect=_boom):
            out = await get_memory_stats(req)
    assert out.timestamp


@pytest.mark.asyncio
async def test_memory_alerts_and_force_cleanup() -> None:
    cm = _connection_manager_stub()
    req = _request_with_container(connection_manager=cm)
    force_m: AsyncMock = cast(AsyncMock, cm.force_cleanup)
    with patch("server.api.monitoring.resolve_connection_manager", return_value=cm):
        alerts = await get_memory_alerts(req)
        assert alerts.alert_count == 0
        msg = await force_memory_cleanup(req)
    force_m.assert_awaited_once()
    assert "completed" in msg.message.lower()


@pytest.mark.asyncio
async def test_dual_connection_and_performance_and_health_stats() -> None:
    cm = _connection_manager_stub()
    req = _request_with_container(connection_manager=cm)
    mock_coll: MagicMock = MagicMock()
    collect_m: MagicMock = MagicMock(return_value={"connection": {}})
    check_alerts_m: MagicMock = MagicMock(return_value=["a"])
    mock_coll.collect_all_metrics = collect_m
    mock_coll.check_alerts = check_alerts_m
    with patch("server.api.monitoring.resolve_connection_manager", return_value=cm):
        with patch("server.api.monitoring._resolve_memory_leak_collector", return_value=mock_coll):
            d = await get_dual_connection_stats(req)
            p = await get_performance_stats(req)
            h = await get_connection_health_stats(req)
    assert d.timestamp == 0.0
    assert p.timestamp == 0.0
    assert h.timestamp == 0.0
    collect_m.assert_called()


def test_resolve_connection_manager_from_request() -> None:
    cm: MagicMock = MagicMock()
    req = _request_with_container(connection_manager=cm)
    with patch("server.api.monitoring.resolve_connection_manager", return_value=cm):
        assert _resolve_connection_manager_from_request(req) is cm


def test_resolve_event_bus_from_request() -> None:
    bus: MagicMock = MagicMock()
    req = _request_with_container(event_bus=bus)
    assert _resolve_event_bus_from_request(req) is bus


def test_resolve_event_bus_missing_raises() -> None:
    container: MagicMock = MagicMock()
    container.event_bus = None
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    with pytest.raises(RuntimeError, match="EventBus"):
        _resolve_event_bus_from_request(req)


def test_resolve_cache_manager_from_container() -> None:
    mgr: MagicMock = MagicMock()
    stats_m: MagicMock = MagicMock(return_value={})
    mgr.get_all_stats = stats_m
    req = _request_with_container(cache_manager=mgr)
    assert _resolve_cache_manager_from_request(req) is mgr


def test_resolve_cache_manager_fallback_global() -> None:
    container: MagicMock = MagicMock()
    container.cache_manager = None
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    mock_mgr: MagicMock = MagicMock()
    get_stats_m: MagicMock = MagicMock(return_value={})
    mock_mgr.get_all_stats = get_stats_m
    with patch("server.caching.lru_cache.get_cache_manager", return_value=mock_mgr):
        assert _resolve_cache_manager_from_request(req) is mock_mgr


@pytest.mark.asyncio
async def test_get_cache_metrics_builds_response() -> None:
    mgr: MagicMock = MagicMock()
    get_stats_m: MagicMock = MagicMock(
        return_value={
            "c1": {
                "size": 1,
                "hit_rate": 0.5,
                "expired_count": 0,
                "expiration_rate": 0.0,
                "capacity_utilization": 0.5,
            },
        },
    )
    mgr.get_all_stats = get_stats_m
    req = _request_with_container(cache_manager=mgr)
    with patch("server.api.monitoring._resolve_cache_manager_from_request", return_value=mgr):
        out = await get_cache_metrics(req)
    assert out.cache_sizes["c1"] == 1


@pytest.mark.asyncio
async def test_get_eventbus_metrics_shapes() -> None:
    bus: MagicMock = MagicMock()
    sub_counts_m: MagicMock = MagicMock(return_value={"e": 1})
    lifecycle_m: MagicMock = MagicMock(
        return_value={
            "total_subscribers": 1,
            "subscription_churn_rate": 0.0,
            "subscription_count": 1,
            "unsubscription_count": 0,
            "recent_subscriptions_last_hour": 0,
            "recent_unsubscriptions_last_hour": 0,
        },
    )
    task_count_m: MagicMock = MagicMock(return_value=0)
    task_details_m: MagicMock = MagicMock(return_value=[])
    bus.get_all_subscriber_counts = sub_counts_m
    bus.get_subscriber_lifecycle_metrics = lifecycle_m
    bus.get_active_task_count = task_count_m
    bus.get_active_task_details = task_details_m
    req = _request_with_container(event_bus=bus)
    out = await get_eventbus_metrics(req)
    assert out.total_subscribers == 1


@pytest.mark.asyncio
async def test_get_task_metrics_from_registry() -> None:
    reg: MagicMock = MagicMock()
    lifecycle_m: MagicMock = MagicMock(
        return_value={
            "active_task_count": 0,
            "task_creation_count": 0,
            "task_completion_count": 0,
            "task_cancellation_count": 0,
            "tasks_by_type": {},
            "tasks_by_service": {},
            "task_creation_rate": 0,
            "task_completion_rate": 0,
            "orphaned_task_count": 0,
            "lifecycle_tasks_count": 0,
        },
    )
    reg.get_task_lifecycle_metrics = lifecycle_m
    with patch("server.api.monitoring._resolve_task_registry", return_value=reg):
        out = await get_task_metrics(MagicMock(spec=Request))
    assert out.active_task_count == 0


@pytest.mark.asyncio
async def test_get_memory_leak_metrics_endpoint() -> None:
    coll: MagicMock = MagicMock()
    collect_m: MagicMock = MagicMock(
        return_value={
            "connection": {},
            "event": {},
            "cache": {},
            "task": {},
            "nats": {},
            "timestamp": 1.0,
        },
    )
    growth_m: MagicMock = MagicMock(return_value={})
    alerts_m: MagicMock = MagicMock(return_value=[])
    coll.collect_all_metrics = collect_m
    coll.calculate_growth_rates = growth_m
    coll.check_alerts = alerts_m
    with patch("server.api.monitoring._resolve_memory_leak_collector", return_value=coll):
        out = await get_memory_leak_metrics(MagicMock(spec=Request))
    assert out.timestamp == 1.0


def test_resolve_memory_leak_collector_singleton_resets_with_patch() -> None:
    import server.api.monitoring as mon  # noqa: PLC0415

    prev: MemoryLeakMetricsCollector | None = cast(
        MemoryLeakMetricsCollector | None,
        mon._memory_leak_collector_instance,  # noqa: SLF001
    )
    try:
        mon._memory_leak_collector_instance = None  # noqa: SLF001
        c1 = cast(MemoryLeakMetricsCollector, _resolve_memory_leak_collector())
        c2 = cast(MemoryLeakMetricsCollector, _resolve_memory_leak_collector())
        assert c1 is c2
    finally:
        mon._memory_leak_collector_instance = prev  # noqa: SLF001


@pytest.mark.asyncio
async def test_get_health_status_healthy_returns_model() -> None:
    from server.api.monitoring import get_health_status  # noqa: PLC0415
    from server.models.health import (  # noqa: PLC0415
        ConnectionsComponent,
        DatabaseComponent,
        ServerComponent,
    )

    cm: MagicMock = MagicMock()
    hs: MagicMock = MagicMock()
    hs.health_check_timeout_seconds = 5.0
    server_h_m: MagicMock = MagicMock(
        return_value=ServerComponent(
            status=HealthStatus.HEALTHY,
            uptime_seconds=1.0,
            memory_usage_mb=1.0,
            cpu_usage_percent=0.0,
        ),
    )
    hs.get_server_component_health = server_h_m
    hs.get_database_component_health_async = AsyncMock(
        return_value=DatabaseComponent(status=HealthStatus.HEALTHY, connection_count=0, last_query_time_ms=None),
    )
    conn_h_m: MagicMock = MagicMock(
        return_value=ConnectionsComponent(
            status=HealthStatus.HEALTHY,
            active_connections=0,
            max_connections=10,
            connection_rate_per_minute=0.0,
        ),
    )
    hs.get_connections_component_health = conn_h_m
    overall_m: MagicMock = MagicMock(return_value=HealthStatus.HEALTHY)
    alerts_m: MagicMock = MagicMock(return_value=[])
    uptime_m: MagicMock = MagicMock(return_value=1.0)
    hs.determine_overall_status = overall_m
    hs.generate_alerts = alerts_m
    hs.get_server_uptime = uptime_m

    req = _request_with_container(connection_manager=cm)
    with patch("server.api.monitoring.get_health_service", return_value=hs):
        with patch("importlib.metadata.version", return_value="0.test"):
            out = await get_health_status(req)
    assert isinstance(out, HealthResponse)
    assert out.status == HealthStatus.HEALTHY


def test_monitoring_router_has_expected_prefix() -> None:
    assert monitoring_router.prefix == "/monitoring"
