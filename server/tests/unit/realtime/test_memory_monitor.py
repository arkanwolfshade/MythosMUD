"""Unit tests for MemoryMonitor."""

# pyright: reportPrivateUsage=false
# Reason: unit tests import memory_monitor private helpers (_SAMPLE_KEYS, _max_connection_age_seconds).

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock, patch

import pytest

from server.realtime.memory_monitor import (
    _SAMPLE_KEYS,
    IDLE_SAMPLER_ENV,
    MemoryMonitor,
    _max_connection_age_seconds,
    collect_idle_memory_sample,
    idle_sampler_enabled,
    idle_sampler_interval_seconds,
    idle_sampler_path,
)


def test_max_connection_age_local() -> None:
    with patch.dict("os.environ", {"LOGGING_ENVIRONMENT": "local"}):
        assert _max_connection_age_seconds() == 1800


def test_max_connection_age_default() -> None:
    with patch.dict("os.environ", {"LOGGING_ENVIRONMENT": "prod"}, clear=False):
        assert _max_connection_age_seconds() == 300


def test_should_cleanup_time_based() -> None:
    monitor = MemoryMonitor()
    monitor.last_cleanup_time = 0.0
    monitor.cleanup_interval = 1
    with patch.object(monitor, "get_memory_usage", return_value=0.1):
        assert monitor.should_cleanup() is True


def test_should_cleanup_memory_threshold() -> None:
    monitor = MemoryMonitor()
    monitor.last_cleanup_time = time.time()
    with patch.object(monitor, "get_memory_usage", return_value=0.85):
        assert monitor.should_cleanup() is True


def test_get_memory_usage_success() -> None:
    monitor = MemoryMonitor()
    process: MagicMock = MagicMock(memory_percent=MagicMock(return_value=42.0))
    with patch("server.realtime.memory_monitor.psutil.Process", return_value=process):
        assert monitor.get_memory_usage() == 0.42


def test_get_memory_usage_error_returns_zero() -> None:
    monitor = MemoryMonitor()
    with patch("server.realtime.memory_monitor.psutil.Process", side_effect=OSError("fail")):
        assert monitor.get_memory_usage() == 0.0


def test_get_memory_stats() -> None:
    monitor = MemoryMonitor()
    process: MagicMock = MagicMock(
        memory_info=MagicMock(return_value=MagicMock(rss=1024 * 1024, vms=2048 * 1024)),
        memory_percent=MagicMock(return_value=10.0),
    )
    vm: MagicMock = MagicMock(available=512 * 1024 * 1024, total=1024 * 1024 * 1024)
    with (
        patch("server.realtime.memory_monitor.psutil.Process", return_value=process),
        patch("server.realtime.memory_monitor.psutil.virtual_memory", return_value=vm),
    ):
        stats = monitor.get_memory_stats()
    assert stats["rss_mb"] == 1.0
    assert stats["percent"] == 10.0


def test_get_memory_alerts() -> None:
    monitor = MemoryMonitor()
    with patch.object(monitor, "get_memory_usage", return_value=0.91):
        alerts = monitor.get_memory_alerts(
            {"connection_attempts": 2000, "pending_messages": 2000, "stale_connections": 2}
        )
    assert any("CRITICAL" in alert for alert in alerts)
    assert any("rate limit" in alert.lower() for alert in alerts)


def test_update_cleanup_time_and_gc() -> None:
    monitor = MemoryMonitor()
    monitor.update_cleanup_time()
    assert monitor.last_cleanup_time > 0
    monitor.force_garbage_collection()


def test_should_cleanup_returns_false() -> None:
    monitor = MemoryMonitor()
    monitor.last_cleanup_time = time.time()
    with patch.object(monitor, "get_memory_usage", return_value=0.1):
        assert monitor.should_cleanup() is False


def test_max_connection_age_e2e() -> None:
    with patch.dict("os.environ", {"LOGGING_ENVIRONMENT": "e2e_test"}):
        assert _max_connection_age_seconds() == 1800


