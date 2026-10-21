# ValueError

> 72 nodes · cohesion 0.05

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
- **test_system_monitoring_endpoints.py** (10 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **_resolve_memory_leak_collector_from_request()** (9 connections) — `server/api/system_monitoring.py`
- **SystemMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **_request_with_container()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_handles_missing_collector_gracefully()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_includes_memory_leak_metrics()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **TestLifespan** (5 connections) — `server/tests/unit/test_main.py`
- **get** (4 connections)
- **.test_lifespan_initialization_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (4 connections) — `server/tests/unit/test_main.py`
- *... and 47 more nodes in this community*

## Relationships

- [FStringLoggingFixer](FStringLoggingFixer.md) (11 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (8 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (7 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (6 shared connections)
- [Room](Room.md) (5 shared connections)
- [Player](Player.md) (2 shared connections)
- [LucidityTierCache](LucidityTierCache.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [npc_database.py](npc_database.py.md) (2 shared connections)
- [test_room_sync_service.py](test_room_sync_service.py.md) (2 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (2 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 174 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*