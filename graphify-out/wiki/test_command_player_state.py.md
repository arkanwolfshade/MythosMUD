# test_command_player_state.py

> 51 nodes

## Key Concepts

- **test_command_player_state.py** (25 connections) — `server/tests/unit/models/test_command_player_state.py`
- **command_player_state.py** (16 connections) — `server/models/command_player_state.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **GroundCommand** (12 connections) — `server/models/command_player_state.py`
- **LogoutCommand** (8 connections) — `server/models/command_player_state.py`
- **QuitCommand** (8 connections) — `server/models/command_player_state.py`
- **SitCommand** (8 connections) — `server/models/command_player_state.py`
- **StandCommand** (8 connections) — `server/models/command_player_state.py`
- **.validate_target_player()** (4 connections) — `server/models/command_player_state.py`
- **.validate_modifier()** (3 connections) — `server/models/command_player_state.py`
- **test_ground_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_target_player_max_length()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_target_player_min_length()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_validate_target_player_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_case_insensitive()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_empty_string()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_invalid()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_none()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_strips_and_lowercases()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_with_modifier_down()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_logout_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_quit_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_sit_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_stand_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- *... and 26 more nodes in this community*

## Relationships

- [BaseCommand](BaseCommand.md) (25 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (3 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (2 shared connections)
- [.create_ground_command](create_ground_command.md) (1 shared connections)
- [.create_lie_command](create_lie_command.md) (1 shared connections)
- [.create_sit_command](create_sit_command.md) (1 shared connections)
- [.create_stand_command](create_stand_command.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/models/command_player_state.py`
- `server/tests/unit/models/test_command_player_state.py`

## Audit Trail

- EXTRACTED: 101 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*