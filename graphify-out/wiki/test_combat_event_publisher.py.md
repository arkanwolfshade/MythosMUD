# test_combat_event_publisher.py

> 164 nodes

## Key Concepts

- **test_combat_event_publisher.py** (54 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (30 connections) — `server/services/combat_event_handler.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **asyncio** (20 connections)
- **test_combat_event_handler.py** (19 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **CombatStartedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **CombatTargetSwitchEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerMortallyWoundedEvent** (15 connections) — `server/events/event_types.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- **_participant()** (13 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **test_publish_paths_nats_publish_error()** (13 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **NPCAttackedEvent** (11 connections) — `server/events/combat_events.py`
- **test_publish_paths_no_nats_service()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **test_publish_paths_not_connected()** (11 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **._publish_attack_events()** (9 connections) — `server/services/combat_event_handler.py`
- **asyncio** (9 connections)
- **.handle_attack_events_and_xp()** (7 connections) — `server/services/combat_event_handler.py`
- **.publish_combat_ended()** (5 connections) — `server/services/combat_event_publisher.py`
- *... and 139 more nodes in this community*

## Relationships

- [combat_service.py](combat_service.py.md) (33 shared connections)
- [event_types.py](event_types.py.md) (15 shared connections)
- [CombatService](CombatService.md) (10 shared connections)
- [EventBus](EventBus.md) (9 shared connections)
- [NATSError](NATSError.md) (7 shared connections)
- [CombatParticipant](CombatParticipant.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (2 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 393 (89%)
- INFERRED: 48 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*