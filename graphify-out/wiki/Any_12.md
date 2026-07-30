# Any

> 251 nodes

## Key Concepts

- **NATSError** (101 connections) — `server/services/nats_exceptions.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **nats_exceptions.py** (33 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **combat_service_events.py** (14 connections) — `server/services/combat_service_events.py`
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **CombatEndedEvent** (12 connections) — `server/events/combat_events.py`
- **NATSUnsubscribeError** (12 connections) — `server/services/nats_exceptions.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **._create_event_message()** (11 connections) — `server/services/combat_event_publisher.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
- *... and 226 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (51 shared connections)
- [circuit breaker](circuit_breaker.md) (44 shared connections)
- [BaseUserManager](BaseUserManager.md) (18 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (15 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (14 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (12 shared connections)
- [world](world.md) (12 shared connections)
- [combat initialization](combat_initialization.md) (11 shared connections)
- [test combat persistence handler persistence](test_combat_persistence_handler_persistence.md) (10 shared connections)
- [test nats message handler subzone](test_nats_message_handler_subzone.md) (8 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (6 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (6 shared connections)

## Source Files

- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_service_events.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 945 (85%)
- INFERRED: 168 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*