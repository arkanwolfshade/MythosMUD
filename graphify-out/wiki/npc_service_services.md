# npc service services

> 65 nodes

## Key Concepts

- **admin_teleport_commands.py** (39 connections) — `server/commands/admin_teleport_commands.py`
- **test_teleport_helpers.py** (31 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **teleport_helpers.py** (24 connections) — `server/commands/teleport_helpers.py`
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
- **test_resolve_teleport_services_no_app()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_services_no_player_service()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_services_success()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_direction_no_direction()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_direction_invalid_exit()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_teleport_direction_valid_exit()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_target_player_not_online()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_resolve_target_player_already_here()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_update_teleport_location_failure()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- **test_update_teleport_location_success()** (3 connections) — `server/tests/unit/commands/test_teleport_helpers.py`
- *... and 40 more nodes in this community*

## Relationships

- [realtime game state](realtime_game_state.md) (15 shared connections)
- [npc rewards combat](npc_rewards_combat.md) (12 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (10 shared connections)
- [admin structured logging](admin_structured_logging.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)
- [character creation service](character_creation_service.md) (1 shared connections)

## Source Files

- `server/commands/admin_teleport_commands.py`
- `server/commands/teleport_helpers.py`
- `server/tests/unit/commands/test_teleport_helpers.py`

## Audit Trail

- EXTRACTED: 285 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*