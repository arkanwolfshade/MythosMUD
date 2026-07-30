# Test exception tracking functionality.

> 25 nodes

## Key Concepts

- **subscribe_to_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **unsubscribe_from_room_events_impl()** (13 connections) — `server/realtime/connection_event_helpers.py`
- **test_connection_event_helpers.py** (13 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **connection_event_helpers.py** (10 connections) — `server/realtime/connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_database_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_attribute_error()** (4 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_subscribe_to_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_success()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **test_unsubscribe_from_room_events_impl_no_event_bus()** (3 connections) — `server/tests/unit/realtime/test_connection_event_helpers.py`
- **Any** (2 connections)
- **Event subscription helpers for connection manager.  This module provides helper** (1 connections) — `server/realtime/connection_event_helpers.py`
- **Subscribe to room movement events for occupant broadcasting.** (1 connections) — `server/realtime/connection_event_helpers.py`
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

- [real time](real_time.md) (7 shared connections)
- [Player](Player.md) (4 shared connections)
- [.validate player name field()](validate_player_name_field%28%29.md) (3 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [world](world.md) (2 shared connections)
- [create access token()](create_access_token%28%29.md) (2 shared connections)

## Source Files

- `server/realtime/connection_event_helpers.py`
- `server/tests/unit/realtime/test_connection_event_helpers.py`

## Audit Trail

- EXTRACTED: 83 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*