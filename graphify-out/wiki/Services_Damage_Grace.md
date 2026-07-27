# Services Damage Grace

> 20 nodes · cohesion 0.10

## Key Concepts

- **test_damage_grace_period.py** (20 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_negative_status_effect_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_blocked_during_grace_period()** (4 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **player_participant()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_allowed_after_grace_period()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_fails_open_on_error()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_combat()** (2 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_connection_manager()** (2 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Unit tests for damage blocking during login grace period.  Tests that damage and** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage application fails open if grace period check errors.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that negative status effects are blocked during grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that positive status effects (buffs) are allowed during grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a mock ConnectionManager.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a mock combat service.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a mock combat instance.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a player combat participant.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage is blocked when target is in login grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage is applied normally after grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`

## Relationships

- [[Look Command Helpers]] (4 shared connections)
- [[Combat Command Handler]] (4 shared connections)
- [[Combat Service Bundle]] (4 shared connections)
- [[Spell Effect Protocols]] (3 shared connections)
- [[Combat Taunt Tests]] (3 shared connections)
- [[NPC Services Bundle]] (2 shared connections)
- [[Game Magic Spell]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
