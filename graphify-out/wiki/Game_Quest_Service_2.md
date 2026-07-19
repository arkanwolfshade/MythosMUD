# Game Quest Service

> 15 nodes · cohesion 0.14

## Key Concepts

- **_make_definition_row()** (17 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_no_instance()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_abandon_success()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_resolve_name_to_quest_id_found()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_active()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_already_completed()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_by_trigger_starts_matching_quest()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **test_start_quest_requires_any_satisfied()** (3 connections) — `server/tests/unit/game/test_quest_service.py`
- **start_quest returns error when player already has active instance.** (2 connections) — `server/tests/unit/game/test_quest_service.py`
- **start_quest succeeds when requires_any has at least one completed.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **start_quest_by_trigger returns result from start_quest when offer and trigger ma** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **abandon updates instance to abandoned and returns success.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **abandon returns error when player has no instance.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **Build a mock definition row with definition JSONB.** (1 connections) — `server/tests/unit/game/test_quest_service.py`
- **resolve_name_to_quest_id returns quest_id when definition exists.** (1 connections) — `server/tests/unit/game/test_quest_service.py`

## Relationships

- [[Game Quest Service]] (16 shared connections)

## Source Files

- `server/tests/unit/game/test_quest_service.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
