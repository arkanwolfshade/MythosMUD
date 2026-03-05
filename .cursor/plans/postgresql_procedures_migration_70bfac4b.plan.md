---
name: PostgreSQL Procedures Migration
overview: Migrate all Python-PostgreSQL interactions to use stored procedures and functions. The codebase uses SQLAlchemy ORM, raw SQL via `text()`, and sync psycopg2 for containers. A big-bang migration will replace all DML/DQL with procedure/function calls, with Python managing transactions.
todos:
  - id: audit-inventory
    content: Create audit spreadsheet of all Python-PostgreSQL touchpoints (session.execute, select, update, merge, delete, text) with proposed proc/func mapping
    status: completed
  - id: audit-group-domains
    content: Group audit results by domain (players, rooms, containers, items, quests, spells, skills, health, npcs, professions, experience, player_effects)
    status: completed
  - id: db-procedures-folder
    content: Create db/procedures/ folder with README.md documenting usage, apply order, and schema notes
    status: completed
  - id: apply-script
    content: Create scripts/apply_procedures.ps1 to apply db/procedures/*.sql to target databases (follow apply_coc_spells_migration.ps1 pattern)
    status: completed
  - id: makefile-apply-procedures
    content: Add apply-procedures Makefile target and make build depend on it
    status: completed
  - id: proc-players
    content: Create db/procedures/players.sql with get_player_by_id, get_player_by_name, upsert_player, soft_delete_player, delete_player, update_player_last_active, get_players_in_room, get_players_batch, etc.
    status: completed
  - id: proc-rooms
    content: Create db/procedures/rooms.sql with get_rooms_with_exits, get_room_exits, get_rooms_by_zone_pattern, get_room_by_stable_id, clear_room_map_origins, set_room_map_origin
    status: completed
  - id: proc-containers
    content: Create db/procedures/containers.sql extending existing functions; add fetch_container_items, create_container, get_container, update_container, delete_container
    status: completed
  - id: proc-items
    content: Create db/procedures/items.sql with ensure_item_instance, get_item_instance, and other item-related functions
    status: completed
  - id: proc-quests
    content: Create db/procedures/quests.sql with get_quest_instance, upsert_quest_instance, get_quest_definitions, etc.
    status: completed
  - id: proc-spells
    content: Create db/procedures/spells.sql with spell and player_spell repository functions
    status: completed
  - id: proc-skills
    content: Create db/procedures/skills.sql with skill, player_skill, skill_use_log repository functions
    status: completed
  - id: proc-health
    content: Create db/procedures/health.sql with update_player_determination_points
    status: completed
  - id: proc-npcs
    content: Create db/procedures/npcs.sql with NPCDefinition and NPCSpawnRule CRUD functions
    status: completed
  - id: proc-professions
    content: Create db/procedures/professions.sql with profession repository functions
    status: completed
  - id: proc-experience
    content: Create db/procedures/experience.sql with experience repository functions
    status: completed
  - id: proc-player-effects
    content: Create db/procedures/player_effects.sql with player_effect repository functions
    status: completed
  - id: python-player-repo
    content: Replace PlayerRepository SQLAlchemy/ORM calls with procedure/function invocations
    status: completed
  - id: python-room-repo
    content: Replace RoomRepository and async_persistence room cache with procedure calls
    status: completed
  - id: python-container-repo
    content: Replace ContainerRepository and container_persistence_async with procedure calls
    status: completed
  - id: python-item-repo
    content: Replace ItemRepository and item_instance_persistence with procedure calls
    status: completed
  - id: python-quest-repos
    content: Replace QuestInstanceRepository and QuestDefinitionRepository with procedure calls
    status: completed
  - id: python-spell-repos
    content: Replace SpellRepository and PlayerSpellRepository with procedure calls
    status: completed
  - id: python-skill-repos
    content: Replace SkillRepository, PlayerSkillRepository, SkillUseLogRepository with procedure calls
    status: completed
  - id: python-health-repo
    content: Replace HealthRepository raw SQL with procedure calls
    status: completed
  - id: python-npc-service
    content: Replace NpcService ORM calls with procedure calls
    status: completed
  - id: python-remaining-repos
    content: Replace ProfessionRepository, ExperienceRepository, PlayerEffectRepository with procedure calls
    status: completed
  - id: python-maps-api
    content: Replace api/maps.py and api/map_helpers.py raw SQL with procedure calls
    status: completed
  - id: schema-aware-calls
    content: Ensure all Python calls use schema-qualified names or correct search_path for mythos_unit/mythos_e2e/mythos_dev
    status: completed
  - id: test-existing
    content: Run make test and make test-comprehensive; fix any failures from repository changes
    status: completed
  - id: test-procedures
    content: Add unit tests that call procedures/functions directly and verify return shape and data
    status: completed
  - id: integrate-test-dbs
    content: Wire apply-procedures into setup-postgresql-test-db or test targets for mythos_unit and mythos_e2e
    status: completed
  - id: adr
    content: Write ADR documenting procedure/function migration decision and approach
    status: completed
  - id: cleanup
    content: Remove or deprecate postgres_adapter.py if unused; optionally trim SQLAlchemy ORM mappings
    status: completed
isProject: false
---

# PostgreSQL Procedures and Functions Migration Plan

## Current State Summary

The codebase has a **mixed** persistence layer:

1. **SQLAlchemy ORM (async)** - Repositories use `select()`, `update()`, `session.merge()`, `session.delete()`:
  - [server/persistence/repositories/player_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\player_repository.py)
  - [server/persistence/repositories/player_spell_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\player_spell_repository.py)
  - [server/persistence/repositories/quest_instance_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\quest_instance_repository.py)
  - [server/persistence/repositories/quest_definition_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\quest_definition_repository.py)
  - [server/persistence/repositories/health_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\health_repository.py)
  - [server/persistence/repositories/spell_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\spell_repository.py)
  - [server/persistence/repositories/skill_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\skill_repository.py)
  - [server/persistence/repositories/experience_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\experience_repository.py)
  - [server/persistence/repositories/player_effect_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\player_effect_repository.py)
  - [server/persistence/repositories/profession_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\profession_repository.py)
  - [server/persistence/repositories/room_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\room_repository.py)
  - [server/persistence/repositories/item_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\item_repository.py)
  - [server/persistence/repositories/container_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\container_repository.py)
  - [server/services/npc_service.py](e:\projects\GitHub\MythosMUD\server\services\npc_service.py) (NPCDefinition, NPCSpawnRule CRUD)
2. **Raw SQL via `text()`** - Direct DML/DQL in Python:
  - [server/persistence/repositories/health_repository.py](e:\projects\GitHub\MythosMUD\server\persistence\repositories\health_repository.py): `UPDATE players SET determination_points = ...`
  - [server/api/maps.py](e:\projects\GitHub\MythosMUD\server\api\maps.py): `UPDATE rooms SET map_origin_room_id = ...` (clear/set)
  - [server/api/map_helpers.py](e:\projects\GitHub\MythosMUD\server\api\map_helpers.py): `SELECT` for exits, rooms by pattern, room by stable_id
  - [server/async_persistence.py](e:\projects\GitHub\MythosMUD\server\async_persistence.py): `_query_rooms_with_exits_async` - large `text()` SELECT with JSON aggregation
  - [server/persistence/container_persistence_async.py](e:\projects\GitHub\MythosMUD\server\persistence\container_persistence_async.py): SELECT, INSERT, UPDATE for containers/container_contents (partially uses existing functions: `clear_container_contents`, `add_item_to_container`)
3. **Sync psycopg2** - [server/persistence/container_persistence.py](e:\projects\GitHub\MythosMUD\server\persistence\container_persistence.py) uses raw SQL via `conn` (psycopg2). PostgresConnection is only used in tests.
4. **Existing PostgreSQL functions** (already in [db/mythos_unit_ddl.sql](e:\projects\GitHub\MythosMUD\db\mythos_unit_ddl.sql)):
  - `add_item_to_container`, `clear_container_contents`, `get_container_contents_json`, `remove_item_from_container`

---

## Phase 1: Audit and Inventory

### 1.1 Create Audit Spreadsheet

Produce a CSV or markdown table listing:


| Domain  | File                 | Operation        | Current Implementation | Proposed Proc/Func                                  |
| ------- | -------------------- | ---------------- | ---------------------- | --------------------------------------------------- |
| Players | player_repository.py | get_player_by_id | SQLAlchemy select      | `get_player_by_id(p_id UUID) RETURNS SETOF players` |
| Players | player_repository.py | save_player      | session.merge          | `upsert_player(...)` PROCEDURE                      |
| ...     | ...                  | ...              | ...                    | ...                                                 |


**Audit scope**: Every `session.execute()`, `select()`, `update()`, `session.merge()`, `session.delete()`, and `text()` call that touches PostgreSQL.

### 1.2 Group by Domain

- **Players**: PlayerRepository, PlayerInventory, player_inventories
- **Rooms**: RoomRepository, async_persistence room cache, map_helpers, maps API
- **Containers**: ContainerRepository, container_persistence_async, container_persistence (sync)
- **Items**: ItemRepository, item_instance_persistence_async
- **Quests**: QuestInstanceRepository, QuestDefinitionRepository
- **Spells**: SpellRepository, PlayerSpellRepository
- **Skills**: SkillRepository, PlayerSkillRepository, SkillUseLogRepository
- **Health/Combat**: HealthRepository (determination_points)
- **NPCs**: NpcService (NPCDefinition, NPCSpawnRule)
- **Professions**: ProfessionRepository
- **Experience**: ExperienceRepository
- **Player Effects**: PlayerEffectRepository

---

## Phase 2: Procedure/Function Design

### 2.1 Naming and Placement

- **Schema**: Use existing `mythos_unit`, `mythos_e2e`, `mythos_dev` (per-environment DDL).
- **Naming**: `verb_entity` (e.g. `get_player_by_id`, `upsert_player`, `update_player_determination_points`).
- **Pragmatic choice**:
  - **FUNCTION** for single-row/aggregate returns (e.g. `get_player_by_id` returns row, `get_rooms_by_zone` returns SETOF).
  - **PROCEDURE** for multi-statement mutations with OUT params (e.g. `create_container` with OUT container_id).

### 2.2 Transaction Model

- Python starts transaction via `async with session.begin()` or `session.commit()`.
- Procedures/functions do **not** manage transactions; they run within the session's transaction.
- Use `session.execute(text("SELECT * FROM get_player_by_id(:id)"), {"id": player_id})` or `session.execute(text("CALL upsert_player(...)"), params)`.

### 2.3 Procedure Storage and Build Integration

**Storage location**: All procedure and function definitions live under `db/procedures/`:

```
db/
  procedures/
    README.md           # Usage, apply order, schema notes
    players.sql         # get_player_by_id, upsert_player, etc.
    rooms.sql           # get_rooms_with_exits, get_room_exits, etc.
    containers.sql      # Extend existing; add fetch_container_items, create_container, etc.
    items.sql
    quests.sql
    spells.sql
    skills.sql
    health.sql          # update_player_determination_points
    npcs.sql
    professions.sql
    experience.sql
    player_effects.sql
```

- One `.sql` file per domain; each file contains `CREATE OR REPLACE FUNCTION` / `CREATE OR REPLACE PROCEDURE` statements.
- Files use schema-qualified names or a `SET search_path` preamble so they apply to mythos_unit, mythos_e2e, mythos_dev.

**Build integration**: Procedures are applied to database schemas as part of `make build`:

1. **New Makefile target** `apply-procedures` (or similar) that runs a PowerShell script to apply all files in `db/procedures/` to configured databases.
2. **Extend `make build`** to depend on `apply-procedures` before the client build, or run both in sequence. Current `build` runs `scripts/build.py` (client npm build only).
3. **Apply script** (e.g. `scripts/apply_procedures.ps1`):
  - Reads `DATABASE_URL` from `.env.local` or `.env` (dev) or `.env.unit_test` (tests).
  - Parses target database(s) from env or a parameter (e.g. `-TargetDbs mythos_dev` for build, or mythos_unit/mythos_e2e for tests).
  - Runs `psql -f db/procedures/<file>.sql` for each file in dependency order (e.g. base tables before dependent procedures).
  - Follows the pattern of [scripts/apply_coc_spells_migration.ps1](e:\projects\GitHub\MythosMUD\scripts\apply_coc_spells_migration.ps1) for connection parsing and psql invocation.
4. **Makefile change**:

```makefile
   build: apply-procedures
   	$(PYTHON) scripts/build.py

   apply-procedures:
   	$(POWERSHELL) scripts/apply_procedures.ps1 -TargetDbs mythos_dev


```

- For CI/test flows, `apply-procedures` may be run separately with `-TargetDbs mythos_unit mythos_e2e` (e.g. from `setup-postgresql-test-db` or test targets).
- If database is unavailable during `make build`, the script can exit gracefully (or fail fast, per project preference).

1. **Execution order**: Procedures that depend on tables must run after DDL. Recommended order: (1) DDL via `mythos_<env>_ddl.sql`, (2) DML seed data, (3) `apply-procedures`. Ensure `make build` runs after DB exists, or document that `setup-postgresql-test-db` (or equivalent) must run first.

### 2.4 Procedure/Function List (Draft)

Based on audit, create procedures/functions for:

**Players**

- `get_player_by_id`, `get_player_by_name`, `get_players_by_user_id`, `get_active_players_by_user_id`
- `upsert_player`, `save_players` (batch)
- `soft_delete_player`, `delete_player`
- `update_player_last_active`, `update_player_determination_points` (from health_repository)
- `get_players_in_room`, `get_players_batch`

**Rooms**

- `get_rooms_with_exits` (replaces `_query_rooms_with_exits_async`)
- `get_room_exits`, `get_rooms_by_zone_pattern`, `get_room_by_stable_id` (map_helpers)
- `clear_room_map_origins`, `set_room_map_origin` (maps API)

**Containers** (extend existing)

- `fetch_container_items` (replace raw SELECT in container_persistence_async)
- `create_container` (replace raw INSERT; may keep Python validation)
- `get_container`, `update_container`, `delete_container`

**Items**

- `ensure_item_instance`, `get_item_instance`, etc.

**Quests**

- `get_quest_instance`, `upsert_quest_instance`, `get_quest_definitions`, etc.

**Spells, Skills, Experience, Effects, Professions, NPCs**

- One function/procedure per repository method that performs DB I/O.

---

## Phase 3: Implementation

### 3.1 Procedure Files and Build Integration

- Create procedure/function definitions in `db/procedures/` (see Section 2.3).
- Each file: `CREATE OR REPLACE FUNCTION ...` / `CREATE OR REPLACE PROCEDURE ...`.
- Create `scripts/apply_procedures.ps1` to apply all files in `db/procedures/` to target databases.
- Extend `make build` to run `apply-procedures` before the client build; procedures are applied to mythos_dev (or configured DB) as part of build.
- For test databases (mythos_unit, mythos_e2e), procedures are applied via `setup-postgresql-test-db` or test targets (see [scripts/apply_coc_spells_migration.ps1](e:\projects\GitHub\MythosMUD\scripts\apply_coc_spells_migration.ps1) pattern).

### 3.2 Python Changes

- Replace SQLAlchemy ORM calls with `session.execute(text("SELECT * FROM schema.func_name(:p1, :p2)"), params)`.
- Replace `session.merge()` with `CALL upsert_entity(...)` or equivalent function.
- Map result rows to domain objects (Player, Room, etc.) in Python; procedures return rows/sets.
- Keep repository interfaces unchanged where possible (same method signatures, different implementation).

### 3.3 Schema-Aware Calls

- Use `SET search_path = mythos_unit` or fully-qualified names (`mythos_unit.get_player_by_id`) so procedures work across environments.
- Ensure `get_session_maker()` and `get_async_session()` use the correct schema.

---

## Phase 4: Testing

### 4.1 Existing Tests

- Run `make test` and `make test-comprehensive` after each domain migration.
- Existing unit and integration tests should continue to pass if repository behavior is preserved.

### 4.2 New SQL Migration Tests

- Add tests in `server/tests/` that:
  - Call procedures/functions directly via `session.execute(text("SELECT * FROM mythos_unit.get_player_by_id(:id)"), {"id": test_uuid})`.
  - Verify return shape and data.
- Optionally: pgTAP or SQL unit tests in `db/tests/` if the project adopts them.

### 4.3 Rollback Strategy (Big Bang)

- Single migration branch; rollback = revert commit and re-run previous schema.
- Consider a feature flag to switch between "raw SQL" and "procedure" paths during development (optional, adds complexity).

---

## Phase 5: Cutover and Cleanup

1. Deploy procedure/function migrations to all environments.
2. Deploy Python changes in one release.
3. Remove unused SQLAlchemy ORM mappings for tables that are now procedure-only (optional; some may remain for Alembic).
4. Deprecate or remove `postgres_adapter.py` if no longer used (currently only in tests).

---

## Risks and Mitigations


| Risk                       | Mitigation                                                                               |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| Large change surface       | Big-bang increases risk; thorough audit and staged testing per domain before final merge |
| ORM removal breaks Alembic | Keep models for DDL migrations; use procedures only for DML/DQL                          |
| Performance regression     | Procedures can reduce round-trips; benchmark critical paths                              |
| Schema drift               | Procedures must be updated when tables change; add to migration checklist                |


---

## Deliverables

1. **Audit document**: Full inventory of Python-PostgreSQL touchpoints and proposed procedure/function mapping.
2. **Procedure definitions**: SQL files in `db/procedures/` creating all procedures and functions (one file per domain).
3. **Build integration**: `scripts/apply_procedures.ps1` and Makefile updates so `make build` applies procedures to database schemas.
4. **Updated Python code**: Repositories and services calling procedures instead of raw SQL/ORM.
5. **Test updates**: Any new tests for procedures; ensure existing tests pass.
6. **ADR**: Document the decision to use procedures/functions and the migration approach (per [mythosmud-adr-authoring](e:\projects\GitHub\MythosMUD.cursor\skills\mythosmud-adr-authoring\SKILL.md)).
