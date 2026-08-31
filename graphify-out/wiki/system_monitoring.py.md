# system_monitoring.py

> 73 nodes

## Key Concepts

- **system_monitoring.py** (25 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (15 connections) — `server/api/system_monitoring.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **test_system_monitoring_endpoints.py** (12 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **_resolve_memory_leak_collector_from_request()** (9 connections) — `server/api/system_monitoring.py`
- **Request** (6 connections)
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **_request_with_container()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_handles_missing_collector_gracefully()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **test_get_system_metrics_includes_memory_leak_metrics()** (5 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (4 connections) — `server/tests/unit/test_main.py`
- *... and 48 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (13 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (8 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (4 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (2 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 181 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*