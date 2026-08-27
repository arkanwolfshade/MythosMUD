# debrief_command.py

> 70 nodes

## Key Concepts

- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (14 connections) — `server/api/system_monitoring.py`
- **asyncio** (14 connections)
- **test_system_monitoring_endpoints.py** (12 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **_resolve_memory_leak_collector_from_request()** (9 connections) — `server/api/system_monitoring.py`
- **Request** (6 connections)
- **TestLifespan** (5 connections) — `server/tests/unit/test_main.py`
- **_request_with_container()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_handles_missing_collector_gracefully()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_includes_memory_leak_metrics()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **.test_lifespan_initialization_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (4 connections) — `server/tests/unit/test_main.py`
- *... and 45 more nodes in this community*

## Relationships

- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (10 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (5 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (1 shared connections)
- [.create_get_command](create_get_command.md) (1 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 133 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*