# Server Models (7)

> 104 nodes

## Key Concepts

- **test_command_combat.py** (30 connections) — `server/tests/unit/models/test_command_combat.py`
- **AttackCommand** (14 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **test_command_factories_combat.py** (14 connections) — `server/tests/unit/utils/test_command_factories_combat.py`
- **validate_combat_target()** (14 connections) — `server/validators/security_validator.py`
- **Validate combat target name format using centralized validation.** (5 connections) — `server/models/command_combat.py`
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
- *... and 79 more nodes in this community*

## Relationships

- [Server Models](Server_Models.md) (17 shared connections)
- [Server Utils (2)](Server_Utils_%282%29.md) (12 shared connections)
- [Server Utils](Server_Utils.md) (8 shared connections)
- [Server Validators](Server_Validators.md) (7 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/utils/test_command_factories_combat.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/utils/command_factories_combat.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 327 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*