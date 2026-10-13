# Community 785

> 21 nodes

## Key Concepts

- **npcs/catalog_dml.py** (21 connections) — `server/game/npcs/catalog_dml.py`
- **prepare_npc_definition()** (12 connections) — `server/game/npcs/catalog_dml.py`
- **_dual_write_one_attack()** (5 connections) — `server/game/npcs/catalog_dml.py`
- **apply_attack_dual_write()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **_ensure_behavior_config()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **render_npc_insert()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **_as_str_object_dict()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_normalize_damage_expr()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **sql_escape()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_sql_literal()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_first_attack_damage()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **_hostility_to_npc_type()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **_optional_description()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **_require_name()** (2 connections) — `server/game/npcs/catalog_dml.py`
- **Emit idempotent npc_definitions DML from catalog JSON (ADR-027 Phase 2). Forces…** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Validate catalog row, dual-write attacks, force arena/inert placement.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Render one idempotent INSERT for npc_definitions.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Escape a string for a single-quoted SQL literal.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Strip DB/flavor suffixes and range bands for legacy min/max.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Fill min/max on one attack from damage_expr when either bound is missing.** (1 connections) — `server/game/npcs/catalog_dml.py`
- **Fill attack min/max from damage_expr when absent.** (1 connections) — `server/game/npcs/catalog_dml.py`

## Relationships

- [Community 1052](Community_1052.md) (7 shared connections)
- [Community 547](Community_547.md) (3 shared connections)
- [Community 841](Community_841.md) (3 shared connections)

## Source Files

- `server/game/npcs/catalog_dml.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*