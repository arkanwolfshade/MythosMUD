# Game Quest Service

> 18 nodes · cohesion 0.11

## Key Concepts

- **test_quest_service.py** (33 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_def_repo()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **mock_instance_repo()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_unknown_quest()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_get_quest_log_empty()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_get_quest_log_excludes_completed_when_requested()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_record_kill_updates_progress()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_resolve_name_to_quest_id_not_found()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_not_found()** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **Unit tests for QuestService.  Covers: resolve_name_to_quest_id, start_quest, aba** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **start_quest returns error when quest id not found.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **Mock QuestDefinitionRepository.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **record_kill updates instance progress for matching kill_n goal.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **Mock QuestInstanceRepository.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **abandon returns error when quest name not found.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **get_quest_log returns empty list when no active or completed.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **get_quest_log with include_completed=False does not call list_completed_by_playe** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **resolve_name_to_quest_id returns None when definition missing.** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [[Game Quest Service]] (23 shared connections)
- [[Quest Service Core]] (1 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 58 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
