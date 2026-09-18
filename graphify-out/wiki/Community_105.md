# Community 105

> 94 nodes

## Key Concepts

- **system_monitoring.py** (24 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (15 connections) — `server/api/system_monitoring.py`
- **asyncio** (14 connections)
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **get_cache_manager()** (10 connections) — `server/caching/lru_cache.py`
- **test_system_monitoring_endpoints.py** (10 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **_resolve_memory_leak_collector_from_request()** (9 connections) — `server/api/system_monitoring.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (7 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **Request** (6 connections)
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **_request_with_container()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_handles_missing_collector_gracefully()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_includes_memory_leak_metrics()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- *... and 69 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (22 shared connections)
- [Community 421](Community_421.md) (12 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (8 shared connections)
- [Community 312](Community_312.md) (6 shared connections)
- [Community 183](Community_183.md) (4 shared connections)
- [Community 178](Community_178.md) (3 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (3 shared connections)
- [Community 255](Community_255.md) (2 shared connections)
- [Community 67](Community_67.md) (2 shared connections)
- [Community 334](Community_334.md) (2 shared connections)
- [Community 887](Community_887.md) (1 shared connections)
- [Community 513](Community_513.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/caching/lru_cache.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 220 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*