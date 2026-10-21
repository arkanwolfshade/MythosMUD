# test_follow_commands.py

> 112 nodes · cohesion 0.03

## Key Concepts

- **go_command.py** (34 connections) — `server/commands/go_command.py`
- **rest_command.py** (34 connections) — `server/commands/rest_command.py`
- **test_go_command.py** (33 connections) — `server/tests/unit/commands/test_go_command.py`
- **cancel_rest_countdown()** (25 connections) — `server/commands/rest_command.py`
- **handle_go_command()** (22 connections) — `server/commands/go_command.py`
- **is_player_resting()** (19 connections) — `server/commands/rest_command.py`
- **asyncio** (16 connections)
- **_setup_go_command()** (13 connections) — `server/commands/go_command.py`
- **check_player_in_combat()** (13 connections) — `server/commands/rest_command.py`
- **Any** (13 connections)
- **_start_rest_countdown()** (13 connections) — `server/commands/rest_command.py`
- **Any** (12 connections)
- **_execute_movement()** (11 connections) — `server/commands/go_command.py`
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **UUID** (11 connections)
- **_validate_exit()** (10 connections) — `server/commands/go_command.py`
- **_validate_player_posture()** (10 connections) — `server/commands/go_command.py`
- **_begin_seated_rest_countdown()** (10 connections) — `server/commands/rest_command.py`
- **.check_and_interrupt_rest()** (9 connections) — `server/commands/combat_handler.py`
- **_cancel_rest_if_moving()** (8 connections) — `server/commands/go_command.py`
- **_delayed_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_stand_after_cancelled_rest()** (8 connections) — `server/commands/rest_command.py`
- **_disconnect_player_intentionally()** (7 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (7 connections) — `server/commands/rest_command.py`
- **rest_countdown_seconds()** (7 connections) — `server/commands/rest_countdown_task.py`
- *... and 87 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (28 shared connections)
- [command_parser.py](command_parser.py.md) (18 shared connections)
- [Room](Room.md) (6 shared connections)
- [.publish_with_pool](publish_with_pool.md) (5 shared connections)
- [CORSConfig](CORSConfig.md) (5 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (4 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (4 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (4 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (4 shared connections)
- [Persistence Layer Refactoring - COMPLETE ✅](Persistence_Layer_Refactoring_-_COMPLETE_✅.md) (3 shared connections)
- [RoomDataCache](RoomDataCache.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/go_command.py`
- `server/commands/rest_command.py`
- `server/commands/rest_countdown_task.py`
- `server/tests/unit/commands/test_go_command.py`

## Audit Trail

- EXTRACTED: 323 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*