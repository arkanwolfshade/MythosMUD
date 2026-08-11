# Emote Schema Validator

> 79 nodes

## Key Concepts

- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_base.py** (22 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **command_exploration.py** (9 connections) — `server/models/command_exploration.py`
- **test_base_command_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_command_base.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **test_base_command_instantiation()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_model_config()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_slots()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_direction_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_look_in()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_instance_number()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 54 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (15 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (8 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (7 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (5 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (3 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 215 (90%)
- INFERRED: 25 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*