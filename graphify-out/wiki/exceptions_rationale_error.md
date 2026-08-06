# exceptions rationale error

> 123 nodes

## Key Concepts

- **test_command_factories_utility.py** (51 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **UtilityCommandFactory** (20 connections) — `server/utils/command_factories_utility.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **.create_teleport_command()** (11 connections) — `server/utils/command_factories_utility.py`
- **.error()** (8 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
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
- *... and 98 more nodes in this community*

## Relationships

- [command inventory models](command_inventory_models.md) (18 shared connections)
- [spell game magic](spell_game_magic.md) (13 shared connections)
- [inventory commands command](inventory_commands_command.md) (5 shared connections)
- [game models stats](game_models_stats.md) (4 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (3 shared connections)
- [command processor rationale](command_processor_rationale.md) (3 shared connections)
- [rate limiter services](rate_limiter_services.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (1 shared connections)
- [middleware error handling](middleware_error_handling.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 366 (93%)
- INFERRED: 28 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*