# command factories create

> 132 nodes

## Key Concepts

- **test_rescue_service.py** (32 connections) — `server/tests/unit/services/test_rescue_service.py`
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
- *... and 107 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (24 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (7 shared connections)
- [realtime real time](realtime_real_time.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (3 shared connections)
- [position player service](position_player_service.md) (3 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/services/rescue_service.py`
- `server/tests/unit/commands/test_rescue_commands.py`
- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 400 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*