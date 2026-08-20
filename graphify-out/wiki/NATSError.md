# NATSError

> 254 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **test_combat_event_publisher.py** (55 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **CombatEventPublisher** (34 connections) — `server/services/combat_event_publisher.py`
- **NATSPublishError** (34 connections) — `server/services/nats_exceptions.py`
- **PlayerDiedEvent** (31 connections) — `server/events/event_types.py`
- **PlayerDPDecayEvent** (29 connections) — `server/events/event_types.py`
- **combat_integration.py** (27 connections) — `server/npc/combat_integration.py`
- **combat_event_publisher.py** (26 connections) — `server/services/combat_event_publisher.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **CombatDeathHandler** (22 connections) — `server/services/combat_death_handler.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
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
- **NATSConnectionError** (14 connections) — `server/services/nats_exceptions.py`
- **test_nats_exceptions.py** (14 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **CombatEndedEvent** (13 connections) — `server/events/combat_events.py`
- **_CombatPublishJob** (13 connections) — `server/services/combat_event_publisher.py`
- *... and 229 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (56 shared connections)
- [EventBus](EventBus.md) (22 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (18 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (14 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (12 shared connections)
- [get_logger](get_logger.md) (12 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (10 shared connections)
- [CombatInstance](CombatInstance.md) (10 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (9 shared connections)
- [player_event_handlers.py](player_event_handlers.py.md) (9 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (9 shared connections)
- [CombatParticipant](CombatParticipant.md) (9 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/events/event_types.py`
- `server/npc/combat_integration.py`
- `server/npc/combat_integration_protocols.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service.py`
- `server/services/combat_service_events.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 651 (86%)
- INFERRED: 107 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*