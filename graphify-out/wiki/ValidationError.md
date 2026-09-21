# ValidationError

> 163 nodes

## Key Concepts

- **ValidationError** (320 connections) — `server/exceptions.py`
- **InventoryCommandFactory** (79 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (50 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
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
- *... and 138 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (40 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (19 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (16 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (15 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (14 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (14 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (12 shared connections)
- [test_player_service_mutations.py](test_player_service_mutations.py.md) (11 shared connections)
- [MythosMUDError](MythosMUDError.md) (10 shared connections)
- [.get_instance](get_instance.md) (10 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (10 shared connections)
- [DatabaseManager](DatabaseManager.md) (9 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/game/test_movement_service.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 374 (59%)
- INFERRED: 259 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*