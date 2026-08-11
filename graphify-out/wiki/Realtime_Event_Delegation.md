# Realtime Event Delegation

> 54 nodes

## Key Concepts

- **NATSMessageBroker** (32 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker.py** (17 connections) — `server/infrastructure/nats_broker.py`
- **MessageBrokerError** (13 connections) — `server/infrastructure/message_broker.py`
- **message_broker.py** (11 connections) — `server/infrastructure/message_broker.py`
- **PublishError** (11 connections) — `server/infrastructure/message_broker.py`
- **SubscribeError** (9 connections) — `server/infrastructure/message_broker.py`
- **RequestError** (9 connections) — `server/infrastructure/message_broker.py`
- **MessageBrokerConnectionError** (8 connections) — `server/infrastructure/message_broker.py`
- **UnsubscribeError** (8 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (7 connections) — `server/infrastructure/nats_broker.py`
- **Any** (5 connections)
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.disconnect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_message()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_subject()** (4 connections) — `server/infrastructure/nats_broker.py`
- **.unsubscribe()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- *... and 29 more nodes in this community*

## Relationships

- [Combat Monitoring Service](Combat_Monitoring_Service.md) (19 shared connections)
- [Player Death Service](Player_Death_Service.md) (3 shared connections)
- [Infrastructure Message Broker](Infrastructure_Message_Broker.md) (2 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (2 shared connections)
- [NATS Subject Exceptions](NATS_Subject_Exceptions.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Components Ui Designtokens](Components_Ui_Designtokens.md) (2 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (1 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`

## Audit Trail

- EXTRACTED: 205 (91%)
- INFERRED: 21 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*