# test_damage_grace_period.py

> 24 nodes

## Key Concepts

- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_positive_status_effect_allowed_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_npc_damage_blocked_during_grace_period()** (5 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **player_participant()** (4 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **asyncio** (4 connections)
- **fixture** (4 connections)
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_combat_service()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_allowed_after_grace_period()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **test_apply_damage_fails_open_on_error()** (3 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Unit tests for damage blocking during login grace period. Tests that damage and…** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage application fails open if grace period check errors.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that NPC damage is blocked when target is in login grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that negative status effects are blocked during grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that positive status effects (buffs) are allowed during grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a mock ConnectionManager.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a mock combat service.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a mock combat instance.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Create a player combat participant.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage is blocked when target is in login grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **Test that damage is applied normally after grace period.** (1 connections) — `server/tests/unit/services/test_damage_grace_period.py`

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [Spell](Spell.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [combat_service.py](combat_service.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (1 shared connections)
- [spell_effects.py](spell_effects.py.md) (1 shared connections)
- [server/models/game.py](server-models-game.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*