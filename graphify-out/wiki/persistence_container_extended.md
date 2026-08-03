# persistence container extended

> 95 nodes

## Key Concepts

- **ContainerData** (34 connections) — `server/persistence/container_data.py`
- **test_container_persistence_extended_parse.py** (26 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **container_query_helpers_async.py** (23 connections) — `server/persistence/container_query_helpers_async.py`
- **container_repository.py** (23 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **ContainerRepository** (16 connections) — `server/persistence/repositories/container_repository.py`
- **_build_container_data_from_row_async()** (14 connections) — `server/persistence/container_query_helpers_async.py`
- **container_data.py** (12 connections) — `server/persistence/container_data.py`
- **get_containers_by_entity_id_async()** (10 connections) — `server/persistence/container_query_helpers_async.py`
- **get_decayed_containers_async()** (10 connections) — `server/persistence/container_query_helpers_async.py`
- **_container_data_to_dict()** (10 connections) — `server/persistence/repositories/container_repository.py`
- **get_containers_by_room_id_async()** (9 connections) — `server/persistence/container_query_helpers_async.py`
- **Any** (7 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **UUID** (5 connections)
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_data_to_dict()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_container_data_to_dict_none_values()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **_parse_jsonb()** (4 connections) — `server/persistence/container_query_helpers_async.py`
- *... and 70 more nodes in this community*

## Relationships

- [persistence container item](persistence_container_item.md) (51 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (26 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (17 shared connections)
- [Database Config](Database_Config.md) (8 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [npc populate databases](npc_populate_databases.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [dialogue definitions admin](dialogue_definitions_admin.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)

## Source Files

- `server/persistence/container_data.py`
- `server/persistence/container_query_helpers_async.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`

## Audit Trail

- EXTRACTED: 389 (92%)
- INFERRED: 35 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*