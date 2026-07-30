# Player

> 324 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **Player** (26 connections) — `server/models/game.py`
- **test_player_service.py** (26 connections) — `server/tests/unit/game/test_player_service.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **player_respawn_wrapper.py** (14 connections) — `server/game/player_respawn_wrapper.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **player_state_service.py** (10 connections) — `server/game/player_state_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (9 connections) — `server/game/player_creation_service.py`
- *... and 299 more nodes in this community*

## Relationships

- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (34 shared connections)
- [. init ()](_init_%28%29.md) (31 shared connections)
- [.initialize()](initialize%28%29.md) (26 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (22 shared connections)
- [Spell Targeting](Spell_Targeting.md) (14 shared connections)
- [real time](real_time.md) (11 shared connections)
- [.validate spell name()](validate_spell_name%28%29.md) (8 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (6 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (5 shared connections)
- [message handler factory](message_handler_factory.md) (5 shared connections)
- [useRoomMapData.test](useRoomMapData.test.md) (4 shared connections)
- [main()](main%28%29.md) (4 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_respawn_wrapper.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`
- `server/schemas/game/weapon.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/models/test_game_status_effect.py`

## Audit Trail

- EXTRACTED: 1137 (96%)
- INFERRED: 53 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*