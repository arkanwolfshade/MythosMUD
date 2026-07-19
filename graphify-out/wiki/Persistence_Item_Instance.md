# Persistence Item Instance

> 20 nodes · cohesion 0.13

## Key Concepts

- **__init__.py** (31 connections) — `server/persistence/__init__.py`
- **ensure_item_instance_async()** (9 connections) — `server/persistence/item_instance_persistence_async.py`
- **ensure_item_instance()** (9 connections) — `server/persistence/item_instance_persistence.py`
- **create_item_instance_async()** (8 connections) — `server/persistence/item_instance_persistence_async.py`
- **create_item_instance()** (6 connections) — `server/persistence/item_instance_persistence.py`
- **container_create_params.py** (5 connections) — `server/persistence/container_create_params.py`
- **get_item_instance()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (4 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (4 connections) — `server/persistence/item_instance_persistence.py`
- **AsyncSession** (3 connections) — `server/persistence/item_instance_persistence_async.py`
- **Ensure an item instance exists in the database, creating it if necessary.      T** (2 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (2 connections) — `server/persistence/item_instance_persistence_async.py`
- **Shared parameters for container creation (sync DB and async repository paths).** (1 connections) — `server/persistence/container_create_params.py`
- **# NOTE: PersistenceLayer and get_persistence removed - all code now uses AsyncPe** (1 connections) — `server/persistence/__init__.py`
- **# NOTE: Removed PersistenceLayer, get_persistence, and reset_persistence from __** (1 connections) — `server/persistence/__init__.py`
- **Create or update an item instance in the database (upsert).      Args:         s** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Retrieve an item instance by ID.      Args:         conn: Database connection** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Check if an item instance exists in the database.      Args:         conn: Datab** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Create a new item instance in the database.      Args:         conn: Database co** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Persistence package for MythosMUD.  This package contains persistence utilities** (1 connections) — `server/persistence/__init__.py`

## Relationships

- [[NPC Admin API]] (16 shared connections)
- [[Container Persistence Layer]] (8 shared connections)
- [[Container Data Models]] (5 shared connections)
- [[Persistence Item Repositories]] (4 shared connections)
- [[Container Repository CRUD]] (3 shared connections)
- [[Container Persistence Queries]] (3 shared connections)
- [[Room Occupancy Class]] (3 shared connections)
- [[Persistence Container Extended]] (2 shared connections)
- [[Health Cold Resistance]] (1 shared connections)

## Source Files

- `server/persistence/__init__.py`
- `server/persistence/container_create_params.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/item_instance_persistence_async.py`

## Audit Trail

- EXTRACTED: 95 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
