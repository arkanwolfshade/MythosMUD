# server api monitoring

> 157 nodes

## Key Concepts

- **api/monitoring.py** (64 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (59 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **HealthStatus** (48 connections) — `server/models/health.py`
- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (21 connections) — `server/services/health_service.py`
- **Request** (19 connections)
- **HealthResponse** (17 connections) — `server/models/health.py`
- **health.py** (15 connections) — `server/models/health.py`
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **HealthErrorResponse** (10 connections) — `server/models/health.py`
- *... and 132 more nodes in this community*

## Relationships

- [server tests unit services test](server_tests_unit_services_test.md) (33 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (33 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (20 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (19 shared connections)
- [healthstatus](healthstatus.md) (11 shared connections)
- [server game movement monitor rationale](server_game_movement_monitor_rationale.md) (7 shared connections)
- [server game movement monitor movementmonitor](server_game_movement_monitor_movementmonitor.md) (7 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (6 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (5 shared connections)
- [server game skill service](server_game_skill_service.md) (4 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (4 shared connections)
- [server caching cache service](server_caching_cache_service.md) (3 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 457 (79%)
- INFERRED: 121 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*