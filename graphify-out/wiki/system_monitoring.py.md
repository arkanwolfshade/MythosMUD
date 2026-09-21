# system_monitoring.py

> 74 nodes

## Key Concepts

- **system_monitoring.py** (24 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **BaseModel** (19 connections)
- **get_system_metrics()** (15 connections) — `server/api/system_monitoring.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **test_system_monitoring_endpoints.py** (10 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **_resolve_memory_leak_collector_from_request()** (9 connections) — `server/api/system_monitoring.py`
- **MessageResponse** (6 connections) — `server/api/monitoring_models.py`
- **Request** (6 connections)
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **AlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **CacheMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **ConnectionHealthStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **DualConnectionStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **EventBusMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **IntegrityResponse** (5 connections) — `server/api/monitoring_models.py`
- **MemoryAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **MemoryLeakMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **MemoryStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **MetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- *... and 49 more nodes in this community*

## Relationships

- [api/monitoring.py](api-monitoring.py.md) (32 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (13 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [lifespan.py](lifespan.py.md) (4 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (4 shared connections)
- [RoomCacheService](RoomCacheService.md) (2 shared connections)
- [admin_summon_command.py](admin_summon_command.py.md) (2 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 203 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*