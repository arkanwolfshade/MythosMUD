# event connection helpers

> 21 nodes

## Key Concepts

- **unsubscribe_from_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **test_connection_event_helpers.py** (13 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Any** (2 connections)
- **Unsubscribe from room movement events.** (1 connections) — `server/realtime/connection_event_helpers.py`
- **Unit tests for connection event helpers.  Tests the connection_event_helpers mod** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() successfully subscribes to events.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles missing event bus.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test subscribe_to_room_events_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() successfully unsubscribes from events.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles missing event bus.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles DatabaseError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Test unsubscribe_from_room_events_impl() handles AttributeError.** (1 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`

## Relationships

- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [npc populate databases](npc_populate_databases.md) (4 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [room websocket updates](room_websocket_updates.md) (2 shared connections)

## Source Files

- `server/realtime/connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`

## Audit Trail

- EXTRACTED: 61 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*