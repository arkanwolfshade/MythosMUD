# Character Creation Revamp and CoC 7th Ed Skills Plan

Align MythosMUD character creation with Call of Cthulhu 7th ed (Chaosium): roll stats first, then profession modifiers; CoC-style skill allocation; skills catalog, viewing, use tracking, and level-up improvement. Add level/level-up as part of this work.

---

## 1. Requirements Summary (from discovery)

- **Flow:** Roll stats first (no profession requirements). Then choose profession and apply stat modifiers (buffs/nerfs). Same stat names: strength, dexterity, constitution, size, intelligence, power, education, charisma, luck.
- **Profession stat modifiers:** Per-profession list of (stat, delta) in profession data (e.g. `stat_modifiers`). Stored and applied after roll.
- **Skills allocation (CoC-style):** Nine slots (8 occupation + Credit Rating): one at 70%, two at 60%, three at 50%, three at 40%. Player freely chooses which skills fill slots (guideline: fit profession). Four personal interest skills: base + 20% each. Per-skill base values in catalog (from CoC 7th ed sheet where possible).
- **Profession skill modifiers:** Fixed bonus/penalty per profession, list of (skill, delta), applied on top of allocation at creation. Support penalties. Provide sensible default occupation-to-skill mappings.
- **Skills visibility:** New ESC menu option (same pattern as Map: e.g. "Skills (New Tab)") and slash command `/skills` so the player can see their skills.
- **Skills list:** CoC 7th ed initially; Cthulhu Mythos in catalog but no allocation at creation.
- **Skill use tracking:** Record each successful use by character at current level.
- **Level-up improvement:** On level up, for each skill successfully used that level: CoC-style roll (d100 over current skill % to gain 1d10 or similar); roll under or equal = no gain.
- **Level system:** Add level and level-up; define source of level (e.g. XP vs. milestones) in this work.

---

## 2. Current State (brief)

- **Client:** [client/src/App.tsx](client/src/App.tsx) orchestrates creation: ProfessionSelectionScreen then StatsRollingScreen. StatsRollingScreen POSTs create-character with name, stats, profession_id and calls onStatsAccepted. No skills step; no level on character.
- **Server:** [server/api/character_creation.py](server/api/character_creation.py) (roll-stats, create-character); [server/game/character_creation_service.py](server/game/character_creation_service.py); [server/game/stats_generator.py](server/game/stats_generator.py) rolls with profession requirements. [server/models/player.py](server/models/player.py): Player has stats (JSONB), profession_id; **level and experience_points already exist** (verify migrations for existing DBs). [server/models/profession.py](server/models/profession.py): stat_requirements, mechanical_effects (JSON text); no stat_modifiers or skill_modifiers yet.
- **ESC menu:** [client/src/components/MainMenuModal.tsx](client/src/components/MainMenuModal.tsx) has Map (New Tab), Settings (placeholder), Logout. No Skills. MainMenuModal does **not** receive `playerId`; Map URL uses room params only. Commands go through client command submit and server command handling.

---

## 3. Target Creation Flow

```mermaid
sequenceDiagram
  participant U
  participant StatsScreen
  participant ProfScreen
  participant SkillScreen
  participant NameScreen
  participant API

  U->>StatsScreen: Roll stats (no profession check)
  StatsScreen->>API: POST roll-stats (no profession_id)
  API-->>StatsScreen: raw stats
  U->>StatsScreen: Accept stats
  StatsScreen->>ProfScreen: stats (no name yet)
  U->>ProfScreen: Choose profession
  ProfScreen->>ProfScreen: Apply stat modifiers (client or API)
  ProfScreen->>SkillScreen: stats (modified), profession
  U->>SkillScreen: Allocate 9 slots (70,60,60,50,50,50,40,40,40) + 4 personal (base+20)
  SkillScreen->>NameScreen: stats, profession, skills payload
  U->>NameScreen: Enter character name
  NameScreen->>API: POST create-character (name, stats, profession_id, skills)
  API->>API: Apply profession skill mods, persist player + skills
  API-->>NameScreen: 201
  NameScreen->>U: Character created; refresh list
```

- Roll is independent of profession. Profession selection happens after stats are accepted. Skill allocation is next; then a dedicated **name step** (new screen) where the player enters the character name and confirms; that step sends the final create payload (name, **rolled** stats, profession_id, skills). Server applies stat_modifiers when saving.

**Integration:** Reordering from current flow (profession → stats + name → create) requires new App state (`pendingStats`, skills payload, creation step). **Mitigation:** Centralize "creation step" (e.g. enum or step index) and derive which screen to show from that; unify the "has characters" and "no characters" branches into one flow. On "Create New Character", clear pending stats and skills so re-entry does not carry stale state.

---

## 4. Backend: Data and Services

### 4.1 Level

- Add `level` (integer, default 1) and `xp` (or similar) to Player. Add migration. **Level source: XP with a logarithmic curve.** Rationale: skill improvement is already harder at high skill % (CoC-style roll), and skills must be used during a level to qualify for improvement; a logarithmic curve keeps XP-to-next-level from exploding so upper-level players still gain levels and get improvement rolls, while the combination of "use it this level" and "roll over current %" keeps mastery of every skill difficult.
  **Integration:** [server/models/player.py](server/models/player.py) and [server/game/player_creation_service.py](server/game/player_creation_service.py) already set `level=1` and `experience_points=0` on create. Verify existing migrations include these columns; add migration only if DBs do not have them yet.
- **Logarithmic curve:** XP required for next level (or total XP to reach level N) grows logarithmically—each level requires more than the last but the increase flattens. **Deferred:** implement a placeholder (e.g. log-style with arbitrary constants, or a simple table) and document in code/ADR that the exact curve will be tuned later; no need to lock the formula in the plan now.
- **Level-up hook:** When a character levels up, run skill improvement for all skills that were successfully used during the previous level (see 4.5).

### 4.2 Skills catalog

- New table `skills`: id, key (e.g. `accounting`, `drive_auto`), name (display), description (optional), base_value (integer, 0–100), allow_at_creation (boolean; false for Cthulhu Mythos). Seed from CoC 7th ed Starter Set skill list and base values. **Own Language (Option A):** At creation, default Own Language = character's Education stat (after profession stat modifiers). If the player allocates Own Language in an occupation or personal-interest slot, that slot value overrides (e.g. 70% from occupation). If they do not allocate it, persist it as EDU. Catalog can store a sentinel or base for Own Language; creation logic applies the EDU rule.
- Optional: category (e.g. interpersonal, knowledge) for UI grouping.

