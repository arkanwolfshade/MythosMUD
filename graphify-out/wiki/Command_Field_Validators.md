# Command Field Validators

> 98 nodes

## Key Concepts

- **monitoring.py** (62 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (57 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **monitoring_models.py** (22 connections) — `server/api/monitoring_models.py`
- **Request** (19 connections)
- **BaseModel** (19 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **_request_with_container()** (11 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector()** (10 connections) — `server/api/monitoring.py`
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
- **get_cache_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_task_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (8 connections) — `server/api/monitoring.py`
- **get_registry()** (7 connections) — `server/app/task_registry.py`
- *... and 73 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (29 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (21 shared connections)
- [Movement Performance Monitor](Movement_Performance_Monitor.md) (16 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (9 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (4 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (1 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Player Left Room Tests](Player_Left_Room_Tests.md) (1 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/app/task_registry.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 533 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*