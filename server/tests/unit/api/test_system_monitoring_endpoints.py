"""Unit tests for server.api.system_monitoring resolvers.

#679: get_system_metrics() used to construct its own MemoryLeakMetricsCollector() per request
(losing all growth-rate history between calls); it now resolves the container-owned instance via
_resolve_memory_leak_collector_from_request(), mirroring server.api.monitoring's pattern.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from fastapi import Request

from server.api.system_monitoring import (
    _resolve_memory_leak_collector_from_request,
    get_system_metrics,
)

# pyright: reportPrivateUsage=false
# Reason: tests call the module-private resolver intentionally.


def _request_with_container(**attrs: object) -> MagicMock:
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


def test_resolve_memory_leak_collector_from_request_returns_container_instance() -> None:
    collector = MagicMock()
    req = _request_with_container(memory_leak_collector=collector)
    assert _resolve_memory_leak_collector_from_request(req) is collector


def test_resolve_memory_leak_collector_from_request_none_when_unset() -> None:
    req = _request_with_container(memory_leak_collector=None)
    assert _resolve_memory_leak_collector_from_request(req) is None


def test_resolve_memory_leak_collector_from_request_none_when_no_container() -> None:
    state: MagicMock = MagicMock(spec=[])
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    assert _resolve_memory_leak_collector_from_request(req) is None


@pytest.mark.asyncio
async def test_get_system_metrics_includes_memory_leak_metrics() -> None:
    """The collector resolved from the container is reused, not rebuilt per request."""
    dashboard = MagicMock()
    dashboard.export_monitoring_data.return_value = {}
    collector = MagicMock()
    collector.collect_all_metrics.return_value = {
        "connection": {"active": 1},
        "event": {},
        "cache": {},
        "task": {},
        "nats": {},
    }
    collector.check_alerts.return_value = []
    collector.calculate_growth_rates.return_value = {}
    req = _request_with_container(memory_leak_collector=collector)

    with (
        patch("server.api.system_monitoring.get_monitoring_dashboard", return_value=dashboard),
        patch("server.caching.lru_cache.get_cache_manager", side_effect=RuntimeError("no cache manager")),
    ):
        result = await get_system_metrics(req)

    leak_metrics = getattr(result, "memory_leak_metrics")  # noqa: B009  # extra="allow" field, no static attr
    assert leak_metrics["connection"] == {"active": 1}
    collector.collect_all_metrics.assert_called_once()


@pytest.mark.asyncio
async def test_get_system_metrics_handles_missing_collector_gracefully() -> None:
    """No collector on the container -- endpoint still succeeds, just without leak metrics."""
    dashboard = MagicMock()
    dashboard.export_monitoring_data.return_value = {}
    req = _request_with_container(memory_leak_collector=None)

    with (
        patch("server.api.system_monitoring.get_monitoring_dashboard", return_value=dashboard),
        patch("server.caching.lru_cache.get_cache_manager", side_effect=RuntimeError("no cache manager")),
    ):
        result = await get_system_metrics(req)

    assert not hasattr(result, "memory_leak_metrics")
