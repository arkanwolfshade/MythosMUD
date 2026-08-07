# services chat logger

> 51 nodes

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **Request** (5 connections)
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.mock_app()** (2 connections) — `server/tests/unit/test_main.py`
- *... and 26 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (14 shared connections)
- [Loot Generation](Loot_Generation.md) (13 shared connections)
- [room cache services](room_cache_services.md) (7 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 187 (96%)
- INFERRED: 7 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*