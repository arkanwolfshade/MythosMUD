# .unsubscribe

> 7 nodes

## Key Concepts

- **.unsubscribe()** (4 connections) — `server/events/event_bus.py`
- **.subscribe()** (3 connections) — `server/events/event_bus.py`
- **.unsubscribe_all_for_service()** (3 connections) — `server/events/event_bus.py`
- **T** (2 connections)
- **Subscribe ``handler`` to ``event_type``. Pass ``service_id`` for shutdown…** (1 connections) — `server/events/event_bus.py`
- **Unsubscribe from events of a specific type with pure async coordination. Args:…** (1 connections) — `server/events/event_bus.py`
- **Unsubscribe all handlers for a specific service. Args: service_id: Service…** (1 connections) — `server/events/event_bus.py`

## Relationships

- [EventBus](EventBus.md) (3 shared connections)

## Source Files

- `server/events/event_bus.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*