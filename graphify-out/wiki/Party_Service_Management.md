# Party Service Management

> 58 nodes

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **test_handle_rest_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_instant()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_starts_countdown()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_true()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_false()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_player_in_combat_no_service()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_true()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_false()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_room()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_check_rest_location_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_disconnect_player_intentionally()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_start_rest_countdown_creates_task()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_start_rest_countdown_timer_expires()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_cancels_task()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_cancel_rest_countdown_not_resting()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_is_player_resting_true()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_is_player_resting_false()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_is_player_resting_no_manager_attribute()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 33 more nodes in this community*

## Relationships

- [Player State Factories](Player_State_Factories.md) (26 shared connections)
- [Realtime WebSocket Auth](Realtime_WebSocket_Auth.md) (5 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (2 shared connections)
- [Architecture Api Openapi](Architecture_Api_Openapi.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (1 shared connections)

## Source Files

- `server/commands/rest_command.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 165 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*