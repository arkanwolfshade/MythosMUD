# CombatCommandFactory

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

- [BaseCommand](BaseCommand.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [CommunicationCommandFactory](CommunicationCommandFactory.md) (1 shared connections)
- [ExplorationCommandFactory](ExplorationCommandFactory.md) (1 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (1 shared connections)
- [ModerationCommandFactory](ModerationCommandFactory.md) (1 shared connections)
- [PlayerStateCommandFactory](PlayerStateCommandFactory.md) (1 shared connections)
- [UtilityCommandFactory](UtilityCommandFactory.md) (1 shared connections)

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