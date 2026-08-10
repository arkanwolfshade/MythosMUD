# JSONB Column Parsing

> 39 nodes

## Key Concepts

- **ContainerData** (34 connections) — `server/persistence/container_data.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **container_query_helpers_async.py** (23 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (23 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **_build_container_data_from_row_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **container_data.py** (12 connections) — `server/persistence/container_data.py`
- **_log_and_resolve_created_container()** (11 connections) — `server/persistence/container_persistence.py`
- **_CreateOutcome** (10 connections) — `server/persistence/container_persistence.py`
- **get_containers_by_entity_id_async()** (10 connections) — `server/persistence/container_query_helpers_async.py`
- **get_decayed_containers_async()** (10 connections) — `server/persistence/container_query_helpers_async.py`
- **get_containers_by_room_id_async()** (9 connections) — `server/persistence/container_query_helpers_async.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_data_to_dict()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_container_data_to_dict_none_values()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **_parse_jsonb()** (4 connections) — `server/persistence/container_query_helpers_async.py`
- **AsyncSession** (4 connections)
- **ContainerData** (4 connections)
- **.__init__()** (3 connections) — `server/persistence/container_data.py`
- **UUID** (3 connections)
- **test_log_and_resolve_created_container_fallback_when_get_missing()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **.to_dict()** (2 connections) — `server/persistence/container_data.py`
- **Any** (2 connections)
- **datetime** (2 connections)
- **Container data class for persistence operations.** (1 connections) — `server/persistence/container_data.py`
- *... and 14 more nodes in this community*

## Relationships

- [Maps API Endpoints](Maps_API_Endpoints.md) (23 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (23 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (18 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (9 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (8 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (6 shared connections)
- [Feature Implementation Phases](Feature_Implementation_Phases.md) (1 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_persistence.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 236 (92%)
- INFERRED: 20 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*