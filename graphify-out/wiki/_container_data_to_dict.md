# _container_data_to_dict

> 20 nodes

## Key Concepts

- **_container_data_to_dict()** (13 connections) — `server/persistence/repositories/container_repository.py`
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **Any** (7 connections)
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **UUID** (5 connections)
- **datetime** (2 connections)
- **ContainerData** (1 connections)
- **Update a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get decayed containers (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Delete a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Convert ContainerData to dict with items_json/metadata_json for compatibility.** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Create a new container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get a container by ID (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get all containers in a room (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get all containers owned by an entity (async).** (1 connections) — `server/persistence/repositories/container_repository.py`

## Relationships

- [ContainerRepository](ContainerRepository.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (4 shared connections)
- [test_container_query_helpers_async.py](test_container_query_helpers_async.py.md) (3 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/container_repository.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*