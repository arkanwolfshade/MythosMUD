# pyright: reportAny=false
# Reason: ApplicationContainer DI fields and psutil memory_info attributes are typed Any in stubs/container.

"""
Memory monitoring and cleanup management for MythosMUD.

This module provides memory usage monitoring, cleanup scheduling,
and memory-related statistics for the real-time connection system.
"""

from __future__ import annotations

import asyncio
import gc
import json
import os
import time
import tracemalloc
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING, TypedDict

import psutil

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..container.main import ApplicationContainer

logger = get_logger(__name__)

IDLE_SAMPLER_ENV = "MYTHOSMUD_IDLE_MEMORY_SAMPLER"
IDLE_SAMPLER_PATH_ENV = "MYTHOSMUD_IDLE_MEMORY_SAMPLER_PATH"
IDLE_SAMPLER_INTERVAL_ENV = "MYTHOSMUD_IDLE_MEMORY_SAMPLER_INTERVAL"
_DEFAULT_SAMPLE_PATH = "logs/idle_memory_samples.jsonl"
_DEFAULT_SAMPLE_INTERVAL = 60.0
_MAX_ALLOC_SITES = 8
_SAMPLE_KEYS = (
    "ts",
    "rss_bytes",
    "vms_bytes",
    "heap_current_bytes",
    "heap_peak_bytes",
    "asyncio_tasks",
    "event_bus_queue",
    "npc_pending_keys",
    "perf_metrics",
    "perf_operation_keys",
    "perf_operation_metrics",
    "log_hour_keys",
    "pool_size",
    "pool_checkedout",
    "pool_overflow",
    "top_alloc_sites",
    "task_qualnames",
)


class AllocSiteSample(TypedDict):
    """Count-only allocation site (no object payloads)."""

    file: str
    size: int


class IdleMemorySample(TypedDict):
    """Bounded idle-memory snapshot. Counts only; no player or SQL payloads."""

    ts: float
    rss_bytes: int
    vms_bytes: int
    heap_current_bytes: int
    heap_peak_bytes: int
    asyncio_tasks: int
    event_bus_queue: int
    npc_pending_keys: int
    perf_metrics: int
    perf_operation_keys: int
    perf_operation_metrics: int
    log_hour_keys: int
    pool_size: int
    pool_checkedout: int
    pool_overflow: int
    top_alloc_sites: list[AllocSiteSample]
    # Deliberately uncapped, unlike top_alloc_sites' _MAX_ALLOC_SITES: a leaking coroutine
    # starts at count 0-1 and would sit outside any top-N cap until already large, which is
    # the early signal this field exists to catch.
    task_qualnames: dict[str, int]


class MemoryStatsSnapshot(TypedDict):
    """Process memory counters exposed to connection stats."""

    rss_mb: float
    vms_mb: float
    percent: float
    available_mb: float
    total_mb: float


class ConnectionStatsSnapshot(TypedDict, total=False):
    """Subset of connection-manager stats used for memory alerts."""

    connection_attempts: int
    pending_messages: int
    stale_connections: int


def _max_connection_age_seconds() -> int:
    """Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops."""
    env = os.environ.get("LOGGING_ENVIRONMENT") or ""
    return 1800 if env in ("e2e_test", "local") else 300


def idle_sampler_enabled() -> bool:
    """Return True when the opt-in idle sampler env flag is set."""
    return os.environ.get(IDLE_SAMPLER_ENV, "").strip().lower() in {"1", "true", "yes", "on"}


def idle_sampler_interval_seconds() -> float:
    """Sample interval in seconds. Defaults to 60; values below 1 are raised to 1."""
    raw = os.environ.get(IDLE_SAMPLER_INTERVAL_ENV, "").strip()
    try:
        interval = float(raw) if raw else _DEFAULT_SAMPLE_INTERVAL
    except ValueError:
        interval = _DEFAULT_SAMPLE_INTERVAL
    return interval if interval >= 1.0 else 1.0


def idle_sampler_path() -> Path:
    """JSONL output path for idle samples."""
    raw = os.environ.get(IDLE_SAMPLER_PATH_ENV, "").strip()
    return Path(raw) if raw else Path(_DEFAULT_SAMPLE_PATH)


