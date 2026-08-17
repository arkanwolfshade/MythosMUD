# ValidationError

> 252 nodes

## Key Concepts

- **ValidationError** (337 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (49 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **CommunicationCommandFactory** (39 connections) — `server/utils/command_factories_communication.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_inventory_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **command_factories_communication.py** (11 connections) — `server/utils/command_factories_communication.py`
- **command_factories_exploration.py** (11 connections) — `server/utils/command_factories_exploration.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **_create_engine_or_raise()** (8 connections) — `server/database.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- *... and 227 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (58 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (31 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (26 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (22 shared connections)
- [BaseCommand](BaseCommand.md) (21 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (20 shared connections)
- [DatabaseManager](DatabaseManager.md) (19 shared connections)
- [get_logger](get_logger.md) (18 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (15 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (13 shared connections)
- [player_creation_service.py](player_creation_service.py.md) (11 shared connections)
- [PlayerService](PlayerService.md) (11 shared connections)

## Source Files

- `server/database.py`
- `server/exceptions.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
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

## Audit Trail

- EXTRACTED: 627 (67%)
- INFERRED: 312 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*