# item_instance_persistence_async.py

> 21 nodes · cohesion 0.13

## Key Concepts

- **item_instance_persistence_async.py** (12 connections) — `server/persistence/item_instance_persistence_async.py`
- **item_repository.py** (11 connections) — `server/persistence/repositories/item_repository.py`
- **create_item_instance_async()** (10 connections) — `server/persistence/item_instance_persistence_async.py`
- **ensure_item_instance_async()** (9 connections) — `server/persistence/item_instance_persistence_async.py`
- **item_instance_exists_async()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **.create_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.ensure_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **.item_instance_exists()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **AsyncSession** (3 connections)
- **Any** (3 connections)
- **Any** (2 connections)
- **Async item instance persistence operations.  Provides async implementations usin** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Check if an item instance exists in the database via item_instance_exists proced** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Ensure an item instance exists in the database, creating it if necessary.      A** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Create or update an item instance in the database (upsert).      Args:         s** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Item repository for async persistence operations.  This module provides async it** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Check if an item instance exists (async).** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Initialize the item repository.          Args:             persistence_layer: De** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Create a new item instance (async).** (1 connections) — `server/persistence/repositories/item_repository.py`
- **Ensure an item instance exists (async).** (1 connections) — `server/persistence/repositories/item_repository.py`

## Relationships

- [DatabaseError](DatabaseError.md) (10 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [container_persistence_async.py](container_persistence_async.py.md) (2 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/item_repository.py`

## Audit Trail

- EXTRACTED: 80 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*