# Player

> 355 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **prototype_registry.py** (19 connections) — `server/game/items/prototype_registry.py`
- **PrototypeRegistryError** (19 connections) — `server/game/items/prototype_registry.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **item_factory.py** (14 connections) — `server/game/items/item_factory.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **stats_generator.py** (14 connections) — `server/game/stats_generator.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **benchmark_model_memory_usage()** (13 connections) — `server/utils/memory_profiler.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- *... and 330 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (36 shared connections)
- [world](world.md) (25 shared connections)
- [.initialize()](initialize%28%29.md) (25 shared connections)
- [message handler factory](message_handler_factory.md) (22 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (21 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (20 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (15 shared connections)
- [Spell Targeting](Spell_Targeting.md) (14 shared connections)
- [test command parser](test_command_parser.md) (10 shared connections)
- [real time](real_time.md) (10 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [.validate spell name()](validate_spell_name%28%29.md) (8 shared connections)

## Source Files

- `server/game/items/__init__.py`
- `server/game/items/component_hooks.py`
- `server/game/items/item_factory.py`
- `server/game/items/item_instance.py`
- `server/game/items/prototype_registry.py`
- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/scripts/validate_prototypes.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`

## Audit Trail

- EXTRACTED: 1349 (94%)
- INFERRED: 84 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*