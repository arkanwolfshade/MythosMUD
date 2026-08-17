# EnvironmentalContainerLoader

> 28 nodes

## Key Concepts

- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (17 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **._parse_lock_state()** (4 connections) — `server/services/environmental_container_loader.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **._validate_container_capacity()** (3 connections) — `server/services/environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_capacity()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_lock_state()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_success()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_containers_for_room_filters_environment()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_creates_new()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_existing()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **Any** (3 connections)
- **asyncio** (3 connections)
- **test_environmental_loader_requires_persistence()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_disabled()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_none_when_missing()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **ContainerComponent** (2 connections)
- **UUID** (2 connections)
- **ContainerLockState** (1 connections)
- **migrate_room_container_to_postgresql.** (1 connections) — `server/services/environmental_container_loader.py`
- **Load all environmental containers for a room from PostgreSQL. Args: room_id:…** (1 connections) — `server/services/environmental_container_loader.py`
- **Service for loading environmental containers from JSON and PostgreSQL. Handles…** (1 connections) — `server/services/environmental_container_loader.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [ValidationError](ValidationError.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/environmental_container_loader.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 46 (79%)
- INFERRED: 12 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*