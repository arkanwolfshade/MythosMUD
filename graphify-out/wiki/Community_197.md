# Community 197

> 74 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (38 connections)
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_target_rest_and_grace_checks()** (13 connections) — `server/services/combat_service_start.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (8 connections) — `server/services/combat_service_attack.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_damage_and_check_involuntary_flee()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_cancels_rest()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_allows_disconnect_grace_target()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_interrupts_ground_channel()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_apply_target_rest_grace_raises_on_grace_period()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_attacker_grace_period_raises()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_check_target_rest_skips_non_player()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_combat_dp_sync_persist_background_persistence_failure_sends_correction()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_end_combat_full_flow()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_handles_errors()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_publish_combat_started_event_success()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_register_combat_delegates_to_service()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_ok()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_validate_combat_can_start_raises_when_in_combat()** (5 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 49 more nodes in this community*

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (35 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (6 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (4 shared connections)
- [Combat Participants](Combat_Participants.md) (3 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (2 shared connections)
- [Community 76](Community_76.md) (2 shared connections)
- [Community 697](Community_697.md) (2 shared connections)
- [Community 273](Community_273.md) (1 shared connections)
- [Community 226](Community_226.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 63](Community_63.md) (1 shared connections)
- [Community 65](Community_65.md) (1 shared connections)

## Source Files

- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 206 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*