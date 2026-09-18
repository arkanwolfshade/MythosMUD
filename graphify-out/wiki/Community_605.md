# Community 605

> 28 nodes

## Key Concepts

- **npcs/catalog_dml.py** (21 connections) — `server/game/npcs/catalog_dml.py`
- **prepare_npc_definition()** (12 connections) — `server/game/npcs/catalog_dml.py`
- **render_migration()** (8 connections) — `server/game/npcs/catalog_dml.py`
- **npcs/test_catalog_dml.py** (7 connections) — `server/tests/unit/game/npcs/test_catalog_dml.py`
- **_dual_write_one_attack()** (5 connections) — `server/game/npcs/catalog_dml.py`
- **apply_attack_dual_write()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **_ensure_behavior_config()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **render_npc_insert()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **_as_str_object_dict()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_normalize_damage_expr()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **sql_escape()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_sql_literal()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_sample_row()** (3 connections) — `server/tests/unit/game/npcs/test_catalog_dml.py`
- **test_prepare_forces_arena_inert_and_dual_write()** (3 connections) — `server/tests/unit/game/npcs/test_catalog_dml.py`
- **test_render_migration_uses_name_sub_zone_conflict()** (3 connections) — `server/tests/unit/game/npcs/test_catalog_dml.py`
- **_first_attack_damage()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **_hostility_to_npc_type()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **_optional_description()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **_require_name()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **Emit idempotent npc_definitions DML from catalog JSON (ADR-027 Phase 2). Forces…** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Validate catalog row, dual-write attacks, force arena/inert placement.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Render one idempotent INSERT for npc_definitions.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Render a full migration SQL file body for one schema.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Escape a string for a single-quoted SQL literal.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Strip DB/flavor suffixes and range bands for legacy min/max.** (1 connections) — `server/game/npcs/catalog_dml.py`
- *... and 3 more nodes in this community*

## Relationships

- [Community 540](Community_540.md) (3 shared connections)
- [Community 835](Community_835.md) (3 shared connections)
- [Community 1377](Community_1377.md) (3 shared connections)

## Source Files

- `server/game/npcs/catalog_dml.py`
- `server/tests/unit/game/npcs/test_catalog_dml.py`

## Audit Trail

- EXTRACTED: 55 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*