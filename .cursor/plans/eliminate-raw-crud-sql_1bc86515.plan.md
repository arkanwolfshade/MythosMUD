---
name: eliminate-raw-crud-sql
overview: Refactor Python-side raw CRUD SQL to use PostgreSQL functions/procedures for rooms, players, skills, and related repositories, in line with the project’s procedures-first architecture.
todos:
  - id: docs-no-select-star
    content: Update CLAUDE.md and ADR-015 to state that all CRUD logic must live in PostgreSQL functions/procedures, and adjust examples away from raw table SQL.
    status: completed
  - id: rooms-procedure-refactor
    content: Verify or introduce get_rooms_with_exits() procedure and ensure async_persistence_room_loader.py only calls the procedure, not tables.
    status: completed
  - id: players-procedure-refactor
    content: Refactor player_repository.py to call dedicated player procedures (get_player_by_id, list_players, etc.) and remove all raw table SQL.
    status: completed
  - id: effects-containers-procedure-refactor
    content: Refactor container_persistence_async.py and player_effect_repository.py to use container/effect procedures instead of direct table SQL.
    status: completed
  - id: quests-skills-procedure-refactor
    content: Refactor quest and skill repositories (quest_definition_repository, quest_instance_repository, skill_repository, skill_use_log_repository, player_skill_repository) to use dedicated procedures.
    status: completed
  - id: spells-procedure-refactor
    content: Refactor spell_repository and player_spell_repository to use get_all_spells, get_spell_by_id, and player-spell procedures, updating SpellRegistry as needed.
    status: completed
  - id: npc-procedure-refactor
    content: Ensure all NPC-related operations in npc_service.py call only functions from db/procedures/npcs.sql and remove raw table SQL.
    status: completed
  - id: integration-tests-update
    content: Align test_procedures_return_shape.py and related integration tests with the new function-based CRUD API, keeping them free of direct table SQL.
    status: completed
  - id: lint-enforcement
    content: Add a Semgrep or similar rule to forbid new raw CRUD SQL in Python (SELECT/INSERT/UPDATE/DELETE on tables), allowing only procedure/function calls.
    status: completed
isProject: false
---

# Eliminate Raw CRUD SQL From Python

### Goals

- **Remove all raw CRUD SQL** (direct table SELECT/INSERT/UPDATE/DELETE) from Python code.
- **Centralize CRUD logic in PostgreSQL functions/procedures**, so Python only calls stable, versioned database APIs.
- Keep behavior and test coverage intact while aligning with existing `db/procedures/*.sql` patterns.

### 1. Clarify Allowed Patterns

- **Allowed in Python:**
  - Calling PostgreSQL functions/procedures via `SELECT` or `CALL`, **with explicit column lists**:
    - `session.execute(text("SELECT col1, col2 FROM schema_name.function_name(:params)"), params)` for set-returning functions.
    - `session.execute(text("SELECT schema_name.function_name(:params)"), params)` or `CALL` where appropriate when the function returns a scalar or is used for side effects.
- **Not allowed in Python:**
  - Direct `SELECT ... FROM table`/`UPDATE table`/`INSERT INTO table`/`DELETE FROM table` in application code or repositories.
  - `SELECT` * in any SQL issued from Python (even when selecting from a function/procedure); column lists **must** be explicit for defensive coding.
- **Docs update (first step):**
  - Update `[CLAUDE.md](CLAUDE.md)` and `[docs/architecture/decisions/ADR-015-postgresql-procedures-migration.md](docs/architecture/decisions/ADR-015-postgresql-procedures-migration.md)` to clearly state:
    - "All CRUD logic lives in PostgreSQL functions/procedures; Python only calls those functions."
    - All examples must use **explicit column lists** in `SELECT` statements; no `SELECT` * anywhere in application or repository code.

### 2. Room Loader: Move CRUD to Procedures

- **Current code:** `[server/async_persistence_room_loader.py](server/async_persistence_room_loader.py)` calls `text("SELECT * FROM get_rooms_with_exits()")` directly.
- **Plan:**
  - Confirm existing function in `[db/procedures/rooms.sql](db/procedures/rooms.sql)` (or equivalent) that encapsulates this query. If absent, add:
    - A `get_rooms_with_exits()` function that returns exactly the columns used by the loader.
  - Refactor loader to **only call the function**, not refer to any tables:
    - Change the call to use an explicit column list, for example `text("SELECT room_id, zone_id, exit_id, ... FROM get_rooms_with_exits()")`, so the query remains function-based but column-safe (no `SELECT` *).
  - Add or update integration tests in `[server/tests/integration/test_procedures_return_shape.py](server/tests/integration/test_procedures_return_shape.py)` to validate the procedure’s shape.

### 3. Player Repository: Wrap All CRUD in Procedures

- **Targets:** `[server/persistence/repositories/player_repository.py](server/persistence/repositories/player_repository.py)` and related constants in `[server/async_persistence_constants.py](server/async_persistence_constants.py)`.
- **Plan:**
  - Inventory all table-oriented functions: `get_player_by_name`, `get_player_by_id`, `get_players_by_user_id`, `get_active_players_by_user_id`, `list_players`, `get_players_in_room`, `get_players_batch`, and any update/insert helpers.
  - For each, either:
    - Confirm existing PostgreSQL function in `[db/procedures/players.sql](db/procedures/players.sql)` (or similar), or
    - Introduce a new function (e.g., `get_player_by_name(name text)`, `list_players()`, `get_players_in_room(room_id uuid)`) that returns the full player row or a stable projection.
  - Refactor repository methods to **call only these functions** via `session.execute(text("SELECT * FROM schema.get_player_by_id(:id)"), {"id": ...})` or similar, removing direct table references.
  - Keep `async_persistence_constants.py` as the single place documenting column sets, but treat it as reference, not as raw SQL assembler.
  - Update or add unit tests around the repository to ensure mappings still behave identically.

