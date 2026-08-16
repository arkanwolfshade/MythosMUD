# CombatInstance

> 486 nodes

## Key Concepts

- **CombatInstance** (174 connections) — `server/models/combat.py`
- **CombatService** (165 connections) — `server/services/combat_service.py`
- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_service.py** (99 connections) — `server/services/combat_service.py`
- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **models/combat.py** (57 connections) — `server/models/combat.py`
- **combat_turn_participant_actions.py** (47 connections) — `server/services/combat_turn_participant_actions.py`
- **CombatParticipantType** (44 connections) — `server/models/combat.py`
- **CombatParticipantData** (37 connections) — `server/services/combat_types.py`
- **nats_exceptions.py** (37 connections) — `server/services/nats_exceptions.py`
- **combat_service_npc.py** (31 connections) — `server/services/combat_service_npc.py`
- **test_combat_service_npc_helpers.py** (31 connections) — `server/tests/unit/services/test_combat_service_npc_helpers.py`
- **combat_service_attack.py** (28 connections) — `server/services/combat_service_attack.py`
- **combat_service_start.py** (28 connections) — `server/services/combat_service_start.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_death_handler.py** (22 connections) — `server/services/combat_death_handler.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **UUID** (20 connections)
- **CombatAttackHandler** (19 connections) — `server/services/combat_attack_handler.py`
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **npc_combat_integration_combat_mixin.py** (18 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **get_combat_id_for_npc()** (17 connections) — `server/services/combat_service_npc.py`
- *... and 461 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (119 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (51 shared connections)
- [TargetMatch](TargetMatch.md) (50 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (43 shared connections)
- [get_logger](get_logger.md) (41 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (31 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (26 shared connections)
- [test_combat_flee_handler.py](test_combat_flee_handler.py.md) (22 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (17 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (17 shared connections)
- [NATSPublishError](NATSPublishError.md) (17 shared connections)
- [reset_config](reset_config.md) (15 shared connections)

## Source Files

- `server/app/lifespan_startup.py`
- `server/config/__init__.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`

## Audit Trail

- EXTRACTED: 1509 (90%)
- INFERRED: 165 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*