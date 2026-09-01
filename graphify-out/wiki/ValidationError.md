# ValidationError

> 243 nodes

## Key Concepts

- **ValidationError** (314 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **test_command_factories_inventory.py** (49 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **test_command_factories_inventory_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **player_respawn_wrapper.py** (16 connections) — `server/game/player_respawn_wrapper.py`
- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **.create_drop_command()** (9 connections) — `server/utils/command_factories_inventory.py`
- **.create_channel_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_local_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_whisper_command()** (8 connections) — `server/utils/command_factories_communication.py`
- **.create_reply_command()** (7 connections) — `server/utils/command_factories_communication.py`
- **.create_emote_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_me_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_say_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_system_command()** (6 connections) — `server/utils/command_factories_communication.py`
- **.create_inventory_command()** (6 connections) — `server/utils/command_factories_inventory.py`
- *... and 218 more nodes in this community*

## Relationships

- [CommandFactory](CommandFactory.md) (123 shared connections)
- [get_logger](get_logger.md) (48 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (28 shared connections)
- [DatabaseManager](DatabaseManager.md) (20 shared connections)
- [api/player_respawn.py](api-player_respawn.py.md) (13 shared connections)
- [MythosMUDError](MythosMUDError.md) (12 shared connections)
- [test_player_service_mutations.py](test_player_service_mutations.py.md) (11 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (9 shared connections)
- [PlayerStateService](PlayerStateService.md) (9 shared connections)
- [Stats](Stats.md) (8 shared connections)
- [test_error_logging.py](test_error_logging.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)

## Source Files

- `server/exceptions.py`
- `server/game/player_respawn_wrapper.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories_communication.py`
- `server/utils/command_factories_inventory.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 601 (68%)
- INFERRED: 284 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*