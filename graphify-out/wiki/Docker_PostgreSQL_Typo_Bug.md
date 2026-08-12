# Docker PostgreSQL Typo Bug

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

- [Combat NPC Lookup](Combat_NPC_Lookup.md) (2 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (2 shared connections)
- [Client Event Store](Client_Event_Store.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/tests/unit/models/test_game_enums.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*