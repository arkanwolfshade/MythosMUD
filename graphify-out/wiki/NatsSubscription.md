# NatsSubscription

> 32 nodes

## Key Concepts

- **NatsSubscription** (6 connections) — `server/services/nats_service_subscriptions.py`
- **JsonMap** (6 connections)
- **NatsMessageCallback** (5 connections) — `server/services/nats_service_subscriptions.py`
- **._verify_subscription_cleanup()** (5 connections) — `server/services/nats_service_subscriptions.py`
- **.get_connection_stats()** (4 connections) — `server/services/nats_service.py`
- **.publish()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **as_json_map()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._acknowledge_message()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._call_callback()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._decode_message_data()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **Msg** (4 connections)
- **_NatsSubscribeFn** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.get_active_subscriptions()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **._negatively_acknowledge_message()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.__call__()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **JsonMap** (3 connections)
- **Protocol** (3 connections)
- **.__call__()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **.drain()** (1 connections) — `server/services/nats_service_subscriptions.py`
- **.unsubscribe()** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Subscription** (1 connections)
- **Publish a message to a NATS subject using connection pool. Args: subject: NATS…** (1 connections) — `server/services/nats_service.py`
- **Send a request to a NATS subject and wait for a response. Args: subject: NATS…** (1 connections) — `server/services/nats_service.py`
- **Get connection statistics from state machine. Returns: Dictionary with…** (1 connections) — `server/services/nats_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (11 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [NATSService](NATSService.md) (4 shared connections)

## Source Files

- `server/services/nats_service.py`
- `server/services/nats_service_subscriptions.py`

## Audit Trail

- EXTRACTED: 52 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*