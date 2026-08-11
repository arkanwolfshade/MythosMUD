# NPC Database Sessions

> 146 nodes

## Key Concepts

- **Stats** (80 connections) — `server/models/game.py`
- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **generate_random_stats()** (6 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/models/game.py`
- **._calculate_max_magic_points()** (4 connections) — `server/models/game.py`
- **._calculate_max_lucidity()** (4 connections) — `server/models/game.py`
- **test_player_create()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_create_custom_stats()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **test_player_read_defaults()** (4 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **._compute_max_dp_if_missing()** (3 connections) — `server/models/game.py`
- **.max_magic_points()** (3 connections) — `server/models/game.py`
- **.max_lucidity()** (3 connections) — `server/models/game.py`
- **._calculate_max_dp()** (3 connections) — `server/models/game.py`
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **character_creation_service()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_character_creation_service_init()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_with_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_with_class()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_without_class_or_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_class_not_available()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_invalid_format()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- *... and 121 more nodes in this community*

## Relationships

- [Application Config Settings](Application_Config_Settings.md) (10 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (9 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (7 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (6 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (5 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (3 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (1 shared connections)
- [Archive Planning Ephemeral](Archive_Planning_Ephemeral.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/models/test_game_stats_methods.py`
- `server/tests/unit/schemas/test_player_schemas.py`

## Audit Trail

- EXTRACTED: 404 (96%)
- INFERRED: 18 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*