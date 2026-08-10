# Magic Lifespan Initialization

> 19 nodes

## Key Concepts

- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **StrEnum** (3 connections)
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **test_attribute_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_attribute_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_all_states()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **Core attribute types for the character system .** (1 connections) — `server/models/game.py`
- **Get the modifier for a given attribute (standard D&D-style calculation).** (1 connections) — `server/models/game.py`
- **Unit tests for game model enums.  Tests AttributeType, StatusEffectType, and Pos** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test AttributeType enum contains expected values.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test AttributeType enum contains all expected types.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test StatusEffectType enum contains expected values.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test StatusEffectType enum contains all expected types.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test PositionState enum contains expected values.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test PositionState enum contains all expected states.** (1 connections) — `server/tests/unit/models/test_game_enums.py`

## Relationships

- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (4 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (3 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (2 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_enums.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*