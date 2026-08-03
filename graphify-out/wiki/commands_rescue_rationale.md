# commands rescue rationale

> 78 nodes

## Key Concepts

- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (31 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **rescue_service.py** (16 connections) — `server/services/rescue_service.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **RescueService** (11 connections) — `server/services/rescue_service.py`
- **Any** (7 connections)
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **.rescue()** (7 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (5 connections)
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **Any** (4 connections)
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 53 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (21 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (13 shared connections)
- [lucidity event services](lucidity_event_services.md) (7 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [rescue service services](rescue_service_services.md) (4 shared connections)
- [command helpers functions](command_helpers_functions.md) (3 shared connections)
- [realtime game state](realtime_game_state.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/services/rescue_service.py`
- `server/tests/unit/commands/test_position_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 288 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*