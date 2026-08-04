# auth endpoints rationale

> 127 nodes

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **test_command_exploration.py** (20 connections) — `server/tests/unit/models/test_command_exploration.py`
- **LookCommand** (19 connections) — `server/models/command_exploration.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
- **GoCommand** (14 connections) — `server/models/command_exploration.py`
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
- **test_look_command_validate_direction_invalid()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- **test_look_command_instance_number_validation_min()** (4 connections) — `server/tests/unit/models/test_command_exploration.py`
- *... and 102 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (37 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (16 shared connections)
- [exceptions rationale error](exceptions_rationale_error.md) (6 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (3 shared connections)
- [Inventory Equip](Inventory_Equip.md) (2 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/models/command_exploration.py`
- `server/tests/unit/models/test_command_admin.py`
- `server/tests/unit/models/test_command_exploration.py`

## Audit Trail

- EXTRACTED: 396 (89%)
- INFERRED: 48 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*