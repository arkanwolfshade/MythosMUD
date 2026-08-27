# ChatModeration

> 36 nodes

## Key Concepts

- **nats_service.py** (34 connections) — `server/services/nats_service.py`
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

- [PrototypeRegistryError](PrototypeRegistryError.md) (12 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (7 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (4 shared connections)
- [server/services/nats_subject_manager/__init__.py](server-services-nats_subject_manager-__init__.py.md) (3 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [RateLimiter](RateLimiter.md) (2 shared connections)
- [test_command_parser_helpers.py](test_command_parser_helpers.py.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [NATSService](NATSService.md) (1 shared connections)

## Source Files

- `server/services/nats_metrics.py`
- `server/services/nats_service.py`

## Audit Trail

- EXTRACTED: 85 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*