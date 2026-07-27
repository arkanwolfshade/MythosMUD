# Game Magic Spell

> 15 nodes · cohesion 0.17

## Key Concepts

- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **spell_materials.py** (6 connections) — `server/game/magic/spell_materials.py`
- **Any** (6 connections) — `server/game/magic/spell_materials.py`
- **UUID** (5 connections) — `server/game/magic/spell_materials.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Spell** (4 connections) — `server/game/magic/spell_materials.py`
- **Spell material handling service.  This module handles checking and consuming spe** (1 connections) — `server/game/magic/spell_materials.py`
- **Build final inventory with consumed materials removed.          Args:** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume spell materials from player inventory.          Args:             player** (1 connections) — `server/game/magic/spell_materials.py`
- **Check if player has all required materials.          Args:             player_id** (1 connections) — `server/game/magic/spell_materials.py`
- **Process a single material requirement.          Args:             material: Mate** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume a material item.          Args:             item: Inventory item** (1 connections) — `server/game/magic/spell_materials.py`

## Relationships

- [[Magic Service Bundle]] (6 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Spell Registry Costs]] (4 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 45 (88%)
- INFERRED: 6 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
