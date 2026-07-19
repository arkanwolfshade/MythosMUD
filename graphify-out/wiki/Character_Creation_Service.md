# Character Creation Service

> 66 nodes · cohesion 0.03

## Key Concepts

- **test_character_creation_service.py** (30 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_character_with_stats()** (6 connections) — `server/game/character_creation_service.py`
- **Any** (6 connections) — `server/game/character_creation_service.py`
- **.validate_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.roll_character_stats()** (4 connections) — `server/game/character_creation_service.py`
- **._get_class_description()** (3 connections) — `server/game/character_creation_service.py`
- **character_creation_service()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_character_creation_service_init()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_validation_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **UUID** (3 connections) — `server/game/character_creation_service.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **Test create_character_with_stats() handles ValidationError.** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **sample_stats()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_custom_starting_room()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_pydantic_error()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_success()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_value_error()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_with_user_id()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_get_available_classes_info()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_get_class_description_all_classes()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_get_class_description_known_class()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_get_class_description_unknown_class()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [[NPC Admin API]] (8 shared connections)
- [[Character Stats Generator]] (4 shared connections)
- [[Character Stats Model]] (3 shared connections)
- [[Character Creation API]] (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 159 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
