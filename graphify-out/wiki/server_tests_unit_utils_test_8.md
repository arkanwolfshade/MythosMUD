# server tests unit utils test

> 40 nodes

## Key Concepts

- **CombatCommandFactory** (23 connections) — `server/utils/command_factories_combat.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **.create_attack_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **test_create_attack_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_attack_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_flee_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_kick_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_kick_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_punch_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_punch_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_strike_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_strike_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_taunt_command()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_taunt_command_no_args()** (4 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **.create_flee_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **Unit tests for combat command factories. Tests the CombatCommandFactory class…** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Test create_attack_command() creates AttackCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Test create_attack_command() allows None target (validation happens later).** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Test create_punch_command() creates PunchCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Test create_punch_command() allows None target (validation happens later).** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- *... and 15 more nodes in this community*

## Relationships

- [server models command base basecommand](server_models_command_base_basecommand.md) (3 shared connections)
- [server models command combat attackcommand](server_models_command_combat_attackcommand.md) (3 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [server game player service playerservice](server_game_player_service_playerservice.md) (1 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (1 shared connections)
- [server models command moderation mutecommand](server_models_command_moderation_mutecommand.md) (1 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`

## Audit Trail

- EXTRACTED: 66 (85%)
- INFERRED: 12 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*