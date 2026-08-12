# Command Service Tests

> 64 nodes

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
- *... and 39 more nodes in this community*

## Relationships

- [Quest Service Core](Quest_Service_Core.md) (3 shared connections)
- [Async Audit Cursor](Async_Audit_Cursor.md) (1 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (1 shared connections)
- [Player GUID Formatter](Player_GUID_Formatter.md) (1 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (1 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)
- [Chat Rate Limiter](Chat_Rate_Limiter.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 168 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*