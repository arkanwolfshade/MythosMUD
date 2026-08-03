# collect quest service

> 26 nodes

## Key Concepts

- **test_quest_service_collect.py** (15 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **_make_collect_quest_row()** (9 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **_quest_service_with_persistence()** (8 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **_make_inventory_player()** (7 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_start_quest_collect_n_seeds_progress_from_holdings()** (5 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_sync_collect_progress_updates_on_inventory_change()** (5 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_sync_collect_progress_nested_container()** (5 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_collect_n_auto_complete_keeps_items()** (5 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_turn_in_collect_n_consumes_items()** (5 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_start_quest_rejects_auto_complete_with_turn_in()** (4 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **test_start_quest_rejects_turn_in_without_entities()** (4 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **mock_def_repo()** (2 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **mock_instance_repo()** (2 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Unit tests for QuestService collect_n sync, auto-complete, and turn-in consumpti** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Mock QuestDefinitionRepository.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Mock QuestInstanceRepository.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Definition with collect_n goal.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Mock player with inventory getters/setters.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **QuestService wired with async_persistence returning player.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **start_quest syncs collect_n progress from current inventory.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **sync_collect_progress reflects increased and decreased holdings.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Nested inner_container items count toward collect_n progress.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Auto-complete collect_n quest does not consume inventory.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Turn-in consumes required collect_n items before completion.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- **Validation rejects auto_complete true combined with turn_in_entities.** (1 connections) — `server/tests/unit/game/test_quest_service_collect.py`
- *... and 1 more nodes in this community*

## Relationships

- [quest game service](quest_game_service.md) (5 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service_collect.py`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*