### 4.3 Player skills and profession skill modifiers

- New table `player_skills`: player_id (FK, UUID), skill_id (FK), value (integer 0–100). PK (player_id, skill_id). Migration.
- Player model: relationship to player_skills (and optionally to skills via join).
- **Profession skill modifiers:** Add to profession data (new field or extend mechanical_effects). Structure: list of { skill_key or skill_id, value (delta) }. Apply after computing initial skills. Support negative values (penalties). **Non-allocated skills (Option A):** Create a player_skill row for any skill that (i) has a profession modifier for this profession, or (ii) has a **catalog base value** (e.g. CoC sheet minimum like Accounting 05%). **IMPORTANT:** If the CoC 7th ed sheet shows a minimum/base for a skill (e.g. Accounting 05%), that skill is added to the player's skills at creation at least at that base (+ profession modifier if any), even if the player did not allocate points to it. So every skill with a base_value in the catalog gets a row at creation; allocated skills get slot value + modifier; non-allocated skills with a base get base + modifier (if any).
- **Default mappings (educated guesses):** e.g. Investigator: +5 Library Use, +5 Spot Hidden; Doctor: +10 First Aid, +5 Medicine; Journalist: +5 Persuade or Fast Talk, +5 Art/Craft (Photography); Professor: +5 Library Use, +5 Other Language; Antiquarian: +5 Appraise, +5 History. Define a small set and document in seed/migration or config.

### 4.4 Profession stat modifiers

- Add `stat_modifiers` to profession (new column or key in mechanical_effects). Structure: list of { stat, value } with stat in current names (strength, dexterity, constitution, size, intelligence, power, education, charisma, luck). Example: `stat_modifiers: [ {"stat": "intelligence", "value": 5}, {"stat": "education", "value": -2} ]`. Apply to rolled stats when profession is chosen (server or client; server is authoritative so apply on create or in a "preview" endpoint).
  **Integration:** [server/models/profession.py](server/models/profession.py) has no stat_modifiers today. For create-character, profession must be loaded by profession_id; validate profession exists and is_available before applying modifiers. Prefer a dedicated column for stat_modifiers (and skill_modifiers) over stuffing mechanical_effects for clarity and querying.
- **Educated guesses (seed data):** Use the following as defaults; adjust per profession name in DB. Investigator: intelligence +5, education +3. Doctor of Medicine: intelligence +3, education +5, constitution -2. Journalist: education +3, charisma +3, intelligence +2. Professor: education +5, intelligence +5, charisma -2. Antiquarian: education +5, intelligence +3. Author: education +5, intelligence +3, charisma +2. Dilettante: charisma +5, education +3. Police Detective: intelligence +3, dexterity +2, constitution +2. Private Investigator: intelligence +5, education +2, dexterity +2. Occultist (if present): power +3, intelligence +3, education +2. Tweak values or add/remove professions when implementing seed or migration.

### 4.5 Skill use tracking and improvement

- **When a skill is "successfully used" (Option A):** There will be a dedicated skill-check path (e.g. a command or API that rolls d100 vs the skill % and returns success/failure). Call `record_successful_skill_use(player_id, skill_id, level)` only when that roll succeeds. Which commands or actions invoke skill checks is to be specified as those commands/triggers are added; the skill-check path is the single place that records successful use.
- New table `skill_use_log` (or equivalent): player_id, skill_id, character_level_at_use (integer), used_at (timestamp). Log only successful uses. Optionally: context (e.g. combat, investigation) for future use.
- **Level-up improvement:** When level increases: for each skill that has at least one row in skill_use_log for (player_id, skill_id, level = new_level - 1), run CoC-style improvement: roll d100; if roll > current skill value, add gain then cap at 99. **Cap:** max skill value is **99%**. **Gain:** if current skill is **90–98**, add **1 point** on success; if current skill is **below 90**, add **1d10** on success. Clamp result to 99. Then clear or mark logged uses for that level so we don't double-count (or query by level_at_use and leave log for history).
- Service: record_successful_skill_use(player_id, skill_id, level); get_skills_used_this_level(player_id, level); run_improvement_rolls(player_id, new_level).

### 4.6 Stat rolling and creation API changes

- **Roll stats:** Remove profession requirement from roll. [server/game/stats_generator.py](server/game/stats_generator.py): keep or add a "raw" roll (no profession validation). API roll-stats may accept optional profession_id only for preview (e.g. "what would my stats look like with this profession?"); creation flow uses unmodified roll first.
  **Integration:** When profession_id is omitted, the API already uses the legacy class-based path (raw roll). For stats-first creation, the client must **not** send profession_id on the initial roll ([client/src/hooks/useStatsRolling.ts](client/src/hooks/useStatsRolling.ts) sends professionId today—StatsRollingScreen must be called without professionId when it is the first step). Any "preview" response (rolled stats + stat_modifiers) must not change the create-character contract: creation always sends rolled stats; server applies modifiers on save. Document that create-character interprets stats as rolled only.
- **Create character:** Extend [server/schemas/players/player_requests.py](server/schemas/players/player_requests.py) CreateCharacterRequest: add skills. **Payload shape (Option A, verify):** Client sends occupation_slots as list of { skill_id, value } for all nine slots (e.g. Library Use 70, Spot Hidden 60, …). Server **verifies** that the nine values are exactly the allowed set (one 70, two 60, three 50, three 40), that skill_ids are in the catalog, and that Cthulhu Mythos is not included; reject if not. Client sends personal_interest as list of four { skill_id } (or skill_id + value); server computes base + 20 for each. Server then adds profession skill_modifiers on top of the verified/computed values. **All catalog-base skills:** For every skill in the catalog that has a base_value (CoC sheet minimum), ensure a player_skill row exists at creation: use allocated value + modifier if the player allocated it; otherwise use base_value + profession modifier (if any). No skill with a sheet minimum is omitted. **Own Language:** If Own Language was not allocated in any slot, set it to Education (after stat modifiers); if allocated, use the slot value. Persist player (with level 1), then persist player_skills.
  **Integration:** Server currently persists whatever stats the client sends ([server/api/character_creation.py](server/api/character_creation.py), [server/game/player_creation_service.py](server/game/player_creation_service.py)). Apply stat_modifiers in **one place** (API or PlayerCreationService); prefer the service layer so a single contract (rolled stats + profession_id + skills) is enforced. Require the new request shape and update the single client and all tests together; avoid optional skills with defaults to prevent double-apply if legacy callers send pre-modified stats. **CharacterCreationService** ([server/game/character_creation_service.py](server/game/character_creation_service.py)) is used in sync contexts (e.g. tests); either have it delegate to the same logic as the API or document it as legacy and test creation via the API.
