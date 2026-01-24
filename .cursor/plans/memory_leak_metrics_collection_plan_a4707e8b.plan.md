---
name: Memory Leak Metrics Collection Plan
overview: Plan to implement metrics and telemetry collection to fill analysis gaps identified in the memory leak audit, including runtime metrics for connection management, event subscriptions, caches, tasks, and client-side resources.
todos:

  - id: task1-1

    content: Add get_closed_websockets_count() method to ConnectionManager
    status: completed

  - id: task1-2

    content: Extend get_memory_stats() to include closed_websockets_count, active_websockets_count, connection_metadata_count, player_websockets_count
    status: completed

  - id: task1-3

    content: Add active_to_player_ratio metric calculation in get_memory_stats()
    status: completed

  - id: task1-4

    content: Add connection cleanup operation tracking (counts and timestamps)
    status: completed

  - id: task1-5

    content: Update statistics_aggregator.py to include new connection metrics
    status: completed

  - id: task1-6

    content: Extend MemoryStatsResponse model to include new connection metrics fields
    status: completed

  - id: task2-1

    content: Verify get_all_subscriber_counts() method exists in EventBus (line 571)
    status: completed

  - id: task2-2

    content: Add get_active_task_count() method to EventBus returning len(self._active_tasks)
    status: completed

  - id: task2-3

    content: Add get_active_task_details() method to EventBus for task debugging
    status: completed

  - id: task2-4

    content: Add subscriber lifecycle tracking (subscription timestamps, unsubscribe operations)
    status: completed

  - id: task2-5

    content: Calculate subscriber churn rate metric
    status: completed

  - id: task2-6

    content: Create EventBusMetricsResponse model in server/api/monitoring.py
    status: completed

  - id: task2-7

    content: Add /monitoring/eventbus endpoint to expose EventBus metrics
    status: completed

  - id: task3-1

    content: Add _expired_count counter to LRUCache.__init__()
    status: completed

  - id: task3-2

    content: Increment _expired_count when entries expire in get() method
    status: completed

  - id: task3-3

    content: Add expired_count and expiration_rate to LRUCache.get_stats() return value
    status: completed

  - id: task3-4

    content: Add expiration rate calculation (expired entries per time period)
    status: completed

  - id: task3-5

    content: Add expired vs LRU evicted ratio tracking
    status: completed

  - id: task3-6

    content: Add cache capacity utilization metrics to CacheManager
    status: completed

  - id: task3-7

    content: Create CacheMetricsResponse model in server/api/monitoring.py
    status: completed

  - id: task3-8

    content: Add /monitoring/caches endpoint to expose cache metrics
    status: completed

  - id: task4-1

    content: Verify if get_active_task_count() exists in TaskRegistry, add if missing
    status: completed

  - id: task4-2

    content: Add get_task_stats_by_type() method to TaskRegistry returning task breakdown by type
    status: completed

  - id: task4-3

    content: Add task lifecycle tracking counters (creation, completion, cancellation)
    status: completed

  - id: task4-4

    content: Calculate task creation rate and completion rate metrics
    status: completed

  - id: task4-5

    content: Add service-level task tracking (tasks by service/component identifier)
    status: completed

  - id: task4-6

    content: Track orphaned tasks count
    status: completed

  - id: task4-7

    content: Create TaskMetricsResponse model in server/api/monitoring.py
    status: completed

  - id: task4-8

    content: Add /monitoring/tasks endpoint to expose TaskRegistry metrics
    status: completed

  - id: task5-1

    content: Add get_active_subscriptions() method to NATSService returning list of subscription subjects
    status: completed

  - id: task5-2

    content: Track subscription count over time in NATSService
    status: completed

  - id: task5-3

    content: Track subscription lifecycle events (subscribe/unsubscribe timestamps)
    status: completed

  - id: task5-4

    content: Add subscription cleanup verification method to NATSService
    status: completed

  - id: task5-5

    content: Log warnings in disconnect() if subscriptions remain after cleanup
    status: completed

  - id: task5-6

    content: Track subscription cleanup timestamps
    status: completed

  - id: task5-7

    content: Extend MetricsResponse model to include subscription metrics
    status: completed

  - id: task5-8

    content: Add subscription metrics to existing /metrics endpoint
    status: completed

  - id: task6-1

    content: Verify ResourceManager.getResourceStats() tracks all resource types (timers, intervals, WebSockets, custom)
    status: completed

  - id: task6-2

    content: Add periodic logging of ResourceManager stats in useResourceCleanup hook
    status: completed

  - id: task6-3

    content: Add Zustand store subscription tracking in connectionStore.ts and gameStore.ts
    status: completed

  - id: task6-4

    content: Log subscription/unsubscription events for Zustand stores
    status: completed

  - id: task6-5

    content: Track active subscriptions per store
    status: completed

  - id: task6-6

    content: Add component mount/unmount event tracking utility
    status: completed

  - id: task6-7

    content: Verify cleanup functions are called on component unmount
    status: completed

  - id: task6-8

    content: Log warnings if cleanup is missing on component unmount
    status: completed

  - id: task6-9

    content: Create client-side metrics collector utility for development logging
    status: completed

  - id: task7-1

    content: Create new file server/monitoring/memory_leak_metrics.py
    status: completed

  - id: task7-2

    content: Implement MemoryLeakMetricsCollector class with initialization
    status: completed

  - id: task7-3

    content: Implement collect_all_metrics() method aggregating from all sources
    status: completed

  - id: task7-4

    content: Implement collect_connection_metrics() method
    status: completed

  - id: task7-5

    content: Implement collect_event_metrics() method
    status: completed

  - id: task7-6

    content: Implement collect_cache_metrics() method
    status: completed

  - id: task7-7

    content: Implement collect_task_metrics() method
    status: completed

  - id: task7-8

    content: Add metrics trend tracking using deque with maxlen=100
    status: completed

  - id: task7-9

    content: Implement growth rate calculation for metrics
    status: completed

  - id: task7-10

    content: Add alert threshold configuration (closed_websockets_max, subscriber_growth_rate, cache_size_limit_factor)
    status: completed

  - id: task7-11

    content: Implement check_alerts() method to check thresholds and return alert list
    status: completed

  - id: task7-12

    content: Create MemoryLeakMetricsResponse model in server/api/monitoring.py
    status: completed

  - id: task7-13

    content: Add /monitoring/memory-leaks endpoint to expose all memory leak metrics
    status: completed

  - id: task8-1

    content: Create _log_memory_metrics_periodically() async function in server/app/lifespan.py
    status: completed

  - id: task8-2

    content: Register periodic logging task with TaskRegistry (5-10 minute interval)
    status: completed

  - id: task8-3

    content: Log metrics on application startup in lifespan startup function
    status: completed

  - id: task8-4

    content: Log metrics on application shutdown in lifespan shutdown function
    status: completed

  - id: task8-5

    content: Calculate and log metrics delta over application lifetime
    status: completed

  - id: task8-6

    content: Add optional metrics persistence to file (JSON format)
    status: completed

  - id: task9-1

    content: Extend /monitoring/memory endpoint to include new memory leak metrics
    status: completed

  - id: task9-2

    content: Add cache metrics to system metrics endpoint
    status: completed

  - id: task9-3

    content: Add event metrics to monitoring summary endpoint
    status: completed

  - id: task9-4

    content: Create MemoryLeakMetricsResponse model with all metric categories
    status: completed

  - id: task9-5

    content: Create EventBusMetricsResponse model
    status: completed

  - id: task9-6

    content: Create CacheMetricsResponse model
    status: completed

  - id: task9-7

    content: Create TaskMetricsResponse model
    status: completed

  - id: task9-8

    content: Document all metrics in API documentation with meanings and thresholds
    status: completed

  - id: task9-9

    content: Add examples of normal vs abnormal metric values to documentation
    status: completed

  - id: task10-1

    content: Check if monitoring_dashboard.py exists and review its structure
    status: completed

  - id: task10-2

    content: Add memory leak metrics panel to monitoring dashboard if it exists
    status: completed

  - id: task10-3

    content: Add trend visualization for memory leak metrics
    status: completed

  - id: task10-4

    content: Check if Prometheus exporter exists, add memory leak metrics if applicable
    status: completed

  - id: task10-5

    content: Create Grafana dashboard configuration for memory leak metrics (if using Grafana)
    status: completed

  - id: task10-6

    content: Set up alerting rules in monitoring system for threshold violations
    status: completed
