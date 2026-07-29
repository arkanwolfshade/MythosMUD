# Connection Manager

> 407 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **players.py** (66 connections) — `server/api/players.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **test_player_service_mutations.py** (34 connections) — `server/tests/unit/game/test_player_service_mutations.py`
- **test_players_api_coverage.py** (28 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **player_schema_converter.py** (19 connections) — `server/game/player_schema_converter.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **PlayerSchemaConverter** (16 connections) — `server/game/player_schema_converter.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **get_player_quests()** (14 connections) — `server/api/players.py`
- **player_creation_service.py** (14 connections) — `server/game/player_creation_service.py`
- **UUID** (14 connections)
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- *... and 382 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (85 shared connections)
- [main()](main%28%29.md) (59 shared connections)
- [APIRouter](APIRouter.md) (56 shared connections)
- [character creation](character_creation.md) (50 shared connections)
- [Core character statistics with Lovecraftian](Core_character_statistics_with_Lovecraftian.md) (12 shared connections)
- [Player Position Service](Player_Position_Service.md) (11 shared connections)
- [Any](Any.md) (11 shared connections)
- [Request](Request.md) (10 shared connections)
- [Spell Targeting](Spell_Targeting.md) (9 shared connections)
- [get room service()](get_room_service%28%29.md) (8 shared connections)
- [get skill repository()](get_skill_repository%28%29.md) (7 shared connections)
- [login grace period](login_grace_period.md) (7 shared connections)

## Source Files

- `server/api/players.py`
- `server/api/skills.py`
- `server/commands/combat_handler.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_creation_service.py`
- `server/game/player_schema_converter.py`
- `server/game/player_search_service.py`
- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/models/game.py`
- `server/schemas/game/weapon.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/__init__.py`
- `server/schemas/quest/quest.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 1662 (92%)
- INFERRED: 149 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*