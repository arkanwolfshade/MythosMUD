# Server Services (68)

> 23 nodes

## Key Concepts

- **CombatResult** (23 connections) — `server/models/combat.py`
- **test_combat_service.py** (18 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_participant()** (10 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_combat_instance()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **_make_service()** (9 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_validate_melee_or_end_combat_ends_combat_on_invalid()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_returns_early_result_on_flee()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_finalize_attack_result_awards_xp_and_completes_combat()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_returns_melee_validation_early_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_process_attack_happy_path_calls_helpers_and_returns_final_result()** (6 connections) — `server/tests/unit/services/test_combat_service.py`
- **.apply_damage_and_check_involuntary_flee()** (5 connections) — `server/services/combat_service.py`
- **test_validate_melee_or_end_combat_returns_none_on_valid()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **test_apply_damage_and_check_involuntary_flee_no_flee_for_npc()** (5 connections) — `server/tests/unit/services/test_combat_service.py`
- **Result of a combat action.** (1 connections) — `server/models/combat.py`
- **Apply attack damage and check for involuntary flee.** (1 connections) — `server/services/combat_service.py`
- **Unit tests for CombatService process_attack flow and private helper methods.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **When melee validation passes, helper returns None and does not end combat.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **When melee validation fails, combat is ended and a failure CombatResult is retur** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **NPC targets never trigger involuntary flee logic.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **When involuntary flee triggers, combat ends and an early CombatResult is returne** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **finalize_attack_result wires target state, events, XP, and completion correctly.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **process_attack returns early CombatResult when melee validation ends combat.** (1 connections) — `server/tests/unit/services/test_combat_service.py`
- **process_attack orchestrates helper calls and returns the final CombatResult.** (1 connections) — `server/tests/unit/services/test_combat_service.py`

## Relationships

- [Server Services (29)](Server_Services_%2829%29.md) (7 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (6 shared connections)
- [Server Services (4)](Server_Services_%284%29.md) (5 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (4 shared connections)
- [Server Models (2)](Server_Models_%282%29.md) (3 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (3 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_service.py`
- `server/tests/unit/services/test_combat_service.py`

## Audit Trail

- EXTRACTED: 118 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*