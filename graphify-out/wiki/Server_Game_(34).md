# Server Game (34)

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

- [Server Game (4)](Server_Game_%284%29.md) (6 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (3 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (2 shared connections)
- [Server Game (18)](Server_Game_%2818%29.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 51 (91%)
- INFERRED: 5 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*