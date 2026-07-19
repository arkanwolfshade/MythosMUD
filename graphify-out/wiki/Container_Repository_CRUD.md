# Container Repository CRUD

> 33 nodes · cohesion 0.11

## Key Concepts

- **ContainerCreateParams** (29 connections) — `server/persistence/container_create_params.py`
- **container_repository.py** (18 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerRepository** (16 connections) — `server/persistence/repositories/container_repository.py`
- **_container_data_to_dict()** (10 connections) — `server/persistence/repositories/container_repository.py`
- **Any** (9 connections) — `server/persistence/repositories/container_repository.py`
- **delete_container_async()** (7 connections) — `server/persistence/container_persistence_async.py`
- **.create_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_entity_id()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_decayed_containers()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.update_container()** (7 connections) — `server/persistence/repositories/container_repository.py`
- **UUID** (7 connections) — `server/persistence/repositories/container_repository.py`
- **.get_containers_by_room_id()** (6 connections) — `server/persistence/repositories/container_repository.py`
- **.delete_container()** (5 connections) — `server/persistence/repositories/container_repository.py`
- **test_create_container_success()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **datetime** (4 connections) — `server/persistence/repositories/container_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerCreateParams** (3 connections) — `server/persistence/repositories/container_repository.py`
- **ContainerData** (3 connections) — `server/persistence/repositories/container_repository.py`
- **Optional fields for creating a container row (beyond source_type).** (1 connections) — `server/persistence/container_create_params.py`
- **Delete a container (async) via delete_container procedure. Returns True if delet** (1 connections) — `server/persistence/container_persistence_async.py`
- **Test create_container successfully creates container.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Container repository for async persistence operations.  This module provides asy** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Update a container (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- **Get decayed containers (async).** (1 connections) — `server/persistence/repositories/container_repository.py`
- *... and 8 more nodes in this community*

## Relationships

- [[Container Data Models]] (25 shared connections)
- [[NPC Admin API]] (17 shared connections)
- [[Container Persistence Layer]] (11 shared connections)
- [[Persistence Item Instance]] (3 shared connections)
- [[Async Persistence Delegates]] (3 shared connections)
- [[Container Persistence Queries]] (2 shared connections)

## Source Files

- `server/persistence/container_create_params.py`
- `server/persistence/container_persistence_async.py`
- `server/persistence/repositories/container_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 146 (84%)
- INFERRED: 27 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
