# PlayerSchemaConverter

> 26 nodes

## Key Concepts

- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **.__init__()** (3 connections) — `server/game/player_schema_converter.py`
- **asyncio** (1 connections)
- **Item prototype registry for command modules.** (1 connections) — `server/commands/combat_handler.py`
- **Get stats, inventory, and status_effects from player, handling async methods.** (1 connections) — `server/game/player_schema_converter.py`
- **Compute derived stats fields (max_dp, max_magic_points, max_lucidity). Returns…** (1 connections) — `server/game/player_schema_converter.py`
- **Get PositionState from position value, with fallback to STANDING.** (1 connections) — `server/game/player_schema_converter.py`
- **Create PlayerRead schema from player object.** (1 connections) — `server/game/player_schema_converter.py`
- **Create PlayerRead schema from player dictionary.** (1 connections) — `server/game/player_schema_converter.py`
- **Convert a player object to PlayerRead schema. Args: player: Player object or…** (1 connections) — `server/game/player_schema_converter.py`
- **Utility class for converting Player objects to PlayerRead schemas.** (1 connections) — `server/game/player_schema_converter.py`
- **Initialize the converter with persistence, optional combat service, and…** (1 connections) — `server/game/player_schema_converter.py`
- **Check if player is in combat.** (1 connections) — `server/game/player_schema_converter.py`
- **Get profession information for player.** (1 connections) — `server/game/player_schema_converter.py`
- *... and 1 more nodes in this community*

## Relationships

- [PrototypeRegistryError](PrototypeRegistryError.md) (7 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (4 shared connections)
- [Stats](Stats.md) (3 shared connections)
- [StatusEffect](StatusEffect.md) (2 shared connections)
- [PlayerStateService](PlayerStateService.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (1 shared connections)
- [combat_loader.py](combat_loader.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`

## Audit Trail

- EXTRACTED: 57 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*