# project paths rationale

> 24 nodes

## Key Concepts

- **EnvironmentalContainerLoader** (16 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (16 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **.load_container_from_room_json()** (8 connections) — `server/services/environmental_container_loader.py`
- **.migrate_room_container_to_postgresql()** (7 connections) — `server/services/environmental_container_loader.py`
- **.__init__()** (3 connections) — `server/services/environmental_container_loader.py`
- **Any** (3 connections)
- **.load_containers_for_room()** (3 connections) — `server/services/environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_capacity()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_invalid_lock_state()** (3 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **ContainerComponent** (2 connections)
- **UUID** (2 connections)
- **test_environmental_loader_requires_persistence()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_none_when_missing()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_disabled()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_container_from_room_json_success()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_existing()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_migrate_room_container_creates_new()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **test_load_containers_for_room_filters_environment()** (2 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **Service for loading environmental containers from JSON and PostgreSQL.      Hand** (1 connections) — `server/services/environmental_container_loader.py`
- **Initialize the environmental container loader.          Args:             persis** (1 connections) — `server/services/environmental_container_loader.py`
- **Load a container definition from room JSON.          Args:             room_json** (1 connections) — `server/services/environmental_container_loader.py`
- **Migrate a container from room JSON to PostgreSQL.          Checks if container a** (1 connections) — `server/services/environmental_container_loader.py`
- **Load all environmental containers for a room from PostgreSQL.          Args:** (1 connections) — `server/services/environmental_container_loader.py`
- **Unit tests for EnvironmentalContainerLoader (room JSON -> container models).** (1 connections) — `server/tests/unit/services/test_environmental_container_loader.py`

## Relationships

- [player event handlers](player_event_handlers.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [add used user](add_used_user.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/services/environmental_container_loader.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 82 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*