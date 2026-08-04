# npc service services

> 80 nodes

## Key Concepts

- **admin_teleport_commands.py** (39 connections) — `server/commands/admin_teleport_commands.py`
- **test_teleport_helpers.py** (31 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **teleport_helpers.py** (24 connections) — `server/commands/teleport_helpers.py`
- **validate_admin_permission()** (20 connections) — `server/commands/admin_permission_utils.py`
- **execute_confirm_teleport()** (11 connections) — `server/commands/teleport_helpers.py`
- **test_admin_permission_utils.py** (11 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **update_player_room_location()** (10 connections) — `server/commands/teleport_helpers.py`
- **admin_permission_utils.py** (9 connections) — `server/commands/admin_permission_utils.py`
- **resolve_teleport_services()** (9 connections) — `server/commands/teleport_helpers.py`
- **Any** (9 connections)
- **resolve_teleport_direction()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_target_player()** (9 connections) — `server/commands/teleport_helpers.py`
- **update_teleport_location()** (9 connections) — `server/commands/teleport_helpers.py`
- **broadcast_teleport_updates()** (9 connections) — `server/commands/teleport_helpers.py`
- **validate_confirm_teleport_context()** (8 connections) — `server/commands/teleport_helpers.py`
- **resolve_target_player_for_teleport()** (8 connections) — `server/commands/teleport_helpers.py`
- **build_teleport_message()** (7 connections) — `server/commands/teleport_helpers.py`
- **log_teleport_success()** (7 connections) — `server/commands/teleport_helpers.py`
- **_BrokenAdminPlayer** (4 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_attribute_error()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_validate_admin_permission_logs_secondary_failure()** (3 connections) — `server/tests/unit/commands/test_admin_permission_utils.py`
- **test_resolve_teleport_services_no_app()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_services_no_player_service()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_services_success()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_direction_no_direction()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- *... and 55 more nodes in this community*

## Relationships

- [realtime game state](realtime_game_state.md) (16 shared connections)
- [player respawn event](player_respawn_event.md) (15 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (10 shared connections)
- [admin structured logging](admin_structured_logging.md) (9 shared connections)
- [NPC Combat](NPC_Combat.md) (6 shared connections)
- [inventory commands command](inventory_commands_command.md) (3 shared connections)
- [commands whisper command](commands_whisper_command.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/teleport_helpers.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`
- `server/tests/unit/commands/test_teleport_helpers.py`

## Audit Trail

- EXTRACTED: 348 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*