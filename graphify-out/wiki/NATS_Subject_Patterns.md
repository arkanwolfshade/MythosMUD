# NATS Subject Patterns

> 41 nodes

## Key Concepts

- **HealthService** (24 connections) — `server/services/health_service.py`
- **.get_health_status()** (10 connections) — `server/services/health_service.py`
- **.check_database_health_async()** (9 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **.get_server_component_health()** (7 connections) — `server/services/health_service.py`
- **.check_database_health()** (6 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **.check_connections_health()** (5 connections) — `server/services/health_service.py`
- **.get_database_component_health()** (5 connections) — `server/services/health_service.py`
- **.get_connections_component_health()** (5 connections) — `server/services/health_service.py`
- **.determine_overall_status()** (5 connections) — `server/services/health_service.py`
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **.get_database_component_health_async()** (4 connections) — `server/services/health_service.py`
- **.generate_alerts()** (4 connections) — `server/services/health_service.py`
- **test_get_health_service_creates_instance()** (4 connections) — `server/tests/unit/services/test_health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **HealthStatus** (3 connections)
- **health_service()** (3 connections) — `server/tests/unit/services/test_health_service.py`
- **Health monitoring service for MythosMUD server.      Provides comprehensive he** (1 connections) — `server/services/health_service.py`
- **Initialize the health service.          Args:             connection_manager:** (1 connections) — `server/services/health_service.py`
- *... and 16 more nodes in this community*

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (14 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (2 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (2 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/services/test_health_service.py`

## Audit Trail

- EXTRACTED: 148 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*