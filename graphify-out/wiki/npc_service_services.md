# npc service services

> 87 nodes

## Key Concepts

- **admin_teleport_commands.py** (39 connections) — `server/commands/admin_teleport_commands.py`
- **test_teleport_helpers.py** (31 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **get_admin_actions_logger()** (27 connections) — `server/structured_logging/admin_actions_logger.py`
- **teleport_helpers.py** (24 connections) — `server/commands/teleport_helpers.py`
- **goto_helpers.py** (21 connections) — `server/commands/goto_helpers.py`
- **validate_admin_permission()** (20 connections) — `server/commands/admin_permission_utils.py`
- **admin_actions_logger.py** (16 connections) — `server/structured_logging/admin_actions_logger.py`
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
- *... and 62 more nodes in this community*

## Relationships

- [player respawn event](player_respawn_event.md) (22 shared connections)
- [realtime game state](realtime_game_state.md) (19 shared connections)
- [models npc rationale](models_npc_rationale.md) (13 shared connections)
- [monitoring dashboard rationale](monitoring_dashboard_rationale.md) (13 shared connections)
- [commands admin mute](commands_admin_mute.md) (8 shared connections)
- [commands inventory put](commands_inventory_put.md) (6 shared connections)
- [admin structured logging](admin_structured_logging.md) (5 shared connections)
- [container schemas containers](container_schemas_containers.md) (4 shared connections)
- [commands position system](commands_position_system.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/commands/admin_permission_utils.py`
- `server/commands/admin_teleport_commands.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/structured_logging/admin_actions_logger.py`
- `server/tests/unit/commands/test_admin_permission_utils.py`
- `server/tests/unit/commands/test_teleport_helpers.py`

## Audit Trail

- EXTRACTED: 416 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*