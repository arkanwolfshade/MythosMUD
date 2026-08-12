# React Node Upgrade Summary

> 185 nodes

## Key Concepts

- **ValidationError** (540 connections) — `server/exceptions.py`
- **test_character_creation_service.py** (31 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **validate_room_data()** (16 connections) — `server/world_loader.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **TestGetRoomEnvironment** (12 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateRoomData** (11 connections) — `server/tests/unit/test_world_loader.py`
- **TestCreateCharacterWithStats** (10 connections) — `server/tests/unit/api/test_character_creation.py`
- **test_world_loader.py** (10 connections) — `server/tests/unit/test_world_loader.py`
- **TestValidateCharacterStats** (9 connections) — `server/tests/unit/api/test_character_creation.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **MythosValidationError** (8 connections)
- **TestGenerateRoomId** (7 connections) — `server/tests/unit/test_world_loader.py`
- **.test_create_character_rate_limit()** (6 connections) — `server/tests/unit/api/test_character_creation.py`
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_unalias_command_alias_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_unalias_command_alias_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_alias.py`
- **test_emote_command_action_min_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_emote_command_action_max_length()** (4 connections) — `server/tests/unit/models/test_command_communication.py`
- **test_go_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_go_command_missing_direction()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_cast_command_validate_spell_name_empty()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- *... and 160 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (56 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (48 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (32 shared connections)
- [Base Command Models](Base_Command_Models.md) (30 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (24 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (23 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (19 shared connections)
- [Playwright Remediation Plan](Playwright_Remediation_Plan.md) (19 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (18 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (18 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (17 shared connections)
- [Command Factory Creators](Command_Factory_Creators.md) (14 shared connections)

## Source Files

- `server/exceptions.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/game/test_character_creation_service.py`
- `server/tests/unit/models/test_command_alias.py`
- `server/tests/unit/models/test_command_communication.py`
- `server/tests/unit/models/test_command_exploration.py`
- `server/tests/unit/models/test_command_magic.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_world_loader.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 607 (56%)
- INFERRED: 470 (44%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*