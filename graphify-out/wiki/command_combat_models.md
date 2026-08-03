# command combat models

> 87 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **BaseModel** (19 connections)
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **Any** (10 connections)
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **get_memory_leak_metrics()** (8 connections) — `server/api/monitoring.py`
- **IntegrityResponse** (5 connections) — `server/api/monitoring_models.py`
- **AlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **MemoryStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **MemoryAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **DualConnectionStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **PerformanceStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **ConnectionHealthStatsResponse** (5 connections) — `server/api/monitoring_models.py`
- **EventBusMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **CacheMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **TaskMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **MemoryLeakMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- *... and 62 more nodes in this community*

## Relationships

- [health models rationale](health_models_rationale.md) (45 shared connections)
- [command inventory factories](command_inventory_factories.md) (18 shared connections)
- [System Metrics](System_Metrics.md) (14 shared connections)
- [grace period login](grace_period_login.md) (8 shared connections)
- [time service rationale](time_service_rationale.md) (6 shared connections)
- [Exception Containers](Exception_Containers.md) (5 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [cache caching service](cache_caching_service.md) (3 shared connections)
- [npc population control](npc_population_control.md) (2 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [room cache services](room_cache_services.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/caching/lru_cache.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 433 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*