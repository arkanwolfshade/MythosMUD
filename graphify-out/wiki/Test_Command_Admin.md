# Test Command Admin

> 76 nodes

## Key Concepts

- **test_command_admin.py** (44 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (20 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **command_admin.py** (15 connections) — `server/models/command_admin.py`
- **GotoCommand** (12 connections) — `server/models/command_admin.py`
- **NPCCommand** (12 connections) — `server/models/command_admin.py`
- **ShutdownCommand** (11 connections) — `server/models/command_admin.py`
- **test_teleport_command_validate_direction_valid()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_with_direction()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_max_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_min_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_validate_player_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_max_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_min_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_cancel()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_multiple_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_max_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_min_length()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_default()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 51 more nodes in this community*

## Relationships

- [Command Aliases](Command_Aliases.md) (23 shared connections)
- [Test Command Factories Utility](Test_Command_Factories_Utility.md) (5 shared connections)
- [Security Validators](Security_Validators.md) (5 shared connections)
- [Test Rooms Write Api](Test_Rooms_Write_Api.md) (5 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 148 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*