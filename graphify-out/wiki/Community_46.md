# Community 46

> 137 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatParticipantType** (46 connections) — `server/models/combat.py`
- **CombatParticipantData** (39 connections) — `server/services/combat_types.py`
- **asyncio** (37 connections)
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **TestCombatParticipantData** (12 connections) — `server/tests/unit/services/test_combat_types.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **check_attacker_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **register_combat()** (7 connections) — `server/services/combat_service_start.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- **._get_persistence()** (6 connections) — `server/services/combat_hp_sync.py`
- **get_connection_manager_for_combat_check()** (6 connections) — `server/services/combat_service_start.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 112 more nodes in this community*

## Relationships

- [Combat Cleanup & Results](Combat_Cleanup_&_Results.md) (39 shared connections)
- [Combat Instance Turn Management](Combat_Instance_Turn_Management.md) (15 shared connections)
- [Community 418](Community_418.md) (13 shared connections)
- [Community 275](Community_275.md) (11 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (11 shared connections)
- [Community 261](Community_261.md) (8 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (7 shared connections)
- [Community 97](Community_97.md) (5 shared connections)
- [Combat Events](Combat_Events.md) (5 shared connections)
- [Community 277](Community_277.md) (4 shared connections)
- [Community 60](Community_60.md) (4 shared connections)
- [Community 89](Community_89.md) (4 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/services/combat_types.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 386 (93%)
- INFERRED: 28 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*