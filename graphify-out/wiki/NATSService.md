# NATSService

> 97 nodes

## Key Concepts

- **NATSService** (72 connections) — `server/services/nats_service.py`
- **Any** (17 connections)
- **.disconnect()** (10 connections) — `server/services/nats_service.py`
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **.connect()** (8 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **.__init__()** (7 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._verify_subscription_cleanup()** (6 connections) — `server/services/nats_service.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service.py`
- **._start_health_monitoring()** (5 connections) — `server/services/nats_service.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service.py`
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **._return_connection()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- *... and 72 more nodes in this community*

## Relationships

- [event_types.py](event_types.py.md) (15 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (4 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [test_nats_service_init_with_subject_manager](test_nats_service_init_with_subject_manager.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [CombatEventPublisher](CombatEventPublisher.md) (2 shared connections)
- [NATSMetrics](NATSMetrics.md) (2 shared connections)
- [nats_service](nats_service.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (1 shared connections)
- [NATSConfig](NATSConfig.md) (1 shared connections)
- [NATSSubjectManager](NATSSubjectManager.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 177 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*