# ContainerRepository

> 24 nodes

## Key Concepts

- **ContainerRepository** (25 connections) — `server/persistence/repositories/container_repository.py`
- **test_container_repository.py** (22 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **_sample_container_data()** (11 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **asyncio** (8 connections)
- **test_create_container()** (5 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_container_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_containers_by_entity_id()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_containers_by_room_id()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_update_container()** (4 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_create_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_container_data_to_dict_renames_keys()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_delete_container()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_container_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **test_get_decayed_containers()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **ContainerData** (1 connections)
- **fixture** (1 connections)
- **Optional fields for creating a container row (beyond source_type).** (1 connections) — `server/persistence/container_create_params.py`
- **Repository for container persistence operations. Uses async SQLAlchemy…** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Initialize the container repository.** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Unit tests for ContainerRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **Test create_container successfully creates container.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Relationships

- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (12 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [_container_data_to_dict](_container_data_to_dict.md) (10 shared connections)
- [container_persistence.py](container_persistence.py.md) (5 shared connections)
- [test_async_persistence_delegates.py](test_async_persistence_delegates.py.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 77 (87%)
- INFERRED: 12 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*