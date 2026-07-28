# Server Persistence (16)

> 17 nodes

## Key Concepts

- **__init__.py** (32 connections) — `server/persistence/__init__.py`
- **item_instance_persistence.py** (14 connections) — `server/persistence/item_instance_persistence.py`
- **ensure_item_instance()** (9 connections) — `server/persistence/item_instance_persistence.py`
- **create_item_instance()** (8 connections) — `server/persistence/item_instance_persistence.py`
- **container_create_params.py** (6 connections) — `server/persistence/container_create_params.py`
- **Any** (4 connections)
- **get_item_instance()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **Persistence package for MythosMUD.  This package contains persistence utilities** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: PersistenceLayer and get_persistence removed - all code now uses AsyncPe** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from __** (1 connections) — `server/persistence/__init__.py`
- **Shared parameters for container creation (sync DB and async repository paths).** (1 connections) — `server/persistence/container_create_params.py`
- **Item instance persistence operations.  As documented in the restricted archives,** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Create a new item instance in the database.      Args:         conn: Database co** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Retrieve an item instance by ID.      Args:         conn: Database connection** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Check if an item instance exists in the database.      Args:         conn: Datab** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Ensure an item instance exists in the database, creating it if necessary.      T** (1 connections) — `server/persistence/item_instance_persistence.py`

## Relationships

- [Server Persistence (5)](Server_Persistence_%285%29.md) (10 shared connections)
- [Server Persistence (2)](Server_Persistence_%282%29.md) (7 shared connections)
- [Server Admin](Server_Admin.md) (7 shared connections)
- [Server Persistence](Server_Persistence.md) (3 shared connections)
- [Server Persistence (7)](Server_Persistence_%287%29.md) (2 shared connections)
- [Server Utils](Server_Utils.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Api](Server_Api.md) (2 shared connections)
- [Server Persistence (15)](Server_Persistence_%2815%29.md) (2 shared connections)
- [Server Services](Server_Services.md) (1 shared connections)
- [Server Persistence (10)](Server_Persistence_%2810%29.md) (1 shared connections)
- [Server Persistence (18)](Server_Persistence_%2818%29.md) (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/item_instance_persistence.py`

## Audit Trail

- EXTRACTED: 88 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*