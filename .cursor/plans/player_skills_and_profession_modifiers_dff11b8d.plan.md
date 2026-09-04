---
name: Player skills and profession modifiers
overview: "Implement plan 10.3 (P1–P5): player_skills table and migration, Profession stat_modifiers/skill_modifiers columns and seed, PlayerSkill model and relationship, SkillService (get catalog, set_player_skills, get_player_skills with ownership), and unit tests."
todos: []
isProject: false
---

# Player skills and profession modifiers (plan 10.3)

Implement the next section of the character creation revamp: player_skills table, profession modifier columns, SkillService, and ownership-checked get_player_skills.

---

## 1. P1: player_skills table and migration

- **Migration:** Add [db/migrations/025_add_player_skills_table.sql](db/migrations/025_add_player_skills_table.sql).
  - Table `player_skills`: `player_id UUID NOT NULL REFERENCES players(player_id) ON DELETE CASCADE`, `skill_id BIGINT NOT NULL REFERENCES skills(id) ON DELETE CASCADE`, `value INTEGER NOT NULL` with `CHECK (value >= 0 AND value <= 100)`.
  - Primary key `(player_id, skill_id)`; indexes on `player_id` and `skill_id` for lookups.
- **Model:** Add [server/models/player_skill.py](server/models/player_skill.py) with `PlayerSkill` (player_id, skill_id, value), FKs to Player and Skill. No need to add relationship from Player to player_skills in this step if we do it in P2.

---

## 2. P2: Profession stat_modifiers and skill_modifiers; Player relationship

- **Profession schema:** Add two new columns to `professions` via migration [db/migrations/026_add_profession_modifiers.sql](db/migrations/026_add_profession_modifiers.sql): `stat_modifiers TEXT NOT NULL DEFAULT '[]'`, `skill_modifiers TEXT NOT NULL DEFAULT '[]'`. Both store JSON arrays (plan 4.4/4.3 shape).
- **Profession model:** In [server/models/profession.py](server/models/profession.py) add `stat_modifiers` and `skill_modifiers` (Text, default `'[]'`); add getters/setters like `get_stat_modifiers()` / `set_stat_modifiers(list[dict])` and same for skill_modifiers (structure: `[{"stat": "intelligence", "value": 5}]` and `[{"skill_key": "library_use", "value": 5}]` or by skill_id).
- **Seed:** Add a data migration or seed file that updates existing profession rows with the educated-guess modifiers from plan 4.4 and 4.3 (by profession name). Option: extend [data/db/01_professions.sql](data/db/01_professions.sql) with `UPDATE professions SET stat_modifiers = '...', skill_modifiers = '...' WHERE name = '...'` for each profession, or a separate [data/db/05_profession_modifiers.sql](data/db/05_profession_modifiers.sql) run after 01 and 024/04_skills. Prefer 05_profession_modifiers.sql so 01 stays insert-only.
- **Player model:** In [server/models/player.py](server/models/player.py) add a relationship to `PlayerSkill` (e.g. `player_skills: Mapped[list["PlayerSkill"]] = relationship(...)` with back_populates). Ensure [server/models/player_skill.py](server/models/player_skill.py) (or the model defining PlayerSkill) has the FK and optional relationship to Skill for joins.

---

## 3. P3: SkillService — get_skills_catalog and set_player_skills

- **Service:** Add [server/game/skill_service.py](server/game/skill_service.py).
  - **get_skills_catalog():** Return list of skill dicts (id, key, name, base_value, allow_at_creation, category, etc.) by delegating to SkillRepository.get_all_skills() and mapping to dicts (or reuse schema SkillData).
  - **set_player_skills(player_id, occupation_slots, personal_interest, profession_id, stats_for_edu):**
    - **occupation_slots:** list of `{skill_id, value}`; plan requires exactly one 70, two 60, three 50, three 40. Validate and reject otherwise.
    - **personal_interest:** list of four `{skill_id}`; each gets catalog base + 20.
    - Load profession by profession_id; load full skills catalog; resolve skill_modifiers (by skill_key or skill_id).
    - Build final skill map: (1) For each skill in catalog with base_value, start with base_value; (2) apply profession skill_modifiers (by skill key/id); (3) overlay occupation_slots and personal (base+20) where allocated; (4) Own Language: if not in any slot, set to stats_for_edu (education stat); if allocated, use slot value + modifier. Clamp all values 0–99.
    - Persist: delete existing player_skills for player_id, then insert new rows (player_id, skill_id, value). Use a new PlayerSkillRepository or direct async session in SkillService; prefer a thin repository for player_skills (insert_many, delete_by_player, get_by_player).
