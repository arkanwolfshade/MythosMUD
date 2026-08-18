# server models command base direction

> 76 nodes

## Key Concepts

- **Direction** (28 connections) — `server/models/command_base.py`
- **test_command_base.py** (24 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_exploration.py** (22 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (18 connections) — `server/models/command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **command_exploration.py** (10 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (4 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (4 connections) — `server/models/command_exploration.py`
- **test_go_command_all_directions()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_required_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_valid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_base_command_instantiation()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_model_config()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_rejects_extra_fields()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_base_command_slots()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_admin_commands()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_combat_commands()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_communication_commands()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_exploration_commands()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_inventory_commands()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_look()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_contains_magic_commands()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_command_type_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- *... and 51 more nodes in this community*

## Relationships

- [claude rules pydantic](claude_rules_pydantic.md) (26 shared connections)
- [server models command base basecommand](server_models_command_base_basecommand.md) (8 shared connections)
- [server models command admin gotocommand](server_models_command_admin_gotocommand.md) (5 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (3 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)

## Source Files

- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 127 (82%)
- INFERRED: 28 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*