# UserManager

> 32 nodes · cohesion 0.11

## Key Concepts

- **items/catalog_dml.py** (17 connections) — `server/game/items/catalog_dml.py`
- **items/test_catalog_dml.py** (12 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **prepare_prototype()** (10 connections) — `server/game/items/catalog_dml.py`
- **apply_weapon_dual_write()** (9 connections) — `server/game/items/catalog_dml.py`
- **render_migration()** (8 connections) — `server/game/items/catalog_dml.py`
- **item_catalog/generate_dml.py** (6 connections) — `data/item_catalog/generate_dml.py`
- **_load_catalog()** (5 connections) — `data/item_catalog/generate_dml.py`
- **_prototype_value_literals()** (5 connections) — `server/game/items/catalog_dml.py`
- **render_prototype_insert()** (5 connections) — `server/game/items/catalog_dml.py`
- **_load_json()** (3 connections) — `data/item_catalog/generate_dml.py`
- **main()** (3 connections) — `data/item_catalog/generate_dml.py`
- **_ensure_weapon_defaults()** (3 connections) — `server/game/items/catalog_dml.py`
- **_normalize_damage_expr()** (3 connections) — `server/game/items/catalog_dml.py`
- **sql_escape()** (3 connections) — `server/game/items/catalog_dml.py`
- **_sql_literal()** (3 connections) — `server/game/items/catalog_dml.py`
- **test_prepare_prototype_accepts_equipment_skill_bonuses()** (3 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **test_prepare_prototype_accepts_tome_metadata()** (3 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **test_render_migration_includes_on_conflict_and_dual_write()** (3 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **_object_dict()** (2 connections) — `data/item_catalog/generate_dml.py`
- **Path** (2 connections)
- **test_apply_weapon_dual_write_fills_min_max_from_expr()** (2 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **test_apply_weapon_dual_write_strips_db_and_shotgun_bands()** (2 connections) — `server/tests/unit/game/items/test_catalog_dml.py`
- **Emit idempotent item_prototypes DML from catalog JSON (ADR-026 Phase 2). Dual-…** (1 connections) — `server/game/items/catalog_dml.py`
- **SQL literals for _DATA_COLUMNS in order.** (1 connections) — `server/game/items/catalog_dml.py`
- **Render one idempotent INSERT for item_prototypes.** (1 connections) — `server/game/items/catalog_dml.py`
- *... and 7 more nodes in this community*

## Relationships

- [item_prototype.schema.json](item_prototype.schema.json.md) (7 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (5 shared connections)
- [catalog_commands.py](catalog_commands.py.md) (2 shared connections)

## Source Files

- `data/item_catalog/generate_dml.py`
- `server/game/items/catalog_dml.py`
- `server/tests/unit/game/items/test_catalog_dml.py`

## Audit Trail

- EXTRACTED: 61 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*