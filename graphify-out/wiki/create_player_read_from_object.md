# .create_player_read_from_object

> 21 nodes

## Key Concepts

- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **Get stats, inventory, and status_effects from player, handling async methods.** (1 connections) — `server/game/player_schema_converter.py`
- **Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…** (1 connections) — `server/game/player_schema_converter.py`
- **Get PositionState from position value, with fallback to STANDING.** (1 connections) — `server/game/player_schema_converter.py`
- **Create PlayerRead schema from player object.** (1 connections) — `server/game/player_schema_converter.py`
- **Create PlayerRead schema from player dictionary.** (1 connections) — `server/game/player_schema_converter.py`
- **Convert a player object to PlayerRead schema. Args: player: Player object or…** (1 connections) — `server/game/player_schema_converter.py`
- **Build InventoryItem from raw item dict, enriching with weapon stats from…** (1 connections) — `server/game/player_schema_converter.py`
- **Initialize the converter with persistence, optional combat service, and…** (1 connections) — `server/game/player_schema_converter.py`
- **Check if player is in combat.** (1 connections) — `server/game/player_schema_converter.py`
- **Get profession information for player.** (1 connections) — `server/game/player_schema_converter.py`

## Relationships

- [PlayerService](PlayerService.md) (9 shared connections)
- [test_player_schema_converter_weapon.py](test_player_schema_converter_weapon.py.md) (6 shared connections)
- [server/models/game.py](server-models-game.py.md) (3 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [Stats](Stats.md) (2 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)

## Source Files

- `server/game/player_schema_converter.py`

## Audit Trail

- EXTRACTED: 55 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*