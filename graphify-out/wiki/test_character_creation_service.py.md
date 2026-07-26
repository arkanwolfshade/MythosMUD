# test_character_creation_service.py

> 68 nodes · cohesion 0.03

## Key Concepts

- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_character_with_stats()** (7 connections) — `server/game/character_creation_service.py`
- **.validate_character_stats()** (6 connections) — `server/game/character_creation_service.py`
- **.roll_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **Any** (5 connections)
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **._get_class_description()** (3 connections) — `server/game/character_creation_service.py`
- **character_creation_service()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_character_creation_service_init()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_pydantic_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_validation_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_create_character_with_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_class_not_available()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_profession_meets_requirements_false()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_with_class()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_with_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_roll_character_stats_without_class_or_profession()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_invalid_format()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_validate_character_stats_value_error()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **UUID** (2 connections)
- **mock_player_service()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **sample_stats()** (2 connections) — `server/tests/unit/game/test_character_creation_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (10 shared connections)
- [Stats](Stats.md) (8 shared connections)
- [character_creation.py](character_creation.py.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [exceptions.py](exceptions.py.md) (1 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 161 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*