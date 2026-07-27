# Arena Zone DML Generator

> 56 nodes · cohesion 0.06

## Key Concepts

- **gen_arena_migration_sql.py** (14 connections) — `scripts/gen_arena_migration_sql.py`
- **gen_arena_dml.py** (13 connections) — `scripts/gen_arena_dml.py`
- **strip_arena_from_dml.py** (10 connections) — `scripts/strip_arena_from_dml.py`
- **generate_migration()** (8 connections) — `scripts/gen_arena_migration_sql.py`
- **should_skip_line()** (8 connections) — `scripts/strip_arena_from_dml.py`
- **gen_room_row()** (7 connections) — `scripts/gen_arena_dml.py`
- **main()** (7 connections) — `scripts/gen_arena_dml.py`
- **gen_room_links()** (6 connections) — `scripts/gen_arena_dml.py`
- **sql_escape()** (6 connections) — `scripts/gen_arena_migration_sql.py`
- **strip_arena_from_file()** (6 connections) — `scripts/strip_arena_from_dml.py`
- **gen_room_link_id()** (5 connections) — `scripts/gen_arena_dml.py`
- **gen_subzone_row()** (5 connections) — `scripts/gen_arena_dml.py`
- **gen_zone_config_row()** (5 connections) — `scripts/gen_arena_dml.py`
- **gen_zone_row()** (5 connections) — `scripts/gen_arena_dml.py`
- **emit_room_links_insert()** (5 connections) — `scripts/gen_arena_migration_sql.py`
- **emit_rooms_insert()** (5 connections) — `scripts/gen_arena_migration_sql.py`
- **emit_subzone_insert()** (5 connections) — `scripts/gen_arena_migration_sql.py`
- **emit_zone_insert()** (5 connections) — `scripts/gen_arena_migration_sql.py`
- **room_stable_id()** (4 connections) — `scripts/gen_arena_dml.py`
- **emit_zone_config_insert()** (4 connections) — `scripts/gen_arena_migration_sql.py`
- **all_room_rows()** (3 connections) — `scripts/gen_arena_dml.py`
- **main()** (3 connections) — `scripts/gen_arena_migration_sql.py`
- **get_copy_section()** (3 connections) — `scripts/strip_arena_from_dml.py`
- **is_arena_room_line()** (3 connections) — `scripts/strip_arena_from_dml.py`
- **is_arena_room_link_line()** (3 connections) — `scripts/strip_arena_from_dml.py`
- *... and 31 more nodes in this community*

## Relationships

- No strong cross-community connections detected

## Source Files

- `scripts/gen_arena_dml.py`
- `scripts/gen_arena_migration_sql.py`
- `scripts/strip_arena_from_dml.py`

## Audit Trail

- EXTRACTED: 190 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
