# command combat models

> 63 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (8 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (8 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (8 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (8 connections) — `server/api/monitoring.py`
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
- *... and 38 more nodes in this community*

## Relationships

- [health models rationale](health_models_rationale.md) (41 shared connections)
- [npc population control](npc_population_control.md) (12 shared connections)
- [System Metrics](System_Metrics.md) (11 shared connections)
- [Exception Containers](Exception_Containers.md) (10 shared connections)
- [grace period login](grace_period_login.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [message nats handler](message_nats_handler.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [player look commands](player_look_commands.md) (2 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 341 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*