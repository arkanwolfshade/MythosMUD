# server tests unit structured logging

> 121 nodes

## Key Concepts

- **UtilityCommandFactory** (65 connections) — `server/utils/command_factories_utility.py`
- **test_command_factories_utility.py** (52 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **.create_summon_command()** (14 connections) — `server/utils/command_factories_utility.py`
- **.create_cast_command()** (12 connections) — `server/utils/command_factories_utility.py`
- **.create_teleport_command()** (11 connections) — `server/utils/command_factories_utility.py`
- **command_factories_utility.py** (11 connections) — `server/utils/command_factories_utility.py`
- **.error()** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.create_alias_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_learn_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_spell_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_unalias_command()** (7 connections) — `server/utils/command_factories_utility.py`
- **.create_aliases_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **.create_goto_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **.create_spells_command()** (6 connections) — `server/utils/command_factories_utility.py`
- **test_create_alias_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_aliases_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_cast_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_goto_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_learn_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_spell_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_spells_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_extra_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_invalid_token()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- **test_create_summon_command_negative_quantity()** (5 connections) — `server/tests/unit/utils/test_command_factories_utility.py`
- *... and 96 more nodes in this community*

## Relationships

- [mythosvalidationerror](mythosvalidationerror.md) (19 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (11 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (11 shared connections)
- [server models command base basecommand](server_models_command_base_basecommand.md) (3 shared connections)
- [server models command admin gotocommand](server_models_command_admin_gotocommand.md) (3 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (2 shared connections)
- [server models command magic castcommand](server_models_command_magic_castcommand.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (1 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)
- [server app lifespan](server_app_lifespan.md) (1 shared connections)

## Source Files

- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/utils/test_command_factories_utility.py`
- `server/utils/command_factories_utility.py`

## Audit Trail

- EXTRACTED: 209 (74%)
- INFERRED: 72 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*