# Emote Schema Validator

> 63 nodes

## Key Concepts

- **CommandType** (84 connections) — `server/models/command_base.py`
- **command_base.py** (23 connections) — `server/models/command_base.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
- **command_exploration.py** (9 connections) — `server/models/command_exploration.py`
- **command_follow.py** (8 connections) — `server/models/command_follow.py`
- **FollowCommand** (6 connections) — `server/models/command_follow.py`
- **UnfollowCommand** (6 connections) — `server/models/command_follow.py`
- **FollowingCommand** (6 connections) — `server/models/command_follow.py`
- **command_party.py** (6 connections) — `server/models/command_party.py`
- **PartyCommand** (6 connections) — `server/models/command_party.py`
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **.validate_direction_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **.validate_direction()** (3 connections) — `server/models/command_exploration.py`
- **test_direction_enum_inheritance()** (3 connections) — `server/tests/unit/models/test_command_base.py`
- **test_look_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_with_direction()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_valid()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_validate_direction_none()** (3 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 38 more nodes in this community*

## Relationships

- [Game Terminal Panels](Game_Terminal_Panels.md) (16 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (13 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (10 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (9 shared connections)
- [NPC Occupant Processor](NPC_Occupant_Processor.md) (9 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (9 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (8 shared connections)
- [Environmental Container Scenario](Environmental_Container_Scenario.md) (7 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (7 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (7 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (6 shared connections)
- [Command Helper Utilities](Command_Helper_Utilities.md) (6 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/models/command_follow.py`
- `server/models/command_party.py`
- `server/tests/unit/models/test_command_base.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 226 (71%)
- INFERRED: 94 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*