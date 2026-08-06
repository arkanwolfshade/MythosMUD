# npc service services

> 116 nodes

## Key Concepts

- **admin_teleport_commands.py** (39 connections) — `server/commands/admin_teleport_commands.py`
- **test_teleport_helpers.py** (31 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **teleport_helpers.py** (24 connections) — `server/commands/teleport_helpers.py`
- **goto_helpers.py** (21 connections) — `server/commands/goto_helpers.py`
- **test_admin_commands_helpers.py** (20 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- **notify_player_of_teleport()** (18 connections) — `server/commands/admin_teleport_utils.py`
- **test_admin_teleport_utils.py** (18 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **broadcast_teleport_effects()** (17 connections) — `server/commands/admin_teleport_utils.py`
- **get_online_player_by_display_name()** (16 connections) — `server/commands/admin_teleport_utils.py`
- **create_teleport_effect_message()** (16 connections) — `server/commands/admin_teleport_utils.py`
- **admin_teleport_utils.py** (14 connections) — `server/commands/admin_teleport_utils.py`
- **execute_confirm_teleport()** (11 connections) — `server/commands/teleport_helpers.py`
- **update_player_room_location()** (10 connections) — `server/commands/teleport_helpers.py`
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
- **Any** (3 connections)
- **test_create_teleport_effect_message_teleport_departure()** (3 connections) — `server/tests/unit/commands/test_admin_commands_helpers.py`
- *... and 91 more nodes in this community*

## Relationships

- [npc rewards combat](npc_rewards_combat.md) (22 shared connections)
- [realtime game state](realtime_game_state.md) (15 shared connections)
- [admin structured logging](admin_structured_logging.md) (9 shared connections)
- [Error Conversion](Error_Conversion.md) (8 shared connections)
- [commands admin mute](commands_admin_mute.md) (4 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (4 shared connections)
- [combat services messaging](combat_services_messaging.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (1 shared connections)
- [realtime real time](realtime_real_time.md) (1 shared connections)

## Source Files

- `server/commands/admin_teleport_commands.py`
- `server/commands/admin_teleport_utils.py`
- `server/commands/goto_helpers.py`
- `server/commands/teleport_helpers.py`
- `server/tests/unit/commands/test_admin_commands_helpers.py`
- `server/tests/unit/commands/test_admin_teleport_utils.py`
- `server/tests/unit/commands/test_teleport_helpers.py`

## Audit Trail

- EXTRACTED: 503 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*