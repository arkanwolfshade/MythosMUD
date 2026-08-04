# exceptions rationale error

> 122 nodes

## Key Concepts

- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
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
- **test_create_alias_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_aliases_command_with_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_unalias_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_unalias_command_multiple_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_negative_quantity()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_token()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_extra_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_teleport_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- *... and 97 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (32 shared connections)
- [auth endpoints rationale](auth_endpoints_rationale.md) (5 shared connections)
- [command factories create](command_factories_create.md) (4 shared connections)
- [player presence tracker](player_presence_tracker.md) (4 shared connections)
- [command commands talk](command_commands_talk.md) (2 shared connections)
- [Spell Validation](Spell_Validation.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [commands who helpers](commands_who_helpers.md) (1 shared connections)
- [message queue realtime](message_queue_realtime.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 365 (95%)
- INFERRED: 21 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*