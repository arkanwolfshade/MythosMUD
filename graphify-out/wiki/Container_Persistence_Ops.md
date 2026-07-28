# Container Persistence Ops

> 174 nodes · cohesion 0.02

## Key Concepts

- **test_container_persistence.py** (61 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **_parse_jsonb_column()** (28 connections) — `server/container_persistence/container_persistence.py`
- **_fetch_container_items()** (25 connections) — `server/container_persistence/container_persistence.py`
- **ContainerData** (23 connections) — `server/container_persistence/container_persistence.py`
- **create_container()** (23 connections) — `server/container_persistence/container_persistence.py`
- **container_persistence.py** (21 connections) — `server/container_persistence/container_persistence.py`
- **update_container()** (17 connections) — `server/container_persistence/container_persistence.py`
- **get_container()** (16 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_entity_id()** (14 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_room_id()** (13 connections) — `server/container_persistence/container_persistence.py`
- **delete_container()** (11 connections) — `server/container_persistence/container_persistence.py`
- **Any** (10 connections)
- **UUID** (9 connections)
- **__init__.py** (9 connections) — `server/container_persistence/__init__.py`
- **test_persistence_container_persistence.py** (8 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **.__init__()** (4 connections) — `server/container_persistence/container_persistence.py`
- **.to_dict()** (4 connections) — `server/container_persistence/container_persistence.py`
- **test_create_container_capacity_too_high()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_get_container_fallback()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_get_container_success()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_invalid_capacity()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_invalid_lock_state()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_invalid_source_type()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_no_id_returned()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- *... and 149 more nodes in this community*

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (23 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (19 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (9 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)

## Source Files

- `server/container_persistence/__init__.py`
- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_persistence_container_persistence.py`

## Audit Trail

- EXTRACTED: 539 (87%)
- INFERRED: 78 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*