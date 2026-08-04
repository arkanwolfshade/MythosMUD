# command factories communication

> 191 nodes

## Key Concepts

- **test_player_model.py** (48 connections) — `server/tests/unit/models/test_player_model.py`
- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- *... and 166 more nodes in this community*

## Relationships

- [combat models rationale](combat_models_rationale.md) (47 shared connections)
- [spell game magic](spell_game_magic.md) (19 shared connections)
- [player service game](player_service_game.md) (14 shared connections)
- [Player Stats](Player_Stats.md) (11 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (6 shared connections)
- [command commands handler](command_commands_handler.md) (6 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [task registry app](task_registry_app.md) (4 shared connections)
- [player death service](player_death_service.md) (4 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/models/invite.py`
- `server/schemas/game/weapon.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`
- `server/tests/unit/models/test_player_model.py`

## Audit Trail

- EXTRACTED: 788 (96%)
- INFERRED: 32 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*