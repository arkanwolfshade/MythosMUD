# server api monitoring models

> 91 nodes

## Key Concepts

- **system_monitoring.py** (24 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (23 connections) — `server/api/monitoring_models.py`
- **BaseModel** (19 connections)
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **MessageResponse** (6 connections) — `server/api/monitoring_models.py`
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
- **PerformanceSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- *... and 66 more nodes in this community*

## Relationships

- [server api monitoring](server_api_monitoring.md) (32 shared connections)
- [server app lifespan](server_app_lifespan.md) (9 shared connections)
- [server api system monitoring get](server_api_system_monitoring_get.md) (7 shared connections)
- [server api players](server_api_players.md) (6 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (6 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (1 shared connections)
- [server caching cache service rationale](server_caching_cache_service_rationale.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 208 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*