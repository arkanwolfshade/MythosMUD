# Container Loot Helpers

> 70 nodes

## Key Concepts

- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
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
- **test_roll_character_stats_with_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_with_class()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_without_class_or_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_class_not_available()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_invalid_format()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_validation_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_pydantic_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_profession_meets_requirements_false()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **UUID** (2 connections)
- **mock_player_service()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- *... and 45 more nodes in this community*

## Relationships

- [Command Parser Helpers](Command_Parser_Helpers.md) (11 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (9 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 175 (93%)
- INFERRED: 14 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*