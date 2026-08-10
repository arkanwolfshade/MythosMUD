# Environmental Container Scenario

> 84 nodes

## Key Concepts

- **test_command_combat.py** (30 connections) — `server/tests/unit/models/test_command_combat.py`
- **command_combat.py** (14 connections) — `server/models/command_combat.py`
- **AttackCommand** (14 connections) — `server/models/command_combat.py`
- **PunchCommand** (14 connections) — `server/models/command_combat.py`
- **KickCommand** (14 connections) — `server/models/command_combat.py`
- **StrikeCommand** (14 connections) — `server/models/command_combat.py`
- **validate_combat_target()** (14 connections) — `server/validators/security_validator.py`
- **TauntCommand** (7 connections) — `server/models/command_combat.py`
- **test_attack_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_punch_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_kick_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_min_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_strike_command_target_max_length()** (4 connections) — `server/tests/unit/models/test_command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **.validate_target()** (3 connections) — `server/models/command_combat.py`
- **test_attack_command_default_values()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_with_target()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_validate_target_calls_validator()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- **test_attack_command_validate_target_none()** (3 connections) — `server/tests/unit/models/test_command_combat.py`
- *... and 59 more nodes in this community*

## Relationships

- [Chat Panel Components](Chat_Panel_Components.md) (8 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (8 shared connections)
- [Emote Schema Validator](Emote_Schema_Validator.md) (7 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (6 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (6 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (6 shared connections)

## Source Files

- `server/models/command_combat.py`
- `server/tests/unit/models/test_command_combat.py`
- `server/tests/unit/validators/test_security_validator.py`
- `server/validators/security_validator.py`

## Audit Trail

- EXTRACTED: 254 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*