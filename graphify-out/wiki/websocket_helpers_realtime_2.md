# websocket helpers realtime

> 39 nodes

## Key Concepts

- **ContainerRepository** (26 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **_container_data_to_dict()** (12 connections) — `server/persistence/repositories/container_repository.py`
- **_sample_container_data()** (11 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **container_create_params.py** (9 connections) — `server/persistence/container_create_params.py`
- **Any** (7 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **UUID** (5 connections)
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **test_create_container()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_data_to_dict_renames_keys()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_container_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_containers_by_room_id()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_containers_by_entity_id()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_update_container()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_container_not_found()** (2 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_decayed_containers()** (2 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_delete_container()** (2 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- *... and 14 more nodes in this community*

## Relationships

- [persistence container item](persistence_container_item.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (10 shared connections)
- [command combat models](command_combat_models.md) (8 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (4 shared connections)
- [retry nats handler](retry_nats_handler.md) (3 shared connections)
- [persistence container helpers](persistence_container_helpers.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`

## Audit Trail

- EXTRACTED: 179 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*