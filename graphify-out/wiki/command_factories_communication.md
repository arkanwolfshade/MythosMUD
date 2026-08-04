# command factories communication

> 182 nodes

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
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
- **.convert_player_to_schema()** (8 connections) — `server/game/player_schema_converter.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- *... and 157 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (21 shared connections)
- [player service game](player_service_game.md) (10 shared connections)
- [NPC Combat](NPC_Combat.md) (9 shared connections)
- [combat models rationale](combat_models_rationale.md) (8 shared connections)
- [Player Stats](Player_Stats.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (7 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (3 shared connections)
- [command utility models](command_utility_models.md) (3 shared connections)
- [npc spawn validator](npc_spawn_validator.md) (3 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (3 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 696 (96%)
- INFERRED: 30 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*