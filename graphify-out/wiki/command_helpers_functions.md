# command helpers functions

> 60 nodes

## Key Concepts

- **rescue_commands.py** (31 connections) — `server/commands/rescue_commands.py`
- **handle_ground_command()** (31 connections) — `server/commands/rescue_commands.py`
- **test_rescue_commands.py** (23 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **handle_rescue_command()** (14 connections) — `server/commands/rescue_commands.py`
- **Any** (7 connections)
- **_apply_grounding_adjustment()** (7 connections) — `server/commands/rescue_commands.py`
- **_get_ground_services()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_context()** (5 connections) — `server/commands/rescue_commands.py`
- **_normalize_player_ids()** (5 connections) — `server/commands/rescue_commands.py`
- **UUID** (5 connections)
- **_send_grounding_failure_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_success_events()** (5 connections) — `server/commands/rescue_commands.py`
- **_validate_ground_target()** (4 connections) — `server/commands/rescue_commands.py`
- **_send_grounding_channeling_events()** (4 connections) — `server/commands/rescue_commands.py`
- **test_handle_ground_command_not_catatonic()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_success()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_target_player_key()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_apply_lucidity_error()** (4 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_target()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_target_player_key()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_app()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_rescue_command_no_state()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- **test_handle_ground_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_rescue_commands.py`
- *... and 35 more nodes in this community*

## Relationships

- [lucidity services helpers](lucidity_services_helpers.md) (11 shared connections)
- [aggro threat services](aggro_threat_services.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)
- [rescue service services](rescue_service_services.md) (3 shared connections)
- [position player service](position_player_service.md) (3 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/tests/unit/commands/test_rescue_commands.py`

## Audit Trail

- EXTRACTED: 225 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*