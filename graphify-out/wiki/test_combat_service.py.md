# test_combat_service.py

> 20 nodes

## Key Concepts

- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (7 connections) — `server/tests/unit/services/test_combat_service.py`
- **asyncio** (7 connections)
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **Unit tests for CombatService process_attack flow and private helper methods.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **When involuntary flee triggers, combat ends and an early CombatResult is…** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **finalize_attack_result wires target state, events, XP, and completion correctly.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **process_attack returns early CombatResult when melee validation ends combat.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **process_attack orchestrates helper calls and returns the final CombatResult.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **When melee validation passes, helper returns None and does not end combat.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **When melee validation fails, combat is ended and a failure CombatResult is…** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **NPC targets never trigger involuntary flee logic.** (1 connections) — `server/tests/unit/services/test_combat_service.py`

## Relationships

- [CombatService](CombatService.md) (9 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*