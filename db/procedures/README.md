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

Files are applied in alphabetical order. Procedures that depend on tables or other
procedures must appear after their dependencies. Recommended order (enforced by
filename prefix if needed):

1. `health.sql` - players table updates (depends on players from DDL)
2. `experience.sql` - players table updates
3. `players.sql` - players, player_inventories
4. `professions.sql` - professions
5. `skills.sql` - skills
6. `player_skills.sql` - player_skills (depends on players, skills)
7. `skill_use_log.sql` - skill_use_log
8. `spells.sql` - spells
9. `player_spells.sql` - player_spells (depends on players, spells)
10. `quests.sql` - quest_definitions, quest_offers, quest_instances
11. `player_effects.sql` - player_effects
12. `items.sql` - item_prototypes, item_instances
13. `containers.sql` - containers, container_contents (extends existing functions)
14. `rooms.sql` - rooms, room_links, subzones, zones
15. `npcs.sql` - npc_definitions, npc_spawn_rules

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
