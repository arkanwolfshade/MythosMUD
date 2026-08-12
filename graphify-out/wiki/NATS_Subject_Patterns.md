# NATS Subject Patterns

> 13 nodes

## Key Concepts

- **.check_database_health_async()** (9 connections) — `server/services/health_service.py`
- **Any** (7 connections)
- **._create_health_response()** (7 connections) — `server/services/health_service.py`
- **._ping_database()** (5 connections) — `server/services/health_service.py`
- **._health_from_pool()** (5 connections) — `server/services/health_service.py`
- **room_service()** (5 connections) — `server/tests/unit/game/test_room_service.py`
- **._status_from_query_ms()** (4 connections) — `server/services/health_service.py`
- **.__init__()** (3 connections) — `server/services/health_service.py`
- **HealthStatus** (3 connections)
- **Initialize the health service.          Args:             connection_manager:** (1 connections) — `server/services/health_service.py`
- **Create a standardized health check response dictionary.          Args:** (1 connections) — `server/services/health_service.py`
- **Async database health check.** (1 connections) — `server/services/health_service.py`
- **Create a RoomService instance.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [Monitoring Response Models](Monitoring_Response_Models.md) (11 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (1 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (1 shared connections)
- [ASCII Map Exit Tests](ASCII_Map_Exit_Tests.md) (1 shared connections)

## Source Files

- `server/services/health_service.py`
- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 49 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*