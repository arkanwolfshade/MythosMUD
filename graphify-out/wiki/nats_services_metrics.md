# nats services metrics

> 59 nodes

## Key Concepts

- **test_container_persistence_async_helpers.py** (40 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **container_persistence_async.py** (34 connections) — `server/persistence/container_persistence_async.py`
- **get_container_async()** (19 connections) — `server/persistence/container_persistence_async.py`
- **create_container_async()** (15 connections) — `server/persistence/container_persistence_async.py`
- **_finalize_container_creation()** (13 connections) — `server/persistence/container_persistence_async.py`
- **update_container_async()** (13 connections) — `server/persistence/container_persistence_async.py`
- **_populate_container_items_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **fetch_container_items_async()** (12 connections) — `server/persistence/container_persistence_async.py`
- **Any** (11 connections)
- **delete_container_async()** (11 connections) — `server/persistence/container_persistence_async.py`
- **_call_create_container_procedure()** (10 connections) — `server/persistence/container_persistence_async.py`
- **validate_lock_state()** (8 connections) — `server/persistence/container_helpers.py`
- **_validate_container_create_params()** (8 connections) — `server/persistence/container_persistence_async.py`
- **AsyncSession** (8 connections)
- **_build_item_dict()** (8 connections) — `server/persistence/container_persistence_async.py`
- **_parse_jsonb()** (7 connections) — `server/persistence/container_persistence_async.py`
- **_row_to_mapping()** (7 connections) — `server/persistence/container_persistence_async.py`
- **_prepare_container_create_params()** (6 connections) — `server/persistence/container_persistence_async.py`
- **_parse_item_metadata()** (6 connections) — `server/persistence/container_persistence_async.py`
- **UUID** (5 connections)
- **ContainerData** (4 connections)
- **test_validate_container_create_params_rejects_invalid()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **test_populate_container_items_skips_invalid_and_failed()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **test_call_create_container_procedure_no_row()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- **test_delete_container_async_db_error()** (3 connections) — `server/tests/unit/persistence/test_container_persistence_async_helpers.py`
- *... and 34 more nodes in this community*

## Relationships

- [persistence container item](persistence_container_item.md) (28 shared connections)
- [Database Config](Database_Config.md) (16 shared connections)
- [command inventory models](command_inventory_models.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [command commands service](command_commands_service.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)

## Source Files

- `server/persistence/container_helpers.py`
- `server/persistence/container_persistence_async.py`
- `server/tests/unit/persistence/test_container_persistence_async_helpers.py`

## Audit Trail

- EXTRACTED: 309 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*