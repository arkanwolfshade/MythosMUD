# Any

> 16 nodes

## Key Concepts

- **SpellMaterialsService** (15 connections) — `server/game/magic/spell_materials.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.__init__()** (3 connections) — `server/game/magic/spell_materials.py`
- **UUID** (3 connections)
- **Service for handling spell material requirements.      Handles checking if playe** (1 connections) — `server/game/magic/spell_materials.py`
- **Initialize the spell materials service.          Args:             player_servic** (1 connections) — `server/game/magic/spell_materials.py`
- **Check if player has all required materials.          Args:             player_id** (1 connections) — `server/game/magic/spell_materials.py`
- **Process a single material requirement.          Args:             material: Mate** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume a material item.          Args:             item: Inventory item** (1 connections) — `server/game/magic/spell_materials.py`
- **Build final inventory with consumed materials removed.          Args:** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume spell materials from player inventory.          Args:             player** (1 connections) — `server/game/magic/spell_materials.py`

## Relationships

- [. init ()](_init_%28%29.md) (4 shared connections)
- [Connection Manager](Connection_Manager.md) (4 shared connections)
- [Spell Targeting](Spell_Targeting.md) (3 shared connections)
- [MagicServiceCore](MagicServiceCore.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 51 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*