---

# Memory Leak Metrics Collection Plan

## Overview

This plan implements metrics and telemetry collection to fill the analysis gaps identified in the memory leak audit report. The metrics will enable runtime monitoring and verification of resource cleanup effectiveness.

## Analysis Gaps to Address

From the audit report, the following metrics are needed:

1. **Connection Management**:

   - `_closed_websockets` set size
   - `active_websockets` dict size vs active player count
   - `connection_metadata` dict size
   - Connection cleanup verification

2. **Event System**:

   - EventBus subscriber count per event type
   - `_active_tasks` set size in EventBus
   - Subscriber lifecycle verification

3. **Cache Management**:

   - Cache sizes and hit rates
   - Expired entry counts (for TTL caches)
   - Cache eviction rates

4. **Task Management**:

   - TaskRegistry active task count
   - Background task counts by service
   - Task lifecycle verification

5. **Client-Side**:

   - ResourceManager resource counts (timers, intervals, WebSockets)
   - Zustand store subscription counts
   - Component unmount verification

6. **Verification Metrics**:

   - NATS subscription cleanup verification
   - DLQ processing frequency
   - Service shutdown cleanup verification

## Implementation Tasks

### Task 1: Extend ConnectionManager Metrics

**Priority**: High

**Files**: `server/realtime/connection_manager.py`, `server/realtime/monitoring/statistics_aggregator.py`

