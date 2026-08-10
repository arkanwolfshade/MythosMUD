# WebSocket Command Handler

> 42 nodes

## Key Concepts

- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **CombatCommandFactory** (12 connections) — `server/utils/command_factories_combat.py`
- **.__init__()** (9 connections) — `server/utils/command_factories.py`
- **FleeCommand** (6 connections) — `server/models/command_combat.py`
- **.create_attack_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_flee_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **test_create_attack_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_attack_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_punch_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_punch_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_kick_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_kick_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_strike_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_strike_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_flee_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_taunt_command()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **test_create_taunt_command_no_args()** (3 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Command for fleeing combat (no target).** (1 connections) — `server/models/command_combat.py`
- **Unit tests for combat command factories.  Tests the CombatCommandFactory class m** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Test create_attack_command() creates AttackCommand.** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **Test create_attack_command() allows None target (validation happens later).** (1 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- *... and 17 more nodes in this community*

## Relationships

- [Environmental Container Scenario](Environmental_Container_Scenario.md) (6 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (4 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (3 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (2 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (1 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (1 shared connections)
- [Base Command Models](Base_Command_Models.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (1 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_combat.py`

## Audit Trail

- EXTRACTED: 121 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*