def test_get_memory_stats_error_returns_empty() -> None:
    monitor = MemoryMonitor()
    with patch("server.realtime.memory_monitor.psutil.Process", side_effect=OSError("fail")):
        assert monitor.get_memory_stats() == {}


def test_get_memory_alerts_warning_and_info_levels() -> None:
    monitor = MemoryMonitor()
    with patch.object(monitor, "get_memory_usage", return_value=0.75):
        alerts = monitor.get_memory_alerts({})
    assert any("INFO" in a for a in alerts)
    with patch.object(monitor, "get_memory_usage", return_value=0.82):
        alerts = monitor.get_memory_alerts({})
    assert any("WARNING" in a for a in alerts)


def test_get_memory_alerts_error_path() -> None:
    monitor = MemoryMonitor()
    with patch.object(monitor, "get_memory_usage", side_effect=RuntimeError("boom")):
        alerts = monitor.get_memory_alerts({})
    assert any("ERROR" in a for a in alerts)


def test_force_garbage_collection_runtime_error() -> None:
    monitor = MemoryMonitor()
    with patch("server.realtime.memory_monitor.gc.collect", side_effect=RuntimeError("gc fail")):
        monitor.force_garbage_collection()


def test_get_memory_usage_invalid_type() -> None:
    monitor = MemoryMonitor()
    process: MagicMock = MagicMock(memory_percent=MagicMock(return_value="bad"))
    with patch("server.realtime.memory_monitor.psutil.Process", return_value=process):
        assert monitor.get_memory_usage() == 0.0


def test_idle_sampler_disabled_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(IDLE_SAMPLER_ENV, raising=False)
    assert idle_sampler_enabled() is False
    monitor = MemoryMonitor()
    assert monitor.is_idle_sampler_running() is False


def test_idle_sampler_interval_and_path(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("MYTHOSMUD_IDLE_MEMORY_SAMPLER_INTERVAL", "not-a-number")
    assert idle_sampler_interval_seconds() == 60.0
    monkeypatch.setenv("MYTHOSMUD_IDLE_MEMORY_SAMPLER_INTERVAL", "0.25")
    assert idle_sampler_interval_seconds() == 1.0
    monkeypatch.setenv("MYTHOSMUD_IDLE_MEMORY_SAMPLER_PATH", str(tmp_path / "samples.jsonl"))
    assert idle_sampler_path() == tmp_path / "samples.jsonl"


def test_collect_idle_sample_shape() -> None:
    sample = collect_idle_memory_sample()
    assert tuple(sample.keys()) == _SAMPLE_KEYS
    assert isinstance(sample["rss_bytes"], int)
    assert isinstance(sample["top_alloc_sites"], list)
    for site in sample["top_alloc_sites"]:
        assert set(site.keys()) == {"file", "size"}


@pytest.mark.asyncio
async def test_idle_sampler_stays_stopped_when_disabled(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(IDLE_SAMPLER_ENV, raising=False)
    monitor = MemoryMonitor()
    await monitor.start_idle_sampler()
    assert monitor.is_idle_sampler_running() is False


@pytest.mark.asyncio
async def test_idle_sampler_writes_jsonl_and_stops(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    sample_path = tmp_path / "idle.jsonl"
    monkeypatch.setenv(IDLE_SAMPLER_ENV, "1")
    monkeypatch.setenv("MYTHOSMUD_IDLE_MEMORY_SAMPLER_PATH", str(sample_path))
    monkeypatch.setenv("MYTHOSMUD_IDLE_MEMORY_SAMPLER_INTERVAL", "1")
    monitor = MemoryMonitor()
    await monitor.start_idle_sampler()
    assert monitor.is_idle_sampler_running() is True
    await monitor.start_idle_sampler()
    deadline = time.time() + 2.0
    while not sample_path.exists() and time.time() < deadline:
        await asyncio.sleep(0.05)
    await monitor.stop_idle_sampler()
    assert monitor.is_idle_sampler_running() is False
    assert sample_path.exists()
    first_line = sample_path.read_text(encoding="utf-8").splitlines()[0]
    sample = cast(dict[str, object], json.loads(first_line))
    for key in _SAMPLE_KEYS:
        assert key in sample
