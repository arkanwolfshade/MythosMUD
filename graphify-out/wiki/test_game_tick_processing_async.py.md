# test_game_tick_processing_async.py

> 40 nodes

## Key Concepts

- **test_monitoring_endpoints.py** (50 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **asyncio** (15 connections)
- **_request_with_container()** (13 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (8 connections) — `server/api/monitoring.py`
- **test_dual_connection_and_performance_and_health_stats()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_health_status_healthy_returns_model()** (7 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_memory_alerts_and_force_cleanup()** (6 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **_connection_manager_stub()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_memory_stats_leak_collector_warning_branch()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_memory_stats_with_leak_collector()** (5 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_cache_metrics_builds_response()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_eventbus_metrics_shapes()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_memory_leak_metrics_endpoint()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_memory_leak_collector_from_request()** (4 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_movement_metrics_logged_http_on_failure()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_movement_metrics_uses_monitor()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_performance_summary_delegates_to_monitor()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_system_alerts_returns_counts()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_get_task_metrics_from_registry()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_reset_movement_metrics_calls_reset()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_resolve_cache_manager_from_container()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- *... and 15 more nodes in this community*

## Relationships

- [inventory_equip_command.py](inventory_equip_command.py.md) (47 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [vite Best Practices](vite_Best_Practices.md) (3 shared connections)
- [.create_get_command](create_get_command.md) (1 shared connections)
- [debrief_command.py](debrief_command.py.md) (1 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 134 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*