**Steps**:

1. **Add `_closed_websockets` size metric**

   - Add method `get_closed_websockets_count() -> int` to ConnectionManager
   - Return `len(self._closed_websockets)`
   - Include in existing `get_memory_stats()` method

2. **Add connection dictionary size tracking**

   - Extend `get_memory_stats()` to include:
     - `active_websockets_count: int`
     - `connection_metadata_count: int`
     - `player_websockets_count: int`
     - `closed_websockets_count: int`
   - Add ratio metrics:
     - `active_to_player_ratio: float` (active connections / active players)

3. **Add connection cleanup metrics**

   - Track cleanup operation counts
   - Track cleanup operation timestamps
   - Add metrics for orphaned connection detection

**Code Changes**:

- Add `get_closed_websockets_count() -> int` method
- Extend `get_memory_stats()` to include new metrics
- Update `server/realtime/monitoring/statistics_aggregator.py` to aggregate these metrics

**Integration**:

- Metrics already exposed via `/monitoring/memory` endpoint
- Extend `MemoryStatsResponse` model to include new fields

---

### Task 2: Add EventBus Subscriber Metrics

**Priority**: High

**Files**: `server/events/event_bus.py`, `server/api/monitoring.py`

**Steps**:

1. **Add subscriber count tracking method**

   - Extend existing `get_subscriber_count()` to return counts for all event types
   - Add `get_all_subscriber_counts() -> dict[str, int]` method (already exists at line 571)
   - Verify this method exists and document it

2. **Add active task tracking**

   - Add method `get_active_task_count() -> int` to return `len(self._active_tasks)`
   - Add method `get_active_task_details() -> list[dict[str, Any]]` for task details

3. **Add subscriber lifecycle metrics**

   - Track subscription timestamps
   - Track unsubscribe operations
   - Calculate subscriber churn rate

4. **Create new metrics endpoint**

   - Add endpoint `/monitoring/eventbus` to expose EventBus metrics
   - Include subscriber counts, active task counts, and lifecycle metrics

**Code Changes**:

- Add `get_active_task_count() -> int` method to EventBus
- Add `get_active_task_details() -> list[dict]` method
- Create new response model `EventBusMetricsResponse`
- Add endpoint in `server/api/monitoring.py`

**Code Structure**:

```python
def get_active_task_count(self) -> int:
    """Get count of active async tasks in EventBus."""
    return len(self._active_tasks)

def get_active_task_details(self) -> list[dict[str, Any]]:
    """Get details of active tasks for debugging."""
    # Implementation

```

