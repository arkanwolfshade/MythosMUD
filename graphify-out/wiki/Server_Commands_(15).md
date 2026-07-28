# Server Commands (15)

> 86 nodes

## Key Concepts

- **test_rest_command.py** (38 connections) — `server/tests/unit/commands/test_rest_command.py`
- **rest_command.py** (26 connections) — `server/commands/rest_command.py`
- **handle_rest_command()** (22 connections) — `server/commands/rest_command.py`
- **cancel_rest_countdown()** (17 connections) — `server/commands/rest_command.py`
- **is_player_resting()** (17 connections) — `server/commands/rest_command.py`
- **_start_rest_countdown()** (12 connections) — `server/commands/rest_command.py`
- **Any** (11 connections)
- **_execute_rest_flow()** (11 connections) — `server/commands/rest_command.py`
- **_check_player_in_combat()** (9 connections) — `server/commands/rest_command.py`
- **UUID** (9 connections)
- **_check_rest_location()** (9 connections) — `server/commands/rest_command.py`
- **apply_target_rest_and_grace_checks()** (9 connections) — `server/services/combat_service_start.py`
- **.check_and_interrupt_rest()** (8 connections) — `server/commands/combat_handler.py`
- **_disconnect_player_intentionally()** (8 connections) — `server/commands/rest_command.py`
- **_begin_seated_rest_countdown()** (8 connections) — `server/commands/rest_command.py`
- **_resolve_rest_command_setup()** (6 connections) — `server/commands/rest_command.py`
- **_get_services_from_app()** (4 connections) — `server/commands/rest_command.py`
- **test_handle_rest_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_already_resting()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_in_combat()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_rest_location_instant()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **test_handle_rest_command_starts_countdown()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- *... and 61 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (16 shared connections)
- [Server Realtime (20)](Server_Realtime_%2820%29.md) (9 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (7 shared connections)
- [Server Commands (19)](Server_Commands_%2819%29.md) (5 shared connections)
- [Server Commands (63)](Server_Commands_%2863%29.md) (3 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (2 shared connections)
- [Server Services (98)](Server_Services_%2898%29.md) (2 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (2 shared connections)
- [Server Commands (72)](Server_Commands_%2872%29.md) (2 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (1 shared connections)
- [Server Commands (82)](Server_Commands_%2882%29.md) (1 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/commands/rest_command.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 342 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*