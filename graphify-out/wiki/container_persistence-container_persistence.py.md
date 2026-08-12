# container_persistence/container_persistence.py

> 30 nodes

## Key Concepts

- **create_container()** (21 connections) — `server/container_persistence/container_persistence.py`
- **container_persistence/container_persistence.py** (21 connections) — `server/container_persistence/container_persistence.py`
- **ContainerData** (18 connections) — `server/container_persistence/container_persistence.py`
- **get_container()** (15 connections) — `server/container_persistence/container_persistence.py`
- **update_container()** (15 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_entity_id()** (13 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_room_id()** (12 connections) — `server/container_persistence/container_persistence.py`
- **delete_container()** (10 connections) — `server/container_persistence/container_persistence.py`
- **Any** (10 connections)
- **server/container_persistence/__init__.py** (9 connections) — `server/container_persistence/__init__.py`
- **UUID** (8 connections)
- **.__init__()** (4 connections) — `server/container_persistence/container_persistence.py`
- **test_create_container_get_container_success()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_update_container_success()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_update_container_with_items()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **.to_dict()** (3 connections) — `server/container_persistence/container_persistence.py`
- **datetime** (3 connections)
- **Container persistence operations for the unified container system. As…** (1 connections) — `server/container_persistence/container_persistence.py`
- **Data class for container information.** (1 connections) — `server/container_persistence/container_persistence.py`
- **Convert container data to dictionary for ContainerComponent.** (1 connections) — `server/container_persistence/container_persistence.py`
- **Create a new container in the database. Args: conn: Database connection…** (1 connections) — `server/container_persistence/container_persistence.py`
- **Get a container by ID. Args: conn: Database connection container_id: Container…** (1 connections) — `server/container_persistence/container_persistence.py`
- **Get all containers in a room. Args: conn: Database connection room_id: Room…** (1 connections) — `server/container_persistence/container_persistence.py`
- **Get all containers owned by an entity (player/NPC). Args: conn: Database…** (1 connections) — `server/container_persistence/container_persistence.py`
- **Update a container's items, lock state, or metadata. Args: conn: Database…** (1 connections) — `server/container_persistence/container_persistence.py`
- *... and 5 more nodes in this community*

## Relationships

- [test_container_persistence.py](test_container_persistence.py.md) (31 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (10 shared connections)
- [_fetch_container_items](_fetch_container_items.md) (6 shared connections)
- [_parse_jsonb_column](_parse_jsonb_column.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_create_container_database_error](test_create_container_database_error.md) (1 shared connections)
- [test_create_container_invalid_source_type](test_create_container_invalid_source_type.md) (1 shared connections)
- [test_create_container_success](test_create_container_success.md) (1 shared connections)
- [test_create_container_with_items](test_create_container_with_items.md) (1 shared connections)
- [test_delete_container_success](test_delete_container_success.md) (1 shared connections)
- [test_get_containers_by_entity_id_database_error](test_get_containers_by_entity_id_database_error.md) (1 shared connections)
- [test_get_containers_by_room_id_empty](test_get_containers_by_room_id_empty.md) (1 shared connections)

## Source Files

- `server/container_persistence/__init__.py`
- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`

## Audit Trail

- EXTRACTED: 187 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*