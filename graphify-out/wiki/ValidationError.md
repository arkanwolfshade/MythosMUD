# ValidationError

> 166 nodes

## Key Concepts

- **ValidationError** (337 connections) — `server/exceptions.py`
- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (49 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_inventory_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **MythosValidationError** (10 connections)
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **test_process_validated_command_validation_error()** (5 connections) — `server/tests/unit/commands/test_command_service.py`
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
- *... and 141 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (19 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (19 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (17 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (16 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (16 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (15 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (13 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (13 shared connections)
- [test_player_service_mutations.py](test_player_service_mutations.py.md) (11 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (10 shared connections)
- [test_exceptions.py](test_exceptions.py.md) (9 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/profession_service.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_factories_inventory.py`

## Audit Trail

- EXTRACTED: 396 (59%)
- INFERRED: 272 (41%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*