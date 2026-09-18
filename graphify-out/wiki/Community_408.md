# Community 408

> 43 nodes

## Key Concepts

- **HealthService** (27 connections) — `server/services/health_service.py`
- **resolve_connection_manager()** (12 connections) — `server/realtime/connection_manager.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (7 connections) — `server/services/health_service.py`
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **.check_database_health()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **test_health_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **test_health_service_accepts_injected_room_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **HealthStatus** (3 connections)
- **Typed wrapper; utils stays free of ConnectionManager imports (import cycles).** (1 connections) — `server/realtime/connection_manager.py`
- *... and 18 more nodes in this community*

## Relationships

- [Community 77](Community_77.md) (12 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (3 shared connections)
- [Community 830](Community_830.md) (2 shared connections)
- [Community 239](Community_239.md) (1 shared connections)
- [Community 178](Community_178.md) (1 shared connections)
- [Community 513](Community_513.md) (1 shared connections)
- [Community 421](Community_421.md) (1 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (1 shared connections)
- [Community 92](Community_92.md) (1 shared connections)
- [Community 42](Community_42.md) (1 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (1 shared connections)
- [Community 499](Community_499.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager.py`
- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 91 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*