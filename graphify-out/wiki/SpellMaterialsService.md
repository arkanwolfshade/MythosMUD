# SpellMaterialsService

> 16 nodes

## Key Concepts

- **SpellMaterialsService** (15 connections) — `server/game/magic/spell_materials.py`
- **spell_materials.py** (10 connections) — `server/game/magic/spell_materials.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- **UUID** (3 connections)
- **Spell material handling service. This module handles checking and consuming…** (1 connections) — `server/game/magic/spell_materials.py`
- **Build final inventory with consumed materials removed. Args: inventory:…** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume spell materials from player inventory. Args: player_id: Player ID…** (1 connections) — `server/game/magic/spell_materials.py`
- **Service for handling spell material requirements. Handles checking if players…** (1 connections) — `server/game/magic/spell_materials.py`
- **Check if player has all required materials. Args: player_id: Player ID spell:…** (1 connections) — `server/game/magic/spell_materials.py`
- **Process a single material requirement. Args: material: Material requirement…** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume a material item. Args: item: Inventory item material_id: Material ID…** (1 connections) — `server/game/magic/spell_materials.py`

## Relationships

- [magic_service.py](magic_service.py.md) (5 shared connections)
- [Spell](Spell.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [test_spell.py](test_spell.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 35 (88%)
- INFERRED: 5 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*