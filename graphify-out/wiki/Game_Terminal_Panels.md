# Game Terminal Panels

> 82 nodes

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **NPCCommand** (13 connections) — `server/models/command_admin.py`
- **GotoCommand** (13 connections) — `server/models/command_admin.py`
- **ShutdownCommand** (12 connections) — `server/models/command_admin.py`
- **test_npc_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_invalid_characters()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_validation_max()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_player_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_player_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **.validate_direction_field()** (3 connections) — `server/models/command_admin.py`
- **test_npc_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_valid()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_strips()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 57 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (17 shared connections)
- [Command Parser Helpers](Command_Parser_Helpers.md) (12 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (7 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (5 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (5 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (2 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 249 (90%)
- INFERRED: 27 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*