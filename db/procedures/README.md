# PostgreSQL Procedures and Functions

This directory contains stored procedure and function definitions for MythosMUD. All
Python-PostgreSQL interactions are intended to go through these procedures/functions
instead of raw DML/DQL in application code.

## Developer guidelines

- **All new CRUD operations must use procs/funcs**: When adding or changing persistence
  behavior, define or extend a stored procedure or function in this directory and call
  it from Python. Do not add new inline `INSERT`, `UPDATE`, `DELETE`, or complex
  `SELECT` statements in application code.
- **Python as orchestration, Postgres as authority**: Application code should manage
  transactions and map procedure results to domain objects; PostgreSQL procedures and
  functions own query shape, validation, and data consistency rules.

## Usage

Procedures are applied to database schemas as part of `make build` and during test
setup. Use `scripts/apply_procedures.ps1` to apply manually:

```powershell
# Apply to dev database (default for make build)
.\scripts\apply_procedures.ps1 -TargetDbs mythos_dev

# Apply to test databases
.\scripts\apply_procedures.ps1 -TargetDbs mythos_unit, mythos_e2e
```

## Apply Order

`scripts/apply_procedures.ps1` globs `*.sql` in this directory and applies them in plain
alphabetical order -- there is no separate manifest to keep in sync. `CREATE OR REPLACE
FUNCTION` is order-independent for function-to-function references (Postgres resolves those
at call time), so alphabetical ordering is safe as long as no file's *table* dependencies
(created by DDL/migrations, not by another procedure file) postdate it -- none currently do.
The list below is the actual current directory contents (2026-08-25, #633), documentation
only:

1. `calendar.sql` - calendar_holidays, calendar_npc_schedules (reads only)
2. `containers.sql` - containers, container_contents
3. `dialogues.sql` - dialogue_definitions
4. `emotes.sql` - emotes, emote_aliases (reads only)
5. `experience.sql` - players table updates
6. `exploration.sql` - player_exploration, coordinate-generation reads over rooms/subzones/zones
7. `health.sql` - players table updates (depends on players from DDL)
8. `items.sql` - item_prototypes, item_instances
9. `lucidity.sql` - zones/subzones special_rules reads
10. `npcs.sql` - npc_definitions, npc_spawn_rules, zone/subzone config reads
11. `player_effects.sql` - player_effects
12. `players.sql` - users, players, player_inventories, invites
13. `professions.sql` - professions
14. `quests.sql` - quest_definitions, quest_offers, quest_instances
15. `rooms.sql` - rooms, room_links, subzones, zones
16. `skills.sql` - skills
17. `spells.sql` - spells

## Schema Notes

- Each environment uses a schema matching the database name: `mythos_unit`,
  `mythos_e2e`, `mythos_dev`.
- Procedure files must set `search_path` or use fully-qualified names
  (`schema_name.function_name`) so they apply correctly to the target schema.
- The apply script runs each file with `-v schema_name=<target_db>` so procedures
  can use `:schema_name` in `CREATE OR REPLACE FUNCTION schema_name.func_name`.

## File Format

Each `.sql` file contains one or more:

```sql
CREATE OR REPLACE FUNCTION schema_name.function_name(...) RETURNS ... AS $$
  ...
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE schema_name.procedure_name(...) AS $$
  ...
$$ LANGUAGE plpgsql;
```

Use `CREATE OR REPLACE` for idempotent application; the script can be run
multiple times safely.

## Moved from DDL

The following functions were moved from `db/mythos_*_ddl.sql` into `containers.sql`:

- `add_item_to_container`
- `clear_container_contents`
- `get_container_contents_json`
- `remove_item_from_container`

They are now applied via `apply_procedures.ps1` alongside other container procedures.

## References

- Audit: `docs/postgresql_procedures_audit.md`
- Plan: PostgreSQL Procedures and Functions Migration Plan
