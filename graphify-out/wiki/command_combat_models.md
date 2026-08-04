# command combat models

> 86 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **BaseModel** (19 connections)
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **__init__.py** (10 connections) — `server/api/__init__.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **Any** (10 connections)
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
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
- **PerformanceSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- *... and 61 more nodes in this community*

## Relationships

- [health models rationale](health_models_rationale.md) (41 shared connections)
- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (10 shared connections)
- [grace period login](grace_period_login.md) (8 shared connections)
- [room cache services](room_cache_services.md) (7 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (5 shared connections)
- [Exception Containers](Exception_Containers.md) (4 shared connections)
- [System Metrics](System_Metrics.md) (4 shared connections)
- [combat commands handler](combat_commands_handler.md) (3 shared connections)
- [follow service game](follow_service_game.md) (3 shared connections)
- [realtime monitoring statistics](realtime_monitoring_statistics.md) (3 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/connection_manager.py`

## Audit Trail

- EXTRACTED: 423 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*