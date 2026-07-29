# Any

> 8 nodes

## Key Concepts

- **.__init__()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_entered_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **.handle_player_left_room()** (4 connections) — `server/realtime/integration/room_event_handler.py`
- **Any** (3 connections)
- **UUID** (2 connections)
- **Initialize the room event handler.          Args:             room_manager: Room** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handle PlayerEnteredRoom events by broadcasting updated occupant count.** (1 connections) — `server/realtime/integration/room_event_handler.py`
- **Handle PlayerLeftRoom events by broadcasting updated occupant count.** (1 connections) — `server/realtime/integration/room_event_handler.py`

## Relationships

- [Any](Any.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/integration/room_event_handler.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*