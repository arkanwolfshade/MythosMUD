# infrastructure nats broker

> 38 nodes

## Key Concepts

- **NATSMessageBroker** (30 connections) — `server/infrastructure/nats_broker.py`
- **.publish()** (6 connections) — `server/infrastructure/nats_broker.py`
- **.connect()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._start_health_monitoring()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._configure_tls()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._error_callback()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_error_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._handle_reconnect_async()** (4 connections) — `server/infrastructure/nats_broker.py`
- **._health_check_loop()** (4 connections) — `server/infrastructure/nats_broker.py`
- **test_connect_with_tls_enabled_passes_tls_options()** (4 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Any** (3 connections)
- **._disconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._handle_disconnect_async()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._reconnected_callback()** (3 connections) — `server/infrastructure/nats_broker.py`
- **._perform_health_check()** (3 connections) — `server/infrastructure/nats_broker.py`
- **nats_broker()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception** (2 connections)
- **NATS implementation of MessageBroker protocol.      This class wraps NATS client** (1 connections) — `server/infrastructure/nats_broker.py`
- **Configure TLS settings for NATS connection (mirrors NATSService._configure_tls).** (1 connections) — `server/infrastructure/nats_broker.py`
- **Connect to NATS server.          Returns:             bool: True if connection s** (1 connections) — `server/infrastructure/nats_broker.py`
- **Check if connected to NATS and healthy.          Returns:             bool: True** (1 connections) — `server/infrastructure/nats_broker.py`
- **Publish message to NATS subject.          Args:             subject: NATS subjec** (1 connections) — `server/infrastructure/nats_broker.py`
- *... and 13 more nodes in this community*

## Relationships

- [command factories communication](command_factories_communication.md) (9 shared connections)
- [broker infrastructure nats](broker_infrastructure_nats.md) (3 shared connections)
- [game models enums](game_models_enums.md) (2 shared connections)
- [message handlers realtime](message_handlers_realtime.md) (2 shared connections)
- [config models rationale](config_models_rationale.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [schemas nats messages](schemas_nats_messages.md) (1 shared connections)
- [message handler factory](message_handler_factory.md) (1 shared connections)

## Source Files

- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 117 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*