# quest service game

> 86 nodes

## Key Concepts

- **QuestService** (84 connections) — `server/game/quest/quest_service.py`
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
- *... and 61 more nodes in this community*

## Relationships

- [quest game service](quest_game_service.md) (26 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (4 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [collect quest service](collect_quest_service.md) (4 shared connections)
- [health realtime monitoring](health_realtime_monitoring.md) (3 shared connections)
- [combat death services](combat_death_services.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (1 shared connections)
- [time service rationale](time_service_rationale.md) (1 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [container main rationale](container_main_rationale.md) (1 shared connections)

## Source Files

- `server/game/quest/quest_service.py`
- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 477 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*