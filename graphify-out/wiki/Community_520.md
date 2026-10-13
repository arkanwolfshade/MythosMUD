# Community 520

> 33 nodes

## Key Concepts

- **NATSServiceSubscriptionMixin** (15 connections) — `server/services/nats_service_subscriptions.py`
- **JsonMap** (6 connections)
- **NatsMessageCallback** (5 connections) — `server/services/nats_service_subscriptions.py`
- **._verify_subscription_cleanup()** (5 connections) — `server/services/nats_service_subscriptions.py`
- **._acknowledge_message()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._call_callback()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._decode_message_data()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **Msg** (4 connections)
- **_NatsSubscribeFn** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.get_active_subscriptions()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **._negatively_acknowledge_message()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.subscribe()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.__call__()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **Protocol** (3 connections)
- **.__call__()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **._close_all_subscriptions()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **._drain_subscriptions()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **.unsubscribe()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **Subscription** (1 connections)
- **Verify all subscriptions were cleaned up and log warnings if any remain.** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Decode message data from NATS message.** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Call the registered callback, handling both async and sync callbacks. Sync…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Acknowledge message if manual ack is enabled. Returns True if acknowledged. AI:…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Negatively acknowledge message if manual ack is enabled. AI: Records metrics…** (1 connections) — `server/services/nats_service_subscriptions.py`
- *... and 8 more nodes in this community*

## Relationships

- [Community 63](Community_63.md) (6 shared connections)
- [NATS Service Config](NATS_Service_Config.md) (1 shared connections)

## Source Files

- `server/services/nats_service_subscriptions.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*