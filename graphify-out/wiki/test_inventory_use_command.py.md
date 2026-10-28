# test_inventory_use_command.py

> 53 nodes · cohesion 0.06

## Key Concepts

- **npcs/catalog_dml.py** (21 connections) — `server/game/npcs/catalog_dml.py`
- **prepare_npc_definition()** (13 connections) — `server/game/npcs/catalog_dml.py`
- **NpcBaseStats** (8 connections) — `server/game/npcs/base_stats_models.py`
- **render_migration()** (8 connections) — `server/game/npcs/catalog_dml.py`
- **test_base_stats_models.py** (8 connections) — `server/tests/unit/game/npcs/test_base_stats_models.py`
- **base_stats_models.py** (7 connections) — `server/game/npcs/base_stats_models.py`
- **npcs/test_catalog_dml.py** (7 connections) — `server/tests/unit/game/npcs/test_catalog_dml.py`
- **npc_catalog/generate_dml.py** (6 connections) — `data/npc_catalog/generate_dml.py`
- **_load_catalog()** (5 connections) — `data/npc_catalog/generate_dml.py`
- **_dual_write_one_attack()** (5 connections) — `server/game/npcs/catalog_dml.py`
- **_load_json_object()** (5 connections) — `server/tests/unit/game/npcs/test_base_stats_models.py`
- **BaseModel** (4 connections)
- **apply_attack_dual_write()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **_ensure_behavior_config()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **render_npc_insert()** (4 connections) — `server/game/npcs/catalog_dml.py`
- **_load_json()** (3 connections) — `data/npc_catalog/generate_dml.py`
- **main()** (3 connections) — `data/npc_catalog/generate_dml.py`
- **NpcArmorMetadata** (3 connections) — `server/game/npcs/base_stats_models.py`
- **NpcAttackMetadata** (3 connections) — `server/game/npcs/base_stats_models.py`
- **NpcCatalogMetadata** (3 connections) — `server/game/npcs/base_stats_models.py`
- **_as_str_object_dict()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_normalize_damage_expr()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_optional_description()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **_require_name()** (3 connections) — `server/game/npcs/catalog_dml.py`
- **sql_escape()** (3 connections) — `server/game/npcs/catalog_dml.py`
- *... and 28 more nodes in this community*

## Relationships

- [catalog_commands.py](catalog_commands.py.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)

## Source Files

- `data/npc_catalog/generate_dml.py`
- `server/game/npcs/base_stats_models.py`
- `server/game/npcs/catalog_dml.py`
- `server/tests/unit/game/npcs/test_base_stats_models.py`
- `server/tests/unit/game/npcs/test_catalog_dml.py`

## Audit Trail

- EXTRACTED: 89 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*