def _as_int(value: object, default: int = -1) -> int:
    """Coerce a duck-typed counter to int without using typing.Any."""
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return int(value)
    return default


def _container_instance() -> ApplicationContainer | None:
    """Return the live container without constructing a new singleton."""
    from ..container.main import ApplicationContainer

    return ApplicationContainer.peek_instance()


def _event_bus_queue_depth() -> int:
    """Return EventBus queue depth, or -1 when the bus is unavailable."""
    from ..events.event_bus import EventBus

    container = _container_instance()
    if container is None:
        return -1
    event_bus_raw: object = container.event_bus
    if not isinstance(event_bus_raw, EventBus):
        return -1
    return event_bus_raw.get_queue_depth()


def _npc_pending_key_count() -> int:
    """Return pending-message dictionary key count, or -1 when unavailable."""
    from ..npc.lifecycle_manager import NPCLifecycleManager

    container = _container_instance()
    if container is None:
        return -1
    lifecycle_raw: object = container.npc_lifecycle_manager
    if not isinstance(lifecycle_raw, NPCLifecycleManager):
        return -1
    return len(lifecycle_raw.thread_manager.message_queue.pending_messages)


def _perf_metric_counts() -> tuple[int, int, int]:
    """Return (primary metrics, operation keys, retained operation metrics)."""
    from ..monitoring.performance_monitor import peek_performance_monitor

    monitor = peek_performance_monitor()
    if monitor is None:
        return (0, 0, 0)
    retained = sum(len(values) for values in monitor.operation_stats.values())
    return (len(monitor.metrics), len(monitor.operation_stats), retained)


def _log_hour_key_count() -> int:
    """Return log-aggregator hourly bucket count, or -1 when unavailable."""
    from ..structured_logging.log_aggregator import peek_log_aggregator

    aggregator = peek_log_aggregator()
    if aggregator is None:
        return -1
    return len(aggregator.stats.entries_by_hour)


def _sqlalchemy_pool_counts() -> tuple[int, int, int]:
    """Return (pool_size, checkedout, overflow), or (-1, -1, -1) when unavailable."""
    try:
        from sqlalchemy.pool import QueuePool

        from ..database import get_engine

        pool = get_engine().sync_engine.pool
        if not isinstance(pool, QueuePool):
            return (-1, -1, -1)
        return (pool.size(), pool.checkedout(), pool.overflow())
    except Exception:  # pylint: disable=broad-exception-caught  # Reason: Sampler must not fail if the engine is not ready
        return (-1, -1, -1)


def _top_alloc_sites(limit: int = _MAX_ALLOC_SITES) -> list[AllocSiteSample]:
    """Return the largest allocation sites. File:line and size only."""
    if not tracemalloc.is_tracing():
        return []
    sites: list[AllocSiteSample] = []
    for stat in tracemalloc.take_snapshot().statistics("lineno")[:limit]:
        frame = stat.traceback[0]
        sites.append({"file": f"{frame.filename}:{frame.lineno}", "size": int(stat.size)})
    return sites


def _task_qualname(task: asyncio.Task[object]) -> str:
    """Return the coroutine qualname a task was created from, for leak attribution.

    Task names (`task.get_name()`) are useless here: none of the codebase's raw
    `asyncio.create_task(...)` sites pass `name=`, so every task is `Task-N`. The coroutine's
    `__qualname__` is the one key that identifies the creating call site for both raw and
    `TaskRegistry`-tracked tasks alike.
    """
    coro = task.get_coro()
    qualname = getattr(coro, "__qualname__", None)
    if isinstance(qualname, str):
        return qualname
    return type(coro).__name__


