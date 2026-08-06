# player service game

> 315 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **__init__.py** (38 connections) — `server/schemas/players/__init__.py`
- **game.py** (32 connections) — `server/models/game.py`
- **PlayerDeathService** (28 connections) — `server/services/player_death_service.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **player_death_service.py** (19 connections) — `server/services/player_death_service.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **UUID** (14 connections)
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **character_creation.py** (10 connections) — `server/schemas/players/character_creation.py`
- *... and 290 more nodes in this community*

## Relationships

- [persistence core infrastructure](persistence_core_infrastructure.md) (24 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (22 shared connections)
- [add used user](add_used_user.md) (21 shared connections)
- [Player Stats](Player_Stats.md) (17 shared connections)
- [combat services turn](combat_services_turn.md) (16 shared connections)
- [System Metrics](System_Metrics.md) (15 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (13 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (12 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [player room realtime](player_room_realtime.md) (11 shared connections)
- [profession models rationale](profession_models_rationale.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (9 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/game/player_schema_converter.py`
- `server/game/player_service.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/stat_values.py`
- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/schemas/test_player_schemas.py`
- `server/tests/unit/services/test_player_death_service.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 1141 (93%)
- INFERRED: 82 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*