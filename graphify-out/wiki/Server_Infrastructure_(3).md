# Server Infrastructure (3)

> 134 nodes

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
- **.__init__()** (5 connections) — `server/infrastructure/nats_broker.py`
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
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- *... and 109 more nodes in this community*

## Relationships

- [Server Services (2)](Server_Services_%282%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Infrastructure (15)](Server_Infrastructure_%2815%29.md) (2 shared connections)
- [Server Schemas (5)](Server_Schemas_%285%29.md) (2 shared connections)
- [Server Services (3)](Server_Services_%283%29.md) (2 shared connections)
- [Server Services (31)](Server_Services_%2831%29.md) (1 shared connections)
- [Server Services (24)](Server_Services_%2824%29.md) (1 shared connections)
- [Server Realtime (71)](Server_Realtime_%2871%29.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 375 (93%)
- INFERRED: 30 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*