# ValidationError

> 194 nodes

## Key Concepts

- **ValidationError** (337 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (48 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **command_helpers.py** (18 connections) — `server/utils/command_helpers.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **TestCreateErrorResponse** (8 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- **increment_exception()** (5 connections) — `server/monitoring/exception_metrics.py`
- **test_create_drop_command_invalid_index()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **test_create_inventory_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- *... and 169 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (61 shared connections)
- [test_command_factories_utility.py](test_command_factories_utility.py.md) (28 shared connections)
- [MythosMUDError](MythosMUDError.md) (26 shared connections)
- [DatabaseError](DatabaseError.md) (26 shared connections)
- [get_logger](get_logger.md) (24 shared connections)
- [test_command_communication.py](test_command_communication.py.md) (23 shared connections)
- [DatabaseManager](DatabaseManager.md) (22 shared connections)
- [test_command_factories_moderation.py](test_command_factories_moderation.py.md) (20 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (18 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (18 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (13 shared connections)
- [Stats](Stats.md) (12 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/game/test_movement_service.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_legacy_error_handlers.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`
- `server/utils/command_helpers.py`
- `server/utils/enhanced_error_logging.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 569 (66%)
- INFERRED: 287 (34%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*