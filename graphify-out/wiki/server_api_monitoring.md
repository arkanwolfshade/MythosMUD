# server api monitoring

> 81 nodes

## Key Concepts

- **api/monitoring.py** (64 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (59 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **Request** (19 connections)
- **HealthResponse** (17 connections) — `server/models/health.py`
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **force_memory_cleanup()** (10 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (10 connections) — `server/api/monitoring.py`
- **reset_metrics()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (10 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (9 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (9 connections) — `server/api/monitoring.py`
- *... and 56 more nodes in this community*

## Relationships

- [server api monitoring models](server_api_monitoring_models.md) (32 shared connections)
- [server models health](server_models_health.md) (19 shared connections)
- [server api players](server_api_players.md) (19 shared connections)
- [healthstatus](healthstatus.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server game movement monitor rationale](server_game_movement_monitor_rationale.md) (5 shared connections)
- [server game movement monitor movementmonitor](server_game_movement_monitor_movementmonitor.md) (5 shared connections)
- [server api system monitoring get](server_api_system_monitoring_get.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [server caching cache service rationale](server_caching_cache_service_rationale.md) (2 shared connections)
- [server app task registry](server_app_task_registry.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 321 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*