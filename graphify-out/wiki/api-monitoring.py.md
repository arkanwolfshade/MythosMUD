# api/monitoring.py

> 88 nodes

## Key Concepts

- **api/monitoring.py** (60 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (55 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **MovementMonitor** (22 connections) — `server/game/movement_monitor.py`
- **Request** (20 connections)
- **asyncio** (15 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get** (14 connections)
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **_request_with_container()** (13 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **force_memory_cleanup()** (10 connections) — `server/api/monitoring.py`
- **get_connection_health_stats()** (10 connections) — `server/api/monitoring.py`
- **get_dual_connection_stats()** (10 connections) — `server/api/monitoring.py`
- **reset_metrics()** (10 connections) — `server/api/monitoring.py`
- **_resolve_memory_leak_collector_from_request()** (10 connections) — `server/api/monitoring.py`
- **validate_room_integrity()** (10 connections) — `server/api/monitoring.py`
- **get_cache_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_eventbus_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_memory_alerts()** (9 connections) — `server/api/monitoring.py`
- **get_memory_leak_metrics()** (9 connections) — `server/api/monitoring.py`
- **get_performance_stats()** (9 connections) — `server/api/monitoring.py`
- **get_performance_summary()** (9 connections) — `server/api/monitoring.py`
- *... and 63 more nodes in this community*

## Relationships

- [system_monitoring.py](system_monitoring.py.md) (32 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (19 shared connections)
- [HealthStatus](HealthStatus.md) (18 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [.get_alerts](get_alerts.md) (9 shared connections)
- [test_movement_monitor.py](test_movement_monitor.py.md) (8 shared connections)
- [HealthErrorResponse](HealthErrorResponse.md) (2 shared connections)
- [RoomCacheService](RoomCacheService.md) (2 shared connections)
- [GameStateProvider](GameStateProvider.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/game/movement_monitor.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`

## Audit Trail

- EXTRACTED: 324 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*