- **Stat modifiers (Option C):** Client applies profession stat_modifiers **for display only** on the profession step (so the player sees "stats after profession"). Create-character API accepts **rolled** stats + profession_id; the **server** applies stat_modifiers when saving so the server remains the single source of truth for final stats. Client does not send pre-modified stats as the authority; server applies from profession_id.

---

## 5. Client: Creation flow and skills UI

### 5.1 Creation flow

- **Order:** Stats (roll, no profession) → Accept → Profession selection (show stat modifiers, apply to displayed stats) → Skill allocation (nine slots + four personal) → **Name** (dedicated step) → Confirm → POST create-character.
- **State:** App holds pending stats, selected profession, skill allocation payload, then name. StatsRollingScreen no longer collects name; it calls onStatsAccepted(stats) only. ProfessionSelectionScreen after stats: choose profession; fetch profession stat_modifiers and apply them to rolled stats **client-side for display only** (so the player sees stats-after-profession); do not send modified stats as final—create-character will send rolled stats + profession_id and server applies modifiers. SkillAssignmentScreen: load skills catalog, enforce 9 slots (70,60,60,50,50,50,40,40,40) and 4 personal (base+20), optionally gray out Cthulhu Mythos; on confirm, advance to name step (no API call yet). **Name screen** (new): single field for character name and "Create character" (or "Confirm"); on submit, POST create-character with name, **rolled** stats, profession_id, skills payload (server applies stat_modifiers when saving); on 201, onComplete() and refresh character list.
- **Files:** [client/src/App.tsx](client/src/App.tsx) (flow and state); [client/src/components/StatsRollingScreen.tsx](client/src/components/StatsRollingScreen.tsx) (remove create call and name field; onStatsAccepted(stats) only); new or refactored profession screen; new SkillAssignmentScreen; new **CharacterNameScreen** (or NameStep) for the name step (and tests).

**Integration:**

- **StatsRollingScreen contract:** Change to `onStatsAccepted(stats)` only (no second argument). Remove name field and create-character POST from StatsRollingScreen. When StatsRollingScreen is the **first** step (stats-first flow), do **not** pass professionId so [useStatsRolling](client/src/hooks/useStatsRolling.ts) sends roll-stats without profession_id and gets a raw roll.
- **handleStatsAccepted:** Must advance to the **next** step (profession) and store `pendingStats`; it must not assume creation already happened (creation happens on the name step).
- **handleCreateCharacter:** Must clear pending stats and skills payload (not only selectedProfession) so re-entering creation does not carry stale state.
- **Both branches:** The "has characters" and "no characters" paths both render ProfessionSelectionScreen then StatsRollingScreen; update both in lockstep so they use the same step state and the new onStatsAccepted(stats) signature.
- **Tests:** [client/src/**tests**/StatRollingWithProfessionRequirements.test.tsx](client/src/__tests__/StatRollingWithProfessionRequirements.test.tsx) and [client/src/App.test.tsx](client/src/App.test.tsx) mock create-character and assert current flow; update mocks and expectations for the new flow and add tests for CharacterNameScreen and full flow.

### 5.2 Skills visibility

- **Current character (Option A):** The **client** always sends the active character id when calling APIs that need it (Map explored rooms, Skills). Server validates that the character belongs to the authenticated user and uses it. No server-side inference of "current" character.
- **ESC menu:** Add "Skills (New Tab)" in [MainMenuModal](client/src/components/MainMenuModal.tsx). When opening the Skills tab, the game client passes the **active character id** in the URL (e.g. `/skills?playerId=<uuid>`) so the new tab can call the skills API with it. Skills page reads auth token from localStorage and playerId from URL; sends both (token in header, playerId in query or body per API contract). Server validates user owns that player_id and returns that character's skills. **Map:** If Map currently does not receive playerId from the client, update Map the same way (client sends active character id; e.g. add playerId to the map URL when opening the tab and have the map API require/use it with ownership check).
  **Integration:** MainMenuModal does not currently receive `playerId`. In [GameClientV2Container](client/src/components/ui-v2/GameClientV2Container.tsx), pass `playerId={gameState.player?.id}` (active character id is available there). Add a "Skills" button that opens `/skills?playerId=...`. Map does not use playerId in the URL today; adding playerId to the map URL is an optional follow-up using the same pattern (ownership check).
- **Slash command `/skills`:** When the user is in the game, the connection or command context is for one character. Server obtains that character id from the request context (e.g. the client sends it with the command, or the WebSocket/session is already bound to that character). Server validates ownership and returns that character's skills as text. Ensure command path receives and sends active character id per Option A.
  **Integration:** Register the command (e.g. in command_parser or command_factories_utility). Reuse how other character-scoped commands (e.g. status, inventory) obtain the current player_id from the connection/session so the handler has the active character id.

---

## 6. Implementation order (suggested)

1. **Level:** Add level to Player + migration; define XP or milestone and level-up trigger (stub or minimal).
2. **Skills catalog:** Table + seed (CoC 7th ed list and base values); Cthulhu Mythos allow_at_creation = false.
3. **Player skills and profession modifiers:** player_skills table; profession stat_modifiers and skill_modifiers (schema + seed defaults); SkillService (get catalog, set player skills, apply profession mods).
4. **Skill use tracking:** skill_use_log table; record_successful_skill_use. Implement a skill-check path (roll d100 vs skill %; return success/failure); when the roll succeeds, call record_successful_skill_use. Which commands/actions use skill checks is defined as those are added.
5. **Level-up improvement:** get_skills_used_this_level; run_improvement_rolls on level-up; wire to level-up hook.
6. **Roll and create API:** Roll without profession requirement; create-character with skills payload and server-side stat/skill modifier application. **Integration:** Do server-side stat_modifiers application and CreateCharacterRequest + skills validation in the **same pass** so create-character has a single contract (rolled stats + profession_id + skills) and one place that applies modifiers and persists. Then update the client flow so the only caller of create-character is the name step.
7. **Client creation flow:** Reorder to stats → profession → skills → name; add SkillAssignmentScreen and CharacterNameScreen (name step); StatsRollingScreen no longer collects name or creates character.
8. **Client skills view:** MainMenuModal Skills (New Tab); `/skills` route or page; server `/skills` command handler.

