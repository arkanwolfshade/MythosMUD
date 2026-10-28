# Improve Layout Systematically

> 17 nodes · cohesion 0.13

## Key Concepts

- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **AttributeType** (9 connections) — `server/models/game.py`
- **StrEnum** (3 connections)
- **.get_attribute_modifier()** (3 connections) — `server/models/game.py`
- **test_attribute_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_attribute_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_all_states()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_position_state_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_all_types()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **test_status_effect_type_enum_values()** (2 connections) — `server/tests/unit/models/test_game_enums.py`
- **Get the modifier for a given attribute (standard D&D-style calculation).** (1 connections) — `server/models/game.py`
- **Core attribute types for the character system .** (1 connections) — `server/models/game.py`
- **Unit tests for game model enums. Tests AttributeType, StatusEffectType, and…** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test PositionState enum contains all expected states.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test AttributeType enum contains expected values.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test StatusEffectType enum contains expected values.** (1 connections) — `server/tests/unit/models/test_game_enums.py`
- **Test PositionState enum contains expected values.** (1 connections) — `server/tests/unit/models/test_game_enums.py`

## Relationships

- [container_endpoints_basic.py](container_endpoints_basic.py.md) (4 shared connections)
- [testing_examples.py](testing_examples.py.md) (3 shared connections)
- [AsciiMapRenderer](AsciiMapRenderer.md) (2 shared connections)
- [test_inventory_mutation_guard_error_handling.py](test_inventory_mutation_guard_error_handling.py.md) (1 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_enums.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*