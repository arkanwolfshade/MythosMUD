# ContainerRepository

> 48 nodes

## Key Concepts

- **ContainerRepository** (25 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerDataCore** (24 connections) — `server/persistence/container_data.py`
- **test_container_repository.py** (21 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_container_data_to_dict()** (13 connections) — `server/persistence/repositories/container_repository.py`
- **_sample_container_data()** (11 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **asyncio** (8 connections)
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **container_create_params.py** (7 connections) — `server/persistence/container_create_params.py`
- **Any** (7 connections)
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **test_create_container()** (5 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **UUID** (5 connections)
- **test_get_container_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_containers_by_entity_id()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_containers_by_room_id()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_update_container()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- *... and 23 more nodes in this community*

## Relationships

- [ContainerData](ContainerData.md) (23 shared connections)
- [container_persistence.py](container_persistence.py.md) (9 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (9 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [update_container](update_container.md) (3 shared connections)
- [test_container_persistence_extended_parse.py](test_container_persistence_extended_parse.py.md) (2 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (1 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/container_data.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 148 (92%)
- INFERRED: 13 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*