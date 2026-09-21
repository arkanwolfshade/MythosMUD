# get_viewer_phantom_names

> 26 nodes

## Key Concepts

- **get_viewer_phantom_names()** (13 connections) — `server/services/phantom_visibility.py`
- **room_has_hallucinating_viewer()** (10 connections) — `server/services/phantom_visibility.py`
- **phantom_visibility.py** (10 connections) — `server/services/phantom_visibility.py`
- **test_phantom_visibility.py** (9 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **send_personalized_occupants_update()** (8 connections) — `server/realtime/room_viewer_fanout.py`
- **._send_room_occupants_update_internal()** (5 connections) — `server/realtime/event_handler.py`
- **.send_room_occupants_update()** (3 connections) — `server/realtime/event_handler.py`
- **test_get_viewer_phantom_names_matches_own_room()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_get_viewer_phantom_names_no_viewer_or_room()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_false_when_no_phantoms_or_deranged()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_true_when_any_player_has_phantoms()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **test_room_has_hallucinating_viewer_true_when_any_player_is_deranged()** (3 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **ConnectionManager** (2 connections)
- **UUID** (2 connections)
- **Internal implementation for sending room occupants update. This method is used…** (1 connections) — `server/realtime/event_handler.py`
- **Send room occupants update to players in the room (public API). Preserves…** (1 connections) — `server/realtime/event_handler.py`
- **Send a `room_occupants` update to each connected player individually. Used by…** (1 connections) — `server/realtime/room_viewer_fanout.py`
- **Shared per-viewer hallucination visibility (#625, #626, #714). Phantom hostiles…** (1 connections) — `server/services/phantom_visibility.py`
- **Return the viewer's own active phantom hostiles in this room, styled as NPC…** (1 connections) — `server/services/phantom_visibility.py`
- **Cheap, in-memory eligibility check: does anyone in this room need a…** (1 connections) — `server/services/phantom_visibility.py`
- **Unit tests for shared per-viewer phantom visibility (#625, #714). Moved from…** (1 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **#625: no phantom names without both a viewer id and a room id.** (1 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **#625: only the viewer's own active phantoms in this room are returned.** (1 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **#714: the fast-path gate is False when nobody has an active phantom or is…** (1 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- **#714: True as soon as one player in the room has an active phantom.** (1 connections) — `server/tests/unit/services/test_phantom_visibility.py`
- *... and 1 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (8 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (5 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [RealTimeEventHandler](RealTimeEventHandler.md) (2 shared connections)
- [MessageBuilder](MessageBuilder.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/realtime/room_viewer_fanout.py`
- `server/services/phantom_visibility.py`
- `server/tests/unit/services/test_phantom_visibility.py`

## Audit Trail

- EXTRACTED: 53 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*