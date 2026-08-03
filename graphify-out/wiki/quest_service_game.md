# quest service game

> 84 nodes

## Key Concepts

- **test_quest_service.py** (42 connections) — `server/tests/unit/game/test_quest_service.py`
- **_MockDefRepo** (31 connections) — `server/tests/unit/game/test_quest_service.py`
- **_MockInstanceRepo** (26 connections) — `server/tests/unit/game/test_quest_service.py`
- **_make_definition_row()** (18 connections) — `server/tests/unit/game/test_quest_service.py`
- **_message()** (17 connections) — `server/tests/unit/game/test_quest_service.py`
- **_InstanceStub** (16 connections) — `server/tests/unit/game/test_quest_service.py`
- **quest_service()** (10 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_inventory_full_blocks_item_reward()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_active()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_completed()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_reaccept_after_abandon()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_success()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_not_active()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_success()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_prereq_not_met()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_requires_any_satisfied()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_complete_activity_updates_progress()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_complete_activity_auto_completes_when_goals_met()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_kill_updates_progress()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_kill_suppresses_intermediate_progress_notify()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_no_instance()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_get_quest_log_returns_entries()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **_make_turn_in_definition_row()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_success()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_no_active_instance_returns_error()** (7 connections) — `server/tests/unit/game/test_quest_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [quest game service](quest_game_service.md) (37 shared connections)
- [inventory commands command](inventory_commands_command.md) (1 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)
- [realtime player connection](realtime_player_connection.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 398 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*