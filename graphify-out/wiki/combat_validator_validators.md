# combat validator validators

> 168 nodes

## Key Concepts

- **NATSService** (120 connections) — `server/services/nats_service.py`
- **test_nats_service_helpers.py** (54 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **NATSConfig** (26 connections) — `server/config/models/nats.py`
- **nats_service.py** (24 connections) — `server/services/nats_service.py`
- **Any** (17 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **.disconnect()** (11 connections) — `server/services/nats_service.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- *... and 143 more nodes in this community*

## Relationships

- [nats services service](nats_services_service.md) (18 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (11 shared connections)
- [models npc rationale](models_npc_rationale.md) (6 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (4 shared connections)
- [motd loader rationale](motd_loader_rationale.md) (4 shared connections)
- [connection state machine](connection_state_machine.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (2 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)
- [admin command setstat](admin_command_setstat.md) (2 shared connections)
- [infrastructure nats broker](infrastructure_nats_broker.md) (2 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 620 (97%)
- INFERRED: 18 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*