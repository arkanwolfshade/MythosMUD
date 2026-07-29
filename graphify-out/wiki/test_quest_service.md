# test quest service

> 63 nodes

## Key Concepts

- **test_quest_service.py** (34 connections) — `server/tests/unit/game/test_quest_service.py`
- **_make_definition_row()** (17 connections) — `server/tests/unit/game/test_quest_service.py`
- **quest_service()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **_make_turn_in_definition_row()** (6 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_inventory_full_blocks_item_reward()** (4 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_resolve_name_to_quest_id_found()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_success()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_active()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_completed()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_reaccept_after_abandon()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_prereq_not_met()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_requires_any_satisfied()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_by_trigger_starts_matching_quest()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_complete_activity_updates_progress()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_complete_activity_auto_completes_when_goals_met()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_success()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_no_instance()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_not_active()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_get_quest_log_returns_entries()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_auto_complete_returns_error()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_success()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_wrong_entity_returns_error()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_no_active_instance_returns_error()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_def_repo()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_instance_repo()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- *... and 38 more nodes in this community*

## Relationships

- [QuestCompleted](QuestCompleted.md) (3 shared connections)
- [collect inventory](collect_inventory.md) (1 shared connections)
- [DropResolved](DropResolved.md) (1 shared connections)
- [ExitStack](ExitStack.md) (1 shared connections)
- [quest events](quest_events.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 168 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*