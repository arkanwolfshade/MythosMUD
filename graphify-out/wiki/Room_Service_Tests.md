# Room Service Tests

> 180 nodes

## Key Concepts

- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_command_magic.py** (27 connections) — `server/tests/unit/models/test_command_magic.py`
- **CastCommand** (20 connections) — `server/models/command_magic.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **SpellCommand** (13 connections) — `server/models/command_magic.py`
- **LearnCommand** (13 connections) — `server/models/command_magic.py`
- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **.create_teleport_command()** (11 connections) — `server/utils/command_factories_utility.py`
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
- **test_spell_command_validate_spell_name_whitespace_only()** (4 connections) — `server/tests/unit/models/test_command_magic.py`
- *... and 155 more nodes in this community*

## Relationships

- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (28 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (28 shared connections)
- [NPC Definition Admin API](NPC_Definition_Admin_API.md) (10 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (4 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (2 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)

## Source Files

- `server/models/command_magic.py`
- `server/tests/unit/models/test_command_magic.py`
- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 532 (93%)
- INFERRED: 37 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*