# StatusEffect

> 127 nodes

## Key Concepts

- **StatusEffect** (31 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_schema_converter_weapon.py** (20 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **InventoryItem** (17 connections) — `server/models/game.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **test_game_status_effect.py** (15 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_weapon_from_prototype_registry()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **test_game_inventory_item.py** (8 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **.get_position_state()** (6 connections) — `server/game/player_schema_converter.py`
- **WeaponStats** (5 connections) — `server/models/game.py`
- **.item_prototype_registry()** (5 connections) — `server/commands/combat_handler.py`
- **BaseModel** (5 connections)
- **.check_player_combat_state()** (4 connections) — `server/game/player_schema_converter.py`
- **.compute_derived_stats_fields()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_player_data_methods()** (4 connections) — `server/game/player_schema_converter.py`
- **.get_profession_details()** (4 connections) — `server/game/player_schema_converter.py`
- **test_create_player_read_from_object_enriches_inventory_weapon()** (4 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_player_add_item_existing()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_add_status_effect()** (4 connections) — `server/tests/unit/models/test_game_player.py`
- *... and 102 more nodes in this community*

## Relationships

- [models/player.py](models-player.py.md) (18 shared connections)
- [Stats](Stats.md) (6 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (5 shared connections)
- [PrototypeRegistryError](PrototypeRegistryError.md) (4 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [MemoryProfiler](MemoryProfiler.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 248 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*