# Monitoring Response Models

> 294 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **test_health_service.py** (43 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health.py** (27 connections) — `server/tests/unit/models/test_health.py`
- **DatabaseComponent** (24 connections) — `server/models/health.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **ServerComponent** (23 connections) — `server/models/health.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **ConnectionsComponent** (22 connections) — `server/models/health.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **health_service.py** (19 connections) — `server/services/health_service.py`
- **HealthResponse** (18 connections) — `server/models/health.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **health.py** (14 connections) — `server/models/health.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_health_status()** (12 connections) — `server/api/monitoring.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **HealthStatus** (11 connections) — `server/models/health.py`
- *... and 269 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (33 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (21 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (13 shared connections)
- [Party Service Management](Party_Service_Management.md) (8 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (8 shared connections)
- [Movement Performance Monitor](Movement_Performance_Monitor.md) (7 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (7 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (5 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (4 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (4 shared connections)
- [Cursor Subagents Docs](Cursor_Subagents_Docs.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/task_registry.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/services/health_service.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`
- `server/tests/unit/models/test_health.py`
- `server/tests/unit/services/test_health_service.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 1284 (98%)
- INFERRED: 24 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*