def collect_idle_memory_sample() -> IdleMemorySample:
    """Collect a count-based idle sample after a GC pass. No user payloads."""
    _ = gc.collect()
    process = psutil.Process()
    memory_info = process.memory_info()
    heap_current, heap_peak = (0, 0)
    if tracemalloc.is_tracing():
        heap_current, heap_peak = tracemalloc.get_traced_memory()
    try:
        tasks: set[asyncio.Task[object]] = asyncio.all_tasks()
    except RuntimeError:
        tasks = set()
    task_count = len(tasks)
    task_qualnames = dict(Counter(_task_qualname(task) for task in tasks))
    perf_metrics, perf_keys, perf_retained = _perf_metric_counts()
    pool_size, pool_checkedout, pool_overflow = _sqlalchemy_pool_counts()
    return {
        "ts": time.time(),
        "rss_bytes": _as_int(getattr(memory_info, "rss", 0), 0),
        "vms_bytes": _as_int(getattr(memory_info, "vms", 0), 0),
        "heap_current_bytes": int(heap_current),
        "heap_peak_bytes": int(heap_peak),
        "asyncio_tasks": task_count,
        "event_bus_queue": _event_bus_queue_depth(),
        "npc_pending_keys": _npc_pending_key_count(),
        "perf_metrics": perf_metrics,
        "perf_operation_keys": perf_keys,
        "perf_operation_metrics": perf_retained,
        "log_hour_keys": _log_hour_key_count(),
        "pool_size": pool_size,
        "pool_checkedout": pool_checkedout,
        "pool_overflow": pool_overflow,
        "top_alloc_sites": _top_alloc_sites(),
        "task_qualnames": task_qualnames,
    }


