# msg

> 36 nodes

## Key Concepts

- **nats_service.py** (33 connections) — `server/services/nats_service.py`
- **JsonMap** (9 connections)
- **_NatsListenerClient** (5 connections) — `server/services/nats_service.py`
- **NatsMessageCallback** (5 connections) — `server/services/nats_service.py`
- **nats_metrics.py** (5 connections) — `server/services/nats_metrics.py`
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
- *... and 11 more nodes in this community*

## Relationships

- [server services nats service natsservice](server_services_nats_service_natsservice.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server realtime message formatters](server_realtime_message_formatters.md) (5 shared connections)
- [server services nats exceptions natsrequesterror](server_services_nats_exceptions_natsrequesterror.md) (5 shared connections)
- [server services nats metrics natsmetrics](server_services_nats_metrics_natsmetrics.md) (2 shared connections)
- [server realtime connection state machine](server_realtime_connection_state_machine.md) (2 shared connections)
- [server events combat events](server_events_combat_events.md) (2 shared connections)
- [server config models nats natsconfig](server_config_models_nats_natsconfig.md) (1 shared connections)
- [server services combat event publisher](server_services_combat_event_publisher.md) (1 shared connections)
- [moduletype](moduletype.md) (1 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [server config init](server_config_init.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 84 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*