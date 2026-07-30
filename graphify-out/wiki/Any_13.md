# Any

> 316 nodes

## Key Concepts

- **NATSError** (101 connections) — `server/services/nats_exceptions.py`
- **test_combat_event_publisher.py** (37 connections) — `server/tests/unit/services/test_combat_event_publisher.py`
- **.get_instance()** (34 connections) — `server/container/main.py`
- **nats_exceptions.py** (33 connections) — `server/services/nats_exceptions.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **CombatEventPublisher** (27 connections) — `server/services/combat_event_publisher.py`
- **combat_service_start.py** (27 connections) — `server/services/combat_service_start.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **nats_service.py** (23 connections) — `server/services/nats_service.py`
- **combat_death_handler.py** (21 connections) — `server/services/combat_death_handler.py`
- **combat_event_publisher.py** (21 connections) — `server/services/combat_event_publisher.py`
- **combat_events.py** (20 connections) — `server/events/combat_events.py`
- **NPCDiedEvent** (18 connections) — `server/events/combat_events.py`
- **CombatDeathHandler** (18 connections) — `server/services/combat_death_handler.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **combat_event_handler.py** (17 connections) — `server/services/combat_event_handler.py`
- **CombatEventHandler** (17 connections) — `server/services/combat_event_handler.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **CombatStartedEvent** (15 connections) — `server/events/combat_events.py`
- **PlayerAttackedEvent** (15 connections) — `server/events/combat_events.py`
- **NPCTookDamageEvent** (15 connections) — `server/events/combat_events.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- *... and 291 more nodes in this community*

## Relationships

- [. initialize handlers()](_initialize_handlers%28%29.md) (44 shared connections)
- [circuit breaker](circuit_breaker.md) (44 shared connections)
- [close db()](close_db%28%29.md) (37 shared connections)
- [BaseUserManager](BaseUserManager.md) (18 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (15 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (15 shared connections)
- [world](world.md) (14 shared connections)
- [Room](Room.md) (13 shared connections)
- [test combat persistence handler persistence](test_combat_persistence_handler_persistence.md) (12 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (12 shared connections)
- [combat initialization](combat_initialization.md) (11 shared connections)
- [test nats message handler subzone](test_nats_message_handler_subzone.md) (8 shared connections)

## Source Files

- `server/container/main.py`
- `server/events/combat_events.py`
- `server/npc/combat_integration_protocols.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_event_handler.py`
- `server/services/combat_event_publisher.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/combat_service_start.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 1206 (85%)
- INFERRED: 215 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*