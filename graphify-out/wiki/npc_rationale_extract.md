# npc rationale extract

> 58 nodes

## Key Concepts

- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_character_with_stats()** (7 connections) — `server/game/character_creation_service.py`
- **.validate_character_stats()** (6 connections) — `server/game/character_creation_service.py`
- **Any** (5 connections)
- **.roll_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **._get_class_description()** (3 connections) — `server/game/character_creation_service.py`
- **character_creation_service()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_character_creation_service_init()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_invalid_format()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_validation_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_pydantic_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **UUID** (2 connections)
- **mock_player_service()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **sample_stats()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_with_class()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_without_class()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_success()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_with_user_id()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_custom_starting_room()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [player service game](player_service_game.md) (10 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (10 shared connections)
- [Loot Generation](Loot_Generation.md) (4 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 146 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*