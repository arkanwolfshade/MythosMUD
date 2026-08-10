# Game Terminal Panels

> 98 nodes

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **NPCCommand** (13 connections) — `server/models/command_admin.py`
- **GotoCommand** (13 connections) — `server/models/command_admin.py`
- **ShutdownCommand** (12 connections) — `server/models/command_admin.py`
- **.create_npc_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **.create_shutdown_command()** (5 connections) — `server/utils/command_factories_utility.py`
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
- **.validate_player_name_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_admin.py`
- **test_npc_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 73 more nodes in this community*

## Relationships

- [Room Service Tests](Room_Service_Tests.md) (21 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (16 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (6 shared connections)
- [Communication Command Models](Communication_Command_Models.md) (3 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 296 (92%)
- INFERRED: 27 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*