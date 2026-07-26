# subscribe_to_room_events_impl

> 21 nodes · cohesion 0.11

## Key Concepts

- **subscribe_to_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **test_connection_event_helpers.py** (13 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Any** (2 connections)
- **Subscribe to room movement events for occupant broadcasting.** (1 connections) — `server/realtime/connection_event_helpers.py`
- **Unit tests for connection event helpers.  Tests the connection_event_helpers mod** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() successfully subscribes to events.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles missing event bus.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() successfully unsubscribes from events.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles missing event bus.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [connection_manager.py](connection_manager.py.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)

## Source Files

- `server/realtime/connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`

## Audit Trail

- EXTRACTED: 61 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*