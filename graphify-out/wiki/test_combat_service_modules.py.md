# test_combat_service_modules.py

> 117 nodes

## Key Concepts

- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (37 connections)
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- **apply_target_rest_and_grace_checks()** (11 connections) — `server/services/combat_service_start.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **UUID** (8 connections)
- **._persist_player_dp_sync()** (7 connections) — `server/services/combat_hp_sync.py`
- **process_attack()** (7 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (7 connections) — `server/services/combat_service_attack.py`
- **._get_persistence()** (6 connections) — `server/services/combat_hp_sync.py`
- **_effective_room_for_melee()** (6 connections) — `server/services/combat_service_attack.py`
- **test_apply_damage_and_check_involuntary_flee_suppresses_non_damaging_phantom()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_and_process_attack()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **test_finalize_attack_result_phantom_dissipation()** (6 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- *... and 92 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (45 shared connections)
- [CombatInstance](CombatInstance.md) (13 shared connections)
- [CombatParticipant](CombatParticipant.md) (11 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [NATSError](NATSError.md) (7 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (7 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (6 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (5 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (3 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (3 shared connections)
- [combat_attack.py](combat_attack.py.md) (2 shared connections)
- [CombatTurnProcessor](CombatTurnProcessor.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 333 (95%)
- INFERRED: 18 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*