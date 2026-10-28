# Player

> 95 nodes · cohesion 0.05

## Key Concepts

- **api/monitoring.py** (60 connections) — `server/api/monitoring.py`
- **test_monitoring_endpoints.py** (55 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **HealthResponse** (17 connections) — `server/models/health.py`
- **asyncio** (15 connections)
- **get** (14 connections)
- **_resolve_connection_manager_from_request()** (14 connections) — `server/api/monitoring.py`
- **get_movement_monitor()** (14 connections) — `server/game/movement_monitor.py`
- **get_health_status()** (13 connections) — `server/api/monitoring.py`
- **_request_with_container()** (13 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **movement_monitor.py** (12 connections) — `server/game/movement_monitor.py`
- **get_memory_stats()** (11 connections) — `server/api/monitoring.py`
- **get_movement_metrics()** (11 connections) — `server/api/monitoring.py`
- **_resolve_event_bus_from_request()** (11 connections) — `server/api/monitoring.py`
- **resolve_connection_manager()** (11 connections) — `server/realtime/connection_manager.py`
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
- *... and 70 more nodes in this community*

## Relationships

- [FStringLoggingFixer](FStringLoggingFixer.md) (29 shared connections)
- [test_logging_utilities.py](test_logging_utilities.py.md) (22 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (21 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (19 shared connections)
- [Room](Room.md) (8 shared connections)
- [MutationDecision](MutationDecision.md) (8 shared connections)
- [handle_read_command](handle_read_command.md) (5 shared connections)
- [✅ POSITIVE FINDINGS](✅_POSITIVE_FINDINGS.md) (4 shared connections)
- [LucidityTierCache](LucidityTierCache.md) (2 shared connections)
- [command_error](command_error.md) (2 shared connections)
- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)

## Source Files

- `server/api/monitoring.py`
- `server/api/monitoring_models.py`
- `server/game/movement_monitor.py`
- `server/models/health.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/game/test_movement_monitor.py`

## Audit Trail

- EXTRACTED: 348 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*