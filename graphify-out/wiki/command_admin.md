# command admin

> 80 nodes

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **Direction** (22 connections) — `server/models/command_base.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
- **TeleportCommand** (18 connections) — `server/models/command_admin.py`
- **command_admin.py** (14 connections) — `server/models/command_admin.py`
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
- *... and 55 more nodes in this community*

## Relationships

- [.validate spell name()](validate_spell_name%28%29.md) (18 shared connections)
- [. init ()](_init_%28%29.md) (12 shared connections)
- [BaseCommand](BaseCommand.md) (6 shared connections)
- [test command factories utility](test_command_factories_utility.md) (6 shared connections)
- [.validate direction()](validate_direction%28%29.md) (5 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [test command base](test_command_base.md) (2 shared connections)
- [.validate topic()](validate_topic%28%29.md) (1 shared connections)
- [test command factories exploration](test_command_factories_exploration.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/models/command_base.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 279 (88%)
- INFERRED: 37 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*