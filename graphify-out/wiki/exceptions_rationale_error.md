# exceptions rationale error

> 182 nodes

## Key Concepts

- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **SpellCommand** (13 connections) — `server/models/command_magic.py`
- **LearnCommand** (13 connections) — `server/models/command_magic.py`
- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **.create_teleport_command()** (11 connections) — `server/utils/command_factories_utility.py`
- **command_magic.py** (10 connections) — `server/models/command_magic.py`
- **SpellsCommand** (8 connections) — `server/models/command_magic.py`
- **.create_alias_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_unalias_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_spell_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_learn_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_aliases_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **.create_goto_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **.create_spells_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **.create_help_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **.create_npc_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **.create_shutdown_command()** (5 connections) — `server/utils/command_factories_utility.py`
- **test_cast_command_validate_spell_name_empty()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_validate_spell_name_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_spell_name_max_length()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_cast_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- **test_spell_command_validate_spell_name_empty()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- *... and 157 more nodes in this community*

## Relationships

- [command factories create](command_factories_create.md) (40 shared connections)
- [command inventory models](command_inventory_models.md) (28 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [feature services flag](feature_services_flag.md) (2 shared connections)
- [time service rationale](time_service_rationale.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)

## Source Files

- `server/models/command_magic.py`
- `server/tests/unit/models/test_command_magic.py`
- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 530 (93%)
- INFERRED: 38 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*