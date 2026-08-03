# skill service game

> 22 nodes

## Key Concepts

- **test_skill_service.py** (36 connections) — `server/tests/unit/game/test_skill_service.py`
- **catalog_with_own_language_and_mythos()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_use_log_repo()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_catalog_returns_list()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_owner_returns_list()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_player_skills_non_owner_returns_none()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_get_skills_used_this_level_returns_repo_result()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_run_improvement_rolls_no_skills_used_no_updates()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_success_records_use_and_returns_true()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_roll_skill_check_failure_does_not_record()** (2 connections) — `server/tests/unit/game/test_skill_service.py`
- **Unit tests for SkillService (get_skills_catalog, set_player_skills, get_player_s** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for cove** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillUseLogRepository for use logging and improvement (plan 10.4).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_catalog returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for owned player returns list of skill dicts.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_player_skills for another user's player returns None.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **get_skills_used_this_level returns distinct skill_ids from repo.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **run_improvement_rolls when no skills used at previous level does not update.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll <= skill value, record_use is called and returns True.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When roll > skill value, record_use is not called and returns False.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [health monitor realtime](health_monitor_realtime.md) (6 shared connections)
- [realtime monitoring performance](realtime_monitoring_performance.md) (6 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [game room service](game_room_service.md) (2 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (1 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [persistence heal player()](persistence_heal_player%28%29.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)
- [npc threading rationale](npc_threading_rationale.md) (1 shared connections)
- [models invite rationale](models_invite_rationale.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*