# GameMechanicsService

> 31 nodes · cohesion 0.08

## Key Concepts

- **NATSServiceSubscriptionMixin** (18 connections) — `server/services/nats_service_subscriptions.py`
- **JsonMap** (6 connections)
- **NatsMessageCallback** (5 connections) — `server/services/nats_service_subscriptions.py`
- **._verify_subscription_cleanup()** (5 connections) — `server/services/nats_service_subscriptions.py`
- **Msg** (4 connections)
- **._acknowledge_message()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._call_callback()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **._decode_message_data()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **.subscribe()** (4 connections) — `server/services/nats_service_subscriptions.py`
- **.get_active_subscriptions()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **._negatively_acknowledge_message()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.unsubscribe()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.__call__()** (3 connections) — `server/services/nats_service_subscriptions.py`
- **.__call__()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **._close_all_subscriptions()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **._drain_subscriptions()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **.get_subscription_count()** (2 connections) — `server/services/nats_service_subscriptions.py`
- **Verify all subscriptions were cleaned up and log warnings if any remain.** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Decode message data from NATS message.** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Call the registered callback, handling both async and sync callbacks. Sync…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Acknowledge message if manual ack is enabled. Returns True if acknowledged. AI:…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Negatively acknowledge message if manual ack is enabled. AI: Records metrics…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Subscribe to a NATS subject and register a callback for incoming messages.…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Get list of all active NATS subscription subjects. Returns: List of subject…** (1 connections) — `server/services/nats_service_subscriptions.py`
- **Unsubscribe from a NATS subject. Args: subject: NATS subject name to…** (1 connections) — `server/services/nats_service_subscriptions.py`
- *... and 6 more nodes in this community*

## Relationships

- [TestRoomDataFixer](TestRoomDataFixer.md) (6 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (3 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (2 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (1 shared connections)

## Source Files

- `server/services/nats_service_subscriptions.py`

## Audit Trail

- EXTRACTED: 47 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*