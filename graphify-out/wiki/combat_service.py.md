# combat_service.py

> 251 nodes

## Key Concepts

- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **test_combat_service_modules.py** (64 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **models/combat.py** (60 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatParticipantType** (45 connections) — `server/models/combat.py`
- **asyncio** (37 connections)
- **combat_service_start.py** (29 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **CombatResult** (22 connections) — `server/models/combat.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **combat_attack_handler.py** (22 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **_combat_instance()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **_dp_sync()** (14 connections) — `server/tests/unit/services/test_combat_service_modules.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **CombatDPSync** (12 connections) — `server/services/combat_hp_sync.py`
- **combat_service_end.py** (12 connections) — `server/services/combat_service_end.py`
- **test_combat_turn_participant_actions.py** (12 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **finalize_attack_result()** (11 connections) — `server/services/combat_service_attack.py`
- *... and 226 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (68 shared connections)
- [CombatParticipant](CombatParticipant.md) (62 shared connections)
- [CombatService](CombatService.md) (47 shared connections)
- [get_logger](get_logger.md) (36 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (33 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (19 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (14 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (13 shared connections)
- [NATSError](NATSError.md) (13 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (8 shared connections)
- [event_types.py](event_types.py.md) (8 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_hp_sync.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_end.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_service_modules.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 862 (95%)
- INFERRED: 48 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*