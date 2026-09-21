# test_combat_service_modules.py

> 116 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (13 connections) — `server/services/combat_hp_sync.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **UUID** (9 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **end_combat()** (7 connections) — `server/services/combat_service_end.py`
- **validate_combat_can_start()** (7 connections) — `server/services/combat_service_start.py`
- **._get_persistence()** (6 connections) — `server/services/combat_hp_sync.py`
- **._publish_correction_to_event_bus()** (6 connections) — `server/services/combat_hp_sync.py`
- **._publish_player_dp_correction_event()** (6 connections) — `server/services/combat_hp_sync.py`
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 91 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (31 shared connections)
- [CombatService](CombatService.md) (17 shared connections)
- [CombatInstance](CombatInstance.md) (13 shared connections)
- [CombatParticipant](CombatParticipant.md) (12 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (12 shared connections)
- [NATSError](NATSError.md) (6 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [PlayerDPUpdated](PlayerDPUpdated.md) (2 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/services/combat_hp_sync.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 316 (95%)
- INFERRED: 16 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*