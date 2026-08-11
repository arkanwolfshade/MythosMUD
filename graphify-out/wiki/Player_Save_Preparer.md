# Player Save Preparer

> 61 nodes

## Key Concepts

- **container_persistence_async.py** (34 connections) — `server/persistence/container_persistence_async.py`
- **ContainerRepository** (16 connections) — `server/persistence/repositories/container_repository.py`
- **create_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **Any** (12 connections)
- **get_container_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **_finalize_container_creation()** (11 connections) — `server/persistence/container_persistence_async.py`
- **_container_data_from_row()** (11 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (10 connections) — `server/persistence/container_persistence_async.py`
- **_container_data_to_dict()** (10 connections) — `server/persistence/repositories/container_repository.py`
- **_populate_container_items_async()** (9 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (9 connections)
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **delete_container_async()** (8 connections) — `server/persistence/container_persistence_async.py`
- **_call_create_container_procedure()** (7 connections) — `server/persistence/container_persistence_async.py`
- **Any** (7 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **UUID** (6 connections)
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **_parse_jsonb()** (5 connections) — `server/persistence/container_persistence_async.py`
- **_validate_container_create_params()** (5 connections) — `server/persistence/container_persistence_async.py`
- *... and 36 more nodes in this community*

## Relationships

- [Maps API Endpoints](Maps_API_Endpoints.md) (34 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (27 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/repositories/container_repository.py`

## Audit Trail

- EXTRACTED: 299 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*