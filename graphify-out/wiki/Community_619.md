# Community 619

> 27 nodes

## Key Concepts

- **items/catalog_dml.py** (16 connections) — `server/game/items/catalog_dml.py`
- **items/test_catalog_dml.py** (12 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **prepare_prototype()** (10 connections) — `server/game/items/catalog_dml.py`
- **apply_weapon_dual_write()** (9 connections) — `server/game/items/catalog_dml.py`
- **render_migration()** (8 connections) — `server/game/items/catalog_dml.py`
- **_prototype_value_literals()** (5 connections) — `server/game/items/catalog_dml.py`
- **render_prototype_insert()** (5 connections) — `server/game/items/catalog_dml.py`
- **_ensure_weapon_defaults()** (3 connections) — `server/game/items/catalog_dml.py`
- **_normalize_damage_expr()** (3 connections) — `server/game/items/catalog_dml.py`
- **sql_escape()** (3 connections) — `server/game/items/catalog_dml.py`
- **_sql_literal()** (3 connections) — `server/game/items/catalog_dml.py`
- **test_prepare_prototype_accepts_equipment_skill_bonuses()** (3 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **test_prepare_prototype_accepts_tome_metadata()** (3 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **test_render_migration_includes_on_conflict_and_dual_write()** (3 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **ItemPrototypeModel** (3 connections)
- **test_apply_weapon_dual_write_fills_min_max_from_expr()** (2 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **test_apply_weapon_dual_write_strips_db_and_shotgun_bands()** (2 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **Emit idempotent item_prototypes DML from catalog JSON (ADR-026 Phase 2). Dual-…** (1 connections) — `server/game/items/catalog_dml.py`
- **SQL literals for _DATA_COLUMNS in order.** (1 connections) — `server/game/items/catalog_dml.py`
- **Render one idempotent INSERT for item_prototypes.** (1 connections) — `server/game/items/catalog_dml.py`
- **Render a full migration SQL file body for one schema.** (1 connections) — `server/game/items/catalog_dml.py`
- **Escape a string for a single-quoted SQL literal.** (1 connections) — `server/game/items/catalog_dml.py`
- **Fill legacy WeaponStats keys when dual-writing from damage_expr.** (1 connections) — `server/game/items/catalog_dml.py`
- **Fill WeaponStats integers from damage_expr when min/max are absent.** (1 connections) — `server/game/items/catalog_dml.py`
- **Strip DB/flavor suffixes and shotgun range bands for legacy min/max.** (1 connections) — `server/game/items/catalog_dml.py`
- *... and 2 more nodes in this community*

## Relationships

- [Community 784](Community_784.md) (7 shared connections)
- [Community 1374](Community_1374.md) (3 shared connections)
- [Community 540](Community_540.md) (2 shared connections)
- [Community 516](Community_516.md) (1 shared connections)

## Source Files

- `server/game/items/catalog_dml.py`
- `server/tests/unit/game/items/test_catalog_dml.py`

## Audit Trail

- EXTRACTED: 54 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*