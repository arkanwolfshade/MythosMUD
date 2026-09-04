---
name: Quest subsystem implementation
overview: "Implement the quest subsystem per [QUEST_SYSTEM_FEATURES.md](e:\\projects\\GitHub\\MythosMUD\\docs\\QUEST_SYSTEM_FEATURES.md) decisions: schema (JSONB definitions, instances, offers), triggers (room/NPC/item), goals (complete-activity, kill N), rewards (XP, item, spell), journal command and GET /quests API, DAG prerequisites, and first quest; with unit tests (70% minimum coverage) and E2E integration tests."
todos:
  - id: migration-tables
    content: Create Alembic migration for quest_definitions, quest_instances, quest_offers tables
    status: completed
  - id: migration-seed
    content: Add seed data for first quest leave_the_tutorial (goal, trigger, reward, quest_offers row)
    status: completed
  - id: schemas
    content: Add Pydantic schemas for quest definition JSONB and instance progress
    status: completed
  - id: repo-definition
    content: Implement QuestDefinitionRepository (get_by_id, get_by_name, list for offer checks)
    status: completed
  - id: repo-instance
    content: Implement QuestInstanceRepository (CRUD, list_active/list_completed by character)
    status: completed
  - id: service-resolve-name
    content: QuestService resolve quest common name to quest_id
    status: completed
  - id: service-start
    content: QuestService start_quest (trigger + prerequisite DAG + create instance)
    status: completed
  - id: service-progress-activity
    content: QuestService progress for complete_activity goal (room exit event)
    status: completed
  - id: service-progress-kill
    content: QuestService progress for kill_N goal (NPC death/kill event)
    status: completed
  - id: service-complete
    content: QuestService completion when all goals met and auto_complete (apply rewards)
    status: completed
  - id: service-turnin
    content: QuestService turn_in (validate turn_in_entities, inventory slot, apply XP/item/spell)
    status: completed
  - id: service-abandon
    content: QuestService abandon by name (set instance state abandoned)
    status: completed
  - id: wire-triggers
    content: Wire room entry, NPC interaction, item acquisition to trigger evaluation and start_quest
    status: completed
  - id: wire-progress
    content: Wire room exit and NPC kill events to progress handlers
    status: completed
  - id: api-get-quests
    content: Add GET /quests authenticated endpoint and update OpenAPI spec
    status: completed
  - id: cmd-journal
    content: Register journal/quests command (alias); handler returns formatted quest log
    status: completed
  - id: cmd-abandon
    content: Register quest abandon command; parse name and call QuestService.abandon
    status: completed
  - id: game-state-push
    content: Include quest log in game state push (or document client GET /quests usage)
    status: completed
  - id: client-display
    content: Client display quest log in Journal/Quest panel from state or API
    status: completed
  - id: unit-repos
    content: Unit tests for QuestDefinitionRepository and QuestInstanceRepository
    status: completed
  - id: unit-service-start-progress
    content: Unit tests for QuestService start, progress (complete_activity, kill_N), DAG
    status: completed
  - id: unit-service-turnin-abandon
    content: Unit tests for QuestService turn-in (rewards, inventory full), abandon
    status: completed
  - id: unit-api-cmd
    content: Unit tests for GET /quests API and journal/quest abandon command handlers
    status: completed
  - id: integration-flow
    content: Server integration tests quest flow (start, progress, complete/turn-in) with test DB
    status: completed
  - id: integration-abandon-get
    content: Server integration tests abandon flow and GET /quests log shape
    status: completed
  - id: e2e-playwright
    content: Playwright E2E scenario quest log visible after login
    status: completed
  - id: doc-quest-system
    content: Developer doc Quest system section or ADR; link to QUEST_SYSTEM_FEATURES.md
    status: completed
  - id: doc-design-guidelines
    content: Developer doc Quest design guidelines (lysator principles)
    status: completed
isProject: false
---

# Quest Subsystem Implementation Plan

## Scope

