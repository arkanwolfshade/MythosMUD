# server commands admin teleport utils

> 86 nodes

## Key Concepts

- **test_teleport_helpers.py** (32 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **teleport_helpers.py** (24 connections) — `server/commands/teleport_helpers.py`
- **test_admin_teleport_utils.py** (19 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **broadcast_teleport_effects()** (17 connections) — `server/commands/admin_teleport_utils.py`
- **notify_player_of_teleport()** (17 connections) — `server/commands/admin_teleport_utils.py`
- **get_online_player_by_display_name()** (15 connections) — `server/commands/admin_teleport_utils.py`
- **admin_teleport_utils.py** (14 connections) — `server/commands/admin_teleport_utils.py`
- **asyncio** (12 connections)
- **execute_confirm_teleport()** (11 connections) — `server/commands/teleport_helpers.py`
- **update_player_room_location()** (10 connections) — `server/commands/teleport_helpers.py`
- **asyncio** (10 connections)
- **broadcast_teleport_updates()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_target_player()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_teleport_direction()** (9 connections) — `server/commands/teleport_helpers.py`
- **resolve_teleport_services()** (9 connections) — `server/commands/teleport_helpers.py`
- **update_teleport_location()** (9 connections) — `server/commands/teleport_helpers.py`
- **Any** (9 connections)
- **resolve_target_player_for_teleport()** (8 connections) — `server/commands/teleport_helpers.py`
- **validate_confirm_teleport_context()** (8 connections) — `server/commands/teleport_helpers.py`
- **build_teleport_message()** (7 connections) — `server/commands/teleport_helpers.py`
- **log_teleport_success()** (7 connections) — `server/commands/teleport_helpers.py`
- **test_broadcast_teleport_effects_no_broadcast_method()** (4 connections) — `server/tests/unit/commands/test_admin_teleport_utils.py`
- **test_broadcast_teleport_updates()** (4 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_execute_confirm_teleport_success()** (4 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_target_player_already_here()** (4 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- *... and 61 more nodes in this community*

## Relationships

- [server commands admin teleport commands](server_commands_admin_teleport_commands.md) (34 shared connections)
- [server commands admin teleport utils](server_commands_admin_teleport_utils.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server structured logging admin actions](server_structured_logging_admin_actions.md) (4 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [server commands admin permission utils](server_commands_admin_permission_utils.md) (2 shared connections)
- [characterinfo](characterinfo.md) (2 shared connections)
- [object](object.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)

## Source Files

- `server/commands/admin_teleport_utils.py`
- `server/commands/teleport_helpers.py`
- `server/tests/unit/commands/test_admin_teleport_utils.py`
- `server/tests/unit/commands/test_teleport_helpers.py`

## Audit Trail

- EXTRACTED: 232 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*