- **PlayerSkillRepository:** Add [server/persistence/repositories/player_skill_repository.py](server/persistence/repositories/player_skill_repository.py): `delete_for_player(player_id)`, `insert_many(player_id, list of (skill_id, value))`, `get_by_player_id(player_id)` returning list of (skill_id, value) or list of PlayerSkill. Used by SkillService.

---

## 4. P4: get_player_skills with ownership check

- **SkillService.get_player_skills(player_id, user_id):** Load player by player_id; if player.user_id != user_id, return None or raise/allow caller to map to 403. Else load all player_skills for player_id (join skills for name/key); return list of {skill_id, key, name, value} (or similar).
- **API:** Add GET `/v1/players/{player_id}/skills` (or under existing players router): auth required; get current user id; call SkillService.get_player_skills(player_id, user_id); if not owner return 403; else return skill list. Schema: response list of {skill_id, skill_key, skill_name, value}.

---

## 5. P5: Seed profession stat_modifiers and skill_modifiers

- **Data:** Create [data/db/05_profession_modifiers.sql](data/db/05_profession_modifiers.sql) with UPDATE statements per plan 4.4 (stat_modifiers) and 4.3 (skill_modifiers) by profession name. Use the educated guesses: e.g. Professor: education +5, intelligence +5, charisma -2; skill_modifiers e.g. Professor: +5 Library Use, +5 Other Language (use skill keys from 04_skills). Ensure at least one profession has non-empty arrays so tests can assert.
- **Load order:** Add 05_profession_modifiers.sql to seed loader scripts (after 01_professions and 04_skills) so professions and skills exist before applying modifiers.

---

## 6. Tests and wiring

- **Unit tests:**
  - SkillService: get_skills_catalog returns list; set_player_skills with valid occupation (one 70, two 60, three 50, three 40) and four personal_interest creates player_skills rows; catalog-base skills get base + modifier; Own Language not allocated = EDU; Cthulhu Mythos in occupation/personal rejected.
  - get_player_skills: returns skills for owned player; returns 403 or empty for other user's player (test via service or API).
- **Dependencies:** Register SkillService in container or provide via Depends (get_skill_service) if the API is to use it; reuse SkillRepositoryDep and add PlayerSkillRepository + SkillService where needed. GET /v1/skills already uses SkillRepository; GET /v1/players/{player_id}/skills will need SkillService (or repository + ownership in API). Prefer SkillService for set_player_skills and get_player_skills so business rules stay in one place.

---

## 7. Implementation order

1. Migration 025 (player_skills table) and 026 (profession stat_modifiers, skill_modifiers columns).
2. Models: PlayerSkill, Profession new columns, Player relationship to player_skills.
3. PlayerSkillRepository (delete_for_player, insert_many, get_by_player_id).
4. SkillService (get_skills_catalog, set_player_skills, get_player_skills with ownership).
5. Seed 05_profession_modifiers.sql and add to loaders.
6. GET /v1/players/{player_id}/skills endpoint and response schema.
7. Unit tests for SkillService and GET player skills (ownership).

---

## 8. Files to add or modify (summary)


| Action | Path                                                                                  |
| ------ | ------------------------------------------------------------------------------------- |
| Add    | db/migrations/025_add_player_skills_table.sql                                         |
| Add    | db/migrations/026_add_profession_modifiers.sql                                        |
| Add    | data/db/05_profession_modifiers.sql                                                   |
| Add    | server/models/player_skill.py                                                         |
| Add    | server/persistence/repositories/player_skill_repository.py                            |
| Add    | server/game/skill_service.py                                                          |
| Add    | server/tests/unit/game/test_skill_service.py (and/or API test for GET player skills)  |
| Modify | server/models/profession.py (stat_modifiers, skill_modifiers)                         |
| Modify | server/models/player.py (relationship to player_skills)                               |
| Modify | server/api/players.py or new server/api/player_skills.py (GET player skills endpoint) |
| Modify | server/schemas/players/ (response for player skills list)                             |
| Modify | scripts/load_seed_via_asyncpg.py etc. (add 05_profession_modifiers.sql)               |


Plan doc [docs/character_creation_revamp_coc_skills_plan.md](docs/character_creation_revamp_coc_skills_plan.md) section 6.1 and 10.3 status should be updated when P1–P5 are done.
