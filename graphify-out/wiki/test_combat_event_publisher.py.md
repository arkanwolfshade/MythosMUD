# test_combat_event_publisher.py

> 185 nodes

## Key Concepts

- **test_combat_event_publisher.py** (55 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **CombatEventHandler** (30 connections) — `server/services/combat_event_handler.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **test_combat_event_handler.py** (20 connections) — `server/tests/unit/services/test_combat_event_handler.py`
- **asyncio** (20 connections)
- **combat_event_handler.py** (18 connections) — `server/services/combat_event_handler.py`
- **._publish_combat_payload()** (17 connections) — `server/services/combat_event_publisher.py`
- **NPCDiedEvent** (16 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (16 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (16 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (16 connections) — `server/services/combat_service_events.py`
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
- **publish_npc_damage_event()** (9 connections) — `server/services/combat_service_events.py`
- *... and 160 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (40 shared connections)
- [event_types.py](event_types.py.md) (17 shared connections)
- [CombatParticipant](CombatParticipant.md) (15 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (10 shared connections)
- [EventBus](EventBus.md) (8 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [NATSError](NATSError.md) (6 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (6 shared connections)
- [NATSService](NATSService.md) (6 shared connections)
- [NATSPublishError](NATSPublishError.md) (5 shared connections)
- [CombatInstance](CombatInstance.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (3 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/tests/unit/services/test_combat_event_handler.py`
- `server/tests/unit/services/test_combat_event_publisher.py`

## Audit Trail

- EXTRACTED: 455 (89%)
- INFERRED: 54 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*