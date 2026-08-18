# server game magic spell materials

> 16 nodes

## Key Concepts

- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/game/magic/spell_materials.py`
- **UUID** (3 connections)
- **Build final inventory with consumed materials removed. Args: inventory:…** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume spell materials from player inventory. Args: player_id: Player ID…** (1 connections) — `server/game/magic/spell_materials.py`
- **Service for handling spell material requirements. Handles checking if players…** (1 connections) — `server/game/magic/spell_materials.py`
- **Initialize the spell materials service. Args: player_service: Player service…** (1 connections) — `server/game/magic/spell_materials.py`
- **Check if player has all required materials. Args: player_id: Player ID spell:…** (1 connections) — `server/game/magic/spell_materials.py`
- **Process a single material requirement. Args: material: Material requirement…** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume a material item. Args: item: Inventory item material_id: Material ID…** (1 connections) — `server/game/magic/spell_materials.py`

## Relationships

- [server game magic spell materials](server_game_magic_spell_materials.md) (7 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (3 shared connections)
- [server api players](server_api_players.md) (2 shared connections)
- [server game magic magic service](server_game_magic_magic_service.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`

## Audit Trail

- EXTRACTED: 30 (86%)
- INFERRED: 5 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*