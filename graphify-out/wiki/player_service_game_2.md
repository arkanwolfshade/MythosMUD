# player service game

> 313 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **Stats** (88 connections) — `server/models/game.py`
- **StatsGenerator** (48 connections) — `server/game/stats_generator.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_player_service.py** (26 connections) — `server/tests/unit/game/test_player_service.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **test_dependency_injection.py** (18 connections) — `server/tests/unit/test_dependency_injection.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **stats_generator.py** (15 connections) — `server/game/stats_generator.py`
- **UUID** (14 connections)
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **Stats** (11 connections)
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **PlayerSearchService** (10 connections) — `server/game/player_search_service.py`
- **get_player_service_for_testing()** (9 connections) — `server/dependencies.py`
- **.delete_player()** (9 connections) — `server/game/player_service.py`
- *... and 288 more nodes in this community*

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (48 shared connections)
- [profession game service](profession_game_service.md) (38 shared connections)
- [schemas unified room](schemas_unified_room.md) (28 shared connections)
- [command inventory models](command_inventory_models.md) (23 shared connections)
- [Player Stats](Player_Stats.md) (18 shared connections)
- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [models npc rationale](models_npc_rationale.md) (16 shared connections)
- [magic completion game](magic_completion_game.md) (14 shared connections)
- [game models player](game_models_player.md) (13 shared connections)
- [NPC Combat](NPC_Combat.md) (13 shared connections)
- [game models stats](game_models_stats.md) (11 shared connections)
- [Database Config](Database_Config.md) (10 shared connections)

## Source Files

- `server/dependencies.py`
- `server/game/character_creation_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/game/test_player_service.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 1151 (90%)
- INFERRED: 125 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*