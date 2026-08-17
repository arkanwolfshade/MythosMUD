# server api monitoring models

> 99 nodes

## Key Concepts

- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **system_monitoring.py** (24 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (23 connections) — `server/api/monitoring_models.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **BaseModel** (19 connections)
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **get_system_metrics()** (12 connections) — `server/api/system_monitoring.py`
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
- *... and 74 more nodes in this community*

## Relationships

- [server api monitoring](server_api_monitoring.md) (33 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (8 shared connections)
- [server app lifespan](server_app_lifespan.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [performancestats](performancestats.md) (7 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (5 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (4 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (4 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (3 shared connections)
- [iteminstance](iteminstance.md) (3 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (3 shared connections)
- [server caching cache service](server_caching_cache_service.md) (2 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 241 (92%)
- INFERRED: 22 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*