# Container Persistence Ops

> 107 nodes · cohesion 0.03

## Key Concepts

- **test_container_persistence.py** (60 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **_fetch_container_items()** (25 connections) — `server/container_persistence/container_persistence.py`
- **create_container()** (21 connections) — `server/container_persistence/container_persistence.py`
- **container_persistence.py** (20 connections) — `server/container_persistence/container_persistence.py`
- **ContainerData** (18 connections) — `server/container_persistence/container_persistence.py`
- **get_container()** (15 connections) — `server/container_persistence/container_persistence.py`
- **update_container()** (15 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_entity_id()** (13 connections) — `server/container_persistence/container_persistence.py`
- **get_containers_by_room_id()** (12 connections) — `server/container_persistence/container_persistence.py`
- **delete_container()** (10 connections) — `server/container_persistence/container_persistence.py`
- **Any** (10 connections) — `server/container_persistence/container_persistence.py`
- **UUID** (9 connections) — `server/container_persistence/container_persistence.py`
- **__init__.py** (9 connections) — `server/container_persistence/__init__.py`
- **.__init__()** (4 connections) — `server/container_persistence/container_persistence.py`
- **.to_dict()** (4 connections) — `server/container_persistence/container_persistence.py`
- **test_create_container_get_container_success()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_update_container_success()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_update_container_with_items()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_init()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_to_dict()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_to_dict_with_all_fields()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_container_data_to_dict_with_datetimes()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_capacity_too_high()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_database_error()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- **test_create_container_get_container_fallback()** (3 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- *... and 82 more nodes in this community*

## Relationships

- [[JSONB Column Parsing]] (20 shared connections)
- [[NPC Admin API]] (16 shared connections)
- [[Container Persistence Queries]] (1 shared connections)
- [[Container Data Models]] (1 shared connections)

## Source Files

- `server/container_persistence/__init__.py`
- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`

## Audit Trail

- EXTRACTED: 417 (98%)
- INFERRED: 9 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
