# manager room npcs

> 17 nodes

## Key Concepts

- **SpellMaterialsService** (17 connections) — `server/game/magic/spell_materials.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.__init__()** (3 connections) — `server/game/magic/spell_materials.py`
- **UUID** (3 connections)
- **materials_service()** (2 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **Service for handling spell material requirements.      Handles checking if playe** (1 connections) — `server/game/magic/spell_materials.py`
- **Initialize the spell materials service.          Args:             player_servic** (1 connections) — `server/game/magic/spell_materials.py`
- **Check if player has all required materials.          Args:             player_id** (1 connections) — `server/game/magic/spell_materials.py`
- **Process a single material requirement.          Args:             material: Mate** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume a material item.          Args:             item: Inventory item** (1 connections) — `server/game/magic/spell_materials.py`
- **Build final inventory with consumed materials removed.          Args:** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume spell materials from player inventory.          Args:             player** (1 connections) — `server/game/magic/spell_materials.py`

## Relationships

- [room realtime rationale](room_realtime_rationale.md) (5 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (4 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (3 shared connections)
- [subject nats manager](subject_nats_manager.md) (1 shared connections)
- [player respawn event](player_respawn_event.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`
- `server/tests/unit/game/magic/test_spell_materials.py`

## Audit Trail

- EXTRACTED: 55 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*