### 6.1 Implementation progress

Completed work (update this section as items are done):

- **Level (4.1) — Done.** L1: level/experience_points already on Player (no new migration). L2: placeholder XP curve in
  [server/game/level_curve.py](server/game/level_curve.py) (total_xp_for_level, xp_required_for_level, level_from_total_xp).
  L3: [server/game/level_service.py](server/game/level_service.py) (grant_xp, check_level_up, level-up hook stub).
  LevelService registered in game bundle and [server/dependencies.py](server/dependencies.py) (LevelServiceDep).
  Tests: server/tests/unit/game/test_level_curve.py, test_level_service.py.
- **Skills catalog (4.2) — Done.** C1: Migration [db/migrations/024_add_skills_table.sql](db/migrations/024_add_skills_table.sql)
  (skills table). C2: Seed [data/db/04_skills.sql](data/db/04_skills.sql) (CoC 7th ed, Cthulhu Mythos allow_at_creation=false,
  Own Language entry). C3: Skill model, SkillRepository, GET /v1/skills, schemas in server/schemas/players/skill.py;
  unit tests in server/tests/unit/api/test_skills.py.
- **Professions seed:** [data/db/01_professions.sql](data/db/01_professions.sql) updated to omit `id` (DB identity generates it);
  upsert uses ON CONFLICT (name) so full seed runs with GENERATED ALWAYS AS IDENTITY.
- **Player skills and profession modifiers (10.3 P1–P5) — Done.** P1: Migration
  [db/migrations/025_add_player_skills_table.sql](db/migrations/025_add_player_skills_table.sql) and
  [server/models/player_skill.py](server/models/player_skill.py). P2: Migration
  [db/migrations/026_add_profession_modifiers.sql](db/migrations/026_add_profession_modifiers.sql);
  [server/models/profession.py](server/models/profession.py) stat_modifiers/skill_modifiers and getters/setters;
  Player relationship to player_skills. P3: [server/persistence/repositories/player_skill_repository.py](server/persistence/repositories/player_skill_repository.py),
  [server/game/skill_service.py](server/game/skill_service.py) (get_skills_catalog, set_player_skills,
  get_player_skills with ownership). P4: GET /v1/api/players/{player_id}/skills, SkillServiceDep,
  [server/schemas/players/skill.py](server/schemas/players/skill.py) PlayerSkillEntry/PlayerSkillsResponse. P5:
  [data/db/05_profession_modifiers.sql](data/db/05_profession_modifiers.sql) and seed loaders. Unit tests:
  [server/tests/unit/game/test_skill_service.py](server/tests/unit/game/test_skill_service.py).
- **Roll and create API (10.5 A1–A4) — Done.** A1: Roll-stats without profession_id returns raw stats
  (\_roll_stats_raw); with profession_id returns rolled stats plus stats_with_profession_modifiers (preview).
  No profession requirement on roll. A2: [server/schemas/players/player_requests.py](server/schemas/players/player_requests.py)
  CreateCharacterRequest has occupation_slots and personal_interest (optional). A3: create-character applies
  stat_modifiers from profession to rolled stats; validates skills via SkillService.validate_skills_payload;
  after creating player calls SkillService.set_player_skills. A4: GET /api/skills and GET player skills (done in 10.3).
  [server/api/character_creation.py](server/api/character_creation.py), [server/game/skill_service.py](server/game/skill_service.py)
  validate_skills_payload.
- **Skill use tracking and improvement (10.4 T1–T5) — Done.** T1: Migration
  [db/migrations/027_add_skill_use_log_table.sql](db/migrations/027_add_skill_use_log_table.sql) (skill_use_log:
  player_id, skill_id, character_level_at_use, used_at). T2: [server/models/skill_use_log.py](server/models/skill_use_log.py),
  [server/persistence/repositories/skill_use_log_repository.py](server/persistence/repositories/skill_use_log_repository.py);
  SkillService.record_successful_skill_use, get_skills_used_this_level. T3: SkillService.run_improvement_rolls (d100
  \> value: +1 if 90–98, +1d10 otherwise; clamp 99). T4: Game bundle wires level-up hook to run_improvement_rolls
  ([server/container/bundles/game.py](server/container/bundles/game.py)). T5: SkillService.roll_skill_check (roll d100
  vs skill %; on success records use and returns True). Commands that resolve skill checks should call
  skill_service.roll_skill_check(player_id, skill_id, character_level). Unit tests:
  [server/tests/unit/game/test_skill_service.py](server/tests/unit/game/test_skill_service.py) (T2–T5).
- **Client creation flow (10.6 F1–F6) — Done.** F1: [client/src/App.tsx](client/src/App.tsx) uses creationStep
  (`'stats' | 'profession' | 'skills' | 'name'`), pendingStats, pendingSkillsPayload, selectedProfession; flow is
  stats → profession → skills → name. F2: [client/src/components/StatsRollingScreen.tsx](client/src/components/StatsRollingScreen.tsx)
  has no name field or create-character POST; onStatsAccepted(stats) only. F3: ProfessionSelectionScreen passes
  (stats, profession) to next step. F4: [client/src/components/SkillAssignmentScreen.tsx](client/src/components/SkillAssignmentScreen.tsx)
  (9 occupation slots 70,60,60,50,50,50,40,40,40; 4 personal interest; onSkillsConfirmed → name step). F5:
  [client/src/components/CharacterNameScreen.tsx](client/src/components/CharacterNameScreen.tsx) (name input;
  POST create-character with name, stats, profession_id, occupation_slots, personal_interest; onComplete on 201).
  F6: App wires steps and creation state through the chain. Tests: [client/src/App.test.tsx](client/src/App.test.tsx)
  (stats-first flow, handle stats error); [client/src/components/StatsRollingScreen.test.tsx](client/src/components/StatsRollingScreen.test.tsx).