- **Source of truth:** [docs/QUEST_SYSTEM_FEATURES.md](e:\projects\GitHub\MythosMUD\docs\QUEST_SYSTEM_FEATURES.md) Review decisions (Features 1–8, 10–11; Feature 9 deferred).
- **Testing:** Unit tests for all new server code (70% minimum coverage); server integration tests for quest API and persistence; at least one client E2E (Playwright) scenario for quest log visibility. Coverage enforced via `make test-ci` / [scripts/run_test_ci.py](e:\projects\GitHub\MythosMUD\scripts\run_test_ci.py).

---

## Definition of done

Implementation is complete only when all of the following are satisfied:

- **Seed data created** — First quest (e.g. leave_the_tutorial) and any quest_offers rows exist and are loadable.
- **Database migrations applied (DDL and DML)** — Alembic migration(s) for quest tables have been run; schema and seed data are present in the target environment.
- **All non-deferred features code complete** — Every included feature from [QUEST_SYSTEM_FEATURES.md](e:\projects\GitHub\MythosMUD\docs\QUEST_SYSTEM_FEATURES.md) (Features 1–8, 10–11) is implemented; deferred items (e.g. Feature 9 repeatable quests) are out of scope.
- **Developer and subsystem documentation created** — Quest system section or ADR and Quest design guidelines (lysator principles) are written and linked from the plan/features doc.
- **Unit tests pass and have at least 70% coverage** — All unit tests for new quest code pass; coverage for new modules meets or exceeds 70% (enforced by `make test-ci` where applicable).
- **Sign-off from Professor Wolfshade** — Final approval from the project owner before considering the implementation done.

---

## 1. Schema and persistence

- **Quest names:** Each quest has a **common name** (player-facing) so players never need to know `quest_id`. Store in definition JSONB as `name` (canonical, unique). UI, journal, and any future commands (e.g. turn-in) show and accept the quest **name**; server resolves name to `quest_id` internally. `quest_id` remains the internal PK for DB and APIs.
- **Alembic migration** (new revision under [server/alembic/versions/](e:\projects\GitHub\MythosMUD\server\alembic\versions)):
  - **quest_definitions:** `id` (PK, text; internal quest_id), `definition` (JSONB), `created_at` / `updated_at`. JSONB holds: `name` (unique, player-facing), `title` (display), `description`, `goals[]` (each: `type`, `target`/config), `rewards[]` (each: `type`, config), `triggers[]` (e.g. `{ "type": "room"|"npc"|"item", "entity_id": "..." }`), `requires_all` / `requires_any` (arrays of quest IDs for DAG), `auto_complete` (bool), `turn_in_entities` (list of entity IDs when `auto_complete` false).
  - **quest_instances:** `id` (PK), `character_id` (FK to population/players as used by game), `quest_id` (FK to quest_definitions), `state` (e.g. `active` / `completed` / `abandoned`), `progress` (JSONB for per-goal counts/state), `accepted_at`, `completed_at` (nullable). Unique on `(character_id, quest_id)` for one active instance per character per quest. Abandoned instances keep the row with `state = 'abandoned'` so the player can re-accept later from the quest giver.
  - **quest_offers:** junction table `(quest_id, offer_entity_type, offer_entity_id)` to link quests to NPCs or rooms (e.g. `npc`+npc_definition_id, `room`+room_id). Supports “who offers this quest” and “where can turn in”.
- **Repositories:** QuestDefinitionRepository (load by id, list for offer checks), QuestInstanceRepository (CRUD by character + quest, list active/completed for character). Use existing patterns in [server/persistence/](e:\projects\GitHub\MythosMUD\server\persistence) and existing PostgreSQL adapter.
- **Seed data:** Migration or separate seed script inserts the first quest definition (e.g. tutorial “exit the room” complete-activity goal) and its `quest_offers` row(s).

---

## 2. Quest service (core logic)

