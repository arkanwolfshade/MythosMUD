# test_get_subscriber_stats

> 8 nodes

## Key Concepts

- **test_get_subscriber_stats()** (3 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_event_bus_unsubscribe()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_subscribe_invalid_event_type()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **test_unsubscribe_all_for_service_partial_cleanup()** (2 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test subscribe() raises error for invalid event type.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe_all_for_service() only removes tracked handlers.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.get_subscriber_stats() returns subscriber statistics.** (1 connections) — `server/tests/unit/events/test_event_bus.py`
- **Test EventBus.unsubscribe() removes subscriber.** (1 connections) — `server/tests/unit/events/test_event_bus.py`

## Relationships

- [test_event_bus.py](test_event_bus.py.md) (4 shared connections)
- [BaseEvent](BaseEvent.md) (1 shared connections)

## Source Files

- `server/tests/unit/events/test_event_bus.py`

## Audit Trail

- EXTRACTED: 8 (89%)
- INFERRED: 1 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*