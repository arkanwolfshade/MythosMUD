# Game Service Bundle

> 124 nodes

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
- **test_create_container_capacity_too_high()** (4 connections) — `server/tests/unit/container_persistence/test_container_persistence.py`
- *... and 99 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (22 shared connections)
- [Character Selection Screens](Character_Selection_Screens.md) (17 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (9 shared connections)
- [Archive Database Migration](Archive_Database_Migration.md) (6 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (1 shared connections)

## Source Files

- `server/container_persistence/__init__.py`
- `server/container_persistence/container_persistence.py`
- `server/tests/unit/container_persistence/test_container_persistence.py`

## Audit Trail

- EXTRACTED: 458 (89%)
- INFERRED: 54 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*