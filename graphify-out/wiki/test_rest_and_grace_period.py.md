# test_rest_and_grace_period.py

> 96 nodes · cohesion 0.05

## Key Concepts

- **test_quest_service.py** (49 connections) — `server/tests/unit/game/test_quest_service.py`
- **_MockDefRepo** (31 connections) — `server/tests/unit/game/test_quest_service.py`
- **asyncio** (27 connections)
- **_MockInstanceRepo** (26 connections) — `server/tests/unit/game/test_quest_service.py`
- **_make_definition_row()** (19 connections) — `server/tests/unit/game/test_quest_service.py`
- **_message()** (17 connections) — `server/tests/unit/game/test_quest_service.py`
- **_InstanceStub** (16 connections) — `server/tests/unit/game/test_quest_service.py`
- **quest_service()** (11 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_turn_in_inventory_full_blocks_item_reward()** (10 connections) — `server/tests/unit/game/test_quest_service.py`
- **_complete_tutorial_with_rewards()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **_RespawnPersistence** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_not_active()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_success()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_active()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_completed()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_reaccept_after_abandon()** (9 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_no_instance()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_get_quest_log_returns_entries()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_complete_activity_auto_completes_when_goals_met()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_complete_activity_updates_progress()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_kill_suppresses_intermediate_progress_notify()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_kill_updates_progress()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_prereq_not_met()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_requires_any_satisfied()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_success()** (8 connections) — `server/tests/unit/game/test_quest_service.py`
- *... and 71 more nodes in this community*

## Relationships

- [item_catalog_repository.py](item_catalog_repository.py.md) (30 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (4 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (2 shared connections)
- [properties](properties.md) (1 shared connections)
- [PassiveMobNPC](PassiveMobNPC.md) (1 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 248 (89%)
- INFERRED: 32 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*