# test_seed_e2e_users.py

> 17 nodes · cohesion 0.15

## Key Concepts

- **._get_next_sequence()** (8 connections) — `server/realtime/message_builders.py`
- **Any** (6 connections)
- **.build_occupants_update_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_entered_message()** (5 connections) — `server/realtime/message_builders.py`
- **.create_player_left_message()** (5 connections) — `server/realtime/message_builders.py`
- **.build_room_state_message()** (4 connections) — `server/realtime/message_builders.py`
- **.build_room_update_message()** (4 connections) — `server/realtime/message_builders.py`
- **.__init__()** (3 connections) — `server/realtime/message_builders.py`
- **NpcOccupant** (1 connections)
- **Build the room occupants update message. Args: room_id_str: Room ID as string…** (1 connections) — `server/realtime/message_builders.py`
- **Build a room update message. Args: room_id: The room ID room_data: The room…** (1 connections) — `server/realtime/message_builders.py`
- **Build a single authoritative room_state message (room metadata + occupants).…** (1 connections) — `server/realtime/message_builders.py`
- **Initialize the message builder. Args: sequence_counter: Callable that returns…** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number.** (1 connections) — `server/realtime/message_builders.py`
- **Get the next sequence number (public API). Returns: The next sequence number…** (1 connections) — `server/realtime/message_builders.py`
- **Create a real-time message for player entering a room. Args: event: The…** (1 connections) — `server/realtime/message_builders.py`
- **Create a real-time message for player leaving a room. Args: event: The…** (1 connections) — `server/realtime/message_builders.py`

## Relationships

- [look_container.py](look_container.py.md) (7 shared connections)
- [BaseEvent](BaseEvent.md) (2 shared connections)

## Source Files

- `server/realtime/message_builders.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*