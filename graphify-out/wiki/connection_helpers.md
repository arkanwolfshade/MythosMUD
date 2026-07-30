# connection helpers

> 72 nodes

## Key Concepts

- **test_command_admin.py** (42 connections) — `server/tests/unit/models/test_command_admin.py`
- **SummonCommand** (21 connections) — `server/models/command_admin.py`
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
- **test_npc_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_subcommand()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_npc_command_with_args()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_valid()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_validate_prototype_id_strips()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_default()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_quantity_valid_range()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_target_type_default()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_summon_command_target_type_npc()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- **test_teleport_command_required_fields()** (3 connections) — `server/tests/unit/models/test_command_admin.py`
- *... and 47 more nodes in this community*

## Relationships

- [Spell Targeting](Spell_Targeting.md) (33 shared connections)
- [.initialize()](initialize%28%29.md) (12 shared connections)
- [test command factories utility](test_command_factories_utility.md) (1 shared connections)

## Source Files

- `server/models/command_admin.py`
- `server/tests/unit/models/test_command_admin.py`

## Audit Trail

- EXTRACTED: 197 (93%)
- INFERRED: 15 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*