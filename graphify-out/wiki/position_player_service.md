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

- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [realtime real time](realtime_real_time.md) (8 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (6 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [party service game](party_service_game.md) (3 shared connections)
- [command factories create](command_factories_create.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [rest grace period](rest_grace_period.md) (2 shared connections)
- [room realtime occupant](room_realtime_occupant.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

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