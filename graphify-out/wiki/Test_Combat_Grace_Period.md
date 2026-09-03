# Test Combat Grace Period

> 18 nodes

## Key Concepts

- **test_combat_grace_period.py** (12 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_blocked_during_grace_period()** (5 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_works_when_not_in_grace_period()** (5 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_allowed_after_grace_period()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_blocked_when_incapacitated()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **asyncio** (4 connections)
- **mock_connection_manager()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **fixture** (3 connections)
- **Unit tests for combat command blocking during login grace period. Tests that…** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Test that attack commands work when player is not in grace period.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Attack command returns incapacitated message when player has 0 to -9 DP (prone,…** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Create a mock ConnectionManager.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Create a mock FastAPI request.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Test that attack commands are blocked during login grace period.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Test that attack commands work normally after grace period expires.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`

## Relationships

- [Combat Handler](Combat_Handler.md) (4 shared connections)
- [Test Login Grace Period](Test_Login_Grace_Period.md) (3 shared connections)
- [Game State Provider](Game_State_Provider.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_combat_grace_period.py`

## Audit Trail

- EXTRACTED: 28 (88%)
- INFERRED: 4 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*