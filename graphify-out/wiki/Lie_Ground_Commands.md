# Lie Ground Commands

> 33 nodes · cohesion 0.09

## Key Concepts

- **test_command_player_state.py** (22 connections) — `server/tests/unit/models/test_command_player_state.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **GroundCommand** (12 connections) — `server/models/command_player_state.py`
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
- **.validate_modifier()** (2 connections) — `server/models/command_player_state.py`
- **Test GroundCommand validates target_player min length.** (2 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Test QuitCommand has no required fields.** (2 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Command for lying down (optionally expressed as 'lie down').** (1 connections) — `server/models/command_player_state.py`
- **Validate optional modifier for the lie command.** (1 connections) — `server/models/command_player_state.py`
- **Command for grounding a catatonic ally back to lucidity.** (1 connections) — `server/models/command_player_state.py`
- **Unit tests for player state command models.  Tests the player state command mode** (1 connections) — `server/tests/unit/models/test_command_player_state.py`
- **Test LieCommand rejects invalid modifier.** (1 connections) — `server/tests/unit/models/test_command_player_state.py`
- *... and 8 more nodes in this community*

## Relationships

- [[Base Command Models]] (19 shared connections)
- [[Moderation Command Models]] (1 shared connections)

## Source Files

- `server/models/command_player_state.py`
- `server/tests/unit/models/test_command_player_state.py`

## Audit Trail

- EXTRACTED: 106 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
