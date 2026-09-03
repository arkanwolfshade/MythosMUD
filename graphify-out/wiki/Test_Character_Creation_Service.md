# Test Character Creation Service

> 68 nodes

## Key Concepts

- **test_character_creation_service.py** (33 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_character_with_stats()** (6 connections) — `server/game/character_creation_service.py`
- **.validate_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **Any** (5 connections)
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.roll_character_stats()** (4 connections) — `server/game/character_creation_service.py`
- **character_creation_service()** (4 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **._get_class_description()** (3 connections) — `server/game/character_creation_service.py`
- **mock_player_service()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **sample_stats()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_character_creation_service_init()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_pydantic_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_validation_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_invalid_format()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **fixture** (3 connections)
- **test_create_character_with_stats_custom_starting_room()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_success()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_with_user_id()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_get_available_classes_info()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_get_class_description_all_classes()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [Stats Generator](Stats_Generator.md) (8 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (7 shared connections)
- [Wearable Container Service](Wearable_Container_Service.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 91 (93%)
- INFERRED: 7 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*