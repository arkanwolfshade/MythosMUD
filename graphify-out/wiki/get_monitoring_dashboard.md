# get_monitoring_dashboard

> 55 nodes

## Key Concepts

- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **TestLifespan** (5 connections) — `server/tests/unit/test_main.py`
- **Request** (5 connections)
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
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_success()** (4 connections) — `server/tests/unit/test_main.py`
- *... and 30 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (7 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (4 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (2 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 125 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*