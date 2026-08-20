# JsonMap

> 32 nodes

## Key Concepts

- **JsonMap** (9 connections)
- **_NatsListenerClient** (5 connections) — `server/services/nats_service.py`
- **NatsMessageCallback** (5 connections) — `server/services/nats_service.py`
- **_NatsSubscription** (4 connections) — `server/services/nats_service.py`
- **._acknowledge_message()** (4 connections) — `server/services/nats_service.py`
- **._call_callback()** (4 connections) — `server/services/nats_service.py`
- **._decode_message_data()** (4 connections) — `server/services/nats_service.py`
- **.get_connection_stats()** (4 connections) — `server/services/nats_service.py`
- **.publish()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **Msg** (4 connections)
- **Protocol** (4 connections)
- **_NatsSubscribeFn** (3 connections) — `server/services/nats_service.py`
- **_as_json_map()** (3 connections) — `server/services/nats_service.py`
- **._negatively_acknowledge_message()** (3 connections) — `server/services/nats_service.py`
- **.__call__()** (3 connections) — `server/services/nats_service.py`
- **.__call__()** (2 connections) — `server/services/nats_service.py`
- **.add_disconnect_listener()** (1 connections) — `server/services/nats_service.py`
- **.add_error_listener()** (1 connections) — `server/services/nats_service.py`
- **.add_reconnect_listener()** (1 connections) — `server/services/nats_service.py`
- **.drain()** (1 connections) — `server/services/nats_service.py`
- **.unsubscribe()** (1 connections) — `server/services/nats_service.py`
- **Subscription** (1 connections)
- **Get connection statistics from state machine. Returns: Dictionary with…** (1 connections) — `server/services/nats_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (8 shared connections)
- [test_nats_service.py](test_nats_service.py.md) (7 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [.disconnect](disconnect.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 52 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*