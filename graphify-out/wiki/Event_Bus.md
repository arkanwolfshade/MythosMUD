# Event Bus

> 11 nodes

## Key Concepts

- **SubscriberLifecycleMetrics** (4 connections) — `server/events/event_bus.py`
- **SubscriberStats** (4 connections) — `server/events/event_bus.py`
- **.get_subscriber_stats()** (4 connections) — `server/events/event_bus.py`
- **.get_all_subscriber_counts()** (3 connections) — `server/events/event_bus.py`
- **.get_subscriber_lifecycle_metrics()** (3 connections) — `server/events/event_bus.py`
- **TypedDict** (2 connections)
- **Get subscriber counts for all event types using pure async coordination.…** (1 connections) — `server/events/event_bus.py`
- **Get subscriber lifecycle metrics including churn rate. Returns: Dictionary with…** (1 connections) — `server/events/event_bus.py`
- **Get subscriber statistics per event type for monitoring. Returns: Dictionary…** (1 connections) — `server/events/event_bus.py`
- **Subscriber counts returned by get_subscriber_stats().** (1 connections) — `server/events/event_bus.py`
- **Lifecycle metrics returned by get_subscriber_lifecycle_metrics().** (1 connections) — `server/events/event_bus.py`

## Relationships

- [Test Event Bus](Test_Event_Bus.md) (3 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*