---

### Task 3: Add Cache Metrics with Expiration Tracking

**Priority**: Medium

**Files**: `server/caching/lru_cache.py`, `server/caching/cache_service.py`, `server/api/monitoring.py`

**Steps**:

1. **Extend cache statistics**

   - Add expired entry count tracking to `LRUCache`
   - Track expiration operations in `_evict_expired()` or `get()` methods
   - Add `expired_entries_count` to cache stats

2. **Add expiration rate metrics**

   - Track expiration rate (expired entries per time period)
   - Calculate expiration percentage of total operations
   - Track expired vs LRU evicted ratio

3. **Add cache size monitoring**

   - Expose current cache sizes for all caches
   - Track cache size over time
   - Add capacity utilization metrics

4. **Create cache metrics endpoint**

   - Add endpoint `/monitoring/caches` to expose cache metrics
   - Include sizes, hit rates, expiration rates, and capacity utilization

**Code Changes**:

- Add `_expired_count` counter to `LRUCache.__init__()`
- Increment counter when entries expire in `get()` method
- Add expiration metrics to `get_stats()` method
- Create `CacheMetricsResponse` model
- Add endpoint in `server/api/monitoring.py`

**Code Structure**:

```python
# In LRUCache.__init__

self._expired_count = 0

# In get() when entry expires

if time.time() - timestamp > self.ttl_seconds:
    del self._cache[key]
    self._expired_count += 1  # Track expiration

# In get_stats()

return {
    # ... existing stats ...

    "expired_count": self._expired_count,
    "expiration_rate": self._expired_count / max(total_requests, 1),
}
```

---

### Task 4: Add Task Registry Metrics

**Priority**: Medium

**Files**: `server/app/task_registry.py`, `server/app/tracked_task_manager.py`, `server/api/monitoring.py`

**Steps**:

1. **Add active task count method**

   - Verify if `get_active_task_count()` exists
   - Add method to return current active task count
   - Add method to return task breakdown by type

2. **Add task lifecycle metrics**

   - Track task creation rate
   - Track task completion rate
   - Track task cancellation count
   - Calculate task lifetime statistics

3. **Add service-level task tracking**

   - Track tasks by service/component identifier
   - Identify services with most active tasks
   - Track orphaned tasks

4. **Create task metrics endpoint**

   - Add endpoint `/monitoring/tasks` to expose TaskRegistry metrics
   - Include active counts, lifecycle metrics, and service breakdown

**Code Changes**:

- Add `get_active_task_count() -> int` method to TaskRegistry
- Add `get_task_stats_by_type() -> dict[str, int]` method
- Add task lifecycle tracking counters
- Create `TaskMetricsResponse` model
- Add endpoint in `server/api/monitoring.py`

---

### Task 5: Add NATS Subscription Metrics

**Priority**: Low

**Files**: `server/services/nats_service.py`, `server/realtime/nats_message_handler.py`, `server/api/metrics.py`

**Steps**:

1. **Add subscription tracking**

   - Add method `get_active_subscriptions() -> list[str]` to NATSService
   - Track subscription count over time
   - Track subscription lifecycle (subscribe/unsubscribe events)

2. **Add subscription cleanup verification**

   - Add method to verify all subscriptions are cleaned up on shutdown
   - Log warnings if subscriptions remain after cleanup
   - Track subscription cleanup timestamps

3. **Extend NATS metrics endpoint**

   - Add subscription metrics to existing `/metrics` endpoint
   - Include subscription counts and cleanup status

**Code Changes**:

- Add `get_active_subscriptions() -> list[str]` to NATSService
- Add subscription tracking in `_subscribe_to_subject()` method
- Add cleanup verification in `disconnect()` method
- Extend `MetricsResponse` to include subscription metrics

**Integration**:

- Metrics can be added to existing `/metrics` endpoint
- Or create dedicated `/monitoring/nats` endpoint

---

### Task 6: Add Client-Side Telemetry

**Priority**: Low

**Files**: `client/src/utils/resourceCleanup.ts`, `client/src/stores/connectionStore.ts`, `client/src/stores/gameStore.ts`

**Steps**:

