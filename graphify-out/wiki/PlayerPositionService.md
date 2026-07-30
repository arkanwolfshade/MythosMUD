# PlayerPositionService

> 184 nodes

## Key Concepts

- **PlayerPositionService** (47 connections) — `server/services/player_position_service.py`
- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (19 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **player_position_service.py** (17 connections) — `server/services/player_position_service.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **Player** (8 connections)
- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **SupportsPlayerPersistence** (6 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (6 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (6 connections) — `server/services/player_position_service.py`
- *... and 159 more nodes in this community*

## Relationships

- [Any](Any.md) (11 shared connections)
- [command admin](command_admin.md) (9 shared connections)
- [real time](real_time.md) (7 shared connections)
- [Validate that player is in](Validate_that_player_is_in.md) (5 shared connections)
- [test magic commands](test_magic_commands.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [Player Position Service](Player_Position_Service.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (4 shared connections)
- [.cleanup dead connections()](cleanup_dead_connections%28%29.md) (3 shared connections)
- [benchmark model memory usage()](benchmark_model_memory_usage%28%29.md) (3 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_rest_command.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 651 (99%)
- INFERRED: 9 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*