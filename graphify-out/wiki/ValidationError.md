# ValidationError

> 396 nodes

## Key Concepts

- **ValidationError** (314 connections) — `server/exceptions.py`
- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **InventoryCommandFactory** (76 connections) — `server/utils/command_factories_inventory.py`
- **player_service.py** (49 connections) — `server/game/player_service.py`
- **test_command_factories_inventory.py** (49 connections) — `server/tests/unit/utils/test_command_factories_inventory.py`
- **CommunicationCommandFactory** (39 connections) — `server/utils/command_factories_communication.py`
- **enhanced_error_logging.py** (38 connections) — `server/utils/enhanced_error_logging.py`
- **test_command_factories_communication.py** (30 connections) — `server/tests/unit/utils/test_command_factories_communication.py`
- **create_error_context()** (29 connections) — `server/exceptions.py`
- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **test_enhanced_error_logging.py** (24 connections) — `server/tests/unit/utils/test_enhanced_error_logging.py`
- **test_command_factories_inventory_helpers.py** (23 connections) — `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- **command_factories.py** (20 connections) — `server/utils/command_factories.py`
- **.create_pickup_command()** (19 connections) — `server/utils/command_factories_inventory.py`
- **.create_equip_command()** (16 connections) — `server/utils/command_factories_inventory.py`
- **player_creation_service.py** (16 connections) — `server/game/player_creation_service.py`
- **player_respawn_wrapper.py** (16 connections) — `server/game/player_respawn_wrapper.py`
- **PlayerRespawnWrapper** (15 connections) — `server/game/player_respawn_wrapper.py`
- **command_factories_inventory.py** (15 connections) — `server/utils/command_factories_inventory.py`
- **.create_put_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **.create_unequip_command()** (14 connections) — `server/utils/command_factories_inventory.py`
- **create_enhanced_error_context()** (14 connections) — `server/utils/enhanced_error_logging.py`
- **test_player_respawn_wrapper.py** (14 connections) — `server/tests/unit/game/test_player_respawn_wrapper.py`
- **.create_get_command()** (13 connections) — `server/utils/command_factories_inventory.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- *... and 371 more nodes in this community*

## Relationships

- [DatabaseError](DatabaseError.md) (62 shared connections)
- [get_logger](get_logger.md) (37 shared connections)
- [get_username_from_user](get_username_from_user.md) (33 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (22 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (22 shared connections)
- [BaseCommand](BaseCommand.md) (22 shared connections)
- [PlayerService](PlayerService.md) (14 shared connections)
- [test_player_service_mutations.py](test_player_service_mutations.py.md) (12 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (11 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (11 shared connections)
- [Stats](Stats.md) (10 shared connections)
- [models/player.py](models-player.py.md) (10 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/exceptions.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/monitoring/exception_metrics.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/game/test_player_respawn_wrapper.py`
- `server/tests/unit/utils/test_command_factories_communication.py`
- `server/tests/unit/utils/test_command_factories_inventory.py`
- `server/tests/unit/utils/test_command_factories_inventory_helpers.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_communication.py`

## Audit Trail

- EXTRACTED: 1010 (77%)
- INFERRED: 304 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*