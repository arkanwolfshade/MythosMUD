# Container Data Models

> 81 nodes · cohesion 0.06

## Key Concepts

- **ContainerData** (52 connections) — `server/persistence/container_data.py`
- **ContainerDataCore** (43 connections) — `server/persistence/container_data.py`
- **ContainerDataExtras** (37 connections) — `server/persistence/container_data.py`
- **container_persistence_async.py** (32 connections) — `server/persistence/container_persistence_async.py`
- **container_query_helpers_async.py** (22 connections) — `server/persistence/container_query_helpers_async.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **get_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **_build_container_data_from_row_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **Any** (14 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **container_data.py** (9 connections) — `server/persistence/container_data.py`
- **get_containers_by_entity_id_async()** (9 connections) — `server/persistence/container_query_helpers_async.py`
- **get_decayed_containers_async()** (9 connections) — `server/persistence/container_query_helpers_async.py`
- **get_containers_by_room_id_async()** (8 connections) — `server/persistence/container_query_helpers_async.py`
- **UUID** (8 connections) — `server/persistence/container_persistence_async.py`
- **validate_lock_state()** (7 connections) — `server/persistence/container_helpers.py`
- **_populate_container_items_async()** (7 connections) — `server/persistence/container_persistence_async.py`
- **ContainerData** (7 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (7 connections) — `server/persistence/container_query_helpers_async.py`
- **ContainerData** (7 connections) — `server/persistence/container_query_helpers_async.py`
- **_call_create_container_procedure()** (6 connections) — `server/persistence/container_persistence_async.py`
- *... and 56 more nodes in this community*

## Relationships

- [[Container Persistence Layer]] (41 shared connections)
- [[NPC Admin API]] (27 shared connections)
- [[Container Repository CRUD]] (25 shared connections)
- [[Container Persistence Queries]] (21 shared connections)
- [[JSONB Column Parsing]] (6 shared connections)
- [[Persistence Item Instance]] (5 shared connections)
- [[Persistence Container Extended]] (5 shared connections)
- [[Container Persistence Ops]] (1 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/container_query_helpers.py`
- `server/persistence/container_query_helpers_async.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`

## Audit Trail

- EXTRACTED: 419 (79%)
- INFERRED: 110 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
