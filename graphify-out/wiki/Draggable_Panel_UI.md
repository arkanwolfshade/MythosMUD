# Draggable Panel UI

> 32 nodes

## Key Concepts

- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **ContainerCreateParams** (20 connections) — `server/persistence/container_create_params.py`
- **item_instance_persistence.py** (20 connections) — `server/persistence/item_instance_persistence.py`
- **ensure_item_instance()** (10 connections) — `server/persistence/item_instance_persistence.py`
- **create_item_instance()** (9 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (7 connections)
- **container_create_params.py** (6 connections) — `server/persistence/container_create_params.py`
- **_handle_item_instance_db_error()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **_execute_item_instance_upsert()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **test_create_container_uuid_string_conversion()** (6 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_create_container_success()** (5 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **_item_instance_row_values()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **get_item_instance()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **test_create_container_with_params()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_with_kwargs()** (4 connections) — `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- **test_create_container_wraps_psycopg2_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`
- **Persistence package for MythosMUD.  This package contains persistence utilities** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: PersistenceLayer and get_persistence removed - all code now uses AsyncPe** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from __** (1 connections) — `server/persistence/__init__.py`
- **Shared parameters for container creation (sync DB and async repository paths).** (1 connections) — `server/persistence/container_create_params.py`
- **Optional fields for creating a container row (beyond source_type).** (1 connections) — `server/persistence/container_create_params.py`
- **Exception** (1 connections)
- **Item instance persistence operations.  As documented in the restricted archives,** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Create a new item instance in the database.** (1 connections) — `server/persistence/item_instance_persistence.py`
- *... and 7 more nodes in this community*

## Relationships

- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (26 shared connections)
- [Maps API Endpoints](Maps_API_Endpoints.md) (16 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (12 shared connections)
- [Integration DB Fixtures](Integration_DB_Fixtures.md) (3 shared connections)
- [Client Security Utilities](Client_Security_Utilities.md) (3 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (3 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [E2E Suite Overview](E2E_Suite_Overview.md) (2 shared connections)
- [Coverage Disconnect Grace](Coverage_Disconnect_Grace.md) (1 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 157 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*