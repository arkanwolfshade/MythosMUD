# Realtime Connection Event

> 21 nodes · cohesion 0.15

## Key Concepts

- **test_connection_event_helpers.py** (12 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **subscribe_to_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- **unsubscribe_from_room_events_impl()** (10 connections) — `server/realtime/connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles DatabaseError.** (2 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles DatabaseError.** (2 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Any** (2 connections) — `server/realtime/connection_event_helpers.py`
- **Subscribe to room movement events for occupant broadcasting.** (1 connections) — `server/realtime/connection_event_helpers.py`
- **Unsubscribe from room movement events.** (1 connections) — `server/realtime/connection_event_helpers.py`
- **Unit tests for connection event helpers.  Tests the connection_event_helpers mod** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() successfully subscribes to events.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles missing event bus.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() successfully unsubscribes from events.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles missing event bus.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`

## Relationships

- [[NPC Admin API]] (5 shared connections)
- [[Room Occupant Events]] (4 shared connections)
- [[Services Service Room]] (2 shared connections)

## Source Files

- `server/realtime/connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`

## Audit Trail

- EXTRACTED: 71 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