### 4. Container & Effect Repositories

- **Targets:**
  - `[server/persistence/container_persistence_async.py](server/persistence/container_persistence_async.py)` – `fetch_container_items`, `get_container`.
  - `[server/persistence/repositories/player_effect_repository.py](server/persistence/repositories/player_effect_repository.py)` – `get_active_effects_for_player`, `get_effects_expiring_this_tick`.
- **Plan:**
  - For each table-level query, design or confirm a **dedicated function** in `db/procedures/containers.sql` and `db/procedures/effects.sql` (names illustrative) that returns the needed rows.
  - Replace the Python SQL with a call to the new function, eliminating any remaining `FROM container_items`, `FROM effects`, etc. from Python.
  - Extend `test_procedures_return_shape` (or add new integration tests) to assert the result shapes of these new functions.

### 5. Quests & Skills Repositories

- **Targets:**
  - `[server/persistence/repositories/quest_definition_repository.py](server/persistence/repositories/quest_definition_repository.py)`.
  - `[server/persistence/repositories/quest_instance_repository.py](server/persistence/repositories/quest_instance_repository.py)`.
  - `[server/persistence/repositories/skill_repository.py](server/persistence/repositories/skill_repository.py)`.
  - `[server/persistence/repositories/skill_use_log_repository.py](server/persistence/repositories/skill_use_log_repository.py)`.
  - `[server/persistence/repositories/player_skill_repository.py](server/persistence/repositories/player_skill_repository.py)`.
- **Plan:**
  - For each repo method that currently uses table SQL, define a **single, clearly named function** in the appropriate `db/procedures/*.sql` file:
    - e.g., `get_quest_definition_by_id(quest_id uuid)`, `list_active_quest_instances_by_player(player_id uuid)`, `get_all_skills()`, `get_skill_by_id(skill_id uuid)`, `get_player_skills_with_skill(player_id uuid)`.
  - Ensure functions return the row shape that the Python layer expects (consult existing models/DTOs).
  - Replace the repo’s `SELECT * FROM table` calls with `SELECT * FROM schema.func_name(:params)` calls.
  - Adjust any shape-sensitive tests to validate the functions instead of tables.

### 6. Spells & Player Spells

- **Targets:**
  - `[server/persistence/repositories/spell_repository.py](server/persistence/repositories/spell_repository.py)`.
  - `[server/persistence/repositories/player_spell_repository.py](server/persistence/repositories/player_spell_repository.py)`.
  - `[server/game/magic/spell_registry.py](server/game/magic/spell_registry.py)` (call site only).
- **Plan:**
  - Ensure `[db/procedures/spells.sql](db/procedures/spells.sql)` exposes functions like `get_all_spells()` and `get_spell_by_id(spell_id uuid)` **as the sole API** to the spells table.
  - Similarly, add or confirm player-spell functions (`get_player_spells`, `get_player_spell`, `learn_spell`).
  - Refactor repositories to call only these functions; no table names left in Python.
  - Keep `SpellRegistry.load_spells()` unchanged in behavior, but verify it consumes the new function outputs correctly.

### 7. NPC Procedures & Statistics

- **Targets:** `[server/services/npc_service.py](server/services/npc_service.py)`.
- **Plan:**
  - For all NPC-related queries (`get_npc_definitions`, `get_npc_definition`, `get_spawn_rules`, `get_spawn_rule`, creation/update functions, `get_npc_system_statistics`), ensure a corresponding function exists in `[db/procedures/npcs.sql](db/procedures/npcs.sql)` and is the **only** interface to NPC tables.
  - Confirm the function definitions (already present for many) fully encapsulate the raw SQL.
  - Update `npc_service` so every `session.execute` references only functions (`SELECT * FROM schema.get_npc_definitions_by_type(:npc_type)` etc.) and not base tables.
  - Align unit tests in `[server/tests/unit/services/test_npc_service.py](server/tests/unit/services/test_npc_service.py)` to mock/probe these function outputs rather than table structures.

### 8. Tests & Diagnostics

- **Integration tests:**
  - `[server/tests/integration/test_procedures_return_shape.py](server/tests/integration/test_procedures_return_shape.py)` should also use **explicit column lists** when selecting from functions (no `SELECT` *), while continuing to validate function result shapes.
- **Docs:**
  - After refactors, update `docs/postgresql_procedures_audit.md` to reflect that all Python-accessible CRUD is through functions and that `SELECT` statements use explicit columns.

### 9. Validation & Regression Checks

- For each refactor batch (players, skills, spells, NPCs, etc.):
  - Run targeted unit tests for the affected repositories/services.
  - Run `pytest server/tests/integration/test_procedures_return_shape.py`.
  - Run `make test-ci` (or at least `make test`) to catch cross-module issues.
  - Run `uv run pre-commit run mypy --all-files` and pylint on changed files.

### 10. Enforcement Going Forward

- Add a **linting/grep-based guard** as a final step:
  - Semgrep (or similar) rule that forbids **direct table CRUD** and `SELECT` * in app code:
    - Disallow `SELECT ... FROM <table>` / `INSERT INTO <table>` / `UPDATE <table>` / `DELETE FROM <table>`.
    - Disallow `SELECT` * in any SQL issued from Python (including `SELECT * FROM schema.function_name(...)`); require explicit column lists instead.
  - Treat any new direct table CRUD or `SELECT` * as a CI failure, forcing new work to go through PostgreSQL functions/procedures with explicit projections.
