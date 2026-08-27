# NPCStartupService

> 34 nodes

## Key Concepts

- **HealthService** (27 connections) — `server/services/health_service.py`
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
- **.get_server_uptime()** (4 connections) — `server/services/health_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **.get_cpu_usage()** (3 connections) — `server/services/health_service.py`
- **.get_memory_usage()** (3 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **HealthStatus** (3 connections)
- **HealthResponse** (1 connections)
- **Create a standardized health check response dictionary. Args: status: Health…** (1 connections) — `server/services/health_service.py`
- **Async database health check.** (1 connections) — `server/services/health_service.py`
- **check_database_health.** (1 connections) — `server/services/health_service.py`
- **Check connection manager health.** (1 connections) — `server/services/health_service.py`
- **Get server component health status.** (1 connections) — `server/services/health_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [vite Best Practices](vite_Best_Practices.md) (9 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)
- [Coverage Improvement Summary - Plan 2 Execution](Coverage_Improvement_Summary_-_Plan_2_Execution.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`

## Audit Trail

- EXTRACTED: 74 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*