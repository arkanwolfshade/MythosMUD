# Command Field Validators

> 125 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (8 connections) — `server/api/monitoring.py`
- **reset_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (8 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (8 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (8 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (8 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- *... and 100 more nodes in this community*

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (21 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (13 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (13 shared connections)
- [Movement Performance Monitor](Movement_Performance_Monitor.md) (10 shared connections)
- [Cursor Subagents Docs](Cursor_Subagents_Docs.md) (7 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Grace Period Blocking Tests](Grace_Period_Blocking_Tests.md) (2 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 637 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*