# Monitoring Response Models

> 105 nodes · cohesion 0.04

## Key Concepts

- **monitoring.py** (61 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **BaseModel** (19 connections)
- **Request** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (9 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (9 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (9 connections) — `server/api/monitoring.py`
- **_resolve_cache_manager_from_request()** (9 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (9 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (8 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (8 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (8 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (8 connections) — `server/api/monitoring.py`
- **get_system_alerts()** (8 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (8 connections) — `server/api/monitoring.py`
- *... and 80 more nodes in this community*

## Relationships

- [Exploration Command Factories](Exploration_Command_Factories.md) (19 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (18 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (17 shared connections)
- [Movement Performance Monitor](Movement_Performance_Monitor.md) (13 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (3 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (3 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (2 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (2 shared connections)
- [Admin Status Commands](Admin_Status_Commands.md) (2 shared connections)
- [Dependency Injection Tests](Dependency_Injection_Tests.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 560 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*