1. **Extend ResourceManager metrics**

   - Add method `getResourceStats()` (already exists at line 77)
   - Verify it tracks all resource types
   - Add periodic logging of resource stats

2. **Add store subscription tracking**

   - Track Zustand store subscriptions in components
   - Log subscription/unsubscription events
   - Track active subscriptions per store

3. **Add client-side metrics API**

   - Create endpoint in client to expose resource stats
   - Send metrics to server for aggregation
   - Or log metrics to console for development

4. **Add component unmount verification**

   - Track component mount/unmount events
   - Verify cleanup functions are called
   - Log warnings if cleanup is missing

**Code Changes**:

- Verify `ResourceManager.getResourceStats()` includes all resources
- Add store subscription tracking in Zustand stores
- Add metrics logging in `useResourceCleanup` hook
- Create client-side metrics collector utility

**Implementation Note**:

- Client-side metrics can be logged to browser console for development
- For production, consider sending metrics to server via WebSocket or HTTP endpoint

---

### Task 7: Create Comprehensive Memory Leak Metrics Module

**Priority**: Medium

**Files**: New file `server/monitoring/memory_leak_metrics.py`, `server/api/monitoring.py`

**Steps**:

1. **Create unified metrics collector**

   - New class `MemoryLeakMetricsCollector`
   - Aggregates metrics from all sources:
     - ConnectionManager
     - EventBus
     - CacheManager
     - TaskRegistry
     - NATSService

2. **Add metrics aggregation methods**

   - `collect_all_metrics() -> dict[str, Any]`
   - `collect_connection_metrics() -> dict`
   - `collect_event_metrics() -> dict`
   - `collect_cache_metrics() -> dict`
   - `collect_task_metrics() -> dict`

3. **Add metrics trend tracking**

   - Track metrics over time (last N measurements)
   - Calculate growth rates
   - Identify abnormal growth patterns

4. **Add alerting thresholds**

   - Warn if `_closed_websockets` exceeds threshold
   - Warn if subscriber counts grow unexpectedly
   - Warn if cache sizes exceed bounds
   - Warn if task counts grow unbounded

5. **Create unified metrics endpoint**

   - Add endpoint `/monitoring/memory-leaks` to expose all memory leak metrics
   - Include aggregated metrics and trend data
   - Include alerts and warnings

**Code Structure**:

```python
class MemoryLeakMetricsCollector:
    def __init__(self):
        self._history: deque[dict[str, Any]] = deque(maxlen=100)
        self._alert_thresholds = {
            "closed_websockets_max": 5000,
            "subscriber_growth_rate": 0.1,  # 10% growth per period
            "cache_size_limit_factor": 1.1,  # 110% of max_size
        }

    def collect_all_metrics(self) -> dict[str, Any]:
        # Aggregate all metrics

        pass

    def check_alerts(self, metrics: dict) -> list[str]:
        # Check thresholds and return alerts

        pass
```

---

### Task 8: Add Periodic Metrics Logging

**Priority**: Low

**Files**: `server/app/lifespan.py`, `server/monitoring/memory_leak_metrics.py`

**Steps**:

1. **Create periodic logging task**

   - Add background task to log memory leak metrics every 5-10 minutes
   - Use TaskRegistry to track the task
   - Log metrics to structured logger

2. **Add startup/shutdown metrics**

   - Log metrics on application startup
   - Log metrics on application shutdown
   - Track metrics delta over lifetime

3. **Add metrics persistence** (optional)

   - Store metrics history in file or database
   - Enable metrics replay for analysis
   - Support metrics export for external analysis

**Code Changes**:

- Add periodic logging task in `server/app/lifespan.py`
- Use existing TaskRegistry to track the task
- Log to structured logger at INFO level

**Code Structure**:

```python
async def _log_memory_metrics_periodically(collector: MemoryLeakMetricsCollector):
    """Log memory metrics periodically."""
    while True:
        await asyncio.sleep(300)  # 5 minutes
        metrics = collector.collect_all_metrics()
        alerts = collector.check_alerts(metrics)
        logger.info("Memory leak metrics", metrics=metrics, alerts=alerts)
```

---

