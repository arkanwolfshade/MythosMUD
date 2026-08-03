# command combat models

> 104 nodes

## Key Concepts

- **test_command_combat.py** (31 connections) — `server/tests/unit/models/test_command_combat.py`
- **AttackCommand** (15 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **CombatCommandFactory** (12 connections) — `server/utils/command_factories_combat.py`
- **.create_attack_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_punch_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_kick_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_strike_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **.create_taunt_command()** (5 connections) — `server/utils/command_factories_combat.py`
- **test_attack_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **.create_flee_command()** (4 connections) — `server/utils/command_factories_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **test_attack_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- *... and 79 more nodes in this community*

## Relationships

- [command utility models](command_utility_models.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (10 shared connections)
- [command factories create](command_factories_create.md) (5 shared connections)
- [Security Validator Tests](Security_Validator_Tests.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/utils/command_factories_combat.py`

## Audit Trail

- EXTRACTED: 303 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*