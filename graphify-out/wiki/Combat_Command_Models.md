# Combat Command Models

> 68 nodes · cohesion 0.05

## Key Concepts

- **test_command_combat.py** (29 connections) — `server/tests/unit/models/test_command_combat.py`
- **AttackCommand** (14 connections) — `server/models/command_combat.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **validate_combat_target()** (14 connections) — `server/validators/security_validator.py`
- **Validate combat target name format using centralized validation.** (5 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **test_attack_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_target_max_length()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_target_min_length()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_validate_target_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_validate_target_none()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_max_length()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_min_length()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_validate_target_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_validate_target_none()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- *... and 43 more nodes in this community*

## Relationships

- [[Base Command Models]] (24 shared connections)
- [[Command Field Validators]] (7 shared connections)
- [[Moderation Command Models]] (1 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 232 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
