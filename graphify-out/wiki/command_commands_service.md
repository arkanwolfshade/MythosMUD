# command commands service

> 36 nodes

## Key Concepts

- **ItemRepository** (15 connections) — `server/persistence/repositories/item_repository.py`
- **create_item_instance_async()** (14 connections) — `server/persistence/item_instance_persistence_async.py`
- **item_instance_persistence_async.py** (13 connections) — `server/persistence/item_instance_persistence_async.py`
- **test_item_instance_persistence_async.py** (13 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **item_repository.py** (12 connections) — `server/persistence/repositories/item_repository.py`
- **ensure_item_instance_async()** (11 connections) — `server/persistence/item_instance_persistence_async.py`
- **item_instance_exists_async()** (7 connections) — `server/persistence/item_instance_persistence_async.py`
- **test_item_repository.py** (7 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **.create_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.ensure_item_instance()** (5 connections) — `server/persistence/repositories/item_repository.py`
- **.__init__()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **.item_instance_exists()** (4 connections) — `server/persistence/repositories/item_repository.py`
- **AsyncSession** (3 connections)
- **Any** (3 connections)
- **test_create_item_instance_async_missing_id()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **test_create_item_instance_async_db_error()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **Any** (2 connections)
- **repository()** (2 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **test_create_item_instance_delegates()** (2 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **test_ensure_item_instance_delegates()** (2 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **test_item_instance_exists_delegates()** (2 connections) — `server/tests/unit/persistence/repositories/test_item_repository.py`
- **test_create_item_instance_async_success()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **test_item_instance_exists_async()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **test_ensure_item_instance_async_delegates()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence_async.py`
- **Async item instance persistence operations.  Provides async implementations usin** (1 connections) — `server/persistence/item_instance_persistence_async.py`
- *... and 11 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [NPC Combat](NPC_Combat.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (2 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [persistence container item](persistence_container_item.md) (1 shared connections)

## Source Files

- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/item_repository.py`
- `server/tests/unit/persistence/repositories/test_item_repository.py`
- `server/tests/unit/persistence/test_item_instance_persistence_async.py`

## Audit Trail

- EXTRACTED: 146 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*