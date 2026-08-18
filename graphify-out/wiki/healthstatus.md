# healthstatus

> 53 nodes

## Key Concepts

- **HealthService** (24 connections) — `server/services/health_service.py`
- **HealthComponents** (21 connections) — `server/models/health.py`
- **health_service.py** (21 connections) — `server/services/health_service.py`
- **resolve_connection_manager()** (13 connections) — `server/realtime/connection_manager.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **get_health_service()** (9 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (9 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **.check_database_health()** (6 connections) — `server/services/health_service.py`
- **room_service()** (6 connections) — `server/tests/unit/game/test_room_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **test_get_health_service_creates_instance()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- *... and 28 more nodes in this community*

## Relationships

- [server models health](server_models_health.md) (29 shared connections)
- [server api monitoring](server_api_monitoring.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (4 shared connections)
- [server api real time](server_api_real_time.md) (2 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (2 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (2 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (1 shared connections)
- [server api system monitoring get](server_api_system_monitoring_get.md) (1 shared connections)
- [server realtime connection manager utils](server_realtime_connection_manager_utils.md) (1 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [roomdictlist](roomdictlist.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/game/test_room_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 141 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*