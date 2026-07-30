# message broker

> 131 nodes

## Key Concepts

- **test_nats_broker.py** (49 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **NATSMessageBroker** (30 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker.py** (17 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (9 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (6 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_error_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **Any** (3 connections)
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- *... and 106 more nodes in this community*

## Relationships

- [MapZoneContext](MapZoneContext.md) (6 shared connections)
- [init](init.md) (2 shared connections)
- [BaseModel](BaseModel.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [FollowTargetValue](FollowTargetValue.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)
- [get subject manager dependency()](get_subject_manager_dependency%28%29.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 360 (92%)
- INFERRED: 30 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*