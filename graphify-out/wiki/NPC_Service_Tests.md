# NPC Service Tests

> 78 nodes · cohesion 0.03

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **test_goto_command_player_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_player_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_subcommand_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_prototype_id_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_validation_max()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_invalid_characters()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_player_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_player_name_min_length()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_admin.py`
- **.validate_direction_field()** (3 connections) — `server/models/command_admin.py`
- **.validate_player_name_field()** (3 connections) — `server/models/command_admin.py`
- **test_goto_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_goto_command_validate_player_name_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_shutdown_command_with_cancel()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 53 more nodes in this community*

## Relationships

- [Admin Command Models](Admin_Command_Models.md) (30 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (12 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 221 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*