def _append_sample_jsonl(path: Path, sample: IdleMemorySample) -> None:
    """Append one JSON object. Creates parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        _ = handle.write(json.dumps(sample, default=str) + "\n")


class MemoryMonitor:
    """
    Monitor memory usage and trigger cleanup when needed.

    This class provides memory monitoring, cleanup scheduling, and
    memory-related statistics for the connection management system.
    """

    def __init__(self) -> None:
        """Initialize the memory monitor with default settings."""
        self.last_cleanup_time: float = time.time()
        self.cleanup_interval: int = 300  # 5 minutes
        self.memory_threshold: float = 0.8  # 80% memory usage triggers cleanup
        self.max_connection_age: int = _max_connection_age_seconds()
        self.max_pending_messages: int = 1000  # Max pending messages per player
        self.max_rate_limit_entries: int = 1000  # Max rate limit entries per player
        self._sampler_task: asyncio.Task[None] | None = None
        self._sampler_stop: asyncio.Event | None = None
        self._started_tracemalloc: bool = False

    def should_cleanup(self) -> bool:
        """
        Check if cleanup should be triggered.

        Returns:
            bool: True if cleanup should be triggered, False otherwise
        """
        current_time = time.time()
        memory_usage = self.get_memory_usage()

        # Time-based cleanup
        if current_time - self.last_cleanup_time > self.cleanup_interval:
            return True

        # Memory-based cleanup
        if memory_usage > self.memory_threshold:
            logger.warning("Memory usage high, triggering cleanup", memory_usage=memory_usage)
            return True

        return False

    def get_memory_usage(self) -> float:
        """
        Get current memory usage as percentage.

        Returns:
            float: Memory usage as a decimal (0.0 to 1.0)
        """
        try:
            process = psutil.Process()
            memory_percent = process.memory_percent()
            return float(memory_percent) / 100.0
        except (OSError, ValueError, TypeError, RuntimeError) as e:
            logger.error("Error getting memory usage", error=str(e), error_type=type(e).__name__, exc_info=True)
            return 0.0

    def get_memory_stats(self) -> MemoryStatsSnapshot | dict[str, object]:
        """
        Get detailed memory statistics.

        Returns:
            dict: Memory statistics including RSS, VMS, percentage, and system memory
        """
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            virtual_memory = psutil.virtual_memory()
            return {
                "rss_mb": float(memory_info.rss) / 1024 / 1024,
                "vms_mb": float(memory_info.vms) / 1024 / 1024,
                "percent": float(process.memory_percent()),
                "available_mb": float(virtual_memory.available) / 1024 / 1024,
                "total_mb": float(virtual_memory.total) / 1024 / 1024,
            }
        except (OSError, ValueError, TypeError, RuntimeError) as e:
            logger.error("Error getting memory stats", error=str(e), error_type=type(e).__name__, exc_info=True)
            return {}

    def get_memory_alerts(self, connection_stats: ConnectionStatsSnapshot) -> list[str]:
        """
        Get memory-related alerts based on current usage and connection statistics.

        Args:
            connection_stats: Current connection and data structure statistics

        Returns:
            list[str]: List of memory-related alerts
        """
        alerts: list[str] = []

        try:
            memory_usage = self.get_memory_usage()

            if memory_usage > 0.9:  # 90%
                alerts.append(f"CRITICAL: Memory usage at {memory_usage:.1%}")
            elif memory_usage > 0.8:  # 80%
                alerts.append(f"WARNING: Memory usage at {memory_usage:.1%}")
            elif memory_usage > 0.7:  # 70%
                alerts.append(f"INFO: Memory usage at {memory_usage:.1%}")

            connection_attempts = _as_int(connection_stats.get("connection_attempts", 0), 0)
            if connection_attempts > 1000:
                alerts.append(f"WARNING: Large number of rate limit entries: {connection_attempts}")

            pending_messages = _as_int(connection_stats.get("pending_messages", 0), 0)
            if pending_messages > 1000:
                alerts.append(f"WARNING: Large number of pending message queues: {pending_messages}")

            stale_count = _as_int(connection_stats.get("stale_connections", 0), 0)
            if stale_count > 0:
                alerts.append(f"WARNING: {stale_count} stale connections detected")

        except (OSError, ValueError, TypeError, RuntimeError) as e:
            logger.error("Error getting memory alerts", error=str(e), error_type=type(e).__name__, exc_info=True)
            alerts.append(f"ERROR: Failed to get memory alerts: {e}")

        return alerts

    def update_cleanup_time(self) -> None:
        """Update the last cleanup time to the current time."""
        self.last_cleanup_time = time.time()

    def force_garbage_collection(self) -> None:
        """Force garbage collection to free memory."""
        try:
            _ = gc.collect()
            logger.debug("Forced garbage collection completed")
        except RuntimeError as e:
            logger.error(
                "Error during forced garbage collection", error=str(e), error_type=type(e).__name__, exc_info=True
            )

    def is_idle_sampler_running(self) -> bool:
        """Return True when the opt-in sampler task is alive."""
        return self._sampler_task is not None and not self._sampler_task.done()

    async def start_idle_sampler(self) -> None:
        """Start the JSONL sampler when enabled. No-op when disabled or already running."""
        if not idle_sampler_enabled() or self.is_idle_sampler_running():
            return
        self._sampler_stop = asyncio.Event()
        self._sampler_task = asyncio.create_task(self._run_idle_sampler())
        logger.info(
            "Idle memory sampler started",
            interval_seconds=idle_sampler_interval_seconds(),
            path=str(idle_sampler_path()),
        )

    async def stop_idle_sampler(self) -> None:
        """Cancel the sampler task and stop tracemalloc if this monitor started it."""
        task = self._sampler_task
        if task is None:
            return
        if self._sampler_stop is not None:
            self._sampler_stop.set()
        _ = task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
        self._sampler_task = None
        if self._started_tracemalloc and tracemalloc.is_tracing():
            tracemalloc.stop()
            self._started_tracemalloc = False
        logger.info("Idle memory sampler stopped")

    async def _run_idle_sampler(self) -> None:
        """Emit one JSONL sample per interval until cancelled or stopped."""
        if not tracemalloc.is_tracing():
            tracemalloc.start()
            self._started_tracemalloc = True
        path = idle_sampler_path()
        interval = idle_sampler_interval_seconds()
        stop_event = self._sampler_stop
        if stop_event is None:
            return
        try:
            while not stop_event.is_set():
                try:
                    sample = collect_idle_memory_sample()
                    _append_sample_jsonl(path, sample)
                    logger.info("Idle memory sample written", rss_bytes=sample["rss_bytes"])
                except (OSError, RuntimeError, TypeError, ValueError) as error:
                    logger.error("Idle memory sample failed", error=str(error), error_type=type(error).__name__)
                try:
                    _ = await asyncio.wait_for(stop_event.wait(), timeout=interval)
                except TimeoutError:
                    continue
        finally:
            if self._started_tracemalloc and tracemalloc.is_tracing():
                tracemalloc.stop()
                self._started_tracemalloc = False