- **Skills visibility (10.7 V1–V5) — Done.** V1: [client/src/components/MainMenuModal.tsx](client/src/components/MainMenuModal.tsx)
  has optional `playerId`; "Skills (New Tab)" button opens `/skills?playerId=...` (or `/skills` if no playerId).
  [client/src/components/ui-v2/GameClientV2Container.tsx](client/src/components/ui-v2/GameClientV2Container.tsx) passes
  `playerId={gameState.player?.id ?? null}`. V2: [client/src/pages/SkillsPage.tsx](client/src/pages/SkillsPage.tsx) reads token from
  localStorage and playerId from URL; GET `/v1/api/players/{player_id}/skills`; renders list or error. Route in
  [client/src/AppRouter.tsx](client/src/AppRouter.tsx) at `/skills`. V3: GET player skills with ownership (P4) already
  implemented. V4: [server/commands/skills_commands.py](server/commands/skills_commands.py) handle_skills_command; command
  type SKILLS, parser/factory/command_service/helpers updated; `/skills` returns active character's skills as text.
  V5: MainMenuModal map button opens `/map?playerId=...` (and room params when currentRoom set); unit tests in
  MainMenuModal.test.tsx.
- **Testing (10.8 E1–E4) — Done.** E1: [e2e-tests/scenarios/scenario-38-revised-character-creation.md](e2e-tests/scenarios/scenario-38-revised-character-creation.md)
  and [client/tests/e2e/runtime/character/revised-character-creation.spec.ts](client/tests/e2e/runtime/character/revised-character-creation.spec.ts).
  E2: [scenario-39-skills-new-tab.md](e2e-tests/scenarios/scenario-39-skills-new-tab.md) and skills-visibility.spec.ts (Skills New Tab + playerId).
  E3: [scenario-40-skills-command.md](e2e-tests/scenarios/scenario-40-skills-command.md) and skills-visibility.spec.ts (/skills command).
  E4: [scenario-41-skills-after-creation.md](e2e-tests/scenarios/scenario-41-skills-after-creation.md) and revised-character-creation.spec.ts (create then /skills).

---

## 7. Files to add or touch (summary)

| Area            | Add                                                                                                           | Modify                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DB              | Migrations: level on players; skills; player_skills; skill_use_log; profession stat_modifiers/skill_modifiers | —                                                                                                                                                                                                                                                                                                                                                                           |
| Server models   | Level on Player; Skill; PlayerSkill; SkillUseLog (or equivalent)                                              | [server/models/player.py](server/models/player.py), [server/models/profession.py](server/models/profession.py)                                                                                                                                                                                                                                                              |
| Server schemas  | Skill catalog, skill assignment, profession mods                                                              | [server/schemas/players/player_requests.py](server/schemas/players/player_requests.py), profession schemas                                                                                                                                                                                                                                                                  |
| Server services | SkillService; level-up + improvement                                                                          | [server/game/character_creation_service.py](server/game/character_creation_service.py), [server/game/stats_generator.py](server/game/stats_generator.py), new skill/level services                                                                                                                                                                                          |
| Server API      | create-character body; GET /api/skills (catalog); /skills command                                             | [server/api/character_creation.py](server/api/character_creation.py), command router                                                                                                                                                                                                                                                                                        |
| Client          | SkillAssignmentScreen; CharacterNameScreen (name step); Skills page (new tab); flow in App                    | [client/src/App.tsx](client/src/App.tsx), [client/src/components/MainMenuModal.tsx](client/src/components/MainMenuModal.tsx), [client/src/components/StatsRollingScreen.tsx](client/src/components/StatsRollingScreen.tsx), [client/src/components/ui-v2/GameClientV2Container.tsx](client/src/components/ui-v2/GameClientV2Container.tsx) (pass playerId to MainMenuModal) |

### 7.1 Integration points and mitigations (summary)

| Area                     | Risk                                   | Mitigation                                                                             |
| ------------------------ | -------------------------------------- | -------------------------------------------------------------------------------------- |
| App creation flow        | Stale state; two branches diverge      | Single "creation step" state; one flow; clear pending state on re-entry                |
| Roll-stats               | Client sends profession_id when not    | Stats-first screen must not pass professionId; document preview vs create              |
| Create-character body    | Double-apply modifiers; old clients    | Server applies modifiers in one place; require new shape; update client/tests together |
| StatsRollingScreen       | Signature/behavior change breaks tests | onStatsAccepted(stats) only; update all callers and tests                              |
| Profession               | No stat_modifiers today                | Add column or key; load profession on create and apply                                 |
| Player level/xp          | Already in model                       | Verify migrations; no double-add                                                       |
| MainMenuModal Skills     | No playerId prop today                 | Add playerId from gameState.player?.id in GameClientV2Container                        |
| Map + playerId           | Map does not use playerId              | Optional follow-up; same pattern as Skills                                             |
| /skills command          | Need active character in context       | Reuse how status/inventory obtain current player_id                                    |
| CharacterCreationService | Sync path may not apply modifiers      | Share logic with API or mark legacy and test via API                                   |
| E2E                      | Old flow assumptions                   | Update scenario steps to stats → profession → skills → name → create                   |

---

## 8. Decided points and implementation notes

Each item below was an open point; the decision is recorded and implementation is described so implementers know exactly what to build.

- **Name collection — Decided.** Name is collected on its own step after the skills step (CharacterNameScreen); flow is stats → profession → skills → name → create.
  **Implementation:** Add a CharacterNameScreen (or equivalent) that receives pending **rolled** stats, profession, and skills payload from App state. Single text input for character name plus a "Create character" (or "Confirm") button. On submit, POST create-character with name, rolled stats, profession_id, and skills (do not send client-modified stats; server applies stat_modifiers). On 201, call onComplete() so App refreshes the character list and exits creation. Do not collect name on StatsRollingScreen or SkillAssignmentScreen. Ensure App passes creation state through the chain so the name step has everything needed for the final POST. **Integration:** create-character is the only creation path for this flow; stats in the request are always interpreted as **rolled** (server applies stat_modifiers when saving). Document this contract so other callers (tests, admin tools) do not send pre-modified stats and get double-applied modifiers.