- **Location:** New module under `server/game/` (e.g. `server/game/quest/` or `server/services/quest_service.py`).
- **QuestService** responsibilities:
  - **Start quest:** Check triggers (room enter, NPC interaction, item acquired); validate prerequisites (resolve DAG: `requires_all` and `requires_any`); create quest_instance in `active` state.
  - **Progress:** On events (room exit for complete-activity, NPC kill for kill-N), resolve active instances and update `progress` JSONB; if all goals met and `auto_complete` true, run completion; else mark “turn-in ready” where applicable.
  - **Turn-in:** When `auto_complete` false, allow turn-in at `turn_in_entities`; validate inventory slot for item rewards; apply rewards (XP, item to inventory, spell via [SpellLearningService.learn_spell_from_quest](e:\projects\GitHub\MythosMUD\server\game\magic\spell_learning_service.py)); set instance to `completed`.
  - **Abandon:** Player can abandon an active quest by common name. Command: `/quest abandon <quest common name>`. Resolve name → quest_id; ensure character has an active instance; set instance state to `abandoned` (no rewards). Player can re-accept the quest from the quest giver later.
  - **Rewards:** XP (existing player/level service), item (inventory service; if full, block turn-in per decision), spell ([learn_spell_from_quest](e:\projects\GitHub\MythosMUD\server\game\magic\spell_learning_service.py) already exists).
- **Event wiring:** Subscribe to room entry, NPC interaction, item acquisition for triggers; to room exit (or specific “complete activity” event) and NPC death/kill for progression. Use existing event bus or NATS patterns (see [server/realtime/](e:\projects\GitHub\MythosMUD\server\realtime), [NATS_SUBJECT_PATTERNS.md](e:\projects\GitHub\MythosMUD\docs\NATS_SUBJECT_PATTERNS.md)) and keep server authoritative.

---

## 3. API and command

- **GET /quests:** Authenticated endpoint returning current character’s quest log (active instances with progress, completed if desired). Response shape: list of `{ quest_id, name, title, description, goals_with_progress, state }`. Clients and players use **name** (and title) for display; quest_id is for internal linking only. Implement in existing API layout; add to OpenAPI per [mythosmud-openapi-workflow](e:\projects\GitHub\MythosMUD.cursor\skills\mythosmud-openapi-workflow\SKILL.md).
- **Commands:** (1) `journal` and `quests` both accepted (alias); handler calls QuestService to get log and returns formatted text (and/or triggers game_state push so client can show journal). (2) `/quest abandon <quest common name>` — abandon an active quest by its common name (e.g. `quest abandon leave_the_tutorial`). Register in same way as other commands (e.g. [server/commands/](e:\projects\GitHub\MythosMUD\server\commands)).

---

## 4. Client (minimal for “command + API only”)

- **Game state:** Ensure quest log is included in existing game state push (or that client can request it via GET /quests) and that client displays active/completed quests (e.g. Journal/Quest panel or equivalent).
- **No new UI flows required** beyond displaying what the server sends for “command + API only” (per Feature 7).

---

## 5. First quest

- One seed quest: **name** `leave_the_tutorial` (canonical), display title e.g. “Leave the tutorial” with goal type **complete_activity** (target: exit tutorial room), trigger **room** (tutorial room id) or **npc** (tutorial NPC). Reward: XP (and optionally item or nothing else). Use `auto_complete: true` for simplicity. Prerequisites: none. Add to seed data and verify via integration test.

---

## 6. Unit tests (70% minimum coverage)

- **Target:** All new Python code in `server/game/quest/`, `server/services/quest_service.py`, `server/persistence/.../quest`_*, and quest-related API/command code.
- **Location:** [server/tests/unit/](e:\projects\GitHub\MythosMUD\server\tests\unit) (pytest; markers per [server/tests/README.md](e:\projects\GitHub\MythosMUD\server\tests\README.md): `@pytest.mark.unit`).
- **Scope:**
  - QuestService: start (trigger + prerequisite checks), progress (complete-activity, kill-N), turn-in (rewards, inventory-full blocks item reward), **abandon** (by name, success; unknown name or not active returns clear error), DAG resolution (`requires_all` / `requires_any`).
  - Repositories: get/create/update instance, get definition, list by character (include filtering by state e.g. active only for journal).
  - Goal/reward parsing and validation (invalid config, unknown type).
  - API: GET /quests returns 401 when unauthenticated and correct shape when authenticated (can use TestClient + mocks).
  - Commands: journal/quests returns formatted log (handler unit test with mocked QuestService); **quest abandon** (by name: success, unknown name, not active).
