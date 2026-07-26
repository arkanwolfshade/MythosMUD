# NATSMessageBroker

> 27 nodes · cohesion 0.10

## Key Concepts

- **NATSMessageBroker** (30 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_error_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._perform_health_check()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._reconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception** (2 connections)
- **Connect to NATS server.          Returns:             bool: True if connection s** (1 connections) — `server/infrastructure/nats_broker.py`
- **NATS implementation of MessageBroker protocol.      This class wraps NATS client** (1 connections) — `server/infrastructure/nats_broker.py`
- **Handle NATS errors.          AI: Runs as fire-and-forget async task to prevent b** (1 connections) — `server/infrastructure/nats_broker.py`
- **Async handler for NATS connection errors.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Handle NATS disconnection.          AI: Runs as fire-and-forget async task to pr** (1 connections) — `server/infrastructure/nats_broker.py`
- **Async handler for NATS disconnection events.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Handle NATS reconnection.          AI: Runs as fire-and-forget async task to pre** (1 connections) — `server/infrastructure/nats_broker.py`
- **Async handler for NATS reconnection events.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Start periodic health check monitoring task.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Periodic health check loop using ping/pong.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Perform a single health check via flush.          Returns:             True if h** (1 connections) — `server/infrastructure/nats_broker.py`
- *... and 2 more nodes in this community*

## Relationships

- [.publish](publish.md) (6 shared connections)
- [MessageBrokerError](MessageBrokerError.md) (4 shared connections)
- [UnsubscribeError](UnsubscribeError.md) (4 shared connections)
- [test_nats_broker.py](test_nats_broker.py.md) (3 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (2 shared connections)
- [PublishError](PublishError.md) (1 shared connections)
- [SubscribeError](SubscribeError.md) (1 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 84 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*