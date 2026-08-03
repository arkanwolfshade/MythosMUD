# panels monitoringPanelTestFixtures Monit

> 21 nodes

## Key Concepts

- **test_item_instance_persistence.py** (16 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **item_instance_persistence.py** (15 connections) — `server/persistence/item_instance_persistence.py`
- **create_item_instance()** (12 connections) — `server/persistence/item_instance_persistence.py`
- **ensure_item_instance()** (11 connections) — `server/persistence/item_instance_persistence.py`
- **get_item_instance()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **item_instance_exists()** (7 connections) — `server/persistence/item_instance_persistence.py`
- **Any** (4 connections)
- **test_create_item_instance_missing_id()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_create_item_instance_db_error()** (3 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_item_instance_exists_true()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_item_instance_exists_false()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_get_item_instance_found()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_get_item_instance_not_found()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_ensure_item_instance_calls_create()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **test_create_item_instance_success()** (2 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`
- **Item instance persistence operations.  As documented in the restricted archives,** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Create a new item instance in the database.      Args:         conn: Database co** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Retrieve an item instance by ID.      Args:         conn: Database connection** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Check if an item instance exists in the database.      Args:         conn: Datab** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Ensure an item instance exists in the database, creating it if necessary.      T** (1 connections) — `server/persistence/item_instance_persistence.py`
- **Unit tests for item_instance_persistence helpers.** (1 connections) — `server/tests/unit/persistence/test_item_instance_persistence.py`

## Relationships

- [persistence container item](persistence_container_item.md) (10 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/persistence/item_instance_persistence.py`
- `server/tests/unit/persistence/test_item_instance_persistence.py`

## Audit Trail

- EXTRACTED: 92 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*