# server exceptions rationale 179

> 146 nodes

## Key Concepts

- **ValidationError** (336 connections) — `server/exceptions.py`
- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (49 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_inventory_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_inventory_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_invalid_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_drop_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_empty_search_term()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_index_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_equip_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_quantity_negative()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_get_command_quantity_zero()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- *... and 121 more nodes in this community*

## Relationships

- [server tests unit utils test](server_tests_unit_utils_test.md) (79 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (47 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (23 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (23 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (18 shared connections)
- [server api character creation apply](server_api_character_creation_apply.md) (13 shared connections)
- [server database databasemanager reset instance](server_database_databasemanager_reset_instance.md) (9 shared connections)
- [computed field](computed_field.md) (8 shared connections)
- [server database config helpers get](server_database_config_helpers_get.md) (8 shared connections)
- [server container persistence container data](server_container_persistence_container_data.md) (7 shared connections)
- [server database helpers close db](server_database_helpers_close_db.md) (7 shared connections)
- [server models command inventory](server_models_command_inventory.md) (7 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/profession_service.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 348 (55%)
- INFERRED: 284 (45%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*