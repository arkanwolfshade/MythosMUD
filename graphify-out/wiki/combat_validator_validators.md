# combat validator validators

> 307 nodes

## Key Concepts

- **NATSService** (120 connections) — `server/services/nats_service.py`
- **test_nats_service.py** (76 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_helpers.py** (54 connections) — `server/tests/unit/services/test_nats_service_helpers.py`
- **nats_exceptions.py** (36 connections) — `server/services/nats_exceptions.py`
- **NATSMetrics** (31 connections) — `server/services/nats_metrics.py`
- **NATSConfig** (26 connections) — `server/config/models/nats.py`
- **nats_service.py** (24 connections) — `server/services/nats_service.py`
- **Any** (17 connections)
- **NATSUnsubscribeError** (14 connections) — `server/services/nats_exceptions.py`
- **NATSRequestError** (11 connections) — `server/services/nats_exceptions.py`
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
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **test_nats_service_init_with_config()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- *... and 282 more nodes in this community*

## Relationships

- [nats exceptions services](nats_exceptions_services.md) (21 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [connection state machine](connection_state_machine.md) (6 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (5 shared connections)
- [commands communication support](commands_communication_support.md) (5 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (4 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (4 shared connections)
- [startup npc services](startup_npc_services.md) (3 shared connections)
- [services combat sync](services_combat_sync.md) (3 shared connections)
- [nats message handler](nats_message_handler.md) (3 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)

## Source Files

- `server/config/models/nats.py`
- `server/services/nats_exceptions.py`
- `server/services/nats_metrics.py`
- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/services/test_nats_service_helpers.py`

## Audit Trail

- EXTRACTED: 992 (97%)
- INFERRED: 33 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*