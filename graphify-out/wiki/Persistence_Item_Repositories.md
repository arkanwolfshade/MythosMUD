# Persistence Item Repositories

> 13 nodes · cohesion 0.18

## Key Concepts

- **ItemRepository** (10 connections) — `server/persistence/repositories/item_repository.py`
- **item_instance_exists_async()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **.create_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.ensure_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **.item_instance_exists()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **Any** (3 connections) — `server/persistence/repositories/item_repository.py`
- **Check if an item instance exists in the database via item_instance_exists proced** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Check if an item instance exists (async).** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Repository for item instance persistence operations.      Uses async SQLAlchemy** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Initialize the item repository.          Args:             persistence_layer: De** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Create a new item instance (async).** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Ensure an item instance exists (async).** (1 connections) — `server/persistence/repositories/item_repository.py`

## Relationships

- [[NPC Admin API]] (10 shared connections)
- [[Persistence Item Instance]] (4 shared connections)

## Source Files

- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/item_repository.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
