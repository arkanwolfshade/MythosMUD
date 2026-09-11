# container_query_helpers.py

> 30 nodes

## Key Concepts

- **container_query_helpers.py** (21 connections) — `server/persistence/container_query_helpers.py`
- **get_decayed_containers()** (13 connections) — `server/persistence/container_query_helpers.py`
- **_build_container_data_from_row()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_entity_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **get_containers_by_room_id()** (12 connections) — `server/persistence/container_query_helpers.py`
- **test_get_containers_by_entity_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Any** (4 connections)
- **ContainerData** (4 connections)
- **test_get_containers_by_entity_id_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_empty()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_containers_by_room_id_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_none_time()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_decayed_containers_success()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **datetime** (2 connections)
- **UUID** (2 connections)
- **Query helper functions for container persistence operations.** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers that have decayed (decay_at < current_time). Args: conn:…** (1 connections) — `server/persistence/container_query_helpers.py`
- **Build ContainerData object from database row. Args: conn: Database connection…** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers in a room. Args: conn: Database connection room_id: Room…** (1 connections) — `server/persistence/container_query_helpers.py`
- **Get all containers owned by an entity (player/NPC). Args: conn: Database…** (1 connections) — `server/persistence/container_query_helpers.py`
- **Test get_containers_by_room_id successfully retrieves containers.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test get_containers_by_room_id returns empty list when no containers.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **Test get_containers_by_room_id handles database errors.** (1 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- *... and 5 more nodes in this community*

## Relationships

- [ContainerData](ContainerData.md) (21 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [server/persistence/__init__.py](server-persistence-__init__.py.md) (4 shared connections)
- [fetch_container_items](fetch_container_items.md) (2 shared connections)
- [container_persistence.py](container_persistence.py.md) (2 shared connections)

## Source Files

- `server/persistence/container_query_helpers.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 76 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*