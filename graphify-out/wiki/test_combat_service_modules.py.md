# test_combat_service_modules.py

> 156 nodes

## Key Concepts

- **test_combat_service_modules.py** (65 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **asyncio** (38 connections)
- **CombatResult** (32 connections) — `server/models/combat.py`
- **combat_service_attack.py** (32 connections) — `server/services/combat_service_attack.py`
- **_NPCCombatIntegrationDeps** (19 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **apply_target_rest_and_grace_checks()** (14 connections) — `server/services/combat_service_start.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatDPSync** (13 connections) — `server/services/combat_hp_sync.py`
- **finalize_attack_result()** (12 connections) — `server/services/combat_service_attack.py`
- **_participant()** (11 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **handle_combat_completion()** (10 connections) — `server/services/combat_service_attack.py`
- **.join_player_to_combat()** (10 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **_attack_participant()** (10 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **UUID** (10 connections)
- **apply_damage_and_check_involuntary_flee()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_location()** (9 connections) — `server/services/combat_service_attack.py`
- **validate_melee_or_end_combat()** (9 connections) — `server/services/combat_service_attack.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **.join_existing_combat_for_mixin()** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **._process_combat_attack()** (9 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **UUID** (9 connections)
- **process_attack()** (8 connections) — `server/services/combat_service_attack.py`
- **queue_combat_action()** (8 connections) — `server/services/combat_service_attack.py`
- *... and 131 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (59 shared connections)
- [CombatInstance](CombatInstance.md) (21 shared connections)
- [CombatParticipant](CombatParticipant.md) (13 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (8 shared connections)
- [test_n_player_combat.py](test_n_player_combat.py.md) (7 shared connections)
- [NATSError](NATSError.md) (7 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [NpcDisposition](NpcDisposition.md) (4 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (3 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (3 shared connections)
- [SuccessLevel](SuccessLevel.md) (3 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/models/combat.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_start.py`
- `server/services/npc_combat_integration_combat_mixin.py`
- `server/tests/unit/services/test_combat_service_modules.py`

## Audit Trail

- EXTRACTED: 442 (95%)
- INFERRED: 25 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*