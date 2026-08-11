# Status Effect Model

> 16 nodes

## Key Concepts

- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_blocked_during_grace_period()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_works_when_not_in_grace_period()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_allowed_after_grace_period()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_blocked_when_incapacitated()** (3 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Unit tests for combat command blocking during login grace period.  Tests that co** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Create a mock ConnectionManager.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Create a mock FastAPI request.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Test that attack commands are blocked during login grace period.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Test that attack commands work normally after grace period expires.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Test that attack commands work when player is not in grace period.** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **Attack command returns incapacitated message when player has 0 to -9 DP (prone,** (1 connections) — `server/tests/unit/commands/test_combat_grace_period.py`

## Relationships

- [Player Respawn Events](Player_Respawn_Events.md) (5 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (4 shared connections)

## Source Files

- `server/tests/unit/commands/test_combat_grace_period.py`

## Audit Trail

- EXTRACTED: 35 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*