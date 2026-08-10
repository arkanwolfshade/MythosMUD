# Services Combat Persistence

> 17 nodes

## Key Concepts

- **PublishError** (11 connections) — `server/infrastructure/message_broker.py`
- **.publish()** (7 connections) — `server/infrastructure/nats_broker.py`
- **Any** (5 connections)
- **.is_connected()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_message()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.subscribe()** (5 connections) — `server/infrastructure/nats_broker.py`
- **.request()** (5 connections) — `server/infrastructure/nats_broker.py`
- **._validate_publish_subject()** (4 connections) — `server/infrastructure/nats_broker.py`
- **test_publish_not_connected()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **test_publish_failure()** (3 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Exception raised when publishing message fails.** (1 connections) — `server/infrastructure/message_broker.py`
- **Check if connected to NATS and healthy.          Returns:             bool: T** (1 connections) — `server/infrastructure/nats_broker.py`
- **Publish message to NATS subject.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Subscribe to NATS subject with message handler.** (1 connections) — `server/infrastructure/nats_broker.py`
- **Send request and wait for reply (request-reply pattern).          Args:** (1 connections) — `server/infrastructure/nats_broker.py`
- **Test publish() raises PublishError when not connected.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`
- **Test publish() raises PublishError on failure.** (1 connections) — `server/tests/unit/infrastructure/test_nats_broker.py`

## Relationships

- [Realtime Event Delegation](Realtime_Event_Delegation.md) (8 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (4 shared connections)
- [Combat Monitoring Service](Combat_Monitoring_Service.md) (3 shared connections)
- [NATS Message Schemas](NATS_Message_Schemas.md) (1 shared connections)
- [Realtime Maintenance Connection](Realtime_Maintenance_Connection.md) (1 shared connections)
- [Database Error Handling](Database_Error_Handling.md) (1 shared connections)

## Source Files

- `server/infrastructure/message_broker.py`
- `server/infrastructure/nats_broker.py`
- `server/tests/unit/infrastructure/test_nats_broker.py`

## Audit Trail

- EXTRACTED: 55 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*