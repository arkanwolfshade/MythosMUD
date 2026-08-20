# get_monitoring_dashboard

> 27 nodes

## Key Concepts

- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **Request** (5 connections)
- **get** (4 connections)
- **post** (1 connections)
- **Response model for system health check.** (1 connections) — `server/api/monitoring_models.py`
- **Response model for system metrics.** (1 connections) — `server/api/monitoring_models.py`
- **Response model for system monitoring summary.** (1 connections) — `server/api/monitoring_models.py`
- **Response model for system alerts.** (1 connections) — `server/api/monitoring_models.py`
- **Response model for alert resolution.** (1 connections) — `server/api/monitoring_models.py`
- **Get comprehensive monitoring summary.** (1 connections) — `server/api/system_monitoring.py`
- **Get system alerts from monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- **Resolve a system alert.** (1 connections) — `server/api/system_monitoring.py`
- **Enhanced health check endpoint using monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- **Get system metrics from monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- *... and 2 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (14 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (13 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (11 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (3 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (1 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (1 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 97 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*