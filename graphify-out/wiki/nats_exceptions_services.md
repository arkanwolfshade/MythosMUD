# nats exceptions services

> 170 nodes

## Key Concepts

- **NATSService** (71 connections) — `server/services/nats_service.py`
- **NATSPublishError** (32 connections) — `server/services/nats_exceptions.py`
- **NATSSubscribeError** (27 connections) — `server/services/nats_exceptions.py`
- **NATSConnectionError** (18 connections) — `server/services/nats_exceptions.py`
- **NATSHealthCheckError** (17 connections) — `server/services/nats_exceptions.py`
- **Any** (17 connections)
- **test_nats_exceptions.py** (13 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **TestNATSConnectionError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSPublishError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSSubscribeError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestNATSHealthCheckError** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **TestExceptionHierarchy** (11 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **TestNATSError** (9 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_exceptions.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **.test_all_errors_inherit_from_nats_error()** (7 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **Exception** (6 connections)
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **.test_all_errors_inherit_from_exception()** (6 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- *... and 145 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (41 shared connections)
- [nats services service](nats_services_service.md) (11 shared connections)
- [NATS Messaging](NATS_Messaging.md) (5 shared connections)
- [config models rationale](config_models_rationale.md) (4 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [command factories exploration](command_factories_exploration.md) (2 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [nats message handler](nats_message_handler.md) (1 shared connections)
- [game room service](game_room_service.md) (1 shared connections)
- [room game service](room_game_service.md) (1 shared connections)

## Source Files

- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_combat_event_publisher.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 565 (88%)
- INFERRED: 78 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*