- **XP vs milestone — Decided.** XP with a **logarithmic** curve. Exact formula deferred (Option C).
  **Implementation:** Add an `xp` (or equivalent) field and `level` to Player; migration to add columns. Implement "XP to reach level N" using a **placeholder** (e.g. log-style with arbitrary constants or a small table) so the curve flattens at higher levels; document in code/ADR that the exact curve will be tuned later. Implement grant_xp(player_id, amount) and check_level_up(player_id); on level-up, run skill improvement for skills used that level (see 4.5). No milestone-only path unless added later.

- **Skills page auth / current character — Decided.** Option A: client always sends active character id; server validates ownership.
  **Implementation:** Skills page URL can include playerId (e.g. `/skills?playerId=<uuid>`). Game client, when opening Skills (New Tab), passes the active character id into that URL (MainMenuModal receives current player id and builds the link). Skills page reads token from localStorage and playerId from URL; calls GET skills API with token + playerId. Server: validate that the authenticated user owns that player_id; then return that character's skills. Apply the same pattern to Map. For slash command `/skills`, ensure the request includes the active character id; server validates and returns that character's skills.

- **Improvement cap — Decided.** Max skill value 99%. On successful improvement: if current 90–98, add 1 point; if current &lt; 90, add 1d10. Clamp result to 99.
  **Implementation:** In the level-up skill improvement logic (run_improvement_rolls or equivalent): for each qualifying skill, after a successful d100 roll (roll &gt; current skill value), compute gain = 1 if current is in [90, 98], else gain = roll 1d10; new_value = min(current + gain, 99). Persist new_value. Do not allow stored skill value to exceed 99. Validation on set: clamp any incoming value to 0–99.

- **Profession stat_modifiers seed — Decided.** Use educated guesses in plan (4.4) for seed/migration.
  **Implementation:** In the migration or seed that creates/updates professions, set `stat_modifiers` (or the chosen storage shape) per profession using the table in section 4.4. Match by profession name or id; if a profession in the DB is not listed, leave stat_modifiers empty or default. Adjust deltas to match actual profession names and game balance during implementation. Ensure the create-character (or preview) path reads stat_modifiers and applies them to rolled stats before persisting.

---

## 9. Testing: unit tests and Playwright integration tests

Testing must be defined and implemented with the feature. Use `make test` from project root for server tests; follow existing Playwright/E2E patterns (e.g. [e2e-tests/scenarios](e2e-tests/scenarios), [docs/E2E_TESTING_GUIDE.md](docs/E2E_TESTING_GUIDE.md)).

**Integration:** Existing tests that touch creation will break when the flow and contracts change. [client/src/**tests**/StatRollingWithProfessionRequirements.test.tsx](client/src/__tests__/StatRollingWithProfessionRequirements.test.tsx) and [client/src/App.test.tsx](client/src/App.test.tsx) mock create-character and the current onStatsAccepted(stats, characterName) contract; update them for the new flow (onStatsAccepted(stats) only, creation on name step) and add tests for CharacterNameScreen and the full chain. E2E scenarios that assume profession → stats + name → create must be updated so steps are: stats (roll, accept) → profession → skills → name → create; ensure prerequisites and step order are correct so scenarios do not time out or assert on the wrong screen.

### 9.1 Server unit tests

- **SkillService (or equivalent):** Get skills catalog (returns list with base_value, allow_at_creation); set player skills (occupation + personal + catalog-base + profession mods); apply profession skill_modifiers; apply profession stat_modifiers to a stats dict; record_successful_skill_use(player_id, skill_id, level); get_skills_used_this_level(player_id, level); run_improvement_rolls(player_id, new_level) with cap 99 and gain rules (90–98 → +1, &lt;90 → +1d10). Ownership: get another user's skills without ownership returns 403 or empty per design.
- **Character creation with skills:** Create character with valid occupation_slots (exactly one 70, two 60, three 50, three 40) and four personal_interest skill_ids; server applies stat_modifiers from profession_id, creates player_skills for allocated skills + all catalog-base skills + profession modifiers; Own Language not allocated → set to Education (after stat mods). Reject: occupation values not the allowed set; Cthulhu Mythos in occupation or personal interest; invalid skill_id; user does not own profession_id if validated.
- **Roll stats:** Roll without profession_id returns raw stats (no requirement check). Optional: roll with profession_id for preview returns stats with stat_modifiers applied (if preview endpoint exists).
- **Level/XP:** grant_xp(player_id, amount) increases xp; check_level_up(player_id) uses placeholder curve and, on level-up, runs skill improvement for skills used that level. Unit test with mocked skill_use_log and assert improvement roll logic (gain 1 vs 1d10, clamp 99).
- **API:** GET /api/skills returns catalog; GET player skills requires auth and player_id ownership. create-character endpoint validates skills payload and returns 400 when occupation set is invalid.
- **Command /skills:** Handler returns current character's skills (with ownership check); response format (e.g. text list) is consistent.

### 9.2 Client unit tests

- **SkillAssignmentScreen:** Renders skills catalog; enforces nine occupation slots with values 70, 60, 60, 50, 50, 50, 40, 40, 40 and four personal interest (base+20); Cthulhu Mythos not selectable or disabled; on confirm, calls parent with skills payload (occupation_slots as skill_id + value, personal_interest as skill_ids); does not POST create-character (advances to name step).
- **CharacterNameScreen:** Renders name input and submit button; on submit, POST create-character with name + **rolled** stats + profession_id + skills from props (server applies stat_modifiers); on 201, calls onComplete(); on error, shows message.
- **StatsRollingScreen:** Does not collect name; on accept, calls onStatsAccepted(stats) only (no create-character call). Existing tests updated for new signature.
- **ProfessionSelectionScreen (if changed):** Applies stat_modifiers client-side for display; displays "stats after profession" when profession selected.
- **MainMenuModal:** Skills (New Tab) button present; on click, opens URL that includes playerId (e.g. `/skills?playerId=...`) when current player id is available.

### 9.3 Playwright integration tests (new scenarios)

