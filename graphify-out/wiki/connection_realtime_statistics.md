# connection realtime statistics

> 59 nodes

## Key Concepts

- **look_command.py** (38 connections) — `server/commands/look_command.py`
- **test_look_command.py** (22 connections) — `server/tests/unit/commands/test_look_command.py`
- **Any** (12 connections)
- **handle_look_command()** (12 connections) — `server/commands/look_command.py`
- **exploration_commands.py** (11 connections) — `server/commands/exploration_commands.py`
- **_route_look_command()** (10 connections) — `server/commands/look_command.py`
- **_validate_look_prerequisites()** (9 connections) — `server/commands/look_command.py`
- **_get_room_drops()** (9 connections) — `server/commands/look_command.py`
- **_setup_look_command()** (9 connections) — `server/commands/look_command.py`
- **_handle_implicit_target_lookup()** (9 connections) — `server/commands/look_command.py`
- **_get_app_and_persistence()** (7 connections) — `server/commands/look_command.py`
- **_try_direction_look()** (7 connections) — `server/commands/look_command.py`
- **_try_explicit_player_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_item_look()** (5 connections) — `server/commands/look_command.py`
- **_try_explicit_container_look()** (5 connections) — `server/commands/look_command.py`
- **_try_implicit_target_lookup()** (5 connections) — `server/commands/look_command.py`
- **test_get_app_and_persistence_from_container()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_get_app_and_persistence_state_fallback()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_validate_look_prerequisites_no_persistence()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_validate_look_prerequisites_room_missing()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_get_room_drops_from_room_manager()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_get_room_drops_no_connection_manager()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_setup_look_command_success()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_handle_look_command_setup_failure()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- **test_handle_look_command_routes_to_room_look()** (3 connections) — `server/tests/unit/commands/test_look_command.py`
- *... and 34 more nodes in this community*

## Relationships

- [look command commands](look_command_commands.md) (8 shared connections)
- [startup npc services](startup_npc_services.md) (5 shared connections)
- [npc realtime occupant](npc_realtime_occupant.md) (5 shared connections)
- [commands whisper command](commands_whisper_command.md) (4 shared connections)
- [look helpers commands](look_helpers_commands.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [npc look commands](npc_look_commands.md) (3 shared connections)
- [room renderer functions](room_renderer_functions.md) (3 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [combat services turn](combat_services_turn.md) (1 shared connections)

## Source Files

- `server/commands/exploration_commands.py`
- `server/commands/look_command.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 245 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*