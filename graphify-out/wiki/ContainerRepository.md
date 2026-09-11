# ContainerRepository

> 30 nodes

## Key Concepts

- **ContainerRepository** (25 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
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
- **test_create_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_container_repository.py`
- **datetime** (2 connections)
- **ContainerData** (1 connections)
- **fixture** (1 connections)
- **Optional fields for creating a container row (beyond source_type).** (1 connections) — `server/persistence/container_create_params.py`
- **Update a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get decayed containers (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Delete a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Convert ContainerData to dict with items_json/metadata_json for compatibility.** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Repository for container persistence operations. Uses async SQLAlchemy…** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Initialize the container repository.** (1 connections) — `server/persistence/repositories/container_repository.py`
- *... and 5 more nodes in this community*

## Relationships

- [ContainerData](ContainerData.md) (18 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [get_session_maker](get_session_maker.md) (7 shared connections)
- [container_persistence.py](container_persistence.py.md) (5 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (4 shared connections)
- [RoomService](RoomService.md) (3 shared connections)
- [test_container_query_helpers_async.py](test_container_query_helpers_async.py.md) (3 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (2 shared connections)
- [item_instance_persistence_async.py](item_instance_persistence_async.py.md) (1 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/repositories/test_container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 85 (87%)
- INFERRED: 13 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*