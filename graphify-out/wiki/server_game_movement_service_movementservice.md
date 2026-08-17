# server game movement service movementservice

> 52 nodes

## Key Concepts

- **MovementService** (45 connections) — `server/game/movement_service.py`
- **UUID** (18 connections)
- **._execute_move_locked()** (14 connections) — `server/game/movement_service.py`
- **._handle_movement_error()** (7 connections) — `server/game/movement_service.py`
- **.move_player()** (7 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **.add_player_to_room()** (6 connections) — `server/game/movement_service.py`
- **._get_rooms_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **._execute_room_transfer()** (5 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **.remove_player_from_room()** (5 connections) — `server/game/movement_service.py`
- **._resolve_posture_player()** (5 connections) — `server/game/movement_service.py`
- **._validate_add_player_ids()** (5 connections) — `server/game/movement_service.py`
- **._validate_move_params()** (5 connections) — `server/game/movement_service.py`
- **._validate_remove_player_params()** (5 connections) — `server/game/movement_service.py`
- **.get_player_room()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._log_successful_move_timing()** (4 connections) — `server/game/movement_service.py`
- **._mark_room_explored()** (4 connections) — `server/game/movement_service.py`
- **._persist_added_player_room()** (4 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **.get_room_players()** (3 connections) — `server/game/movement_service.py`
- **.validate_player_location()** (3 connections) — `server/game/movement_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (13 shared connections)
- [server game movement helpers](server_game_movement_helpers.md) (5 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (4 shared connections)
- [followtargetvalue](followtargetvalue.md) (3 shared connections)
- [server commands go command](server_commands_go_command.md) (2 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (2 shared connections)
- [server exceptions rationale 179](server_exceptions_rationale_179.md) (2 shared connections)
- [server api monitoring](server_api_monitoring.md) (2 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (1 shared connections)
- [server npc idle movement idlemovementhandler](server_npc_idle_movement_idlemovementhandler.md) (1 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`

## Audit Trail

- EXTRACTED: 120 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*