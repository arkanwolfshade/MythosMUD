# CombatService

> 343 nodes

## Key Concepts

- **CombatService** (173 connections) — `server/services/combat_service.py`
- **combat_service.py** (104 connections) — `server/services/combat_service.py`
- **test_combat_event_publisher.py** (55 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **CombatPersistenceHandler** (22 connections) — `server/services/combat_persistence_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **UUID** (20 connections)
- **asyncio** (20 connections)
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **.connection_manager()** (14 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- *... and 318 more nodes in this community*

## Relationships

- [CombatInstance](CombatInstance.md) (83 shared connections)
- [NATSError](NATSError.md) (67 shared connections)
- [CombatParticipant](CombatParticipant.md) (30 shared connections)
- [PlayerEnteredRoom](PlayerEnteredRoom.md) (23 shared connections)
- [get_logger](get_logger.md) (22 shared connections)
- [TargetMatch](TargetMatch.md) (19 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (14 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (13 shared connections)
- [EventBus](EventBus.md) (12 shared connections)
- [event_types.py](event_types.py.md) (11 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (9 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_initialization.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_persistence_handler.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_combat_service_npc_in_combat.py`

## Audit Trail

- EXTRACTED: 836 (85%)
- INFERRED: 145 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*