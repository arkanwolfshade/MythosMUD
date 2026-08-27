# PerformanceMonitor

> 56 nodes

## Key Concepts

- **test_health.py** (29 connections) — `server/tests/unit/models/test_health.py`
- **HealthStatus** (22 connections) — `server/models/health.py`
- **health.py** (15 connections) — `server/models/health.py`
- **DatabaseComponent** (12 connections) — `server/models/health.py`
- **ServerComponent** (12 connections) — `server/models/health.py`
- **ConnectionsComponent** (11 connections) — `server/models/health.py`
- **HealthResponse** (10 connections) — `server/models/health.py`
- **HealthComponents** (9 connections) — `server/models/health.py`
- **HealthErrorResponse** (8 connections) — `server/models/health.py`
- **test_health_response_creation()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_default_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_response_with_alerts()** (8 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_creation()** (7 connections) — `server/tests/unit/models/test_health.py`
- **test_health_components_rejects_extra_fields()** (7 connections) — `server/tests/unit/models/test_health.py`
- **BaseModel** (6 connections)
- **test_connections_component_creation()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_connections_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_creation()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_database_component_without_last_query_time()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_server_component_creation()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_server_component_frozen()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_server_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_health.py`
- **test_health_error_response_creation()** (3 connections) — `server/tests/unit/models/test_health.py`
- **test_health_error_response_frozen()** (3 connections) — `server/tests/unit/models/test_health.py`
- *... and 31 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (5 shared connections)
- [bench_cache.py](bench_cache.py.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (1 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (1 shared connections)
- [test_chat_nats_publisher.py](test_chat_nats_publisher.py.md) (1 shared connections)

## Source Files

- `server/models/health.py`
- `server/tests/unit/models/test_health.py`

## Audit Trail

- EXTRACTED: 114 (87%)
- INFERRED: 17 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*