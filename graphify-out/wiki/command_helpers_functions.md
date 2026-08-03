# command helpers functions

> 80 nodes

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
- *... and 55 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (11 shared connections)
- [commands position system](commands_position_system.md) (8 shared connections)
- [aggro threat services](aggro_threat_services.md) (7 shared connections)
- [combat services persistence](combat_services_persistence.md) (5 shared connections)
- [combat npc services](combat_npc_services.md) (4 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [rescue service services](rescue_service_services.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [world models rationale](world_models_rationale.md) (3 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (3 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (2 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)

## Source Files

- `server/commands/rescue_commands.py`
- `server/services/rescue_service.py`
- `server/tests/unit/commands/test_rescue_commands.py`
- `server/tests/unit/services/test_rescue_service.py`

## Audit Trail

- EXTRACTED: 292 (95%)
- INFERRED: 14 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*