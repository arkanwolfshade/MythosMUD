# Container System Architecture

> 28 nodes

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
- **Retrieve an item instance by ID.** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Check if an item instance exists in the database.** (1 connections) — `server/persistence/item_instance_persistence.py`
- *... and 3 more nodes in this community*

## Relationships

- [Maps API Endpoints](Maps_API_Endpoints.md) (14 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (8 shared connections)
- [Persistence Item Instance](Persistence_Item_Instance.md) (8 shared connections)
- [Combat Command Models](Combat_Command_Models.md) (7 shared connections)
- [JSONB Column Parsing](JSONB_Column_Parsing.md) (6 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (3 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (3 shared connections)
- [Container Data Models](Container_Data_Models.md) (3 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Feature Implementation Phases](Feature_Implementation_Phases.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/infrastructure/test_async_persistence_delegates.py`
- `server/tests/unit/persistence/test_container_persistence_extended_row_helpers.py`

## Audit Trail

- EXTRACTED: 145 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*