### Task 9: Extend Existing Monitoring Endpoints

**Priority**: Medium

**Files**: `server/api/monitoring.py`, `server/api/metrics.py`

**Steps**:

1. **Extend existing endpoints**

   - Add memory leak metrics to `/monitoring/memory` endpoint
   - Add cache metrics to system metrics
   - Add event metrics to monitoring summary

2. **Create response models**

   - `MemoryLeakMetricsResponse` for comprehensive metrics
   - `EventBusMetricsResponse` for event system metrics
   - `CacheMetricsResponse` for cache metrics
   - `TaskMetricsResponse` for task metrics

3. **Add metrics documentation**

   - Document all metrics in API documentation
   - Explain metric meanings and thresholds
   - Provide examples of normal vs abnormal values

**Code Changes**:

- Extend existing response models
- Add new endpoints as needed
- Update API documentation

---

### Task 10: Add Metrics Dashboard Integration

**Priority**: Low

**Files**: `server/monitoring/monitoring_dashboard.py` (if exists)

**Steps**:

1. **Integrate with monitoring dashboard**

   - Add memory leak metrics to dashboard if it exists
   - Create memory leak metrics panel
   - Add trend visualization

2. **Add Grafana/Prometheus integration** (if applicable)

   - Export metrics in Prometheus format
   - Create Grafana dashboards for memory leak metrics
   - Set up alerts in monitoring system

**Code Changes**:

- Extend monitoring dashboard if it exists
- Add Prometheus exporter if monitoring stack uses it
- Create dashboard configuration files

---

## Metrics Schema

### Connection Metrics

```python
{
    "active_websockets_count": int,
    "connection_metadata_count": int,
    "player_websockets_count": int,
    "closed_websockets_count": int,
    "active_to_player_ratio": float,
    "orphaned_connections": int,
}
```

### Event Metrics

```python
{
    "subscriber_counts_by_type": dict[str, int],
    "total_subscribers": int,
    "active_task_count": int,
    "task_details": list[dict],
    "subscription_churn_rate": float,
}
```

### Cache Metrics

```python
{
    "cache_sizes": dict[str, int],
    "cache_hit_rates": dict[str, float],
    "expired_entry_counts": dict[str, int],
    "expiration_rates": dict[str, float],
    "capacity_utilization": dict[str, float],
}
```

### Task Metrics

```python
{
    "active_task_count": int,
    "tasks_by_type": dict[str, int],
    "task_creation_rate": float,
    "task_completion_rate": float,
    "orphaned_task_count": int,
}
```

### NATS Metrics

```python
{
    "active_subscriptions": list[str],
    "subscription_count": int,
    "cleanup_verified": bool,
    "last_cleanup_time": str,
}
```

### Client Metrics

```python
{
    "active_timers": int,
    "active_intervals": int,
    "active_websockets": int,
    "active_subscriptions": int,
    "component_mount_count": int,
    "cleanup_missing_count": int,
}
```

---

## Implementation Order

1. **Phase 1 (Critical)**: Tasks 1, 2, 3 (Connection, Event, Cache metrics)
2. **Phase 2 (Important)**: Tasks 4, 7 (Task metrics, unified collector)
3. **Phase 3 (Verification)**: Tasks 5, 6 (NATS, client-side metrics)
4. **Phase 4 (Monitoring)**: Tasks 8, 9, 10 (Logging, endpoints, dashboard)

---

## Testing Strategy

1. **Unit Tests**: Test each metrics collection method
2. **Integration Tests**: Test metrics aggregation
3. **Load Tests**: Verify metrics don't impact performance
4. **Monitoring Tests**: Verify metrics are logged and exposed correctly

---

## Success Criteria

All metrics from audit report are collected

- Metrics are exposed via API endpoints
- Metrics are logged periodically
- Alerts are generated for threshold violations
- Metrics enable verification of cleanup effectiveness
- Client-side metrics are tracked (if applicable)

---

## Notes

Metrics collection should be lightweight to avoid performance impact

- Use lazy evaluation where possible (calculate metrics on request, not continuously)
- Consider rate limiting metrics endpoints
- Document metric meanings and expected ranges
- Set up alerts for critical thresholds
