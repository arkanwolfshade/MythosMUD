# Persistence Item Instance

> 34 nodes

## Key Concepts

- **CreateItemInstanceInput** (23 connections) — `server/async_persistence_constants.py`
- **item_instance_persistence_async.py** (18 connections) — `server/persistence/item_instance_persistence_async.py`
- **item_repository.py** (14 connections) — `server/persistence/repositories/item_repository.py`
- **ItemRepository** (12 connections) — `server/persistence/repositories/item_repository.py`
- **EnsureItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **create_item_instance_async()** (11 connections) — `server/persistence/item_instance_persistence_async.py`
- **ensure_item_instance_async()** (10 connections) — `server/persistence/item_instance_persistence_async.py`
- **async_persistence_constants.py** (7 connections) — `server/async_persistence_constants.py`
- **datetime** (6 connections)
- **_metadata_from_options()** (6 connections) — `server/persistence/item_instance_persistence_async.py`
- **_item_instance_upsert_params()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **_run_item_instance_upsert()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **item_instance_exists_async()** (5 connections) — `server/persistence/item_instance_persistence_async.py`
- **.create_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.ensure_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **AsyncSession** (4 connections)
- **.__init__()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **.item_instance_exists()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **TypedDict** (2 connections)
- **Any** (2 connections)
- **Constants and shared types for async persistence layer.  Extracted to keep async** (1 connections) — `server/async_persistence_constants.py`
- **Optional fields for create_item_instance. owner_type, owner_id, etc. with defaul** (1 connections) — `server/async_persistence_constants.py`
- **Optional fields for ensure_item_instance.** (1 connections) — `server/async_persistence_constants.py`
- **Async item instance persistence operations.  Provides async implementations usin** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- **Create or update an item instance in the database (upsert).** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- *... and 9 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (15 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (9 shared connections)
- [Container System Architecture](Container_System_Architecture.md) (8 shared connections)
- [Conftest Migration Plan](Conftest_Migration_Plan.md) (5 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (2 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (2 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Player Save Preparer](Player_Save_Preparer.md) (2 shared connections)

## Source Files

- `server/async_persistence_constants.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/item_repository.py`

## Audit Trail

- EXTRACTED: 158 (91%)
- INFERRED: 15 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*