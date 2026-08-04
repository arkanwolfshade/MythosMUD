# subject admin controller

> 26 nodes

## Key Concepts

- **RoomEventHandler** (21 connections) — `server/realtime/integration/room_event_handler.py`
- **room_event_handler.py** (13 connections) — `server/realtime/integration/room_event_handler.py`
- **test_room_event_handler.py** (13 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **__init__.py** (5 connections) — `server/realtime/integration/__init__.py`
- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (3 connections)
- **UUID** (2 connections)
- **room_handler()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_to_events()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_to_events_no_bus()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_unsubscribe_from_events()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_room_broadcasts()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_room_missing_room_id()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_skips_uuid_player_names()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_left_room_broadcasts()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_handle_player_entered_nats_publish_failure()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **test_subscribe_handles_exception()** (2 connections) — `server/tests/unit/realtime/integration/test_room_event_handler.py`
- **Integration components for connection management.  This package provides integra** (1 connections) — `server/realtime/integration/__init__.py`
- **Room event handling for connection management.  This module provides integration** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handles room movement events and broadcasts occupant updates.      This class pr** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Initialize the room event handler.          Args:             room_manager: Room** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handle PlayerEnteredRoom events by broadcasting updated occupant count.** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handle PlayerLeftRoom events by broadcasting updated occupant count.** (1 connections) — `server/realtime/integration/room_event_handler.py`
- *... and 1 more nodes in this community*

## Relationships

- [taunt combat commands](taunt_combat_commands.md) (5 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (4 shared connections)
- [room look commands](room_look_commands.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [combat services turn](combat_services_turn.md) (1 shared connections)
- [nats services metrics](nats_services_metrics.md) (1 shared connections)

## Source Files

- `server/realtime/integration/__init__.py`
- `server/realtime/integration/room_event_handler.py`
- `server/tests/unit/realtime/integration/test_room_event_handler.py`

## Audit Trail

- EXTRACTED: 96 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*