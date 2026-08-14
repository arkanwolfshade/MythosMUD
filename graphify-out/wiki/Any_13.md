# Any

> 50 nodes

## Key Concepts

- **Any** (17 connections)
- **.publish_with_pool()** (10 connections) — `server/services/nats_service.py`
- **._create_tracked_task()** (9 connections) — `server/services/nats_service.py`
- **._flush_batch()** (7 connections) — `server/services/nats_service.py`
- **.publish_batch()** (6 connections) — `server/services/nats_service.py`
- **._get_connection()** (5 connections) — `server/services/nats_service.py`
- **._on_error()** (5 connections) — `server/services/nats_service.py`
- **.publish()** (5 connections) — `server/services/nats_service.py`
- **._retry_failed_batch_groups()** (5 connections) — `server/services/nats_service.py`
- **._batch_timeout()** (4 connections) — `server/services/nats_service.py`
- **._handle_error_async()** (4 connections) — `server/services/nats_service.py`
- **._on_disconnect()** (4 connections) — `server/services/nats_service.py`
- **._on_reconnect()** (4 connections) — `server/services/nats_service.py`
- **.request()** (4 connections) — `server/services/nats_service.py`
- **._return_connection()** (4 connections) — `server/services/nats_service.py`
- **.subscribe()** (4 connections) — `server/services/nats_service.py`
- **NATS** (4 connections)
- **._acknowledge_message()** (3 connections) — `server/services/nats_service.py`
- **._call_callback()** (3 connections) — `server/services/nats_service.py`
- **._decode_message_data()** (3 connections) — `server/services/nats_service.py`
- **.get_connection_stats()** (3 connections) — `server/services/nats_service.py`
- **._handle_disconnect_async()** (3 connections) — `server/services/nats_service.py`
- **._handle_reconnect_async()** (3 connections) — `server/services/nats_service.py`
- **._negatively_acknowledge_message()** (3 connections) — `server/services/nats_service.py`
- **.recover_failed_batches()** (3 connections) — `server/services/nats_service.py`
- *... and 25 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (28 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (5 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (1 shared connections)
- [NATSConnectionStateMachine](NATSConnectionStateMachine.md) (1 shared connections)
- [NATSConfig](NATSConfig.md) (1 shared connections)

## Source Files

- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 93 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*