- **Coverage:** Run `make test-server-coverage` and ensure new modules meet 70% line coverage; critical paths (start, progress, turn-in, rewards) should be well covered. CI enforces thresholds via [scripts/run_test_ci.py](e:\projects\GitHub\MythosMUD\scripts\run_test_ci.py).

---

## 7. E2E integration tests

- **Server integration (pytest):** In [server/tests/integration/](e:\projects\GitHub\MythosMUD\server\tests\integration), add tests marked `@pytest.mark.integration` (and `serial` if sharing DB/state):
  - With test DB and seeded quest: character starts quest (via trigger or API if you add a “start quest” endpoint), performs activity (e.g. move room or kill NPC via test helpers), then either auto-complete or turn-in; assert instance state and rewards (e.g. XP applied, spell learned).
  - **Abandon:** Character has active quest; call abandon by common name; assert instance state is `abandoned` and quest no longer in active log; character can re-accept from giver.
  - GET /quests: authenticated request returns quest log; after completion, completed quest appears as expected; abandoned quests not in active list.
- **Client E2E (Playwright):** At least one scenario in [client/tests/e2e/runtime/](e:\projects\GitHub\MythosMUD\client\tests\e2e\runtime) (or equivalent per [docs/E2E_TESTING_GUIDE.md](e:\projects\GitHub\MythosMUD\docs\E2E_TESTING_GUIDE.md)): e.g. log in, open journal/quests (command or UI), assert that quest list is visible and reflects server state (e.g. “Leave the tutorial” active or completed). Use `make test-playwright` / `test-client-runtime` to run.

---

## 8. Documentation and design principles

- **Developer doc:** Add a short “Quest system” section (or ADR) describing: **quest name** (canonical, player-facing; players use name, not quest_id), goal types (complete_activity, kill_n), reward types (xp, item, spell), triggers (room, npc, item), DAG prerequisites, and that turn-in is blocked if inventory full for item reward; **abandon** via `/quest abandon <quest common name>`. Link to [QUEST_SYSTEM_FEATURES.md](e:\projects\GitHub\MythosMUD\docs\QUEST_SYSTEM_FEATURES.md).
- **Lysator design principles (Feature 11):** Add “Quest design guidelines” to docs (clear hints, no un-warned death, winnable without meta-knowledge, meaningful rewards; avoid syntax quests and boring grind) as content/design guidance for future quest authors.

---

## Implementation order (suggested)

1. Alembic migration: tables + seed for first quest.
2. Repositories and models/schemas for definitions and instances.
3. QuestService (start, progress, turn-in, rewards) and event wiring.
4. GET /quests API; journal/quests and quest abandon commands; game state push if needed.
5. Client display of quest log (use existing panel or minimal new UI).
6. Unit tests for service, repositories, API, command (achieve 70%+ on new code).
7. Server integration tests (quest flow and GET /quests).
8. One Playwright E2E scenario (quest log visibility).
9. Developer doc and quest design guidelines.

---

## Detailed todos (resumable)

Use this list to resume after an interruption. Complete in order where dependencies apply; mark items
done as you go.

**Schema and persistence**

1. Create Alembic migration: add `quest_definitions`, `quest_instances`, `quest_offers` tables with
  all columns, FKs, unique constraint on (character_id, quest_id), and indexes.
2. Add seed data (in migration or separate script): first quest `leave_the_tutorial` with
  complete_activity goal, trigger (room or NPC), XP reward, `auto_complete: true`; insert
   corresponding `quest_offers` row(s).
