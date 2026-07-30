# Linting Complexity Alignment

> 12 nodes

## Key Concepts

- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_valid_creates_rows()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_own_language_not_allocated_equals_edu()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_values_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_occupation_skill_ids_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_count_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Four personal interest (skill_ids only); distinct and no overlap with occupation** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **set_player_skills with valid occupation and personal calls delete then insert_ma** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When Own Language is not in occupation or personal, its value is stats_for_edu.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots not length 9 raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots with wrong value set (e.g. two 70s) raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots with duplicate skill_id raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [test player service](test_player_service.md) (6 shared connections)
- [test websocket room updates build](test_websocket_room_updates_build.md) (5 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*