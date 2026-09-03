# Monitoring Models

> 100 nodes

## Key Concepts

- **system_monitoring.py** (25 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (23 connections) — `server/api/monitoring_models.py`
- **BaseModel** (19 connections)
- **get_system_metrics()** (15 connections) — `server/api/system_monitoring.py`
- **asyncio** (14 connections)
- **test_system_monitoring_endpoints.py** (12 connections) — `server/tests/unit/api/test_system_monitoring_endpoints.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
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
- **PerformanceStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- *... and 75 more nodes in this community*

## Relationships

- [Monitoring](Monitoring.md) (32 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (17 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (9 shared connections)
- [Performance Monitor](Performance_Monitor.md) (7 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (3 shared connections)
- [Cache Service](Cache_Service.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/tests/unit/api/test_system_monitoring_endpoints.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 234 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*