3. Add Pydantic schemas for quest definition JSONB (name, title, description, goals, rewards,
  triggers, requires_all, requires_any, auto_complete, turn_in_entities) and for instance progress.

**Repositories**

1. Implement QuestDefinitionRepository: get_by_id, get_by_name (for name-to-id resolve), list or
  methods for offer checks (e.g. quests offered by entity).
2. Implement QuestInstanceRepository: get_by_character_and_quest, create, update (state, progress),
  list_active_by_character, list_completed_by_character (if needed for API).

**QuestService**

1. QuestService: resolve quest common name to quest_id (via definition repo).
2. QuestService: start_quest — evaluate trigger (room/NPC/item), check prerequisites (DAG
  requires_all/requires_any), create quest_instance in active state.
3. QuestService: progress for complete_activity goal (on room exit event); update instance
  progress; if all goals met and auto_complete, run completion.
4. QuestService: progress for kill_N goal (on NPC death/kill event); update counts; if all goals
  met and auto_complete, run completion.
5. QuestService: completion — apply rewards (XP, item to inventory if slot available, spell via
  learn_spell_from_quest); set instance state completed.
6. QuestService: turn_in — when auto_complete false, validate turn_in_entities and inventory slot
  for item reward; apply rewards; set instance completed.
7. QuestService: abandon — resolve name to quest_id, get active instance for character, set
  state abandoned.

**Event wiring**

1. Wire room entry, NPC interaction, item acquisition events to trigger evaluation and start_quest.
2. Wire room exit event to complete_activity progress handler.
3. Wire NPC kill/death event to kill_N progress handler.

**DI and app registration**

1. Register QuestService (and repos) in DI container / lifespan (see [server/app/lifespan_startup.py](e:\projects\GitHub\MythosMUD\server\app\lifespan_startup.py), [server/dependencies.py](e:\projects\GitHub\MythosMUD\server\dependencies.py)).

**API and commands**

1. Add GET /quests authenticated endpoint; return quest log (quest_id, name, title, description,
  goals_with_progress, state); update OpenAPI spec.
2. Register journal and quests commands (alias); handler calls QuestService.get_log, returns
  formatted text and/or triggers game_state push.
3. Register quest abandon command; parse `quest abandon <name>`, call QuestService.abandon.

**Client**

1. Ensure quest log is in game state push or client can call GET /quests; client displays
  active/completed quests in Journal or Quest panel.

**Unit tests (70%+ coverage on new code)**

1. Unit tests: QuestDefinitionRepository, QuestInstanceRepository.
2. Unit tests: QuestService start (triggers, prerequisites DAG), progress (complete_activity,
  kill_N), completion and turn_in (rewards, inventory full blocks), abandon (success, unknown
    name, not active).
3. Unit tests: GET /quests API (401, authenticated response shape).
4. Unit tests: journal/quests and quest abandon command handlers.

**Integration and E2E**

1. Server integration tests: full quest flow (start via trigger, progress, complete or turn-in);
  assert instance state and rewards.
2. Server integration tests: abandon by name; assert state abandoned and re-accept possible; GET
  /quests excludes abandoned from active list.
3. Playwright E2E: one scenario — login, open journal/quests, assert quest list visible and
  reflects server state.

**Documentation**

1. Developer doc: add Quest system section (or ADR) — quest name, goal types, reward types,
  triggers, DAG prerequisites, turn-in rules, abandon command; link to QUEST_SYSTEM_FEATURES.md.
2. Developer doc: add Quest design guidelines (lysator principles — hints, no un-warned death,
  winnable without meta-knowledge, meaningful rewards; avoid syntax quests and grind).

---

## Out of scope (per feature review)

- Repeatable quests (deferred).
- Quest content beyond first quest (only one seed quest required).
- Party/group quest sync (TBD in [docs/PLANNING_ephemeral_grouping.md](e:\projects\GitHub\MythosMUD\docs\PLANNING_ephemeral_grouping.md)).