- **Revised character creation flow (stats → profession → skills → name → create):** Log in (or use user with no characters); trigger creation; complete **stats** step (roll, accept); complete **profession** step (select profession, see stat modifiers in UI); complete **skills** step (allocate nine occupation + four personal, confirm); complete **name** step (enter name, submit); assert character appears in character list and can be selected / entered. Covers the full flow and server create-character with skills and stat_modifiers.
- **Skills visibility — ESC menu:** In game as a character, open ESC menu; click Skills (New Tab); assert new tab opens with URL containing playerId (and token or redirect to login if not authenticated); assert skills page loads and shows that character's skills (or appropriate error). Optionally assert Map passes playerId when opening map tab.
- **Skills visibility — /skills command:** In game as a character, send `/skills` command; assert response contains that character's skills (e.g. skill names and values in terminal output). If multiple characters exist, assert response is for the active character.
- **Create character and verify skills persisted:** After creating a character through the new flow (with at least one occupation and one personal interest skill), use /skills or GET skills API (with auth and player_id) and assert the created character has the expected skills (allocated + catalog-base + profession mods, Own Language = EDU if not allocated).

New Playwright scenarios should live under [e2e-tests/scenarios](e2e-tests/scenarios) with descriptive names (e.g. scenario-XX-revised-character-creation-with-skills.md) and follow the format of existing scenarios (prerequisites, steps, expected results). Run via project Playwright/E2E harness; respect server start/stop and one-server rules.

---

## 10. Implementation todos and validation

Each todo has a short id, description, and **Validation** steps. Complete validation for a todo before marking it done. Run `make test` (and E2E where noted) as part of validation.

### 10.1 Level (plan 4.1)

**Status:** L1–L3 done (level_curve.py, level_service.py, LevelService in bundle; tests in test_level_curve.py, test_level_service.py).

| Id  | Todo                                                                                                                                            | Validation                                                                                                                  |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| L1  | Add `level` (int, default 1) and `xp` (or equivalent) columns to Player model; create and run migration.                                        | Migration runs cleanly; existing players get level=1 and xp=0 (or default). DB schema shows new columns.                    |
| L2  | Implement placeholder "XP to reach level N" (log-style or table); document in code/ADR that curve will be tuned later.                          | Unit test: given xp, level is correct; threshold for level 2 exists and is finite.                                          |
| L3  | Implement grant_xp(player_id, amount) and check_level_up(player_id). On level-up, invoke hook for skill improvement (stub if 4.5 not yet done). | Unit test: grant_xp increases xp; check_level_up when over threshold increments level and calls improvement hook (or stub). |

### 10.2 Skills catalog (plan 4.2)

**Status:** C1–C3 done (024_add_skills_table.sql, 04_skills.sql, Skill model, SkillRepository, GET /v1/skills, test_skills.py).

| Id  | Todo                                                                                                                                            | Validation                                                                                                                      |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| C1  | Create `skills` table (id, key, name, description, base_value, allow_at_creation); migration.                                                   | Migration runs; table exists.                                                                                                   |
| C2  | Seed skills from CoC 7th ed list with base values; Cthulhu Mythos allow_at_creation=false. Own Language has a catalog entry (base or sentinel). | GET /api/skills (or equivalent) returns list; Cthulhu Mythos present with allow_at_creation=false; base_value present for each. |
| C3  | Unit tests for catalog: list returned, base_value and allow_at_creation correct for sample skills.                                              | `make test` includes catalog tests; they pass.                                                                                  |

### 10.3 Player skills and profession modifiers (plan 4.3, 4.4)

**Status: P1–P5 implemented.** See section 6.1 for file references and test location.

| Id  | Todo                                                                                                                                                                                                                 | Validation                                                                                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P1  | Create `player_skills` table (player_id FK, skill_id FK, value); PK (player_id, skill_id); migration.                                                                                                                | Migration runs; table exists; FK to players and skills.                                                                                                                                   |
| P2  | Add Player relationship to player_skills. Add profession fields: stat_modifiers and skill_modifiers (new columns or mechanical_effects); migration/seed.                                                             | Player has relationship; profession has stat_modifiers and skill_modifiers; seed data per plan 4.4 and 4.3.                                                                               |
| P3  | SkillService: get_skills_catalog(); set_player_skills(player_id, occupation_slots, personal_interest, profession_id, stats_for_edu) applying catalog-base + profession mods + Own Language = EDU when not allocated. | Unit test: create character with mixed allocation; assert player_skills has rows for all catalog-base skills, allocated skills have slot+modifier, Own Language = EDU when not allocated. |
| P4  | SkillService: get_player_skills(player_id); ownership check (user owns player_id).                                                                                                                                   | Unit test: returns skills for owned character; returns 403 or empty for other user's character.                                                                                           |
| P5  | Seed profession stat_modifiers and skill_modifiers per plan 4.4 and 4.3 (educated guesses).                                                                                                                          | At least one profession has non-empty stat_modifiers and skill_modifiers; create-character applies them (validated in P3 / 10.6).                                                         |

### 10.4 Skill use tracking and improvement (plan 4.5)

**Status: T1–T5 implemented.** See section 6.1 for migrations, repositories, SkillService methods, and tests.

| Id  | Todo                                                                                                                                                                                                    | Validation                                                                                                                 |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| T1  | Create skill_use_log table (player_id, skill_id, character_level_at_use, used_at); migration.                                                                                                           | Migration runs; table exists.                                                                                              |
| T2  | Implement record_successful_skill_use(player_id, skill_id, level). Implement get_skills_used_this_level(player_id, level).                                                                              | Unit test: record_successful_skill_use delegates to repo; get_skills_used_this_level returns repo result.                  |
| T3  | Implement run_improvement_rolls(player_id, new_level): for each skill with use in skill_use_log for level=new_level-1, roll d100; if roll > current value, add 1 (90–98) or 1d10 (&lt;90), clamp to 99. | Unit test: improvement applied when roll > value (+1d10 or +1); roll ≤ current no change; previous level &lt; 1 no-op.     |
| T4  | Wire level-up hook (from L3) to run_improvement_rolls.                                                                                                                                                  | Game bundle passes \_skill_improvement_on_level_up to LevelService; test_level_service covers hook invocation.             |
| T5  | Implement skill-check path (roll d100 vs skill %); on success call record_successful_skill_use. Document where commands will plug in.                                                                   | Unit test: roll_skill_check success records use and returns True; failure/unknown skill returns False and does not record. |

### 10.5 Roll and create API (plan 4.6)

