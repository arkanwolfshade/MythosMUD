# server persistence container data

> 113 nodes

## Key Concepts

- **test_container_persistence_extended_crud.py** (42 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **ContainerData** (40 connections) — `server/persistence/container_data.py`
- **server/persistence/__init__.py** (32 connections) — `server/persistence/__init__.py`
- **test_container_persistence_extended_parse.py** (26 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **ContainerDataExtras** (18 connections) — `server/persistence/container_data.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **persistence/container_data.py** (13 connections) — `server/persistence/container_data.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **parse_jsonb_column()** (11 connections) — `server/persistence/container_helpers.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_missing_item_instance_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_items_only_prototype_id()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_uuid_string_conversion()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_data_to_dict()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_container_data_to_dict_none_values()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **test_create_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_entity_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_container_data_init()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_parse.py`
- **Any** (4 connections)
- *... and 88 more nodes in this community*

## Relationships

- [composed](composed.md) (45 shared connections)
- [server persistence container persistence async](server_persistence_container_persistence_async.md) (15 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (14 shared connections)
- [server persistence container query helpers](server_persistence_container_query_helpers.md) (12 shared connections)
- [server persistence container create params](server_persistence_container_create_params.md) (11 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (9 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (6 shared connections)
- [server container persistence container data](server_container_persistence_container_data.md) (4 shared connections)
- [server persistence protocols playerrepositoryprotocol](server_persistence_protocols_playerrepositoryprotocol.md) (1 shared connections)
- [server persistence repositories experience repository](server_persistence_repositories_experience_repository.md) (1 shared connections)
- [server models player playerchannelpreferences](server_models_player_playerchannelpreferences.md) (1 shared connections)
- [server persistence repositories room repository](server_persistence_repositories_room_repository.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_data.py`
- `server/persistence/container_helpers.py`
- `server/persistence/container_query_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_parse.py`

## Audit Trail

- EXTRACTED: 258 (88%)
- INFERRED: 35 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*