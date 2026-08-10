# Zone Config Loader

> 50 nodes

## Key Concepts

- **test_command_player_state.py** (23 connections) — `server/tests/unit/models/test_command_player_state.py`
- **command_player_state.py** (15 connections) — `server/models/command_player_state.py`
- **LieCommand** (15 connections) — `server/models/command_player_state.py`
- **GroundCommand** (12 connections) — `server/models/command_player_state.py`
- **QuitCommand** (8 connections) — `server/models/command_player_state.py`
- **LogoutCommand** (8 connections) — `server/models/command_player_state.py`
- **SitCommand** (8 connections) — `server/models/command_player_state.py`
- **StandCommand** (8 connections) — `server/models/command_player_state.py`
- **test_lie_command_validate_modifier_invalid()** (4 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_empty_string()** (4 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_target_player_min_length()** (4 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_target_player_max_length()** (4 connections) — `server/tests/unit/models/test_command_player_state.py`
- **.validate_target_player()** (3 connections) — `server/models/command_player_state.py`
- **test_quit_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_logout_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_sit_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_stand_command_no_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_with_modifier_down()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_strips_and_lowercases()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_case_insensitive()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_lie_command_validate_modifier_none()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **test_ground_command_validate_target_player_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_player_state.py`
- **.validate_modifier()** (2 connections) — `server/models/command_player_state.py`
- *... and 25 more nodes in this community*

## Relationships

- [Emote Schema Validator](Emote_Schema_Validator.md) (8 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (7 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (7 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (4 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (4 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (3 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (2 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (1 shared connections)

## Source Files

- `server/models/command_player_state.py`
- `server/tests/unit/models/test_command_player_state.py`

## Audit Trail

- EXTRACTED: 160 (91%)
- INFERRED: 16 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*