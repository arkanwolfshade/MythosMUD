# CombatService

> 353 nodes

## Key Concepts

- **CombatService** (181 connections) — `server/services/combat_service.py`
- **combat_service.py** (100 connections) — `server/services/combat_service.py`
- **models/combat.py** (50 connections) — `server/models/combat.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatParticipantData** (36 connections) — `server/services/combat_types.py`
- **CombatParticipantType** (35 connections) — `server/models/combat.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **combat_service_attack.py** (26 connections) — `server/services/combat_service_attack.py`
- **combat_event_publisher.py** (22 connections) — `server/services/combat_event_publisher.py`
- **CombatResult** (20 connections) — `server/models/combat.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **UUID** (20 connections)
- **combat_turn_processor.py** (19 connections) — `server/services/combat_turn_processor.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **npc_combat_data_provider.py** (18 connections) — `server/services/npc_combat_data_provider.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **.create_combat_instance()** (17 connections) — `server/services/combat_initialization.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **npc_combat_integration_combat_mixin.py** (16 connections) — `server/services/npc_combat_integration_combat_mixin.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **TestCombatInitializer** (15 connections) — `server/tests/unit/services/test_combat_initialization.py`
- *... and 328 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (57 shared connections)
- [CombatInstance](CombatInstance.md) (55 shared connections)
- [CombatParticipant](CombatParticipant.md) (43 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (39 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (36 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (30 shared connections)
- [NATSService](NATSService.md) (27 shared connections)
- [TargetMatch](TargetMatch.md) (18 shared connections)
- [spell_effects_heal.py](spell_effects_heal.py.md) (16 shared connections)
- [build_event](build_event.md) (16 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (9 shared connections)
- [test_combat_service.py](test_combat_service.py.md) (9 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/combat.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_initialization.py`
- `server/services/combat_service.py`
- `server/services/combat_service_attack.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_start.py`
- `server/services/combat_service_state.py`
- `server/services/combat_service_types.py`
- `server/services/combat_turn_processor.py`
- `server/services/combat_types.py`
- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_combat_mixin.py`

## Audit Trail

- EXTRACTED: 1633 (95%)
- INFERRED: 89 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*