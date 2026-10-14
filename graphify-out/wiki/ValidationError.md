# ValidationError

> 213 nodes

## Key Concepts

- **ValidationError** (325 connections) — `server/exceptions.py`
- **InventoryCommandFactory** (98 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (70 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_get_command()** (20 connections) — `server/utils/command_factories_inventory.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (17 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **MythosValidationError** (10 connections)
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **.create_use_command()** (7 connections) — `server/utils/command_factories_inventory.py`
- **test_create_get_command_separator_needs_both_sides()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_put_command_separator_needs_both_sides()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_create_use_command_rejects_missing_or_zero_selector()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_deposit_and_withdraw_share_item_and_quantity_parsing()** (6 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **_pop_trailing_quantity()** (6 connections) — `server/utils/command_factories_inventory.py`
- **_split_item_container()** (6 connections) — `server/utils/command_factories_inventory.py`
- **parametrize** (6 connections)
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_inventory_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_pickup_command_invalid_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- *... and 188 more nodes in this community*

## Relationships

- [log_and_raise_enhanced](log_and_raise_enhanced.md) (52 shared connections)
- [get_logger](get_logger.md) (45 shared connections)
- [command_parser.py](command_parser.py.md) (23 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (19 shared connections)
- [BaseCommand](BaseCommand.md) (17 shared connections)
- [PlayerService](PlayerService.md) (14 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (14 shared connections)
- [test_player_respawn_api.py](test_player_respawn_api.py.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [DatabaseManager](DatabaseManager.md) (10 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (10 shared connections)
- [npc_database.py](npc_database.py.md) (9 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/profession_service.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 474 (62%)
- INFERRED: 288 (38%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*