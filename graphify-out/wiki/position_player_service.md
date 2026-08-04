# position player service

> 122 nodes

## Key Concepts

- **PlayerPositionService** (47 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **position_commands.py** (19 connections) — `server/commands/position_commands.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **_handle_position_change()** (11 connections) — `server/commands/position_commands.py`
- **test_position_commands.py** (11 connections) — `server/tests/unit/commands/test_position_commands.py`
- **_format_room_posture_message()** (10 connections) — `server/commands/position_commands.py`
- **handle_stand_command()** (9 connections) — `server/commands/position_commands.py`
- **handle_lie_command()** (9 connections) — `server/commands/position_commands.py`
- **test_position_commands_helpers.py** (9 connections) — `server/tests/unit/commands/test_position_commands_helpers.py`
- **handle_sit_command()** (8 connections) — `server/commands/position_commands.py`
- **Player** (8 connections)
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **SupportsPlayerPersistence** (6 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (6 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (6 connections) — `server/services/player_position_service.py`
- **.save_player()** (5 connections) — `server/services/player_position_service.py`
- **SupportsConnectionManager** (5 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (5 connections) — `server/services/player_position_service.py`
- **Any** (4 connections)
- **.get_player_by_name()** (4 connections) — `server/services/player_position_service.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- *... and 97 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (10 shared connections)
- [commands party examples](commands_party_examples.md) (6 shared connections)
- [Database Config](Database_Config.md) (5 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (4 shared connections)
- [commands admin mute](commands_admin_mute.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [command helpers functions](command_helpers_functions.md) (3 shared connections)
- [rest grace period](rest_grace_period.md) (2 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)

## Source Files

- `server/commands/position_commands.py`
- `server/services/player_position_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_position_commands_helpers.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 415 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*