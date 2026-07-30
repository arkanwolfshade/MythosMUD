# test player service

> 16 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **catalog_with_own_language_and_mythos()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_record_successful_skill_use_calls_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_previous_level_under_1_no_op()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_unknown_skill_returns_false()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills, get_player_s** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for cove** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_catalog returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **record_successful_skill_use delegates to repo.record_use with correct args.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls with new_level 1 does nothing (previous level 0).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **roll_skill_check when player has no value for skill_id returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > skill value, record_use is not called and returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [test websocket room updates build](test_websocket_room_updates_build.md) (6 shared connections)
- [Linting Complexity Alignment](Linting_Complexity_Alignment.md) (6 shared connections)
- [real time](real_time.md) (3 shared connections)
- [test quest definition repository](test_quest_definition_repository.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [test_get_current_lucidity_not_found](test_get_current_lucidity_not_found.md) (1 shared connections)
- [test_get_player_data_for_delirium_respawn_success](test_get_player_data_for_delirium_respawn_success.md) (1 shared connections)
- [test_get_player_data_for_delirium_respawn_no_connection_manager](test_get_player_data_for_delirium_respawn_no_connection_manager.md) (1 shared connections)
- [AppState](AppState.md) (1 shared connections)
- [test_get_player_data_for_delirium_respawn_error_handling](test_get_player_data_for_delirium_respawn_error_handling.md) (1 shared connections)
- [test_get_player_data_for_delirium_respawn_player_not_found](test_get_player_data_for_delirium_respawn_player_not_found.md) (1 shared connections)
- [test_handle_player_delirium_respawned_success](test_handle_player_delirium_respawned_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*