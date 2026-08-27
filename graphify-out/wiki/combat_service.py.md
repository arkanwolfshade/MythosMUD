# combat_service.py

> 144 nodes

## Key Concepts

- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (36 connections)
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **check_attacker_grace_period()** (9 connections) — `server/services/combat_service_start.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **broadcast_aggro_target_switches()** (8 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (8 connections) — `server/services/combat_service_events.py`
- **check_target_rest_and_grace_period()** (8 connections) — `server/services/combat_service_start.py`
- *... and 119 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (38 shared connections)
- [models/combat.py](models-combat.py.md) (21 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (20 shared connections)
- [CombatInstance](CombatInstance.md) (19 shared connections)
- [CombatParticipant](CombatParticipant.md) (15 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [NATSError](NATSError.md) (13 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (11 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (7 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (6 shared connections)
- [event_types.py](event_types.py.md) (5 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 495 (94%)
- INFERRED: 33 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*