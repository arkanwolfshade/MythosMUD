# NATS

> 105 nodes

## Key Concepts

- **NATSService** (71 connections) — `server/services/nats_service.py`
- **Any** (17 connections)
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
- **._build_connect_options()** (4 connections) — `server/services/nats_service.py`
- **._configure_tls()** (4 connections) — `server/services/nats_service.py`
- **._close_all_subscriptions()** (4 connections) — `server/services/nats_service.py`
- **._health_check_loop()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- *... and 80 more nodes in this community*

## Relationships

- [nats config()](nats_config%28%29.md) (15 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [Any](Any.md) (5 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (5 shared connections)
- [NATSMetrics](NATSMetrics.md) (2 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (2 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [connection state machine](connection_state_machine.md) (1 shared connections)
- [message broker](message_broker.md) (1 shared connections)
- [metrics](metrics.md) (1 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 346 (97%)
- INFERRED: 10 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*