**Status: A1–A4 implemented.** See section 6.1 for file references.

| Id  | Todo                                                                                                                                                                                                                                                                                                                                                                                           | Validation                                                                                                                                                                                                 |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A1  | Roll-stats: support roll without profession_id; return raw stats (no profession requirement). Optional: with profession_id return stats with stat_modifiers for preview.                                                                                                                                                                                                                       | Unit test: roll without profession_id returns stats; no validation against profession.                                                                                                                     |
| A2  | CreateCharacterRequest: add occupation_slots (list of { skill_id, value }) and personal_interest (list of { skill_id }); keep name, stats, profession_id.                                                                                                                                                                                                                                      | Schema validates; example in OpenAPI.                                                                                                                                                                      |
| A3  | create_character_with_stats: verify occupation_slots are exactly one 70, two 60, three 50, three 40; reject otherwise. Verify skill_ids in catalog; reject Cthulhu Mythos in occupation or personal. Apply stat_modifiers from profession_id to rolled stats; persist player with level 1; call SkillService to set player_skills (allocated + catalog-base + profession mods + Own Language). | Unit test: valid payload creates player and player_skills; invalid occupation set returns 400; Cthulhu Mythos in payload returns 400; Own Language not allocated = EDU; all catalog-base skills have rows. |
| A4  | GET /api/skills returns catalog. GET /api/players/{player_id}/skills (or equivalent) requires auth and ownership; returns that character's skills.                                                                                                                                                                                                                                             | Unit test: GET skills returns list; GET player skills with valid ownership returns skills; without ownership returns 403 or 404.                                                                           |

### 10.6 Client creation flow (plan 5.1)

**Status: F1–F6 implemented.** See section 6.1 for file references and tests.

| Id  | Todo                                                                                                                                                                                                                | Validation                                                                                                     |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| F1  | App: reorder flow to stats → profession → skills → name. State: pending stats, selected profession, skills payload; no name until name step.                                                                        | Flow in code matches; no create-character until name step.                                                     |
| F2  | StatsRollingScreen: remove name field and create-character POST; on accept call onStatsAccepted(stats) only.                                                                                                        | Unit test: onStatsAccepted called with stats; no fetch to create-character.                                    |
| F3  | ProfessionSelectionScreen: when profession selected, apply stat_modifiers to rolled stats client-side for display only; pass (stats, profession) to next step.                                                      | Display shows modified stats; create-character still receives rolled stats + profession_id (validated in E2E). |
| F4  | Add SkillAssignmentScreen: load catalog; enforce 9 slots (70,60,60,50,50,50,40,40,40) and 4 personal (base+20); Cthulhu Mythos disabled; on confirm pass (stats, profession, skills payload) to name step; no POST. | Unit test: enforces slot counts and values; confirm calls parent with payload; no create-character.            |
| F5  | Add CharacterNameScreen: name input, submit → POST create-character (name, rolled stats, profession_id, skills payload); on 201 call onComplete(); on error show message.                                           | Unit test: submit sends correct body; onComplete called on 201.                                                |
| F6  | App: pass creation state (stats, profession, skills) through profession → skills → name; Name screen has everything for final POST.                                                                                 | E2E or manual: complete flow and create character; character appears in list.                                  |

### 10.7 Skills visibility (plan 5.2)

**Status: V1–V5 implemented.** V3 already done (P4). V5: Map URL includes playerId (client); map API ownership
check is optional follow-up. See section 6.1 for file refs.

| Id  | Todo                                                                                                                                                                         | Validation                                                                                              |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| V1  | MainMenuModal: add "Skills (New Tab)" button; on click open `/skills?playerId=<active_character_id>`. Ensure active character id is available (from game state/props).       | Unit test: button present; click opens URL with playerId param.                                         |
| V2  | Add /skills route (Skills page): read token from localStorage, playerId from URL; call GET player skills with auth + playerId; render list (or "Not authenticated" / error). | Manual or E2E: open tab with valid playerId and token; skills display; without token show login prompt. |
| V3  | Server: GET player skills endpoint requires auth and validates user owns player_id; returns that character's skills.                                                         | Unit test: 200 for owner; 403/404 for non-owner.                                                        |
| V4  | Implement /skills command: request includes active character id; server returns that character's skills as text.                                                             | Unit test or E2E: /skills returns skill list for active character.                                      |
| V5  | If Map does not already use playerId: add playerId to map URL when opening from menu; map API requires/uses it with ownership check.                                         | MainMenuModal opens /map?playerId=... (and room params when set); unit test asserts URL.                |

### 10.8 Testing (plan 9)

**Status: E1–E4 implemented.** Scenario docs in e2e-tests/scenarios; specs in client/tests/e2e/runtime/character/.

| Id  | Todo                                                                                                                                              | Validation                                                                                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| U1  | Add server unit tests per section 9.1 (SkillService, creation with skills, roll, level/XP, API, /skills command).                                 | `make test` passes; new tests in server/tests/; coverage for new code.                           |
| U2  | Add client unit tests per section 9.2 (SkillAssignmentScreen, CharacterNameScreen, StatsRollingScreen, ProfessionSelectionScreen, MainMenuModal). | Client test run passes; new tests for new/updated components.                                    |
| E1  | Add Playwright scenario: revised character creation (stats → profession → skills → name → create); character in list.                             | Scenario 38 + revised-character-creation.spec.ts; flow completes and character selectable.       |
| E2  | Add Playwright scenario: Skills (New Tab) opens with playerId; skills page shows that character's skills.                                         | Scenario 39 + skills-visibility.spec.ts; URL and Character Skills page asserted.                 |
| E3  | Add Playwright scenario: /skills command returns active character's skills.                                                                       | Scenario 40 + skills-visibility.spec.ts; command response contains "Your skills:".               |
| E4  | Add Playwright scenario (or extend E1): after creation, GET skills or /skills shows expected skills (allocated + catalog-base + profession mods). | Scenario 41 + E4 test in revised-character-creation.spec.ts; after create, /skills shows skills. |

### 10.9 Definition of done per todo

- **Done:** Todo implemented, validation steps executed, and any referenced tests passing. For migrations, applied in dev and test env. For E2E, scenario runs without failure per project harness.

---

_Plan drafted for review and iteration. No code changes until you approve._
