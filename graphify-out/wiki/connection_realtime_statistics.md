# connection realtime statistics

> 61 nodes

## Key Concepts

- **look_command.py** (38 connections) — `server/commands/look_command.py`
- **test_look_command.py** (22 connections) — `server/tests/unit/commands/test_look_command.py`
- **look_helpers.py** (16 connections) — `server/commands/look_helpers.py`
- **Any** (12 connections)
- **handle_look_command()** (12 connections) — `server/commands/look_command.py`
- **_is_direction()** (11 connections) — `server/commands/look_helpers.py`
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
- *... and 36 more nodes in this community*

## Relationships

- [look command commands](look_command_commands.md) (13 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (7 shared connections)
- [player realtime presence](player_realtime_presence.md) (6 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (5 shared connections)
- [look helpers commands](look_helpers_commands.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (3 shared connections)
- [player service game](player_service_game.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [player cache rationale](player_cache_rationale.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)

## Source Files

- `server/commands/look_command.py`
- `server/commands/look_helpers.py`
- `server/tests/unit/commands/test_look_command.py`

## Audit Trail

- EXTRACTED: 262 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*