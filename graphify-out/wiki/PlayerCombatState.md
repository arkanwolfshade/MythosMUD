# PlayerCombatState

> 32 nodes · cohesion 0.10

## Key Concepts

- **position_commands.py** (20 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (12 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (10 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **SupportsPlayerPersistence** (8 connections) — `server/services/player_position_service.py`
- **_get_position_command_services()** (7 connections) — `server/commands/position_commands.py`
- **SupportsConnectionManager** (7 connections) — `server/services/player_position_service.py`
- **asyncio** (5 connections)
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **test_handle_ground_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_lie_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_sit_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_already_standing_still_sends_player_update()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **test_handle_stand_command()** (4 connections) — `server/tests/unit/commands/test_position_commands.py`
- **Protocol** (3 connections)
- **.get_player_by_name()** (2 connections) — `server/services/player_position_service.py`
- **.save_player()** (2 connections) — `server/services/player_position_service.py`
- **Command handlers for posture adjustments within MythosMUD. According to…** (1 connections) — `server/commands/position_commands.py`
- **Handle /stand command.** (1 connections) — `server/commands/position_commands.py`
- **Handle /lie command (accepts optional 'down').** (1 connections) — `server/commands/position_commands.py`
- **Shared entry point for posture-changing commands.** (1 connections) — `server/commands/position_commands.py`
- **Persistence surface required for posture updates.** (1 connections) — `server/services/player_position_service.py`
- **Live presence surface used to mirror posture into online player records.** (1 connections) — `server/services/player_position_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (15 shared connections)
- [LoggingConfig](LoggingConfig.md) (6 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (5 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (3 shared connections)
- [RoomDataCache](RoomDataCache.md) (3 shared connections)
- [test_connection_establishment.py](test_connection_establishment.py.md) (3 shared connections)
- [Room](Room.md) (2 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*