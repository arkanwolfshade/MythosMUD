# command commands talk

> 24 nodes

## Key Concepts

- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_valid_creates_rows()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_own_language_not_allocated_equals_edu()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_occupation_rejected()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_values_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_occupation_skill_ids_raises()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_personal_rejected()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_wrong_occupation_count_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_personal_interest_not_four_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_personal_skill_ids_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_overlap_occupation_and_personal_raises()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Valid 9 slots: one 70, two 60, three 50, three 40; 9 distinct skill_ids (no over** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Four personal interest (skill_ids only); distinct and no overlap with occupation** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **set_player_skills with valid occupation and personal calls delete then insert_ma** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **When Own Language is not in occupation or personal, its value is stats_for_edu.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Occupation slot with Cthulhu Mythos (allow_at_creation=False) raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Personal interest with Cthulhu Mythos raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots not length 9 raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots with wrong value set (e.g. two 70s) raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **personal_interest must have exactly 4 entries.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **occupation_slots with duplicate skill_id raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **personal_interest with duplicate skill_id raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Occupation and personal interest sharing a skill_id raises ValueError.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (12 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 66 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*