# CombatService

> 246 nodes

## Key Concepts

- **CombatService** (175 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **UUID** (21 connections)
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- **publish_combat_started_event()** (9 connections) — `server/services/combat_service_start.py`
- **broadcast_aggro_target_switches()** (8 connections) — `server/services/combat_service_events.py`
- **publish_npc_died_event()** (8 connections) — `server/services/combat_service_events.py`
- *... and 221 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (44 shared connections)
- [get_logger](get_logger.md) (36 shared connections)
- [CombatParticipant](CombatParticipant.md) (18 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (17 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (14 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (14 shared connections)
- [spell_effects.py](spell_effects.py.md) (13 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (12 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (12 shared connections)
- [EventBus](EventBus.md) (10 shared connections)
- [NATSPublishError](NATSPublishError.md) (6 shared connections)
- [NATSError](NATSError.md) (6 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_start.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 559 (83%)
- INFERRED: 117 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*