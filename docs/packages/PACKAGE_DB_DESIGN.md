# db/ Package Design

**Version 1.0.0** · MythosMUD · 2026-09-16

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`db/` is the schema-agnostic PostgreSQL definition for all three MythosMUD environments
(`mythos_dev` / `mythos_unit` / `mythos_e2e`, #811) — the **noun** to
[`DATABASE_ARCHITECTURE.md`](../architecture/DATABASE_ARCHITECTURE.md)'s **verb** (how Python reaches
this schema). Reverse-engineered from `db/schema.sql`; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md)). Written to close
[`#745`](https://github.com/arkanwolfshade/MythosMUD/issues/745), which originally named three
per-environment DDL files (`mythos_dev_ddl.sql` etc.) retired by #811 — see
[`db/LEGACY_FILES.md`](../../db/LEGACY_FILES.md).

## 2. Members

**[SPEC]**

| Path | Role | Versioned as |
| --- | --- | --- |
| `db/schema.sql` | The DDL baseline — all 45 tables, indexes, constraints. Object names unqualified; loader must `SET search_path` first. | Committed, regenerated wholesale via `scripts/generate_schema_from_dev.ps1` |
| `db/migrations/` | dbmate migrations applied **after** the baseline, in filename order, tracked per-database in `schema_migrations` | Incremental ledger, via `scripts/migrate.ps1` |
| `db/procedures/*.sql` | Stored procedures/functions — the intended sole path for Python↔PostgreSQL data access (ADR-015) | Idempotent `CREATE OR REPLACE`, reapplied wholesale, not incremental history |
| `db/databases/databases.sql` | Creates the three databases, `pgcrypto`, UTC timezone, access grants | Run once per environment, idempotent |
| `db/roles/roles.sql` | Creates the PostgreSQL roles/owners per environment | Run once per environment, idempotent |
| `data/db/seed.sql` (data submodule) | Static world seed — loaded with `search_path` set, alongside `schema.sql` | Reapplied wholesale by `scripts/load_world_seed.py`, **destructive** (drops all tables first) |
| `db/corruption_adjustment_log.sql` | Loose file at `db/` root — see §3 note | Unclear; not part of the composition order below |

## 3. Composition — how a database gets built

**[SPEC]**
Execution order (`db/databases/README.md`'s "Execution Order", `db/README.md` §"Usage in CI/CD"):

```
1. db/roles/roles.sql          — create owner roles           (once, per environment)
2. db/databases/databases.sql  — create DBs + pgcrypto         (once, per environment)
3. db/schema.sql                — apply DDL (search_path set)  (fresh DB only, destructive re-apply)
4. data/db/seed.sql              — apply static world seed      (fresh DB only, destructive re-apply)
5. db/procedures/*.sql           — apply stored procs/funcs     (every build/test run — make apply-procedures)
6. db/migrations/                — apply dbmate ledger          (every run — see §4)
```

Steps 1–2 are idempotent and safe to re-run. Steps 3–4 are **not** — `load_world_seed.py`'s own
banner states it drops every table; it is gated on `CONFIRM_LOAD_WORLD_SEED=1` and its allow-list
covers all three environments. Step 5 is idempotent (`CREATE OR REPLACE`). Step 6 is additive-only —
see §4.

**[NOTE]** `db/corruption_adjustment_log.sql` at `db/` root does not appear in this composition order
and is not a schema/migration/procedure file in the sense of the rows above — flagged here rather than
silently omitted, since its purpose relative to the `corruption_adjustment_log` table
(`db/schema.sql:3562`) was not established during this pass.

## 4. Migration currency by environment

**[SPEC]**
| Database | Reconverges when | Mechanism |
| --- | --- | --- |
| `mythos_e2e` | Every E2E run | `bootstrap_e2e_database.ps1` → `migrate.ps1 -Environment e2e` |
| `mythos_unit` | Every server-test run | `Makefile` test targets → `migrate.ps1 -Environment unit` |
| `mythos_dev` | Every `start_local.ps1` run | `scripts/start_server.ps1`'s Step 3.5 → `migrate.ps1 -Environment dev` (#864) |

`scripts/migrate.ps1` restricts its verb to `up`/`status` — there is no reachable path through it that
drops, truncates, or rolls anything back, which is what makes automatic triggering at server start
safe against `mythos_dev` (PROTECTED, see `.claude/rules/database.md`). See
[`db/migrations/README.md`](../../db/migrations/README.md) for the full mechanism.

## 5. Data model

**[SPEC]**
45 tables, grouped by domain. FK edges only — no column lists; those live in `db/schema.sql` and a
duplicated copy here would have no CI gate keeping it current (see §8's roster gate for what *is*
checked). Regenerate this table with `grep -nE '^CREATE TABLE' db/schema.sql` if it looks stale.

| Domain | Tables | Key FK edges |
| --- | --- | --- |
| Identity & auth | `users`, `id_map_users`, `id_map_players`, `invites`, `account_sanctions`, `muting_rules` | `id_map_players.user_uuid → users`, `invites.created_by_user_id/used_by_user_id → users`, `account_sanctions.user_id → users`, `account_sanctions.issued_by_player_id/lifted_by_player_id → players` |
| Player core | `players`, `player_channel_preferences`, `player_inventories`, `player_exploration` | `players.user_id → users`; the rest → `players.player_id`, cascade on delete |
| World | `zones`, `subzones`, `rooms`, `room_links`, `zone_configurations`, `calendar_holidays`, `calendar_npc_schedules` | `subzones.zone_id → zones`, `rooms.subzone_id → subzones`, `room_links.from_room_id/to_room_id → rooms`, `zone_configurations.zone_id/subzone_id → zones/subzones` |
| Items & containers | `item_prototypes`, `item_instances`, `item_component_states`, `containers`, `container_contents` | `item_instances.prototype_id → item_prototypes`, `containers.entity_id/owner_id → players`, `container_contents.container_id/item_instance_id → containers/item_instances` |
| NPC & dialogue | `npc_definitions`, `npc_relationships`, `npc_spawn_rules`, `dialogue_definitions` | `npc_relationships.npc_id_1/npc_id_2 → npc_definitions`, `dialogue_definitions.npc_definition_id → npc_definitions` |
| Quests | `quest_definitions`, `quest_instances`, `quest_offers` | `quest_instances.player_id/quest_id → players/quest_definitions`, `quest_offers.quest_id → quest_definitions` |
| Skills & spells | `skills`, `player_skills`, `skill_use_log`, `spells`, `player_spells` | `player_skills.player_id/skill_id → players/skills`, `player_spells.player_id/spell_id → players/spells` |
| Effects, corruption & lucidity | `player_effects`, `corruption_adjustment_log`, `corruption_cooldowns`, `player_lucidity`, `lucidity_adjustment_log`, `lucidity_cooldowns`, `lucidity_exposure_state` | All keyed off `players.player_id`, cascade on delete |
| Social & chat | `aliases`, `emotes`, `emote_aliases` | `emote_aliases.emote_id → emotes` |
| Standalone / reference | `professions`, `calendar_holidays`, `calendar_npc_schedules`, `aliases`, `id_map_users` | No FK in or out — lookup/reference tables |

## 6. Invariants and where they live

**[SPEC]**
Every table-level invariant here is one of three things — recorded so a reader doesn't have to guess
which:

- **CHECK constraints** — enforced by PostgreSQL itself, cannot be bypassed by application code.
  Examples: `player_lucidity_current_lcd_check` (−100 to 100), `containers_capacity_slots_check`
  (1–20), `player_skills_value_check`/`player_spells_mastery_check` (0–100), enum-style `ANY (ARRAY[...])`
  checks on `sanction_type`, `lock_state`, `npc_type`, `relationship_type`, `quest_instances.state`,
  `spells.school`/`range_type`/`target_type`, and the shared `environment` vocabulary reused across
  `rooms`/`subzones`/`zones` (`chk_*_environment`).
- **FOREIGN KEY constraints** — referential integrity, `ON DELETE CASCADE` on nearly every
  player-owned table (§5) so deleting a player cleans up its effects/lucidity/inventory/skills/spells
  rows; `SET NULL` where the reference is informational (e.g. `containers.owner_id`,
  `account_sanctions.issued_by_player_id`); `RESTRICT` on `room_links.to_room_id` (a room cannot be
  deleted while something still links to it).
- **Stored procedures** (`db/procedures/*.sql`) — business-rule invariants that span rows or need
  transactional atomicity (e.g. `containers.sql`'s capacity checks, `item_catalog.sql`'s
  `list_item_prototypes_page`). ADR-015 is the source of truth for which procedure owns which table's
  write path — not re-derived here.
- **Application code** — anything not enforced by the three above is, by construction, *not*
  guaranteed at the database level. Treat any invariant not listed here as an application-level
  convention until proven otherwise.

## 7. Developer guide

**[NOTE]**

- **Changing the schema**: edit `mythos_dev` directly (dev workflow), then
  `.\scripts\generate_schema_from_dev.ps1` to regenerate `db/schema.sql`, or add a dbmate migration
  under `db/migrations/` for anything past the baseline — see
  [`db/migrations/README.md`](../../db/migrations/README.md) §"Adding a migration".
- **Provisioning `mythos_dev` from scratch**: the sequence in §3, with `CONFIRM_LOAD_WORLD_SEED=1`
  before step 4. See [`CONTRIBUTING.md`](../../CONTRIBUTING.md) and
  [`docs/DEVELOPMENT.md`](../DEVELOPMENT.md) for the runnable command sequence.
- **Adding a new table**: add it to `db/schema.sql` (or a migration), regroup it into §5's domain
  table here, and add its FK edges. If it has no FK in or out, it belongs in the "Standalone /
  reference" row.
- **Adding a new write path**: goes in `db/procedures/*.sql`, not inline SQL in Python — enforced,
  see [`DATABASE_ARCHITECTURE.md`](../architecture/DATABASE_ARCHITECTURE.md) §5.

## 8. Roster gate

**[SPEC]**
`server/tests/unit/infrastructure/test_db_design_table_roster.py` extracts every `CREATE TABLE` name
from `db/schema.sql` and every table name from this document's §5, and asserts the two sets match. It
runs under `pyproject.toml`'s `testpaths = ["server/tests"]`, so it is collected by ordinary `pytest`
and `make test` runs — no new script, Makefile target, or CI job. A table added to `db/schema.sql`
without a corresponding §5 update fails this test.

## 9. Troubleshooting

**[NOTE]**

- **"schema drift" from `make verify-schema`**: that check compares `db/schema.sql` against a live
  database's DDL, not this document. See
  [`db/README.md`](../../db/README.md) §"Verification" for its scope (table/column DDL only, not
  procedure bodies or dbmate ledger currency).
- **New table missing from this doc**: run the roster gate (§8) locally — `pytest
  server/tests/unit/infrastructure/test_db_design_table_roster.py` — to confirm before assuming it's
  just stale prose.
- **Confusion about where a write-path invariant lives**: work through §6's three buckets in order
  (CHECK → FK → procedure) before assuming it's enforced only in application code.

## 10. Related docs

**[SPEC]**

- [`DATABASE_ARCHITECTURE.md`](../architecture/DATABASE_ARCHITECTURE.md) — the access-layer
  counterpart to this data model.
- [`docs/packages/PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md) — the SQLAlchemy ORM entities
  mapped onto these tables.
- [ADR-006](../architecture/decisions/ADR-006-postgresql-primary-datastore.md) — PostgreSQL as
  primary datastore.
- [ADR-015](../architecture/decisions/ADR-015-postgresql-procedures-migration.md) — procedures as
  the data-access boundary; owns `db/procedures/`.
- [`db/README.md`](../../db/README.md), [`db/LEGACY_FILES.md`](../../db/LEGACY_FILES.md) —
  operational detail (regeneration, verification, what #811 retired) this doc doesn't duplicate.

## 11. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-09-16 | Initial version — closes #745 |
