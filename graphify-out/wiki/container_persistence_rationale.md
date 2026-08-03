# container persistence rationale

> 140 nodes

## Key Concepts

- **test_container_persistence.py** (61 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **_parse_jsonb_column()** (28 connections) — `server/container_persistence/container_persistence.py`
- **_fetch_container_items()** (25 connections) — `server/container_persistence/container_persistence.py`
- **ContainerData** (23 connections) — `server/container_persistence/container_persistence.py`
- **create_container()** (23 connections) — `server/container_persistence/container_persistence.py`
- **container_persistence.py** (21 connections) — `server/container_persistence/container_persistence.py`
- **update_container()** (17 connections) — `server/container_persistence/container_persistence.py`
- **get_container()** (16 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_entity_id()** (14 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_room_id()** (13 connections) — `server/container_persistence/container_persistence.py`
- **delete_container()** (11 connections) — `server/container_persistence/container_persistence.py`
- **Any** (10 connections)
- **__init__.py** (9 connections) — `server/container_persistence/__init__.py`
- **UUID** (9 connections)
- **test_persistence_container_persistence.py** (8 connections) — `server/tests/unit/persistence/test_persistence_container_persistence.py`
- **.__init__()** (4 connections) — `server/container_persistence/container_persistence.py`
- **.to_dict()** (4 connections) — `server/container_persistence/container_persistence.py`
- **test_create_container_invalid_source_type()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_invalid_capacity()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_invalid_lock_state()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_update_container_invalid_lock_state()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_get_container_database_error()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_success()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_no_id_returned()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- *... and 115 more nodes in this community*

## Relationships

- [persistence container extended](persistence_container_extended.md) (17 shared connections)
- [npc populate databases](npc_populate_databases.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (12 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (7 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [persistence container item](persistence_container_item.md) (2 shared connections)

## Source Files

- `server/container_persistence/__init__.py`
- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_persistence_container_persistence.py`

## Audit Trail

- EXTRACTED: 488 (89%)
- INFERRED: 61 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*