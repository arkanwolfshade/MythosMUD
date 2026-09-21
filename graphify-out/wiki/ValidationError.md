# ValidationError

> 279 nodes

## Key Concepts

- **ValidationError** (320 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (106 connections) — `server/utils/enhanced_error_logging.py`
- **InventoryCommandFactory** (79 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (50 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_command_factories_inventory_helpers.py** (22 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **SchemaValidator** (21 connections) — `schemas/validator.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **validate_room_data()** (17 connections) — `server/world_loader.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **player_state_service.py** (13 connections) — `server/game/player_state_service.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_exploration.py** (11 connections) — `server/utils/command_factories_exploration.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **create_validator()** (10 connections) — `schemas/validator.py`
- **test_world_loader.py** (10 connections) — `server/tests/unit/test_world_loader.py`
- *... and 254 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (50 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (33 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (27 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (26 shared connections)
- [BaseCommand](BaseCommand.md) (25 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (22 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (22 shared connections)
- [DatabaseManager](DatabaseManager.md) (21 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (15 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (13 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (13 shared connections)

## Source Files

- `schemas/validator.py`
- `server/exceptions.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/game/profession_service.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/command_factories_utility.py`
- `server/utils/enhanced_error_logging.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 742 (74%)
- INFERRED: 263 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*